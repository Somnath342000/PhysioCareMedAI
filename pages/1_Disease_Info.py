import streamlit as st
import pandas as pd

st.set_page_config(page_title="Disease Information")

st.title("🩺 Disease Information")

df = pd.read_csv("data/diseases.csv")

disease = st.selectbox(
    "Select Disease",
    df["Disease"]
)

row = df[df["Disease"] == disease].iloc[0]

st.subheader("Symptoms")
st.write(row["Symptoms"])

st.subheader("Causes")
st.write(row["Causes"])

st.subheader("Prevention")
st.write(row["Prevention"])

st.subheader("Treatment")
st.write(row["Treatment"])

st.warning("⚠️ This information is for educational purposes only.")
