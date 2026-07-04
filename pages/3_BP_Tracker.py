import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(page_title="Blood Pressure Tracker")

st.title("❤️ Blood Pressure Tracker")

conn = sqlite3.connect("physiocare.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bp(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    record_date TEXT,
    systolic INTEGER,
    diastolic INTEGER,
    pulse INTEGER,
    category TEXT
)
""")
conn.commit()

name = st.text_input("Patient Name")
record_date = st.date_input("Date", date.today())

systolic = st.number_input("Systolic (mmHg)", min_value=70, max_value=250, value=120)
diastolic = st.number_input("Diastolic (mmHg)", min_value=40, max_value=150, value=80)
pulse = st.number_input("Pulse Rate", min_value=40, max_value=200, value=72)


def bp_category(sys, dia):
    if sys < 120 and dia < 80:
        return "Normal"
    elif 120 <= sys < 130 and dia < 80:
        return "Elevated"
    elif (130 <= sys < 140) or (80 <= dia < 90):
        return "High BP Stage 1"
    elif (140 <= sys < 180) or (90 <= dia < 120):
        return "High BP Stage 2"
    else:
        return "Hypertensive Crisis"


if st.button("💾 Save Record"):
    category = bp_category(systolic, diastolic)

    cursor.execute("""
    INSERT INTO bp
    (name, record_date, systolic, diastolic, pulse, category)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, str(record_date), systolic, diastolic, pulse, category))

    conn.commit()

    st.success("Record Saved Successfully")
    st.info(f"Category: {category}")

st.divider()

st.subheader("📋 Saved Records")

df = pd.read_sql_query(
    "SELECT * FROM bp ORDER BY id DESC",
    conn
)

st.dataframe(df, use_container_width=True)

conn.close()
