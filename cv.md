# Mahmoud Alyosify — CV

## Contact

- **Email:** mahmoud.alyosify@gmail.com
- **Phone:** +20 114 555 7959
- **Location:** New Cairo, Egypt · Open to Relocation
- **LinkedIn:** [linkedin.com/in/mahmoudalyosify](https://linkedin.com/in/mahmoudalyosify)
- **GitHub:** [github.com/MahmoudAlyosify](https://github.com/MahmoudAlyosify)
- **Portfolio:** [mahmoudalyosifysite.github.io](https://mahmoudalyosifysite.github.io/)
- **Hugging Face:** [huggingface.co/mahmoudalyosify](https://huggingface.co/mahmoudalyosify)
- **Kaggle:** [kaggle.com/mahmoudalyosify](https://kaggle.com/mahmoudalyosify)

## Professional Summary

AI & Machine Learning Engineer building end-to-end intelligent systems across **LLM fine-tuning and inference optimisation**, **multi-agent systems**, **self-supervised learning**, and **reinforcement learning**. Completing an **MSc in Artificial Intelligence at Queen's University, Canada** on a **Digilians Presidential Scholarship**, with a master's research project on training-free, decoding-time efficiency for large language models. Delivered production-oriented systems on **AWS** spanning autonomous OSINT threat intelligence, retrieval-ready vision pipelines, deep-RL cloud autoscaling, and satellite collision risk prediction; taught **10,000+ learners** (**700K+ views**). Seeking AI/ML engineering roles in LLM systems, MLOps, and efficient inference at scale.

## Education

### MSc in Artificial Intelligence — Queen's University, Kingston, Canada
**Sep 2025 – Present** | Expected 2026

- **Digilians Presidential Scholarship** — competitive national AI graduate fellowship.
- **Master's Research Project (CISC 898):** *Verbosity-Aware Decoding for Token-Efficient Language Model Inference* — Supervisor: Dr. Rahatara Ferdousi.
- Coursework: **Large Language Models, Generative AI, Deep Learning, Reinforcement Learning, Cloud Computing, End-to-End ML Pipelines**.

### B.Sc. Computer & Information Science (Bioinformatics) — Assiut University, Egypt
**Sep 2019 – Jul 2023** | GPA: 3.53 / 4.00

- Graduation Project: [**Vitalism Solution**](https://vitalismsolution.github.io/) — contactless vital-sign estimation via rPPG. **Grade A+**; **Semi-Finalist, Microsoft Imagine Cup 2023**.

## Technical Skills

| Category | Skills |
|----------|--------|
| **AI & LLM Systems** | Large Language Models, Fine-Tuning (LoRA, QLoRA, PEFT), RAG, Transformers, Hugging Face, LangChain, Multi-Agent Systems, Agentic Workflows, Prompt Engineering, Custom Decoding, Knowledge Graphs |
| **ML & Deep Learning** | PyTorch, TensorFlow, Scikit-learn, XGBoost, LightGBM, CNNs, Computer Vision, NLP, Self-Supervised & Contrastive Learning, Reinforcement Learning (PPO, DQN), Optuna, SHAP |
| **Data & MLOps** | Pandas, NumPy, PySpark, ETL Pipelines, Feature Engineering, AWS, Docker, CI/CD, ONNX, FastAPI, Streamlit, FAISS, ChromaDB, MySQL, MongoDB, Git/GitHub, Linux |
| **Evaluation & Research** | Benchmarking (MT-Bench, XSum, SQuAD-v2), BERTScore, ROUGE, LLM-as-Judge, Statistical Testing, Ablation Studies, Reproducible Experiment Design |
| **Programming** | Python, C++, C, C#, Go, JavaScript, SQL, MATLAB, Bash |

## Professional Experience

### Machine Learning Instructor — National Telecommunication Institute (NTI)
**Jul 2025 – Sep 2025** | Cairo, Egypt

- Delivered a **90-hour** hands-on ML program for engineering and CS students covering supervised learning, PCA, and neural networks, with practical lab sessions throughout.

### AI in Cybersecurity Intern — e& Egypt (via NTI, On-the-Job Training)
**Jun 2025 – Jul 2025** | Cairo, Egypt

- Applied AI-driven security tooling across threat intelligence, digital forensics, and enterprise security analysis.

### Systems Engineer (Military Service) — National Company for Roads Building & Development
**Feb 2024 – Mar 2025** | Cairo, Egypt

- Supported backend systems for national toll infrastructure serving **50%+ of Egyptian vehicles** across **70%+ of national roads**.
- Co-developed an internal data-management and reporting desktop application in **C#, .NET, Entity Framework, SQL Server,** and **Crystal Reports**.

### Online Instructor — AI, Algorithms & Data Science — Udemy & YouTube
**2020 – Present** | Remote

- Built and taught Arabic-language technical curricula reaching **10,000+ learners** and **700K+ YouTube views**.

## Selected Research & Engineering Projects

### Verbosity-Aware Decoding for Token-Efficient Language Model Inference
**MSc Research Project (CISC 898), Queen's University · Supervisor: Dr. Rahatara Ferdousi** | July 2026 – Present
[GitHub](https://github.com/MahmoudAlyosify/minimal-lm)

- Designed a **training-free LogitsProcessor** that cuts generated tokens at **decoding time** by combining stop-token, n-gram-repetition and semantic-redundancy signals under an **entropy-driven gate** — no retraining, no architecture change, no KV-cache or attention overhead.
- Validated across **three open-weight model families** (Mistral-7B-Instruct, Llama-3.1-8B-Instruct, Qwen2.5-3B-Instruct) on **MT-Bench, YapBench, XSum** and **SQuAD-v2**.
- Built a **pre-registered evaluation protocol** proving semantic preservation through paired **non-inferiority testing** (BERTScore, ROUGE, exact-match/F1, length-controlled LLM judge) alongside token reduction, latency (TTFT / inter-token) and **GPU energy** via NVML — fully deterministic and reproducible on pinned AWS GPU instances.

### HORUS Sentinel — Autonomous Multi-Agent OSINT & Threat-Intelligence Platform
**Python · Multi-Agent Systems · Fine-Tuned LLM · Knowledge Graphs · Self-Hosted Inference** | May 2026 – July 2026
[GitHub](https://github.com/MahmoudAlyosify/horus-sentinel)

- Architected an autonomous intelligence analyst in which a **swarm of specialised passive agents** continuously collects open-source intelligence and correlates every finding into a **living Intelligence Knowledge Graph**.
- A **self-hosted, fine-tuned language model** reasons over the graph to deliver **prioritised, evidence-backed intelligence reports**, compressing hours of manual analyst work into minutes.

### RL-Cloud-Autoscaler — Autonomous Cloud Resource Provisioning via Deep Reinforcement Learning
**Python · PPO · DQN · Gymnasium · Cloud Cost Optimisation** | May 2026 – Jun 2026
[GitHub](https://github.com/MahmoudAlyosify/RL-Cloud-Autoscaler)

- Built a **custom Gymnasium environment** simulating cloud workload dynamics and trained **PPO** and **DQN** agents to make autonomous provisioning decisions in real time.
- Optimised the **cost–latency trade-off** under fluctuating demand, benchmarking both algorithms against static and reactive threshold-based autoscaling baselines.

### SimCLR-Vision-SSL — Self-Supervised Contrastive Representation Learning
**PyTorch · SimCLR · SupCon · ONNX · FAISS** | Apr 2026 – Jun 2026
[GitHub](https://github.com/MahmoudAlyosify/SimCLR-Vision-SSL)

- Built a self-supervised vision pipeline with a **42-experiment augmentation sweep**, a semi-supervised **SupCon** extension and deployment-ready **ONNX/FAISS** retrieval, reaching **84.30% top-1 accuracy** on classification and image-retrieval evaluation.

### Horus-OSINT — Cloud-Based Threat-Intelligence Assistant
**Python · Meta-Llama-3-8B · Fine-Tuning · AWS** | Mar 2026 – Apr 2026
[GitHub](https://github.com/MahmoudAlyosify/Horus-OSINT)

- Fine-tuned **Meta-Llama-3-8B** on **159,826** GTD/GDELT records and deployed it on **AWS** as an interactive assistant for querying global event and terrorism intelligence.

### Additional Projects

- **[Automated Multimodal Agent](https://github.com/MahmoudAlyosify/Automated-Multimodal-Agent-PDF-to-Narrated-PowerPoint)** — autonomous agentic workflow converting PDFs into narrated PowerPoint decks by coordinating content extraction, slide generation and audio narration end to end.
- **[SCRAP](https://github.com/MahmoudAlyosify/SCRAP-Satellite-Collision-Risk-Assessment-and-Prediction)** — supervised ML pipeline predicting satellite collision risk from conjunction data available **48+ hours** before closest approach.
- **[Human vs. Agentic Pull Requests](https://github.com/MahmoudAlyosify/Analyzing-Review-Effort-in-Human-vs.-Agentic-Pull-Requests)** — reproducible GitHub-mining pipeline comparing code-review effort on agent-generated versus human-authored pull requests.
- **[AudioShield](https://github.com/MahmoudAlyosify/AudioShield)** — CNN-based deepfake audio detection served through a Streamlit application.
- Also: Vitalism Solution (rPPG) · Diabetes Onset Prediction · ATM Transaction Analysis · E-Commerce Web App · Mini-FAT File System.

## Certifications

| Certification | Issuer |
|---------------|--------|
| AWS Academy — ML Foundations, ML for NLP, Data Engineering | Amazon |
| Machine Learning Specialization | DeepLearning.AI |
| HCIP — AI | Huawei |
| Microsoft Certified: Data Analyst Associate | Microsoft |
| AI in Cybersecurity (420 hrs) | NTI |
| ML Internship (200 hrs) | ITIDA / Egypt Makes Electronics |
| Generative AI & Prompt Engineering | IBM / Coursera |
| Full Stack Diploma — .NET & Angular | Route Academy |

## Achievements & Awards

- **1st Place** — Smart Cities Hackathon 2022
- **Semi-Finalist** — Microsoft Imagine Cup 2023
- **Ideal Student Award** — Assiut University, 2022–2023
- **1st Place** — Science & Technology Content Competition

## Leadership & Languages

- **Secretary**, Higher Scientific & Technological Committee, Student Union, Assiut University
- **Ambassador**, Information Technology Institute (ITI), Assiut
- **Volunteer Team Leader**, USAID University Center for Career Development

### Languages
- **Arabic:** Native
- **English:** Professional Working Proficiency
