<div align="center">

# 한의정 · Han Eui Jeong

### Domain-Driven AI Engineer | MLOps | AI PM 

**도메인은 빠르게, 구조는 끝까지.**
낯선 분야를 파고들어 기획부터 배포까지 완결하는 AI 엔지니어

`공공조달` · `금융/공시` · `소상공인` — 서로 다른 3개 도메인, 3개의 End-to-End AI 서비스

</div>

---

## 🎯 What I Do

세 가지 강점, 하나의 방식.<br>
파고들고 → 판단하고 → 완결합니다.

| | 강점 | 증거 |
| :---: | :--- | :--- |
| **①** | **낯선 도메인을 빠르게** — 처음 보는 분야도 구조부터 파악해 풀어야 할 문제로 정의합니다. | 공공조달·금융·소상공인, 서로 다른 3개 도메인을 직접 서비스로 |
| **②** | **철저한 데이터 기반의 판단** — 기술을 그냥 쓰지 않고 비교·검증해 고릅니다. 그 판단의 기준은 현장에서 온 도메인 이해입니다. | RAG 12개 조합 비교·선정 · faithfulness 근거로 LoRA 제외 결정 |
| **③** | **End-to-End 완결** — 모델 설계·평가부터 서빙·배포까지. 만들다 마는 게 아니라 실제 사용자가 쓰는 단계까지 끌고 갑니다. | 입찰메이트 GCP 배포 · foRG 구독 서비스 · 카페광고AI 출시 |

---

## 💻 Featured Projects

세 프로젝트는 각각 다른 도메인이지만, 패턴은 같습니다 — **현장의 문제 → 직접 만든 AI → 서비스화.**

<table>
  <thead>
    <tr>
      <th width="20%">프로젝트</th>
      <th width="56%">설명</th>
      <th width="24%">기술 스택</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b><a href="https://github.com/GunhoJin/2Team_Project">입찰메이트<br>(BidMate)</a></b><br><sub>🏛️ 공공조달</sub></td>
      <td>
        <b>B2G 공공조달 RAG 시스템</b> · <i>Retrieval/생성 평가 리드</i><br>
        • 임베딩 3종 × LLM 4종 = <b>12개 조합 비교 실험</b> 후 KURE-v1 + Phi-4-mini 최종 선정<br>
        • 쿼리 유형별 Dual Routing 서빙 아키텍처 설계<br>
        • 평가 파이프라인 구축 → <b>Hit@5 0.91 / MRR 0.85 / nDCG 0.81</b><br>
        • <i>(개편 중)</i> 실제 입찰 실무 노하우를 로직화 — 정성/정량 평가기준 RFP 대조, 블라인드 위반(회사 식별 문구) 자동 점검, 마감 전 보완서류 확인 안내 + GCP 재호스팅
      </td>
      <td><code>KURE-v1</code> <code>KoE5</code> <code>ChromaDB</code> <code>BM25(Kiwi)</code> <code>bge-reranker-v2-m3</code> <code>Phi-4-mini</code> <code>Gemma</code> <code>GCP</code></td>
    </tr>
    <tr>
      <td><b><a href="https://github.com/EuijeongHan/forg">foRG</a></b><br><sub>📈 금융/공시</sub></td>
      <td>
        <b>DART 공시 자동 요약·알림 서비스</b> · <i>구독 서비스로 발전 중</i><br>
        • 공시 정보 추출 → LLM 요약 → 텔레그램 실시간 푸시<br>
        • "공시 알림은 푸시가 본질"이라 판단해 앱이 아닌 봇으로 설계<br>
        • 무료/유료 티어 구독 구조 설계 → 소규모 사용자 가치 검증 진행
      </td>
      <td><code>FastAPI</code> <code>PostgreSQL</code> <code>Docker</code> <code>Telegram Bot</code> <code>DART API</code> <code>Claude API</code></td>
    </tr>
    <tr>
      <td><b>카페 광고 AI</b><br><sub>🏪 소상공인 · <i>2026.07 개발</i></sub></td>
      <td>
        <b>소상공인 광고·콘텐츠 생성 AI</b> · <i>실제 서비스 출시 목표</i><br>
        • 직접 브랜드 광고를 만드는 <b>증강 도구</b>(Software 3.0)<br>
        • 카피(LLM) + 브랜드 톤 일관성(RAG) + 브랜드 비주얼(Diffusion·LoRA)<br>
        • 브랜드 스타일을 LoRA로 학습, 출시 단계는 경량화 방식으로 전환
      </td>
      <td><code>LLM</code> <code>RAG</code> <code>Diffusion</code> <code>LoRA</code> <code>FastAPI</code></td>
    </tr>
  </tbody>
</table>

<details>
<summary><b>📂 More Projects</b></summary>

<br>

