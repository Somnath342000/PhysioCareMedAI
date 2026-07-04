import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.title("❤️ Blood Pressure Tracker")

conn = sqlite3.connect("physiocare.db")
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

systolic = st.number_input("Systolic (mmHg)",80,250)

diastolic = st.number_input("Diastolic (mmHg)",40,150)

pulse = st.number_input("Pulse",40,180)

def category(sys,dia):

    if sys<120 and dia<80:
        return "Normal"

    elif sys<130 and dia<80:
        return "Elevated"

    elif sys<140 or dia<90:
        return "High BP Stage 1"

    elif sys<180 or dia<120:
        return "High BP Stage 2"

    else:
        return "Hypertensive Crisis"

if st.button("Save Record"):

    cat=category(systolic,diastolic)

    cursor.execute("""
    INSERT INTO bp(name,record_date,systolic,diastolic,pulse,category)
    VALUES(?,?,?,?,?,?)
    """,(name,str(record_date),systolic,diastolic,pulse,cat))

    conn.commit()

    st.success("Record Saved Successfully")

st.divider()

st.subheader("Previous Records")

df=pd.read_sql("SELECT * FROM bp ORDER BY id DESC",conn)

st.dataframe(df,use_container_width=True)

conn.close()
