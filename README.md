# 🧠 Machine Learning Zoomcamp – Homework & Projects

This repository contains my homework assignments, projects, and notes for [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp), a free 4-month practical course on **machine learning engineering** by DataTalks.Club.  

The course covers the full ML lifecycle — from model training and evaluation to deployment and production-ready serving.

---

## 📚 Course Overview

**Topics covered:**
- Introduction to ML & CRISP-DM
- Regression & classification models (scikit-learn, XGBoost)
- Evaluation metrics (precision, recall, F1, AUC, etc.)
- Feature engineering & model selection
- Deploying ML with FastAPI, Docker, and cloud platforms
- Decision trees & ensemble methods
- Neural networks & deep learning (TensorFlow & PyTorch)
- Serverless ML deployment
- Kubernetes & TensorFlow Serving
- Capstone project

---

## 🗂 Repository Structure

```bash
ml-zoomcamp-homework/
│
├── 01-intro/          # Homework & notes (Intro to ML, CRISP-DM)
├── 02-regression/     # Car price prediction with linear regression
├── 03-classification/ # Customer churn prediction with logistic regression
├── 04-metrics/        # Evaluation metrics and imbalanced datasets
├── 05-deployment/     # Deploy models with FastAPI + Docker
├── 06-trees/          # Decision trees, Random Forest, XGBoost
├── 08-deep-learning/  # Tensorflow, Keras
├── 09-serverless/     # Serverless ML deployment
├── 10-kubernetes/     # Kubernetes & TensorFlow Serving
├── 11-kserve/         # EKS, KServe
│
├── midterm-project/   # End-to-end ML project (find dataset, train & deploy)
├── capstone-project/  # Final project with deployment
│
├── requirements.txt   # Dependencies
└── README.md          # This file
```

---

## 🚀 How to Run

Clone this repo and set up dependencies:

```bash
git clone https://github.com/<your-username>/ml-zoomcamp-homework.git
cd ml-zoomcamp-homework
pip install -r requirements.txt
```

Each module has its own `README.md` with instructions. Example:

```bash
cd module02-regression
jupyter notebook car_price_prediction.ipynb
```

---

## 📊 Highlights

- **Module 2 – Regression:** Built a linear regression model for car price prediction; experimented with feature engineering & regularization.  
- **Module 3 – Classification:** Created a logistic regression model for churn prediction; learned about categorical encoding & feature selection.  
- **Module 5 – Deployment:** Packaged a model into a REST API with FastAPI and Docker.  
- **Midterm Project:** (To be filled once complete — e.g., fraud detection, house price prediction, etc.)  
- **Capstone Project:** (To be filled once complete — end-to-end ML system with deployment).  

---

## 🛠 Tech Stack

- **Languages:** Python 3.10+  
- **Libraries:** scikit-learn, XGBoost, pandas, numpy, matplotlib, seaborn  
- **Deployment:** FastAPI, Docker, AWS / GCP  
- **Deep Learning:** TensorFlow, Keras, PyTorch  
- **MLOps Tools:** Kubernetes, TensorFlow Serving  

---

## 🎯 Goals

- Apply ML engineering concepts beyond just model training  
- Practice deploying models into real-world environments  
- Build a portfolio of end-to-end ML projects  

---

## 🙌 Acknowledgements

- [DataTalks.Club](https://datatalks.club) for providing ML Zoomcamp  
- [Alexey Grigorev](https://github.com/alexeygrigorev) and the ML Zoomcamp community for materials and support  
