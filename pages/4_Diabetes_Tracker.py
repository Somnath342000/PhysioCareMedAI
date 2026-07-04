import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Diabetes Tracker",
    page_icon="🩸",
    layout="wide"
)

st.title("🩸 Diabetes Tracker")

st.info("Fill only the tests you have. You don't need to enter all values.")

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("physiocare.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS diabetes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
patient_name TEXT,
record_date TEXT,
fasting REAL,
post_meal REAL,
random_bs REAL,
hba1c REAL
)
""")

conn.commit()

# ---------------- INPUT ---------------- #

st.subheader("Patient Details")

name = st.text_input("Patient Name")

record_date = st.date_input(
    "Test Date",
    date.today()
)

st.divider()

st.subheader("Blood Sugar Tests")

fasting = st.number_input(
    "A) Fasting Blood Sugar (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0,
    help="Enter 0 if test not done."
)

post_meal = st.number_input(
    "B) Post Meal Blood Sugar (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0,
    help="Enter 0 if test not done."
)

random_bs = st.number_input(
    "C) Random Blood Sugar (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0,
    help="Enter 0 if test not done."
)

hba1c = st.number_input(
    "D) HbA1c (%)",
    min_value=0.0,
    value=0.0,
    step=0.1,
    help="Enter 0 if test not done."
)

st.divider()

# ---------------- SAVE ---------------- #

if st.button("💾 Save Record"):

    if name.strip() == "":
        st.error("Please enter Patient Name.")

    elif (
        fasting == 0 and
        post_meal == 0 and
        random_bs == 0 and
        hba1c == 0
    ):
        st.error("Please enter at least one test result.")

    else:

        cursor.execute("""

        INSERT INTO diabetes
        (
        patient_name,
        record_date,
        fasting,
        post_meal,
        random_bs,
        hba1c
        )

        VALUES
        (?,?,?,?,?,?)

        """,
        (
            name,
            str(record_date),
            fasting if fasting!=0 else None,
            post_meal if post_meal!=0 else None,
            random_bs if random_bs!=0 else None,
            hba1c if hba1c!=0 else None
        ))

        conn.commit()

        st.success("Record Saved Successfully.")

st.divider()
# ---------------- DIABETES RESULT ANALYSIS ---------------- #

st.divider()
st.header("🩺 Diabetes Test Interpretation")

# ---------- FASTING ----------

if fasting > 0:

    st.subheader("A) Fasting Blood Sugar")

    if fasting < 70:
        st.error(f"Result : {fasting} mg/dL")
        st.error("Status : Low Blood Sugar (Hypoglycemia)")
        st.info("Advice : Eat fast-acting glucose if symptomatic and contact your healthcare provider if symptoms are severe or persistent.")

    elif fasting <= 99:
        st.success(f"Result : {fasting} mg/dL")
        st.success("Status : Normal")
        st.info("Advice : Maintain a balanced diet, regular exercise and routine health check-ups.")

    elif fasting <= 125:
        st.warning(f"Result : {fasting} mg/dL")
        st.warning("Status : Prediabetes")
        st.info("Advice : Increase physical activity, reduce refined sugar and follow up with your doctor.")

    else:
        st.error(f"Result : {fasting} mg/dL")
        st.error("Status : Diabetes Range")
        st.info("Advice : Consult a qualified physician for evaluation and management.")

# ---------- POST MEAL ----------

if post_meal > 0:

    st.subheader("B) Post Meal Blood Sugar")

    if post_meal < 140:
        st.success(f"Result : {post_meal} mg/dL")
        st.success("Status : Normal")
        st.info("Advice : Continue healthy eating habits and regular physical activity.")

    elif post_meal <= 199:
        st.warning(f"Result : {post_meal} mg/dL")
        st.warning("Status : Prediabetes")
        st.info("Advice : Consider lifestyle changes and discuss the result with your healthcare provider.")

    else:
        st.error(f"Result : {post_meal} mg/dL")
        st.error("Status : Diabetes Range")
        st.info("Advice : Seek medical evaluation. Persistent high post-meal glucose needs professional assessment.")

# ---------- RANDOM ----------

if random_bs > 0:

    st.subheader("C) Random Blood Sugar")

    if random_bs < 140:
        st.success(f"Result : {random_bs} mg/dL")
        st.success("Status : Normal")
        st.info("Advice : Continue your current healthy lifestyle.")

    elif random_bs < 200:
        st.warning(f"Result : {random_bs} mg/dL")
        st.warning("Status : Elevated")
        st.info("Advice : Repeat testing if advised and consult your healthcare provider if needed.")

    else:
        st.error(f"Result : {random_bs} mg/dL")
        st.error("Status : Diabetes Range")
        st.info("Advice : A high random glucose may require prompt medical evaluation, especially if you have symptoms.")

# ---------- HbA1c ----------

if hba1c > 0:

    st.subheader("D) HbA1c")

    if hba1c < 5.7:
        st.success(f"Result : {hba1c}%")
        st.success("Status : Normal")
        st.info("Advice : Continue maintaining a healthy lifestyle.")

    elif hba1c < 6.5:
        st.warning(f"Result : {hba1c}%")
        st.warning("Status : Prediabetes")
        st.info("Advice : Lifestyle modification is recommended. Arrange follow-up testing as advised.")

    else:
        st.error(f"Result : {hba1c}%")
        st.error("Status : Diabetes Range")
        st.info("Advice : HbA1c suggests diabetes. Please consult a qualified physician for diagnosis and treatment.")

st.divider()
# ==========================================================
# IMPORTANCE OF EACH TEST
# ==========================================================

st.header("📚 Importance of Diabetes Tests")

with st.expander("🅰️ Why is Fasting Blood Sugar Important?"):

    st.write("""
