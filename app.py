from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model globally
model = None
model_path = os.path.abspath("autism_model.pkl")

print("🧪 FILES IN CURRENT DIRECTORY:")
print(os.listdir("."))

try:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model: {e}")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template("index.html", prediction_text="Error: Model is not loaded.")

    try:
        # Collect input features from form
        features = [float(request.form[f"A{i}_Score"]) for i in range(1, 11)]
        features.append(float(request.form["age"]))
        features.append(float(request.form["jundice"]))
        features.append(float(request.form["austim"]))

        # Format input for prediction
        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)[0]

        result = "Likely ASD" if prediction == 1 else "No ASD traits detected"
        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error during prediction: {e}")

if __name__ == "__main__":
    # Required for Cloud Run — 0.0.0.0 and dynamic port
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
