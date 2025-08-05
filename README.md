# 🩺 Breast Cancer Prediction (SVM)

This is a simple web app that predicts whether a breast tumor is **benign** or **malignant** based on **two key features** from the **Breast Cancer Wisconsin dataset**.  
It uses a **Support Vector Machine (SVM)** model trained with scikit-learn.

---

## 📊 Features Used
- **Mean Radius** – Average size of tumor cells
- **Mean Texture** – Variation in cell surface texture

---

## 🧠 Tech Stack
- **Python 3**
- **Flask** (web backend)
- **HTML/CSS** (frontend UI)
- **scikit-learn** (machine learning)
- **StandardScaler** (feature scaling)

---

## 📁 Project Structure

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

## 🔧 Installation

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

## 🖥️ Sample UI

**Input**:

<img width="663" height="587" alt="image" src="https://github.com/user-attachments/assets/58f3e7ac-e6f8-4393-b688-1801694ab30f" />

**Output**:

<img width="663" height="587" alt="image" src="https://github.com/user-attachments/assets/444efd72-4e65-4def-817e-bf38959948d1" />

---

## 🙋‍♂️ Author

**Hari Prasath S**  
[GitHub Profile](https://github.com/hariprasath2105)

---

## 📘 License

This project is open source and free to use.
