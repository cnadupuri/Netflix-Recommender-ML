import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model(netflix).pkl")
preprocessor = joblib.load("preprocessor(netflix).pkl")

st.title("Netflix Recommendation Model")

st.write("Enter Movie Information")

# Example Inputs (replace with your actual feature names)
type_ = st.selectbox("Type", ["Movie", "TV Show"])
release_year = st.number_input("Release Year", 1900, 2030)
duration = st.number_input("Duration")
rating = st.selectbox("Rating", ["G","PG","PG-13","R","TV-MA"])

if st.button("Predict"):

    sample = pd.DataFrame({
        "type":[type_],
        "release_year":[release_year],
        "duration":[duration],
        "rating":[rating]
    })

    x = preprocessor.transform(sample)

    prediction = model.predict(x)

    st.success(prediction[0])
