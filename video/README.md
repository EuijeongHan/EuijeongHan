# video/ — 60초 포트폴리오 영상

이력서를 대체하는 물건이 아니라, README 최상단과 LinkedIn에 얹는 **훅**이다.

```
video/
├─ portfolio.html   재생·스크럽 가능한 타임라인 (브라우저에서 바로 열림)
├─ render.py        프레임 캡처 → mp4 렌더러
├─ SCRIPT.md        컷시트(60s/30s), 촬영 지침, 나레이션 원고
├─ clips/           데모 클립 3개를 넣는 곳
└─ out/             렌더 결과물
```

## 빠르게

```bash
# 1) 미리보기 — 브라우저에서 열고 ▶ 재생 / 스크럽 / 30초 전환
open video/portfolio.html

# 2) 데모 클립 넣기 (없으면 플레이스홀더로 렌더링됨)
cp ~/adnova_demo.mp4  video/clips/adnova.mp4
cp ~/bidmate_demo.mp4 video/clips/bidmate.mp4
cp ~/forg_demo.mp4    video/clips/forg.mp4

# 3) 렌더
cd video
pip install playwright && playwright install chromium   # 최초 1회
python3 render.py            # → out/portfolio_60s.mp4
python3 render.py --cut 30   # → out/portfolio_30s.mp4
```

`ffmpeg`(libx264 포함)와 한글 폰트(`Noto Sans CJK KR`)가 필요하다.
Ubuntu 기준: `apt install ffmpeg fonts-noto-cjk`

## 동작 방식

`portfolio.html`은 CSS 애니메이션이 아니라 **결정론적 타임라인**으로 동작한다.
`window.seek(t)` 한 번이면 t초 시점의 화면이 완전히 결정되고, 데모 클립의 `currentTime`까지 같이 맞춘다.
그래서 브라우저 미리보기와 프레임 렌더 결과가 정확히 일치하고, 화면 녹화 없이 프레임 단위로 mp4를 뽑을 수 있다.

## 고칠 곳

| 무엇 | 어디 |
|---|---|
| 문구 | `portfolio.html`의 각 `<section class="scene" id="S*">` |
| 씬 길이 | `portfolio.html` 상단 `CUTS` 상수 |
| 등장 타이밍 | 각 요소의 `data-s`(시작 비율) / `data-d`(지속 비율) — 씬 길이 대비 0~1 |
| 색 / 타이포 | `:root` CSS 변수 |
