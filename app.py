import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("BestModel_DietAcademic.joblib")

# Title
st.title("🍽️ Dietary Habits vs Academic Performance 🎓")

st.write("Enter your dietary habits to predict your expected exam performance.")

# Input fields
breakfast = st.selectbox("Do you eat breakfast regularly?", ["Yes", "Sometimes", "No"])
fast_food = st.selectbox("Fast food frequency", ["Never", "Occasionally", "Frequently"])
fruit_veg = st.selectbox("Fruit & Vegetable intake", ["Daily", "Sometimes", "Never"])
meals = st.selectbox("Meals per day", ["1-2 Times", "2-3 Times", "More Than 3 Times"])
caffeine = st.selectbox("Caffeine consumption", ["None", "Low", "High"])

gender = st.selectbox("Gender", ["Male", "Female"])
accommodation = st.selectbox("Accommodation", ["Hostelite", "Day Scholar"])
residency = st.selectbox("Residency", ["Urban", "Rural"])

# Encode categorical inputs like in training
def map_breakfast(x):
    return 10 if x == 'Yes' else 5 if x == 'Sometimes' else 0

def map_fastfood(x):
    return 0 if x == 'Frequently' else 5 if x == 'Occasionally' else 10

def map_fruits(x):
    return 10 if x == 'Daily' else 5 if x == 'Sometimes' else 0

def map_meals(x):
    return 3 if x == '1-2 Times' else 7 if x == '2-3 Times' else 10

def map_caffeine(x):
    return 10 if x == 'None' else 5 if x == 'Low' else 0

# Encoding for model input
gender_val = 1 if gender == "Female" else 0
accom_val = 1 if accommodation == "Hostelite" else 0
residency_val = 1 if residency == "Urban" else 0

# Calculate score
eating_habit_score = (
    map_breakfast(breakfast) +
    map_fastfood(fast_food) +
    map_fruits(fruit_veg) +
    map_meals(meals) +
    map_caffeine(caffeine)
)

# Predict button
if st.button("Predict Exam Marks"):
    input_data = np.array([[eating_habit_score, gender_val, accom_val, residency_val,
                            map_breakfast(breakfast), map_fastfood(fast_food),
                            map_fruits(fruit_veg), map_meals(meals), map_caffeine(caffeine)]])
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Exam Marks: {prediction:.2f}")
