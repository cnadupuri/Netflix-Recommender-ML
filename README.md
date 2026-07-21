# 🎬 Netflix Recommendation System (MLOps)

<p align="center">
  <img src="images/banner.png" alt="Netflix Recommendation Banner" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-2088FF?logo=githubactions)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## 🌐 Live Demo

🔗 **https://netflix-recommender-ml.onrender.com**

---

# 📖 Project Overview

This project is an end-to-end **Machine Learning Recommendation System** that predicts Netflix recommendations based on user inputs.

The application is built with **Python, XGBoost, Streamlit**, containerized using **Docker**, automated using **GitHub Actions**, and deployed on **Render**.

---

# 🚀 Features

- 🎬 Netflix Recommendation Prediction
- 📊 Machine Learning Model
- ⚡ Streamlit Web Interface
- 🐳 Docker Container
- 🔄 GitHub Actions CI Pipeline
- 📦 Docker Hub Integration
- ☁️ Render Deployment
- 📈 Production Ready

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| ML | Scikit-learn, XGBoost |
| UI | Streamlit |
| Container | Docker |
| CI | GitHub Actions |
| Registry | Docker Hub |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 🏗 Architecture

```text
                 Netflix Dataset
                        │
                        ▼
               Data Preprocessing
                        │
                        ▼
               Feature Engineering
                        │
                        ▼
                XGBoost Model
                        │
                        ▼
            model.pkl + preprocessor.pkl
                        │
                        ▼
                Streamlit Application
                        │
                        ▼
                    Docker Image
                        │
                        ▼
                GitHub Repository
                        │
                        ▼
             GitHub Actions (CI/CD)
                        │
                        ▼
                  Docker Hub
                        │
                        ▼
                     Render
                        │
                        ▼
                 Live Application
```

---

# 📂 Project Structure

```text
Netflix-Recommender-ML
│
├── artifacts
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── images
│   ├── banner.png
│   ├── home.png
│   ├── prediction.png
│   ├── github-actions.png
│   └── architecture.png
│
├── app.py
├── requirements.txt
├── Dockerfile
├── render.yaml
├── .github
│    └── workflows
│          └── ci.yml
│
└── README.md
```

---

# 📸 Screenshots

## 🏠 Home Page

![Home](images/home.png)

---

## 🎯 Prediction Result

![Prediction](images/prediction.png)

---

## 🔄 GitHub Actions

![CI Pipeline](images/github-actions.png)

---

## ☁️ Render Deployment

![Render](images/render.png)

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Netflix-Recommender-ML.git
```

Move into the project

```bash
cd Netflix-Recommender-ML
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run locally

```bash
streamlit run app.py
```

---

# 🐳 Docker

Build Docker Image

```bash
docker build -t netflix-recommender .
```

Run Docker Container

```bash
docker run -p 8501:8501 netflix-recommender
```

---

# 🔄 CI/CD Pipeline

The pipeline automatically performs:

- Repository Checkout
- Install Dependencies
- Verify Model Files
- Run Tests
- Build Docker Image
- Push Docker Image
- Deploy to Render

---

# 📊 Model Information

| Model | XGBoost |
|---------|----------|
| Framework | Scikit-learn |
| Target | Recommendation |
| Dataset | Netflix Titles |

---

# 👨‍💻 Author

**Chaitanya**

GitHub:
https://github.com/YOUR_GITHUB_USERNAME

---
## Home Page

![Home](images/home.png)

## Prediction Result

![Prediction](images/prediction.png)

## GitHub Actions

![GitHub Actions](images/github-actions.png)

## Render Deployment

![Render](images/render.png)

# ⭐ Support

If you like this project, don't forget to ⭐ the repository.

---

# 📜 License

This project is licensed under the MIT License.
