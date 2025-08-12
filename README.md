# Breast Cancer Prediction (SVM)

This is a simple web app that predicts whether a breast tumor is **benign** or **malignant** based on **two key features** from the **Breast Cancer Wisconsin dataset**.  
It uses a **Support Vector Machine (SVM)** model trained with scikit-learn.

---

## Features Used
- **Mean Radius** – Average size of tumor cells
- **Mean Texture** – Variation in cell surface texture

---

## Tech Stack
- **Python 3**
- **Flask** 
- **HTML/CSS** 
- **scikit-learn** 
- **StandardScaler**
  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

## Project Structure

```
breast-cancer-svm-app/
│
├── train_model.py 
├── model.pkl 
├── scaler.pkl 
├── app.py 
│
├── templates/
│ └── index.html 
│
├── static/
│ └── style.css 
│
└── README.md 
```

## Installation

### 1. Install Dependencies
```bash
pip install flask scikit-learn pandas numpy
```

### 2. Train the Model (if not already)
```bash
python model.py
```

### 3. Run the Flask App
```bash
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## Sample UI

**Input**:

<img width="663" height="587" alt="image" src="https://github.com/user-attachments/assets/58f3e7ac-e6f8-4393-b688-1801694ab30f" />

**Output**:

<img width="663" height="587" alt="image" src="https://github.com/user-attachments/assets/444efd72-4e65-4def-817e-bf38959948d1" />

---
