#!/usr/bin/env python3
"""
portfolio.html 타임라인을 프레임 단위로 캡처해 mp4로 렌더링한다.

  python3 render.py                      # 60초 컷, 1920x1080, 30fps
  python3 render.py --cut 30             # 30초 컷
  python3 render.py --w 960 --h 540 --fps 15 --out out/preview.mp4

clips/ 에 mp4를 넣어두면 데모 구간에 자동으로 합성된다.
비어 있으면 플레이스홀더가 그대로 렌더링된다(구성 확인용).
"""
import argparse, os, subprocess, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
CHROME = os.environ.get(
    "PW_CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut", type=int, default=60, choices=[30, 60])
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--w", type=int, default=1920)
    ap.add_argument("--h", type=int, default=1080)
    ap.add_argument("--crf", type=int, default=18)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    out = Path(a.out) if a.out else HERE / "out" / f"portfolio_{a.cut}s.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)

    # 1920x1080 기준으로 디자인되어 있으므로, 더 작은 해상도는 deviceScaleFactor로 축소한다.
    dsf = a.w / 1920

    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
         "-f", "image2pipe", "-c:v", "png", "-r", str(a.fps), "-i", "-",
         "-c:v", "libx264", "-preset", "medium", "-crf", str(a.crf),
         "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)],
        stdin=subprocess.PIPE,
    )

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME,
            args=["--autoplay-policy=no-user-gesture-required",
                  "--disable-lcd-text", "--force-color-profile=srgb"],
        )
        page = browser.new_page(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=dsf,
        )
        page.goto((HERE / "portfolio.html").as_uri())
        page.evaluate("document.body.classList.add('render')")
        page.evaluate("window.fit()")   # 렌더 모드에서는 1:1 (축소 해제)
        page.evaluate("window.clipsReady")           # 클립 메타데이터 로딩 대기
        page.evaluate(f"window.setCut({a.cut})")
        page.wait_for_timeout(400)

        total = page.evaluate("window.getTotal()")
        n = int(round(total * a.fps))
        stage = page.locator("#stage")
        t_start = time.time()

        for i in range(n):
            t = i / a.fps
            page.evaluate("t => window.seek(t)", t)
            page.evaluate("window.seekSettled()")
            ff.stdin.write(stage.screenshot(type="png", animations="disabled"))
            if i % a.fps == 0:
                el = time.time() - t_start
                sys.stderr.write(
                    f"\r  {i:5d}/{n} frames  ({t:5.1f}s / {total:.0f}s)  "
                    f"경과 {el:5.1f}s"
                )
                sys.stderr.flush()
        browser.close()

    ff.stdin.close()
    ff.wait()
    sys.stderr.write("\n")
    print(f"완료: {out}  ({out.stat().st_size/1e6:.1f} MB, {n} frames @ {a.fps}fps)")


if __name__ == "__main__":
    main()