Fasting Blood Sugar (FBS) measures your blood glucose level after at least
8 hours without food. It is one of the most commonly used screening tests
for diabetes and prediabetes.

A normal fasting blood sugar indicates that your body is regulating glucose
effectively. Elevated fasting levels may suggest insulin resistance or
diabetes and should be discussed with a healthcare professional.
""")

with st.expander("🅱️ Why is Post Meal Blood Sugar Important?"):

    st.write("""
Post Meal Blood Sugar (PPBS) measures blood glucose about 2 hours after a
meal. This test shows how well your body manages the rise in blood sugar
after eating.

High post-meal glucose may increase the risk of heart disease, stroke,
kidney disease and nerve damage if it remains uncontrolled over time.
""")

with st.expander("🅲 Why is Random Blood Sugar Important?"):

    st.write("""
Random Blood Sugar (RBS) can be measured at any time of the day regardless
of meals. It is often used when diabetes is suspected based on symptoms.

A high random blood sugar, especially when accompanied by symptoms such as
increased thirst, frequent urination or unexplained weight loss, should be
assessed by a healthcare professional.
""")

with st.expander("🅳 Why is HbA1c Important?"):

    st.write("""
HbA1c reflects your average blood sugar level over approximately the last
2 to 3 months. Unlike a single glucose reading, it provides a longer-term
picture of blood sugar control.

It is widely used to help diagnose diabetes and to monitor how effectively
blood sugar has been managed over time.
""")

st.divider()

# ==========================================================
# OVERALL RECOMMENDATION
# ==========================================================

st.header("🩺 Overall Health Recommendation")

high = False
prediabetes = False

if fasting >= 126:
    high = True
elif 100 <= fasting <= 125:
    prediabetes = True

if post_meal >= 200:
    high = True
elif 140 <= post_meal <= 199:
    prediabetes = True

if random_bs >= 200:
    high = True
elif 140 <= random_bs < 200:
    prediabetes = True

if hba1c >= 6.5:
    high = True
elif 5.7 <= hba1c < 6.5:
    prediabetes = True


if high:

    st.error("🔴 Overall Status : Diabetes Range")

    st.write("""
• Arrange an appointment with a qualified physician.

• Do not ignore persistent high blood sugar values.

• Follow your prescribed treatment plan if you have already been diagnosed.

• Maintain a healthy diet and regular physical activity as advised by your healthcare provider.

• Attend regular follow-up appointments and recommended laboratory tests.
""")

elif prediabetes:

    st.warning("🟡 Overall Status : Prediabetes")

    st.write("""
• Increase physical activity.

• Reduce sugary drinks and refined carbohydrates.

• Maintain a healthy body weight.

• Eat a balanced diet rich in vegetables, whole grains and lean protein.

• Repeat testing and follow up with your healthcare provider as recommended.
""")

else:

    st.success("🟢 Overall Status : Normal")

    st.write("""
• Continue a balanced diet.

• Exercise regularly.

• Maintain a healthy body weight.

• Get sufficient sleep.

• Have routine health check-ups.
""")

st.divider()

# ==========================================================
# MEDICAL DISCLAIMER
# ==========================================================

st.warning("""
⚠️ Medical Disclaimer

This application is intended for educational and health tracking purposes
only. It does not provide medical diagnosis or replace consultation with a
qualified healthcare professional.

