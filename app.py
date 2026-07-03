import streamlit as st

st.set_page_config(
    page_title="PhysioCare AI",
    page_icon="🏥",
    layout="wide"
)

# Sidebar Menu
st.sidebar.title("🏥 PhysioCare AI")
menu = st.sidebar.selectbox(
    "Choose Module",
    [
        "Home",
        "BMI Calculator",
        "TDEE Calculator",
        "Diet Planner"
    ]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.title("🏥 PhysioCare AI")
    st.subheader("Your Personal Health & Physiotherapy Assistant")

    st.write("""
    👋 Welcome to PhysioCare AI

    This app helps you with:
    - 🩺 Health Information
    - ⚖️ BMI & TDEE Calculation
    - 🥗 Diet Planning
    - 🏃 Physiotherapy Guidance

    ⚠️ Note: This app is for educational purposes only and not a replacement for medical advice.
    """)

# ---------------- BMI ----------------
elif menu == "BMI Calculator":
    st.title("⚖️ BMI Calculator")

    weight = st.number_input("Enter Weight (kg)", 1.0)
    height = st.number_input("Enter Height (cm)", 1.0)

    if st.button("Calculate BMI"):
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.info("Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Normal weight")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Obese")

# ---------------- TDEE ----------------
elif menu == "TDEE Calculator":
    st.title("🔥 TDEE Calculator")

    age = st.number_input("Age", 1)
    weight = st.number_input("Weight (kg)", 1.0)
    height = st.number_input("Height (cm)", 1.0)

    gender = st.selectbox("Gender", ["Male", "Female"])
    activity = st.selectbox(
        "Activity Level",
        [
            "Sedentary",
            "Lightly Active",
            "Moderately Active",
            "Very Active"
        ]
    )

    if st.button("Calculate TDEE"):

        # BMR calculation (Mifflin-St Jeor)
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        activity_multiplier = {
            "Sedentary": 1.2,
            "Lightly Active": 1.375,
            "Moderately Active": 1.55,
            "Very Active": 1.725
        }

        tdee = bmr * activity_multiplier[activity]

        st.success(f"BMR: {bmr:.2f} kcal")
        st.success(f"TDEE: {tdee:.2f} kcal")

        st.info(f"""
        📉 Weight Loss: {tdee - 500:.0f} kcal/day  
        ⚖️ Maintenance: {tdee:.0f} kcal/day  
        📈 Weight Gain: {tdee + 500:.0f} kcal/day  
        """)

# ---------------- DIET ----------------
elif menu == "Diet Planner":
    st.title("🥗 Diet Planner")

    goal = st.selectbox(
        "Select Goal",
        [
            "Weight Loss",
            "Weight Gain",
            "Maintenance"
        ]
    )

    diet_plan = {
        "Weight Loss": [
            "Morning: Lemon water + oats",
            "Lunch: Rice + vegetables + dal",
            "Snack: Fruits",
            "Dinner: Salad + soup"
        ],
        "Weight Gain": [
            "Morning: Milk + banana + nuts",
            "Lunch: Rice + chicken/fish + dal",
            "Snack: Peanut butter sandwich",
            "Dinner: Roti + paneer + vegetables"
        ],
        "Maintenance": [
            "Balanced breakfast",
            "Rice + protein + vegetables",
            "Healthy snacks",
            "Light dinner"
        ]
    }

    for item in diet_plan[goal]:
        st.write("✔️", item)
