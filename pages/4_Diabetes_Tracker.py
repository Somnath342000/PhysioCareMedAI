import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(page_title="Diabetes Tracker")

st.title("🩸 Diabetes Tracker")

conn = sqlite3.connect("physiocare.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS diabetes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    record_date TEXT,
    fasting INTEGER,
    pp INTEGER,
    random INTEGER,
    hba1c REAL
)
""")

conn.commit()

name = st.text_input("Patient Name")

record_date = st.date_input("Date", date.today())

fasting = st.number_input(
    "Fasting Blood Sugar (mg/dL)",
    min_value=50,
    max_value=500,
    value=90
)

pp = st.number_input(
    "Post Meal Blood Sugar (mg/dL)",
    min_value=50,
    max_value=600,
    value=130
)

random = st.number_input(
    "Random Blood Sugar (mg/dL)",
    min_value=50,
    max_value=600,
    value=120
)

hba1c = st.number_input(
    "HbA1c (%)",
    min_value=3.0,
    max_value=20.0,
    value=5.5,
    step=0.1
)

if st.button("💾 Save Diabetes Record"):

    cursor.execute("""
    INSERT INTO diabetes
    (name,record_date,fasting,pp,random,hba1c)
    VALUES(?,?,?,?,?,?)
    """,
    (
        name,
        str(record_date),
        fasting,
        pp,
        random,
        hba1c
    ))

    conn.commit()

    st.success("Record Saved Successfully!")

st.divider()

st.subheader("📋 Previous Records")

df = pd.read_sql_query(
    "SELECT * FROM diabetes ORDER BY id DESC",
    conn
)

st.dataframe(df, use_container_width=True)

conn.close()