Always consult your physician regarding abnormal blood sugar results,
symptoms, medication or treatment decisions.
""")
#---------#

st.divider()

st.subheader("🔍 Search Patient Records")

search_name = st.text_input("Enter Patient Name")

if search_name:

    query = """
    SELECT *
    FROM diabetes
    WHERE patient_name LIKE ?
    ORDER BY record_date DESC
    """

    search_df = pd.read_sql_query(
        query,
        conn,
        params=(f"%{search_name}%",)
    )

    if len(search_df)==0:

        st.warning("No patient found.")

    else:

        st.success(f"{len(search_df)} Record(s) Found")

        st.dataframe(
            search_df,
            use_container_width=True
        )

st.divider()
# ==========================================================
# DASHBOARD & CHARTS
# ==========================================================

import plotly.express as px

st.divider()
st.header("📊 Diabetes Dashboard")

df = pd.read_sql_query(
    "SELECT * FROM diabetes ORDER BY record_date",
    conn
)

if len(df) > 0:

    df["record_date"] = pd.to_datetime(df["record_date"])

    # ---------------- DATE FILTER ----------------

    min_date = df["record_date"].min().date()
    max_date = df["record_date"].max().date()

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "From",
            min_date,
            min_value=min_date,
            max_value=max_date
        )

    with col2:
        end_date = st.date_input(
            "To",
            max_date,
            min_value=min_date,
            max_value=max_date
        )

    filtered_df = df[
        (df["record_date"].dt.date >= start_date) &
        (df["record_date"].dt.date <= end_date)
    ]

    # ---------------- STATISTICS ----------------

    st.subheader("📈 Statistics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Records",
        len(filtered_df)
    )

    c2.metric(
        "Avg Fasting",
        round(filtered_df["fasting"].mean(),1)
        if filtered_df["fasting"].notna().any()
        else "-"
    )

    c3.metric(
        "Avg Post Meal",
        round(filtered_df["post_meal"].mean(),1)
        if filtered_df["post_meal"].notna().any()
        else "-"
    )

    c4.metric(
        "Avg HbA1c",
        round(filtered_df["hba1c"].mean(),1)
        if filtered_df["hba1c"].notna().any()
        else "-"
    )

    st.divider()

    # ---------------- FASTING ----------------

    fasting_df = filtered_df.dropna(subset=["fasting"])

    if len(fasting_df)>0:

        st.subheader("📊 Fasting Blood Sugar Trend")

        fig = px.line(
            fasting_df,
            x="record_date",
            y="fasting",
            markers=True,
            title="Fasting Blood Sugar"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------- POST MEAL ----------------

    post_df = filtered_df.dropna(subset=["post_meal"])

    if len(post_df)>0:

        st.subheader("📊 Post Meal Blood Sugar Trend")

        fig = px.line(
            post_df,
            x="record_date",
            y="post_meal",
            markers=True,
            title="Post Meal Blood Sugar"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------- RANDOM ----------------

    random_df = filtered_df.dropna(subset=["random_bs"])

    if len(random_df)>0:

        st.subheader("📊 Random Blood Sugar Trend")

        fig = px.line(
            random_df,
            x="record_date",
            y="random_bs",
            markers=True,
            title="Random Blood Sugar"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------- HBA1C ----------------

    hba_df = filtered_df.dropna(subset=["hba1c"])

    if len(hba_df)>0:

        st.subheader("📊 HbA1c Trend")

        fig = px.line(
            hba_df,
            x="record_date",
            y="hba1c",
            markers=True,
            title="HbA1c"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

else:

    st.info("No records available.")

# ---------------- PREVIOUS RECORDS ---------------- #

st.subheader("📋 Previous Records")

df = pd.read_sql_query(
    "SELECT * FROM diabetes ORDER BY id DESC",
    conn
)

st.dataframe(
    df,
    use_container_width=True
)
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

st.divider()
st.header("📄 Generate PDF Report")

if st.button("📥 Download Patient Report PDF"):

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, 750, "Diabetes Report")

    p.setFont("Helvetica", 10)
    p.drawString(50, 720, f"Patient Name: {name}")
    p.drawString(50, 700, f"Date: {record_date}")

    y = 670

    if fasting > 0:
        p.drawString(50, y, f"Fasting: {fasting} mg/dL")
        y -= 20

    if post_meal > 0:
        p.drawString(50, y, f"Post Meal: {post_meal} mg/dL")
        y -= 20

    if random_bs > 0:
        p.drawString(50, y, f"Random: {random_bs} mg/dL")
        y -= 20

    if hba1c > 0:
        p.drawString(50, y, f"HbA1c: {hba1c}%")
        y -= 20

    y -= 20
    p.drawString(50, y, "⚠ This report is for educational purposes only.")

    p.showPage()
    p.save()

    buffer.seek(0)

    st.download_button(
        label="⬇ Download PDF",
        data=buffer,
        file_name="diabetes_report.pdf",
        mime="application/pdf"
    )
conn.close()
