# Airline-satisfaction-mlfastapi
A machine learning project using MLflow and FastAPI for airline satisfaction prediction.

---

## 📝 Project Overview

1. **Training Models**:  
   - The dataset `Invistico_Airline.csv` is used.  
   - Four models are trained: Logistic Regression, Decision Tree, Random Forest, and SVM.  
   - Random Forest achieved the highest accuracy and is selected as the production model.

2. **MLflow Tracking**:  
   - All models and their metrics (accuracy, F1-score) are tracked using MLflow.  
   - Models are logged with parameters and input examples for reproducibility.  

3. **Deployment**:  
   - The selected Random Forest model is deployed using **FastAPI**.  
   - Interactive API documentation is available via Swagger (`/docs` endpoint).

---

## 📁 Project Structure

airline-satisfaction-mlfastapi/

── app.py # FastAPI application

── airline.ipynb # Notebook for training models & MLflow tracking

── RF_airline.joblib # Saved Random Forest model

── requirements.txt # Python dependencies

── README.md # Project documentation


---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/airline-satisfaction-mlfastapi.git
cd airline-satisfaction-mlfastapi
```
2. (Optional) Create a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Running MLflow

1. Start the MLflow UI:
```bash
mlflow ui --backend-store-uri ./mlruns
```
2. Open http://127.0.0.1:5000
 in your browser to view logged experiments.

## 🏃 Running FastAPI
1.Start the server:
```bash
uvicorn app:app --reload
```
2. Open http://127.0.0.1:8000/docs
 to test the API via Swagger.
3. Use the /predict POST endpoint to send passenger details and get satisfaction predictions.

---

### 🧠 Example Request (for Swagger or FastAPI)

```json
{
  "Customer_Type": "Loyal Customer",
  "Age": 35,
  "Type_of_Travel": "Business",
  "Class_": "Eco",
  "Flight_Distance": 500,
  "Seat_comfort": 4,
  "Departure_Arrival_time_convenient": 4,
  "Food_and_drink": 4,
  "Gate_location": 4,
  "Inflight_wifi_service": 4,
  "Inflight_entertainment": 4,
  "Online_support": 4,
  "Ease_of_Online_booking": 4,
  "Onboard_service": 4,
  "Leg_room_service": 4,
  "Baggage_handling": 4,
  "Checkin_service": 4,
  "Cleanliness": 4,
  "Online_boarding": 4,
  "Departure_Delay_in_Minutes": 0,
  "Arrival_Delay_in_Minutes": 0
}
```
Response Example:
```json
{
  "prediction_text": "satisfied",
  "prediction_numeric": 1
}
```
---

## ✅ Key Features

- 🧠 **ML Models Training with Scikit-learn**  
  Includes preprocessing, model building, and evaluation using algorithms such as Random Forest and Logistic Regression.

- 📊 **Experiment Tracking with MLflow**  
  Automatically logs model parameters, metrics, and artifacts for easy comparison and reproducibility.

- ⚡ **FastAPI Deployment**  
  Provides a lightweight and high-performance API for real-time predictions.

- 💻 **Interactive Swagger UI**  
  Test your API endpoints directly from the browser with a clean interface.

- 🔁 **Easy Reproducibility and Extensibility**  
  Well-structured project allowing quick integration of new models or features.

- 🧾 **Clear Dataset Reference**  
  Uses the publicly available **Invistico Airline Satisfaction dataset** for transparency and learning.

---

## 📌 Notes

- Ensure the file **`RF_airline.joblib`** is in the same folder as **`app.py`** before running the FastAPI server.  
- The dataset is publicly available here:  
  👉 [Invistico Airline Dataset (CSV)](https://raw.githubusercontent.com/ManonYa09/MachineLearningT3/refs/heads/main/Dataset/Invistico_Airline.csv)  
- Start the FastAPI app with:
  ```bash
  uvicorn app:app --reload

