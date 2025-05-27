# 💖 Heart Disease Prediction – MLOps Pipeline

This project implements an end-to-end MLOps pipeline for predicting heart disease using machine learning. It includes preprocessing, model training, deployment via Flask API, CI/CD automation via GitHub Actions, and Docker-based containerization.

---

## 🛠 Project Structure

├── data/
│ ├── heart.csv
│ └── heart_clean.csv
├── models/
│ └── heart_model.pkl
├── src/
│ ├── preprocessing/
│ │ └── preprocess.py
│ ├── training/
│ │ └── train_model.py
│ └── api/
│ └── app.py
├── tests/
│ ├── test_model.py
│ └── test_preprocess.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│ └── workflows/
│ └── main.yml
└── README.md

---

## ⚙️ CI/CD Workflow

This project uses **GitHub Actions** to automate:

- ✅ Code checkout and Python setup  
- ✅ Install dependencies from `requirements.txt`  
- ✅ Preprocess dataset using `preprocess.py`  
- ✅ Train model and save it as `heart_model.pkl`  
- ✅ Run unit tests for model and data quality  
- ✅ Deploy via Docker or Google VM manually  

---

## 🧪 Unit Testing Strategy

- `test_model.py`: Validates model file is present and loadable.
- `test_preprocess.py`: Confirms data is cleaned, no nulls, proper column structure.

---

## 🔁 Retraining Strategy

- Workflow retriggers when changes are pushed to `data/` or `src/training/`.
- Model will retrain automatically via GitHub Actions.

---

## 🐳 Deployment

- Model API served with **Flask** from `src/api/app.py`
- Hosted on a **Google Cloud VM** at:  
  👉 http://34.140.129.239:5000

- Docker build & run:
```bash
docker build -t heart-api .
docker run -d -p 5000:5000 heart-api

---

## 👤 Author

**Richa Mandal**  
MSc in Big Data Analytics  
Atlantic Technological University – Letterkenny