<table>
  <thead>
    <tr>
      <th width="20%">프로젝트</th>
      <th width="56%">설명</th>
      <th width="24%">기술 스택</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b><a href="https://github.com/EuijeongHan/pill_detection_project">알약 탐지<br>(HealthEat)</a></b></td>
      <td>알약 객체 탐지·분류 (73종) · <i>Data Engineering 리드</i> · 전처리·증강 파이프라인 전담, DETR 베이스라인 독립 실험 · <b>Kaggle mAP@0.5 0.986</b></td>
      <td><code>YOLO11</code> <code>PyTorch</code> <code>DETR</code> <code>COCO</code></td>
    </tr>
    <tr>
      <td><b><a href="https://github.com/EuijeongHan/streamlit_forg-mini">DART 공시 조회<br>(foRG-mini)</a></b></td>
      <td>foRG 경량 데모 · DART API + LLM 요약 </td>
      <td><code>Streamlit</code> <code>OpenRouter</code> <code>Phi-4-mini</code>
    </tr>
    <tr>
      <td><b><a href="https://github.com/EuijeongHan/codeit_mission18-movie-review">Movie Sentiment</a></b></td>
      <td>영화 리뷰 감성분석 풀스택 앱 · DB 연동 및 PDF 리포트(한글 폰트 렌더링)</td>
      <td><code>KcELECTRA</code> <code>FastAPI</code> <code>Streamlit</code></td>
    </tr>
    <tr>
      <td><b><a href="https://github.com/EuijeongHan/codeit_mission17-pill-mnist">MNIST & PillFinder</a></b></td>
      <td>실시간 캔버스 숫자 인식 + 알약 탐지 · Docker Hub 배포</td>
      <td><code>PyTorch</code> <code>CNN</code> <code>YOLO11</code> <code>Docker</code></td>
    </tr>
  </tbody>
</table>

</details>

---

## 🔍 Project Demo

<table>
  <tr>
    <td align="center" width="25%"><b>MNIST Service</b></td>
    <td align="center" width="25%"><b>Pill Detection Finder</b></td>
    <td align="center" width="25%"><b>Movie Review & Sentiment</b></td>
    <td align="center" width="25%"><b>foRG-mini Service</b></td>
  </tr>
  <tr>
    <td align="center" width="25%"><video src="https://github.com/user-attachments/assets/e7f70aa0-1481-4e7e-bd2c-76453c7f7f33" muted autoplay loop playsinline></video></td>
    <td align="center" width="25%"><video src="https://github.com/user-attachments/assets/b4d1dcda-703b-4f6d-b78c-a102975ef180" muted autoplay loop playsinline></video></td>
    <td align="center" width="25%"><video src="https://github.com/user-attachments/assets/5707452c-cac7-4c57-a013-17554110c5e9" muted autoplay loop playsinline></video></td>
    <td align="center" width="25%"><video src="https://github.com/user-attachments/assets/1559169a-27ad-467a-baed-949b735d9c2d" muted autoplay loop playsinline></video></td>
  </tr>
</table>

---

## 🛠️ Tech Stack

**Language & ML**<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=PyTorch&logoColor=white"/> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"/>

**LLM & RAG**<br>
<img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black"/> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/> <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square&logo=chromadb&logoColor=white"/> <img src="https://img.shields.io/badge/Claude%20API-D97757?style=flat-square&logo=anthropic&logoColor=white"/>

**Computer Vision**<br>
<img src="https://img.shields.io/badge/YOLO-111F68?style=flat-square&logo=yolo&logoColor=white"/> <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/> <img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white"/>

**Serving & Infra**<br>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"/> <img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/>

---

## 👋 About Me

깊이 파고드는 힘, 데이터로 판단하는 눈, 방법을 찾아 뚫고 나가는 돌파력. 이것이 분야를 바꿔가며 단련해온 저만의 무기입니다. <br>
카페 운영, 공공 배달 플랫폼을 거쳐 AI 엔지니어가 되기까지 — 매번 새 분야를 파고들었고, 막힐 때마다 길을 찾아냈습니다.

- 🔭 **Now:** 입찰메이트 도메인 고도화 + GCP 배포 · foRG 구독 서비스화
- 🚀 **Next:** 카페 광고 AI 서비스 출시 (2026.07)
- 📜 **Certifications:** SQLD · ADsP · 정보처리기사 · 빅데이터분석기사 *(준비 중)*

### ⏳ Timeline

```
2025.12 - Present   Codeit AI Engineer Bootcamp (8기)
2023.12 - 2025.12   (주)코리아경기도 플랫폼사업실 기획팀 (배달특급 기획/운영)
2020.08 - 2023.07   CAFE.STAYPLACE 총괄 운영
2015.01 - 2019.04   5급 공무원(재경직) 공개채용 준비
2009.03 - 2017.08   숭실대학교 산업정보시스템공학 (공학사)
```

---

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=EuijeongHan&show_icons=true&theme=tokyonight&hide_border=true" height="160" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=EuijeongHan&layout=compact&theme=tokyonight&hide_border=true" height="160" />

<br><br>

📫 **hej4016@gmail.com**  ·  🔗 **[LinkedIn](https://www.linkedin.com/in/의정-한-652185314)**

</div>

