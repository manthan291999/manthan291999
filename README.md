<p align="center">
  <img src="./terminal.svg" alt="Terminal: Manthan Mittal, AI/ML Engineer" width="100%">
</p>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=900&color=7EE787&center=true&vCenter=true&width=680&lines=Building+recommenders+that+explain+themselves;Shipping+multi-agent+LLM+copilots+in+Rust;Catching+anomalies+in+real+sensor+streams;ML+that+survives+contact+with+real+users" alt="Typing SVG"></a>
</p>

<p align="center">
  <a href="https://manthanmittal.in"><img src="https://img.shields.io/badge/Portfolio-1f2328?style=for-the-badge&logo=googlechrome&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/manthanmittal"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="mailto:manthanmittal93@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <img src="https://komarev.com/ghpvc/?username=manthan291999&style=for-the-badge&color=2ea043&label=PROFILE+VIEWS">
</p>

## 🧠 About me

> **I care about ML that survives contact with real users and real data.**

Most of my time goes to **recommendation systems**, **agentic LLM workflows**, and the unglamorous
data engineering underneath both.

```python
class Manthan:
    role      = "AI/ML Engineer"
    based_in  = "Ahmedabad, India 🇮🇳"
    education = "MSc Artificial Intelligence · University of Essex 🎓"
    focus     = ["Recommender systems", "RAG & multi-agent LLMs", "MLOps"]
    currently = "Shipping anomaly detection on live industrial sensor streams"
    learning  = ["Graph ML at scale", "Low-latency inference"]

    def philosophy(self):
        return "If it only works in the notebook, it doesn't work."
```

## 🚀 Featured work

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🎙️ <a href="https://github.com/manthan291999/Roxi-a-real-time-AI-meeting-copilot">Roxi</a> — real-time AI meeting copilot</h3>
      <p>Desktop copilot that listens to <b>both sides</b> of any Zoom / Meet / Teams call and surfaces explanations, action items, risks and suggested replies <i>while the meeting is still happening</i>.</p>
      <ul>
        <li>Rust-native <b>multi-agent pipeline</b> with a chit-chat gate and complexity routing to keep LLM cost down</li>
        <li>Streaming STT (AssemblyAI v3, Speechmatics fallback) + speaker diarization via voice embeddings</li>
        <li><b>Ask Roxi</b>: LangGraph adaptive RAG over meeting history (BM25 / FTS5), documents (Qdrant) and the web</li>
      </ul>
      <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white">
      <img src="https://img.shields.io/badge/Tauri_v2-24C8DB?style=flat-square&logo=tauri&logoColor=white">
      <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white">
      <img src="https://img.shields.io/badge/Qdrant-DC244C?style=flat-square">
    </td>
    <td width="50%" valign="top">
      <h3>🎯 <a href="https://github.com/manthan291999/Recengine">Hybrid recommendation engine</a></h3>
      <p>Collaborative filtering + deep learning + <b>graph neural networks</b>, with an LLM layer that explains <i>why</i> something was recommended.</p>
      <ul>
        <li>Designed for <b>cold-start</b> users and items and sparse interaction data</li>
        <li>Multiple candidate generators blended by a single hybrid ranker</li>
        <li>Natural-language explanations grounded in the signals that drove each score</li>
      </ul>
      <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white">
      <img src="https://img.shields.io/badge/GNN-8957e5?style=flat-square">
      <img src="https://img.shields.io/badge/LLM_explanations-1f6feb?style=flat-square">
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>📈 <a href="https://github.com/manthan291999/PredictML-Studio">PredictML Studio</a> — explainable AutoML</h3>
      <p>End-to-end ML platform for tabular data: automated model selection, global and local explainability, and GPT-4 written narratives of what the model learned.</p>
      <ul>
        <li><b>SHAP</b> and <b>LIME</b> explanations, per prediction and per model</li>
        <li>FastAPI + scikit-learn backend, React + Vite frontend</li>
      </ul>
      <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white">
      <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white">
      <img src="https://img.shields.io/badge/SHAP_·_LIME-6e40c9?style=flat-square">
    </td>
    <td width="50%" valign="top">
      <h3>🏭 Sensor anomaly detection <sub>(in production)</sub></h3>
      <p>ETL pipelines and deep learning models monitoring equipment efficiency on <b>live industrial sensor streams</b>.</p>
      <ul>
        <li>From raw, noisy sensor data to reliable features</li>
        <li>Models that flag drops in efficiency before they become downtime</li>
      </ul>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
      <img src="https://img.shields.io/badge/ETL-0e8a16?style=flat-square">
      <img src="https://img.shields.io/badge/Time_series-b60205?style=flat-square">
    </td>
  </tr>
