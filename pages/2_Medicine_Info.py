import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medicine Information")

st.title("💊 Medicine Information")

df = pd.read_csv("data/medicines.csv")

medicine = st.selectbox(
    "Select Medicine",
    df["Medicine"]
)

row = df[df["Medicine"] == medicine].iloc[0]

st.subheader("Generic Name")
st.write(row["Generic"])

st.subheader("Uses")
st.write(row["Uses"])

st.subheader("Side Effects")
st.write(row["Side Effects"])

st.subheader("Warning")
st.write(row["Warning"])

st.warning("⚠️ Do not take any medicine without consulting a qualified healthcare professional.")
