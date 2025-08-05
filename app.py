from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            inputs = [
                float(request.form['mean_radius']),
                float(request.form['mean_texture'])
            ]
            features = np.array([inputs])
            features_scaled = scaler.transform(features)
            pred = model.predict(features_scaled)[0]
            prediction = "Benign ✅" if pred == 1 else "Malignant ❌"
        except:
            prediction = "Invalid input. Please enter valid numbers."

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
