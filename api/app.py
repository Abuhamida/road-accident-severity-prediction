import pickle
import numpy as np
import os
from flask import Flask, request, render_template

# Define file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoder.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# Load the trained model, label encoders, and scaler
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    label_encoders = pickle.load(f)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

# Define categorical columns (ensure these match the training phase)
categorical_columns = [
    "1st Road Class", "Road Surface", "Lighting Conditions", 
    "Weather Conditions", "Casualty Severity", "Sex of Casualty", "Type of Vehicle", 
    "age_group", "vehicle_group"
]

# Flask App
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    predicted_class_name = None  # Ensure variable is always defined

    if request.method == "POST":
        try:
            # Get form data
            form_data = {
                "Number of Vehicles": request.form.get("num_vehicles"),
                "Time (24hr)": request.form.get("time"),
                "1st Road Class": request.form.get("road_class"),
                "Road Surface": request.form.get("road_surface"),
                "Lighting Conditions": request.form.get("lighting"),
                "Weather Conditions": request.form.get("weather"),
                "Casualty Severity": request.form.get("casualty_severity"),
                "Sex of Casualty": request.form.get("sex_of_casualty"),
                "Age of Casualty": request.form.get("age_of_casualty"),
                "Type of Vehicle": request.form.get("type_of_vehicle"),
                "age_group": request.form.get("age_group"),
                "vehicle_group": request.form.get("vehicle_group")
            }

            # Encode categorical features
            for col in categorical_columns:
                if col in label_encoders:
                    form_data[col] = label_encoders[col].transform([form_data[col]])[0]
                else:
                    raise KeyError(f"Label encoder for '{col}' not found.")

            # Prepare input features
            numerical_features = [
                float(form_data["Number of Vehicles"]),
                float(form_data["Time (24hr)"]),
                float(form_data["Age of Casualty"]),
            ]

            features_array = np.array([[  
    *numerical_features,  # Add numerical features
    *[form_data[col] for col in categorical_columns]  # Add encoded categorical features
]])
            processed_data = scaler.transform(features_array)
            prediction_code = model.predict(processed_data)[0]
            predicted_class_name = label_encoders["Casualty Class"].inverse_transform([prediction_code])[0]
        
        except Exception as e:
            error = str(e)

    return render_template("index.html", prediction=predicted_class_name, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