</table>

## 🏗️ Under the hood

<details open>
<summary><b>How Roxi turns live audio into insights</b></summary>
<br>

```mermaid
flowchart LR
    A["🎤 Mic + system audio<br/>CoreAudio · BlackHole"] --> B["⚙️ Rust core<br/>Tauri v2"]
    B --> C["📝 Streaming STT<br/>AssemblyAI v3 ↺ Speechmatics"]
    C --> D["🗣️ Speaker diarization<br/>voice embeddings"]
    D --> E{"Chit-chat<br/>gate"}
    E -- small talk --> X["🗑️ dropped locally"]
    E -- signal --> F["🧭 Context manager<br/>importance · complexity"]
    F -- simple --> G["⚡ Light agent"]
    F -- complex --> H["🧠 Parallel agents<br/>technical · risk · summary"]
    G --> I["🪟 Live overlay<br/>insights · actions · replies"]
    H --> I
    D --> J[("SQLite FTS5")]
    J --> K["💬 Ask Roxi<br/>LangGraph adaptive RAG"]
    Q[("Qdrant")] --> K
    W["🌐 Web search"] --> K

    classDef core fill:#0d1117,stroke:#7ee787,color:#e6edf3
    classDef agent fill:#0d1117,stroke:#d2a8ff,color:#e6edf3
    classDef store fill:#0d1117,stroke:#79c0ff,color:#e6edf3
    class A,B,C,D core
    class E,F,G,H,K agent
    class J,Q,W,I,X store
```

</details>

<details>
<summary><b>How the hybrid recommender scores and explains</b></summary>
<br>

```mermaid
flowchart LR
    U["👤 User–item interactions"] --> CF["Collaborative filtering"]
    U --> DL["Deep model<br/>user / item embeddings"]
    U --> G["Graph neural network<br/>user–item graph"]
    M["🏷️ Item & user metadata"] --> CS["Content features<br/>for cold-start"]
    CF --> R{"Hybrid ranker"}
    DL --> R
    G --> R
    CS --> R
    R --> T["🎯 Top-K recommendations"]
    R --> L["🤖 LLM explainer"]
    L --> T

    classDef core fill:#0d1117,stroke:#7ee787,color:#e6edf3
    classDef model fill:#0d1117,stroke:#d2a8ff,color:#e6edf3
    class U,M,T core
    class CF,DL,G,CS,R,L model
```

</details>

## 🛠 Toolbox

<table>
  <tr>
    <td align="right"><b>Languages</b></td>
    <td><img src="https://skillicons.dev/icons?i=py,rust,ts,kotlin,postgres,sqlite" height="40"></td>
  </tr>
  <tr>
    <td align="right"><b>ML & data</b></td>
    <td>
      <img src="https://skillicons.dev/icons?i=pytorch,sklearn" height="40">
      <img src="https://img.shields.io/badge/XGBoost-337AB7?style=for-the-badge&logo=xgboost&logoColor=white">
      <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
      <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
    </td>
  </tr>
  <tr>
    <td align="right"><b>LLMs & agents</b></td>
    <td>
      <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white">
      <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white">
      <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white">
      <img src="https://img.shields.io/badge/Qdrant-DC244C?style=for-the-badge">
      <img src="https://img.shields.io/badge/AssemblyAI-2545D3?style=for-the-badge">
    </td>
  </tr>
  <tr>
    <td align="right"><b>Apps & APIs</b></td>
    <td><img src="https://skillicons.dev/icons?i=fastapi,react,tauri,nodejs,vite" height="40"></td>
  </tr>
  <tr>
    <td align="right"><b>Infra & workflow</b></td>
    <td>
      <img src="https://skillicons.dev/icons?i=docker,git,github,linux" height="40">
      <img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white">
      <img src="https://img.shields.io/badge/Confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white">
    </td>
  </tr>
</table>

## 📊 GitHub stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=manthan291999&show_icons=true&hide_border=true&include_all_commits=true&theme=tokyonight&bg_color=00000000&title_color=7ee787&icon_color=79c0ff">
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=manthan291999&layout=compact&hide_border=true&langs_count=6&theme=tokyonight&bg_color=00000000&title_color=7ee787">
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=manthan291999&theme=tokyonight&hide_border=true&background=00000000&ring=7ee787&fire=ff7b72&currStreakLabel=7ee787">
</p>

## 🤝 Let's connect

<p align="center">
  <b>Happy to talk recommender systems, applied LLM work, or anything involving messy real-world data.</b><br>
  <sub>⭐ If something here helps you, a star goes a long way.</sub>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7ee787,50:79c0ff,100:d2a8ff&height=120&section=footer" width="100%">
