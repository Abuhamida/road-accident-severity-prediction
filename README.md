# Road Accident Severity Prediction 🚗💥

This project predicts the severity of road accidents based on various input features using a machine learning model deployed with Flask. The model leverages Random Forest classification for robust predictions. It also includes unit tests to ensure the correctness of the deployment.

---

## 🚀 Features

- Predicts accident severity based on user-provided details.
- Flask-based web interface for user interaction.
- Unit tests for validating endpoints and model predictions.
- Easy-to-follow deployment instructions.

---

## 💂️ Project Structure

```
├── app.py                 # Main Flask application
├── best_model.pkl         # Pre-trained machine learning model
├── label_encoders.pkl     # Encoders for categorical variables
├── scaler.pkl             # Scaler for feature normalization
├── templates/
│   └── index.html         # Frontend for user input and displaying predictions
├── tests      
│   └── test_app.py        # Unit tests for the Flask application
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 💻 Setup Instructions

### Prerequisites:
- Python 3.8+
- pip

### 🔧 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Abuhamida/road-accident-severity-prediction.git
   cd road-accident-severity-prediction
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\\Scripts\\activate     # On Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application:**
   ```bash
   python app.py
   ```

   The app will run at: `http://127.0.0.1:5000/`

---

## 🤍 Running Tests

Unit tests ensure the app works as expected:

```bash
python -m unittest tests/test_app.py
```

Check the console output to ensure all tests pass successfully.

---

## 💡 Usage Guide

- Navigate to the homepage (`/`).
- Fill in the form fields such as number of vehicles, time, road class, etc.
- Click the **Predict** button.
- View the predicted accident severity instantly.

---

## 🖼️ Screenshots

### **Homepage Interface:**
![Homepage Screenshot](https://raw.githubusercontent.com/Abuhamida/road-accident-severity-prediction/main/images/home.jpeg)

### **Prediction Result:**
![Prediction Screenshot](https://raw.githubusercontent.com/Abuhamida/road-accident-severity-prediction/main/images/predict.jpeg)

---

## 💼 Documentation

For detailed API documentation, model performance, setup guide, and test results, refer to the full **Documentation PDF**.

---

## 🛠️ Troubleshooting

- **App Not Starting?**
  - Ensure `best_model.pkl`, `label_encoders.pkl`, and `scaler.pkl` are present in the root directory.
  - Confirm Python version compatibility.

- **Test Failures?**
  - Verify that form keys in `test_app.py` match those expected in `app.py`.
  - Confirm that the Flask app is running before executing tests.

---

## 🤝 Contributing

Contributions are welcome! Here’s how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## 🤝 Connect with Me
- 📧 **Email**: mohamedabuhamida3@gamil.com
- 🌐 [**Portfolio**](https://mohamed-abuhamida.vercel.app/)
- 💼 [**LinkedIn**](https://www.linkedin.com/in/mohammed-abuhamida-969693220/)
- 🐙 [**GitHub**](https://github.com/Abuhamida)

---

> ⚡ *Feel free to contribute by creating issues or submitting pull requests to improve this project!* 🚀


