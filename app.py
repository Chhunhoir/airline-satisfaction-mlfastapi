# app.py
import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

# ----------------------------
# FastAPI instance
app = FastAPI(title="Airline Satisfaction Prediction API")

# ----------------------------
# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'RF_airline.joblib')

try:
    loaded_model = joblib.load(model_path)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    raise e

# ----------------------------
# Pydantic model
class Passenger(BaseModel):
    Customer_Type: Literal["Loyal Customer", "Disloyal Customer"]
    Age: int
    Type_of_Travel: Literal["Business", "Personal"]
    Class: Literal["Eco", "Business", "Eco Plus"]
    Flight_Distance: int
    Seat_comfort: int
    Departure_Arrival_time_convenient: int
    Food_and_drink: int
    Gate_location: int
    Inflight_wifi_service: int
    Inflight_entertainment: int
    Online_support: int
    Ease_of_Online_booking: int
    On_board_service: int
    Leg_room_service: int
    Baggage_handling: int
    Checkin_service: int
    Cleanliness: int
    Online_boarding: int
    Departure_Delay_in_Minutes: int
    Arrival_Delay_in_Minutes: float

# ----------------------------
# Endpoint
@app.post("/predict")
def predict_satisfaction(passenger: Passenger):
    # Convert input to DataFrame
    input_df = pd.DataFrame([{
        "Customer Type": passenger.Customer_Type,
        "Age": passenger.Age,
        "Type of Travel": passenger.Type_of_Travel,
        "Class": passenger.Class,
        "Flight Distance": passenger.Flight_Distance,
        "Seat comfort": passenger.Seat_comfort,
        "Departure/Arrival time convenient": passenger.Departure_Arrival_time_convenient,
        "Food and drink": passenger.Food_and_drink,
        "Gate location": passenger.Gate_location,
        "Inflight wifi service": passenger.Inflight_wifi_service,
        "Inflight entertainment": passenger.Inflight_entertainment,
        "Online support": passenger.Online_support,
        "Ease of Online booking": passenger.Ease_of_Online_booking,
        "On-board service": passenger.On_board_service,
        "Leg room service": passenger.Leg_room_service,
        "Baggage handling": passenger.Baggage_handling,
        "Checkin service": passenger.Checkin_service,
        "Cleanliness": passenger.Cleanliness,
        "Online boarding": passenger.Online_boarding,
        "Departure Delay in Minutes": passenger.Departure_Delay_in_Minutes,
        "Arrival Delay in Minutes": passenger.Arrival_Delay_in_Minutes
    }])

    try:
        # Predict using the loaded model
        prediction_text = loaded_model.predict(input_df)[0]
        prediction_numeric = 1 if prediction_text == "satisfied" else 0
        return {
            "prediction_text": prediction_text,
            "prediction_numeric": prediction_numeric
        }
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}

# ----------------------------
# Root endpoint
@app.get("/")
def root():
    return {"message": "Airline Satisfaction Prediction API is running!"}

# import os
# import streamlit as st
# import pandas as pd
# import joblib
# import pickle
# # ----------------------------
# # Path to model
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(BASE_DIR, 'RF_airline.joblib')

# # Load model once
# @st.cache_resource
# def load_model(path):
#     return joblib.load(path)

# try:
#     loaded_model = load_model(model_path)
#     st.success("✅ Model loaded successfully!")
# except Exception as e:
#     st.error(f"❌ Error loading model: {e}")
#     st.stop()

# # ----------------------------
# st.title("✈️ Airline Satisfaction Prediction")
# st.write("Enter passenger details to predict satisfaction:")

# # ----------------------------
# # Input fields
# Customer_Type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
# Age = st.number_input("Age", min_value=0, max_value=120, value=35)
# Type_of_Travel = st.selectbox("Type of Travel", ["Business", "Personal"])
# Class_ = st.selectbox("Class", ["Eco", "Business", "Eco Plus"])
# Flight_Distance = st.number_input("Flight Distance", min_value=0, value=500)
# Seat_comfort = st.number_input("Seat Comfort", min_value=0, max_value=5, value=4)
# Departure_Arrival_time_convenient = st.number_input("Departure/Arrival Time Convenient", min_value=0, max_value=5, value=4)
# Food_and_drink = st.number_input("Food and Drink", min_value=0, max_value=5, value=4)
# Gate_location = st.number_input("Gate Location", min_value=0, max_value=5, value=4)
# Inflight_wifi_service = st.number_input("Inflight Wifi Service", min_value=0, max_value=5, value=4)
# Inflight_entertainment = st.number_input("Inflight Entertainment", min_value=0, max_value=5, value=4)
# Online_support = st.number_input("Online Support", min_value=0, max_value=5, value=4)
# Ease_of_Online_booking = st.number_input("Ease of Online Booking", min_value=0, max_value=5, value=4)
# Onboard_service = st.number_input("On-board Service", min_value=0, max_value=5, value=4)
# Leg_room_service = st.number_input("Leg Room Service", min_value=0, max_value=5, value=4)
# Baggage_handling = st.number_input("Baggage Handling", min_value=0, max_value=5, value=4)
# Checkin_service = st.number_input("Check-in Service", min_value=0, max_value=5, value=4)
# Cleanliness = st.number_input("Cleanliness", min_value=0, max_value=5, value=4)
# Online_boarding = st.number_input("Online Boarding", min_value=0, max_value=5, value=4)
# Departure_Delay_in_Minutes = st.number_input("Departure Delay in Minutes", min_value=0, value=0)
# Arrival_Delay_in_Minutes = st.number_input("Arrival Delay in Minutes", min_value=0.0, value=0.0)

# # ----------------------------
# # Predict button
# if st.button("Predict Satisfaction"):
#     input_data = pd.DataFrame([{
#         "Customer Type": Customer_Type,
#         "Age": Age,
#         "Type of Travel": Type_of_Travel,
#         "Class": Class_,
#         "Flight Distance": Flight_Distance,
#         "Seat comfort": Seat_comfort,
#         "Departure/Arrival time convenient": Departure_Arrival_time_convenient,
#         "Food and drink": Food_and_drink,
#         "Gate location": Gate_location,
#         "Inflight wifi service": Inflight_wifi_service,
#         "Inflight entertainment": Inflight_entertainment,
#         "Online support": Online_support,
#         "Ease of Online booking": Ease_of_Online_booking,
#         "On-board service": Onboard_service,
#         "Leg room service": Leg_room_service,
#         "Baggage handling": Baggage_handling,
#         "Checkin service": Checkin_service,
#         "Cleanliness": Cleanliness,
#         "Online boarding": Online_boarding,
#         "Departure Delay in Minutes": Departure_Delay_in_Minutes,
#         "Arrival Delay in Minutes": Arrival_Delay_in_Minutes
#     }])

#     try:
#         prediction_text = loaded_model.predict(input_data)[0]
#         prediction_numeric = 1 if prediction_text == "satisfied" else 0
#         st.success(f"Predicted Satisfaction: {prediction_text} (Numeric: {prediction_numeric})")
#     except Exception as e:
#         st.error(f"Prediction failed: {e}")

# #