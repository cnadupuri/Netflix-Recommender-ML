import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessor
model = joblib.load("model(netflix).pkl")
preprocessor = joblib.load("preprocessor(netflix).pkl")

st.title("Netflix Content Classifier")

# User Inputs
type_ = st.selectbox("Type", ["Movie", "TV Show"])

country = st.text_input("Country", "India")

release_year = st.number_input(
    "Release Year",
    min_value=1900,
    max_value=2035,
    value=2020
)

duration = st.text_input("Duration", "90 min")

listed_in = st.text_input("Genre", "Drama")

if st.button("Predict"):

    sample = pd.DataFrame({
        "type": [type_],
        "country": [country],
        "release_year": [release_year],
        "duration": [duration],
        "listed_in": [listed_in]
    })

    sample_processed = preprocessor.transform(sample)

    prediction = model.predict(sample_processed)

    st.success(f"Prediction: {prediction[0]}")
