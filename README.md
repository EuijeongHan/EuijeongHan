# 한의정 · Han Eui Jeong
### AI Engineer | MLOps

> **"Density over Speed"** — 모델 학습부터 평가·서빙·배포까지 End-to-End 구조적 완결성을 고민합니다.

<p align="left">
  <code>RAG</code> · <code>Computer Vision</code> · <code>NLP</code> · <code>Model Serving</code>
</p>

---

## 🎯 Core Competencies

| 영역 | 핵심 기술 및 역량 |
| :------------------ | :------------------- |
| **RAG / LLM** | 임베딩·LLM 12개 조합 비교 평가 후 모델 선정 · Hybrid Search(BM25+Dense), Reranking, Query Routing 설계 · Retrieval/생성 평가 파이프라인(Hit@K, MRR, nDCG, RAGAS) · LLM-as-Judge 자동화 |
| **Computer Vision** | 객체 탐지 파이프라인 구축(YOLO11, DETR) · 비교 실험(RetinaNet, Faster R-CNN) · 데이터 전처리·증강(Stratified Split, Copy-Paste, CLAHE, Letterbox) · COCO 포맷 어노테이션 관리 |
| **NLP** | KcELECTRA 파인튜닝, 감성분석 · PEFT(LoRA, AdaLoRA, Prompt Tuning) 비교 실험 · KoBART 요약, Seq2Seq+Attention 번역 |
| **Serving / MLOps** | FastAPI, Streamlit, Docker(Hub 배포) · 모델 export(ONNX) 및 양자화(Quantization) · GCP 환경 학습·서빙 |

---

## 💻 Featured Projects

| 프로젝트 | 설명 | 기술 스택 |
| :-------------------- | :---------------------------------------------------------------- | :-------------------------------------------------- |
| **[입찰메이트 (BidMate)](https://github.com/GunhoJin/2Team_Project)** | **B2G 공공조달 RAG 시스템** · *Retrieval/생성 평가 리드*<br>• 임베딩 3종 × LLM 4종 = **12개 조합 비교 실험** 후 KURE-v1 + Phi-4-mini 최종 선정<br>• 쿼리 유형별 Dual Routing 서빙 아키텍처 설계<br>• 평가 파이프라인 구축 → **Hit@5 0.91 / MRR 0.85 / nDCG 0.81** | `KURE-v1` `KoE5`<br>`ChromaDB` `BM25(Kiwi)`<br>`bge-reranker-v2-m3`<br>`Phi-4-mini` `Gemma` |
| **[알약 탐지 (HealthEat)](https://github.com/EuijeongHan/pill_detection_project)** | **알약 객체 탐지·분류 (73종)** · *Data Engineering 리드*<br>• 전처리·증강 파이프라인 전담 및 공유 모듈 구축<br>• DETR 베이스라인 독립 실험<br>• **Kaggle mAP@0.5 0.986** 달성 | `YOLO11` `PyTorch`<br>`DETR` `COCO`<br>`FastAPI` |
| **[foRG](https://github.com/EuijeongHan/forg)** | **DART 공시 데이터 자동화 시스템**<br>• 공시 정보 추출 → LLM 요약 파이프라인<br>• 텔레그램 봇 연동 실시간 리포팅 자동화 | `FastAPI` `PostgreSQL`<br>`Docker` `Telegram Bot`<br>`Claude API` |
<details>
<summary><b>📂 More Projects</b></summary>

| 프로젝트 | 설명 | 기술 스택 |
| :------- | :--------------- | :------------------ |
| **[Movie Sentiment](https://github.com/EuijeongHan/codeit_mission18-movie-review)** | 영화 리뷰 감성분석 풀스택 앱 · DB 연동 및 PDF 리포트(한글 폰트 렌더링) | `KcELECTRA` `FastAPI`<br>`Streamlit` `SQLModel` |
| **[MNIST & PillFinder](https://github.com/EuijeongHan/codeit_mission17-pill-mnist)** | 실시간 캔버스 숫자 인식 + 알약 탐지 · Docker Hub 배포 | `PyTorch` `CNN`<br>`YOLO11` `Docker` |
| **[foRG-mini](https://github.com/EuijeongHan/streamlit_forg-mini)** | foRG 경량 데모 · DART API + LLM 요약 프로토타입 | `Streamlit`<br>`OpenRouter` |

</details>

<br>

<div align="center">

### 🔍 Project Demo

<table>
  <tr>
    <td align="center"><b>MNIST Service</b></td>
    <td align="center"><b>Pill Detection Finder</b></td>
  </tr>
  <tr>
    <td align="center">
      <video src="https://github.com/user-attachments/assets/e7f70aa0-1481-4e7e-bd2c-76453c7f7f33" width="380" autoplay loop muted playsinline></video>
    </td>
    <td align="center">
      <video src="https://github.com/user-attachments/assets/b4d1dcda-703b-4f6d-b78c-a102975ef180" width="380" autoplay loop muted playsinline></video>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td align="center"><b>foRG-mini Service</b></td>
    <td align="center"><b>Movie Review & Sentiment</b></td>
  </tr>
  <tr>
    <td align="center">
      <video src="https://github.com/user-attachments/assets/1559169a-27ad-467a-baed-949b735d9c2d" width="380" autoplay loop muted playsinline></video>    
    </td>
    <td align="center">
      <video src="https://github.com/user-attachments/assets/8be287b3-7aaf-4f6f-a6af-6c815a879f47" width="380" autoplay loop muted playsinline></video>
    </td>
  </tr>
</table>

</div>

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

산업공학 전공 배경과 공공 플랫폼 기획·운영 경력을 가진 AI 엔지니어입니다.<br>
배달특급(경기도 공공배달 플랫폼) 운영 당시 유일한 공학 배경 인력으로 데이터 추출·보안 문서화·나라장터 조달 프로세스를 담당했고, 이때의 도메인 경험을 공공조달 RAG(입찰메이트), 금융·공시 자동화(foRG)로 연결하고 있습니다.

* 🔭 **Current Focus:** RAG·CV·NLP 서비스의 End-to-End 설계 — 학습·평가·서빙·배포
* 💡 **Interests:** 금융·공시 도메인 특화 AI, LLM 기반 정밀 정보 추출 파이프라인
* 📜 **Certifications:** SQLD, ADsP 보유 · 정보처리기사·빅데이터분석기사 취득 준비 중

### ⏳ Timeline & Experience

* 📅 2025.12 - Present   │ Codeit AI Engineer Bootcamp (8기)
* 📅 2023.12 - 2025.12   │ (주)코리아경기도 플랫폼사업실 기획팀 재직 (배달특급 기획/운영)
* 📅 2020.08 - 2023.07   │ CAFE.STAYPLACE 총괄 운영
* 📅 2015.01 - 2019.04   │ 5급 공무원(재경직) 공개채용 준비
* 📅 2009.03 - 2017.08   │ 숭실대학교 산업정보시스템공학 (공학사 심화)

---
<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=EuijeongHan&show_icons=true&theme=tokyonight&hide_border=true" height="160" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=EuijeongHan&layout=compact&theme=tokyonight&hide_border=true" height="160" />
</div>

---

## ✉️ Contact
* **Email:** hej4016@gmail.com
* **LinkedIn:** [의정 한](https://www.linkedin.com/in/의정-한-652185314)

