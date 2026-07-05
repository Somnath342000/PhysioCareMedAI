import streamlit as st

st.set_page_config(
    page_title="Blood Report Analyzer",
    page_icon="🩸",
    layout="wide"
)

st.title("🩸 Blood Report Analyzer")
st.info("Enter available blood test values. Leave the others as 0.")
#-------------------
st.divider()

st.header("🩸 Diabetes Profile")

fasting_bs = st.number_input(
    "Fasting Blood Sugar (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

pp_bs = st.number_input(
    "Post Meal Blood Sugar (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

random_bs = st.number_input(
    "Random Blood Sugar (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

hba1c = st.number_input(
    "HbA1c (%)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
#-------------
st.header("Complete Blood Count (CBC)")

hb = st.number_input("Hemoglobin (g/dL)", min_value=0.0, value=0.0, step=0.1)
wbc = st.number_input("WBC (/µL)", min_value=0, value=0)
rbc = st.number_input("RBC (million/µL)", min_value=0.0, value=0.0, step=0.1)
platelet = st.number_input("Platelet (/µL)", min_value=0, value=0)
esr = st.number_input("ESR (mm/hr)", min_value=0, value=0)
#-------------------
st.divider()

st.header("🧈 Lipid Profile")

total_cholesterol = st.number_input(
    "Total Cholesterol (mg/dL)",
    min_value=0,
    value=0
)

hdl = st.number_input(
    "HDL Cholesterol (mg/dL)",
    min_value=0,
    value=0
)

ldl = st.number_input(
    "LDL Cholesterol (mg/dL)",
    min_value=0,
    value=0
)

triglyceride = st.number_input(
    "Triglycerides (mg/dL)",
    min_value=0,
    value=0
)
#-------------------
st.divider()

st.header("🧪 Liver Function Test (LFT)")

alt = st.number_input(
    "ALT / SGPT (U/L)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

ast = st.number_input(
    "AST / SGOT (U/L)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

bilirubin = st.number_input(
    "Total Bilirubin (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

albumin = st.number_input(
    "Albumin (g/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

alp = st.number_input(
    "Alkaline Phosphatase (ALP) (U/L)",
    min_value=0.0,
    value=0.0,
    step=1.0
)
#-----------KFT--------
st.divider()

st.header("🩺 Kidney Function Test (KFT)")

creatinine = st.number_input(
    "Serum Creatinine (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

urea = st.number_input(
    "Blood Urea (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

uric_acid = st.number_input(
    "Uric Acid (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

egfr = st.number_input(
    "eGFR (mL/min/1.73m²)",
    min_value=0.0,
    value=0.0,
    step=1.0
)
#-------------------
st.divider()

st.header("🦋 Thyroid Profile")

tsh = st.number_input(
    "TSH (µIU/mL)",
    min_value=0.0,
    value=0.0,
    step=0.01
)

t3 = st.number_input(
    "Total T3 (ng/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

t4 = st.number_input(
    "Total T4 (µg/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
#-------------------
st.divider()

st.header("⚡ Electrolytes & Minerals")

sodium = st.number_input(
    "Sodium (Na⁺) (mEq/L)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

potassium = st.number_input(
    "Potassium (K⁺) (mEq/L)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

chloride = st.number_input(
    "Chloride (Cl⁻) (mEq/L)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

calcium = st.number_input(
    "Calcium (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

magnesium = st.number_input(
    "Magnesium (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

phosphorus = st.number_input(
    "Phosphorus (mg/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
#-------------------
st.divider()

st.header("💊 Vitamin & Iron Profile")

vitamin_d = st.number_input(
    "Vitamin D (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

vitamin_b12 = st.number_input(
    "Vitamin B12 (pg/mL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

serum_iron = st.number_input(
    "Serum Iron (µg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

ferritin = st.number_input(
    "Ferritin (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

tibc = st.number_input(
    "TIBC (µg/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)
#-------------------
st.divider()

st.header("🦴 Inflammatory & Autoimmune Tests")

crp = st.number_input(
    "C-Reactive Protein (CRP) (mg/L)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

rf = st.number_input(
    "Rheumatoid Factor (IU/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

anti_ccp = st.number_input(
    "Anti-CCP Antibody (U/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

aso = st.number_input(
    "ASO Titre (IU/mL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

ana = st.selectbox(
    "ANA Test",
    ["Not Done","Negative","Positive"]
)
#-------------------
st.divider()

st.header("🩸 Coagulation Profile")

pt = st.number_input(
    "Prothrombin Time (PT) (seconds)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

inr = st.number_input(
    "INR",
    min_value=0.0,
    value=0.0,
    step=0.1
)

aptt = st.number_input(
    "aPTT (seconds)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
#-----------------
st.divider()

st.header("❤️ Cardiac Markers")

troponin = st.number_input(
    "Troponin I (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=0.01
)

ckmb = st.number_input(
    "CK-MB (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

bnp = st.number_input(
    "BNP (pg/mL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)
#-------------
st.divider()

st.header("🦠 Infection Profile")

dengue_ns1 = st.selectbox(
    "Dengue NS1 Antigen",
    ["Not Done","Negative","Positive"]
)

dengue_igm = st.selectbox(
    "Dengue IgM",
    ["Not Done","Negative","Positive"]
)

dengue_igg = st.selectbox(
    "Dengue IgG",
    ["Not Done","Negative","Positive"]
)

malaria = st.selectbox(
    "Malaria Antigen",
    ["Not Done","Negative","Positive"]
)

typhoid = st.selectbox(
    "Typhoid (IgM / Widal)",
    ["Not Done","Negative","Positive"]
)

hbsag = st.selectbox(
    "HBsAg (Hepatitis B)",
    ["Not Done","Negative","Positive"]
)

anti_hcv = st.selectbox(
    "Anti-HCV",
    ["Not Done","Negative","Positive"]
)

hiv = st.selectbox(
    "HIV 1 & 2 Screening",
    ["Not Done","Negative","Positive"]
)
#----------
st.divider()

st.header("🧬 Tumor Markers")

psa = st.number_input(
    "PSA (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

cea = st.number_input(
    "CEA (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

ca125 = st.number_input(
    "CA-125 (U/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

ca199 = st.number_input(
    "CA 19-9 (U/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

afp = st.number_input(
    "AFP (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)
#--------
st.divider()

st.header("🧬 Hormone Profile")

testosterone = st.number_input(
    "Testosterone (ng/dL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

fsh = st.number_input(
    "FSH (mIU/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

lh = st.number_input(
    "LH (mIU/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

prolactin = st.number_input(
    "Prolactin (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

estradiol = st.number_input(
    "Estradiol (pg/mL)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

progesterone = st.number_input(
    "Progesterone (ng/mL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

cortisol = st.number_input(
    "Morning Cortisol (µg/dL)",
    min_value=0.0,
    value=0.0,
    step=0.1
)

#-----
#-------
#-------------------
if st.button("🔍 Analyze Report"):
#---------
  st.divider()
st.header("🩸 Diabetes Profile Analysis")

# ---------- FBS ----------
if fasting_bs > 0:

    if fasting_bs < 70:
        st.warning(f"Fasting Blood Sugar : {fasting_bs} mg/dL → Low (Hypoglycemia)")

    elif fasting_bs <= 99:
        st.success(f"Fasting Blood Sugar : {fasting_bs} mg/dL → Normal")

    elif fasting_bs <= 125:
        st.warning(f"Fasting Blood Sugar : {fasting_bs} mg/dL → Prediabetes")

    else:
        st.error(f"Fasting Blood Sugar : {fasting_bs} mg/dL → Diabetes Range")


# ---------- PPBS ----------
if pp_bs > 0:

    if pp_bs < 140:
        st.success(f"Post Meal Blood Sugar : {pp_bs} mg/dL → Normal")

    elif pp_bs <= 199:
        st.warning(f"Post Meal Blood Sugar : {pp_bs} mg/dL → Prediabetes")

    else:
        st.error(f"Post Meal Blood Sugar : {pp_bs} mg/dL → Diabetes Range")


# ---------- Random ----------
if random_bs > 0:

    if random_bs < 140:
        st.success(f"Random Blood Sugar : {random_bs} mg/dL → Normal")

    elif random_bs < 200:
        st.warning(f"Random Blood Sugar : {random_bs} mg/dL → Elevated")

    else:
        st.error(f"Random Blood Sugar : {random_bs} mg/dL → Diabetes Range")


# ---------- HbA1c ----------
if hba1c > 0:

    if hba1c < 5.7:
        st.success(f"HbA1c : {hba1c}% → Normal")

    elif hba1c < 6.5:
        st.warning(f"HbA1c : {hba1c}% → Prediabetes")

    else:
        st.error(f"HbA1c : {hba1c}% → Diabetes Range")
    #---------
st.divider()

st.subheader("🩺 Overall Diabetes Summary")

diabetes_flag = False
prediabetes_flag = False

if fasting_bs >= 126:
    diabetes_flag = True
elif 100 <= fasting_bs <= 125:
    prediabetes_flag = True

if pp_bs >= 200:
    diabetes_flag = True
elif 140 <= pp_bs <= 199:
    prediabetes_flag = True

if random_bs >= 200:
    diabetes_flag = True
elif 140 <= random_bs < 200:
    prediabetes_flag = True

if hba1c >= 6.5:
    diabetes_flag = True
elif 5.7 <= hba1c < 6.5:
    prediabetes_flag = True

if diabetes_flag:
    st.error("🔴 Overall Interpretation: Results are in the Diabetes Range.")
    st.info("These results should be evaluated by a qualified healthcare professional. Diagnosis should not be based on a single test result alone.")

elif prediabetes_flag:
    st.warning("🟡 Overall Interpretation: Results suggest Prediabetes.")
    st.info("Lifestyle changes and follow-up testing may be appropriate. Please consult your healthcare provider.")

else:
    st.success("🟢 Overall Interpretation: Results are within the common reference ranges.")

#--------


    st.subheader("📋 CBC Analysis")

    # Hemoglobin
    if hb > 0:
        if hb < 12:
            st.error(f"Hemoglobin: {hb} g/dL → Low")
            st.info("May indicate anemia. Consult your healthcare provider.")
        elif hb <= 17:
            st.success(f"Hemoglobin: {hb} g/dL → Normal")
        else:
            st.warning(f"Hemoglobin: {hb} g/dL → High")
            st.info("Can be associated with dehydration or other medical conditions.")

    # WBC
    if wbc > 0:
        if wbc < 4000:
            st.error(f"WBC: {wbc}/µL → Low")
        elif wbc <= 11000:
            st.success(f"WBC: {wbc}/µL → Normal")
        else:
            st.warning(f"WBC: {wbc}/µL → High")
            st.info("May indicate infection or inflammation.")

    # RBC
    if rbc > 0:
        if rbc < 4.2:
            st.error(f"RBC: {rbc} million/µL → Low")
        elif rbc <= 6.1:
            st.success(f"RBC: {rbc} million/µL → Normal")
        else:
            st.warning(f"RBC: {rbc} million/µL → High")

    # Platelet
    if platelet > 0:
        if platelet < 150000:
            st.error(f"Platelet: {platelet}/µL → Low")
        elif platelet <= 450000:
            st.success(f"Platelet: {platelet}/µL → Normal")
        else:
            st.warning(f"Platelet: {platelet}/µL → High")

    # ESR
    if esr > 0:
        if esr <= 20:
            st.success(f"ESR: {esr} mm/hr → Normal")
        else:
            st.warning(f"ESR: {esr} mm/hr → High")
            st.info("A high ESR may indicate inflammation. It is not specific to one disease.")
          # ---------------- LIPID PROFILE ----------------

st.subheader("🧈 Lipid Profile Analysis")

# Total Cholesterol

if total_cholesterol > 0:

    if total_cholesterol < 200:
        st.success(f"Total Cholesterol : {total_cholesterol} mg/dL → Normal")

    elif total_cholesterol <= 239:
        st.warning(f"Total Cholesterol : {total_cholesterol} mg/dL → Borderline High")
        st.info("Reduce saturated fat intake and exercise regularly.")

    else:
        st.error(f"Total Cholesterol : {total_cholesterol} mg/dL → High")
        st.info("Consult your healthcare provider for further evaluation.")

# HDL

if hdl > 0:

    if hdl >= 60:
        st.success(f"HDL : {hdl} mg/dL → Excellent (Protective)")

    elif hdl >= 40:
        st.success(f"HDL : {hdl} mg/dL → Normal")

    else:
        st.warning(f"HDL : {hdl} mg/dL → Low")
        st.info("Regular exercise and healthy fats may help improve HDL.")

# LDL

if ldl > 0:

    if ldl < 100:
        st.success(f"LDL : {ldl} mg/dL → Optimal")

    elif ldl <= 129:
        st.warning(f"LDL : {ldl} mg/dL → Near Optimal")

    elif ldl <= 159:
        st.warning(f"LDL : {ldl} mg/dL → Borderline High")

    elif ldl <= 189:
        st.error(f"LDL : {ldl} mg/dL → High")

    else:
        st.error(f"LDL : {ldl} mg/dL → Very High")

# Triglycerides

if triglyceride > 0:

    if triglyceride < 150:
        st.success(f"Triglycerides : {triglyceride} mg/dL → Normal")

    elif triglyceride <= 199:
        st.warning(f"Triglycerides : {triglyceride} mg/dL → Borderline High")

    elif triglyceride <= 499:
        st.error(f"Triglycerides : {triglyceride} mg/dL → High")

    else:
        st.error(f"Triglycerides : {triglyceride} mg/dL → Very High")
      #-------------- Liver Function test analysis-------#
st.subheader("🧪 Liver Function Test Analysis")

# ALT
if alt > 0:
    if alt <= 56:
        st.success(f"ALT (SGPT): {alt} U/L → Normal")
    else:
        st.warning(f"ALT (SGPT): {alt} U/L → High")
        st.info("May indicate liver inflammation or injury. Please consult your healthcare provider.")

# AST
if ast > 0:
    if ast <= 40:
        st.success(f"AST (SGOT): {ast} U/L → Normal")
    else:
        st.warning(f"AST (SGOT): {ast} U/L → High")
        st.info("May be associated with liver or muscle disorders.")

# Bilirubin
if bilirubin > 0:
    if bilirubin <= 1.2:
        st.success(f"Total Bilirubin: {bilirubin} mg/dL → Normal")
    else:
        st.warning(f"Total Bilirubin: {bilirubin} mg/dL → High")
        st.info("High bilirubin may be associated with jaundice or liver disease.")

# Albumin
if albumin > 0:
    if 3.5 <= albumin <= 5.0:
        st.success(f"Albumin: {albumin} g/dL → Normal")
    else:
        st.warning(f"Albumin: {albumin} g/dL → Abnormal")
        st.info("Abnormal albumin may indicate liver, kidney or nutritional problems.")

# ALP
if alp > 0:
    if 44 <= alp <= 147:
        st.success(f"ALP: {alp} U/L → Normal")
    else:
        st.warning(f"ALP: {alp} U/L → Abnormal")
        st.info("Abnormal ALP may be associated with liver or bone disorders.")

#----KFT------#
st.subheader("🩺 Kidney Function Test Analysis")

# Creatinine
if creatinine > 0:

    if 0.6 <= creatinine <= 1.3:
        st.success(f"Creatinine: {creatinine} mg/dL → Normal")

    elif creatinine < 0.6:
        st.warning(f"Creatinine: {creatinine} mg/dL → Low")
        st.info("Low creatinine may be associated with low muscle mass or other conditions.")

    else:
        st.error(f"Creatinine: {creatinine} mg/dL → High")
        st.info("High creatinine may indicate reduced kidney function. Please consult your healthcare provider.")

# Urea
if urea > 0:

    if 15 <= urea <= 40:
        st.success(f"Blood Urea: {urea} mg/dL → Normal")

    elif urea < 15:
        st.warning(f"Blood Urea: {urea} mg/dL → Low")

    else:
        st.error(f"Blood Urea: {urea} mg/dL → High")
        st.info("High blood urea may occur with dehydration, kidney disease, or other conditions.")

# Uric Acid
if uric_acid > 0:

    if 3.5 <= uric_acid <= 7.2:
        st.success(f"Uric Acid: {uric_acid} mg/dL → Normal")

    elif uric_acid < 3.5:
        st.warning(f"Uric Acid: {uric_acid} mg/dL → Low")

    else:
        st.error(f"Uric Acid: {uric_acid} mg/dL → High")
        st.info("High uric acid may increase the risk of gout or kidney stones.")

# eGFR
if egfr > 0:

    if egfr >= 90:
        st.success(f"eGFR: {egfr} → Normal Kidney Function")

    elif egfr >= 60:
        st.warning(f"eGFR: {egfr} → Mildly Decreased Kidney Function")

    elif egfr >= 30:
        st.error(f"eGFR: {egfr} → Moderately Decreased Kidney Function")

    elif egfr >= 15:
        st.error(f"eGFR: {egfr} → Severely Decreased Kidney Function")

    else:
        st.error(f"eGFR: {egfr} → Kidney Failure Range")
        st.info("Please seek prompt medical evaluation.")
#-------------------
st.subheader("🦋 Thyroid Profile Analysis")

# ---------- TSH ----------

if tsh > 0:

    if 0.4 <= tsh <= 4.0:
        st.success(f"TSH : {tsh} µIU/mL → Normal")

    elif tsh < 0.4:
        st.warning(f"TSH : {tsh} µIU/mL → Low")
        st.info("Low TSH may suggest Hyperthyroidism. Clinical correlation is required.")

    else:
        st.error(f"TSH : {tsh} µIU/mL → High")
        st.info("High TSH may suggest Hypothyroidism. Please consult your healthcare provider.")

# ---------- T3 ----------

if t3 > 0:

    if 80 <= t3 <= 200:
        st.success(f"T3 : {t3} ng/dL → Normal")

    elif t3 < 80:
        st.warning(f"T3 : {t3} ng/dL → Low")
        st.info("Low T3 may occur in hypothyroidism or other illnesses.")

    else:
        st.warning(f"T3 : {t3} ng/dL → High")
        st.info("High T3 may suggest hyperthyroidism.")

# ---------- T4 ----------

if t4 > 0:

    if 5.0 <= t4 <= 12.0:
        st.success(f"T4 : {t4} µg/dL → Normal")

    elif t4 < 5.0:
        st.warning(f"T4 : {t4} µg/dL → Low")
        st.info("Low T4 may indicate hypothyroidism.")

    else:
        st.warning(f"T4 : {t4} µg/dL → High")
        st.info("High T4 may indicate hyperthyroidism.")
#-------------------
st.subheader("⚡ Electrolytes & Minerals Analysis")

# Sodium
if sodium > 0:
    if 135 <= sodium <= 145:
        st.success(f"Sodium: {sodium} mEq/L → Normal")
    elif sodium < 135:
        st.warning(f"Sodium: {sodium} mEq/L → Low (Hyponatremia)")
        st.info("Low sodium may cause weakness, confusion or seizures in severe cases.")
    else:
        st.error(f"Sodium: {sodium} mEq/L → High (Hypernatremia)")
        st.info("High sodium may occur with dehydration or excessive water loss.")

# Potassium
if potassium > 0:
    if 3.5 <= potassium <= 5.0:
        st.success(f"Potassium: {potassium} mEq/L → Normal")
    elif potassium < 3.5:
        st.warning(f"Potassium: {potassium} mEq/L → Low (Hypokalemia)")
        st.info("Low potassium may cause muscle weakness or abnormal heart rhythm.")
    else:
        st.error(f"Potassium: {potassium} mEq/L → High (Hyperkalemia)")
        st.info("High potassium can affect heart rhythm and requires prompt medical evaluation.")

# Chloride
if chloride > 0:
    if 98 <= chloride <= 107:
        st.success(f"Chloride: {chloride} mEq/L → Normal")
    else:
        st.warning(f"Chloride: {chloride} mEq/L → Abnormal")
        st.info("Abnormal chloride levels may reflect dehydration or acid-base imbalance.")

# Calcium
if calcium > 0:
    if 8.5 <= calcium <= 10.5:
        st.success(f"Calcium: {calcium} mg/dL → Normal")
    elif calcium < 8.5:
        st.warning(f"Calcium: {calcium} mg/dL → Low")
        st.info("Low calcium may cause tingling, muscle cramps or spasms.")
    else:
        st.warning(f"Calcium: {calcium} mg/dL → High")
        st.info("High calcium may be associated with parathyroid disorders or other conditions.")

# Magnesium
if magnesium > 0:
    if 1.7 <= magnesium <= 2.4:
        st.success(f"Magnesium: {magnesium} mg/dL → Normal")
    elif magnesium < 1.7:
        st.warning(f"Magnesium: {magnesium} mg/dL → Low")
    else:
        st.warning(f"Magnesium: {magnesium} mg/dL → High")

# Phosphorus
if phosphorus > 0:
    if 2.5 <= phosphorus <= 4.5:
        st.success(f"Phosphorus: {phosphorus} mg/dL → Normal")
    elif phosphorus < 2.5:
        st.warning(f"Phosphorus: {phosphorus} mg/dL → Low")
    else:
        st.warning(f"Phosphorus: {phosphorus} mg/dL → High")
#-------------------
st.subheader("💊 Vitamin & Iron Profile Analysis")

# Vitamin D
if vitamin_d > 0:

    if vitamin_d < 20:
        st.error(f"Vitamin D : {vitamin_d} ng/mL → Deficient")
        st.info("Vitamin D deficiency may affect bone health and muscle function. Consult your healthcare provider.")

    elif vitamin_d < 30:
        st.warning(f"Vitamin D : {vitamin_d} ng/mL → Insufficient")

    elif vitamin_d <= 100:
        st.success(f"Vitamin D : {vitamin_d} ng/mL → Normal")

    else:
        st.warning(f"Vitamin D : {vitamin_d} ng/mL → High")


# Vitamin B12
if vitamin_b12 > 0:

    if vitamin_b12 < 200:
        st.error(f"Vitamin B12 : {vitamin_b12} pg/mL → Low")
        st.info("Low Vitamin B12 may contribute to anemia and nerve-related symptoms.")

    elif vitamin_b12 <= 900:
        st.success(f"Vitamin B12 : {vitamin_b12} pg/mL → Normal")

    else:
        st.warning(f"Vitamin B12 : {vitamin_b12} pg/mL → High")


# Serum Iron
if serum_iron > 0:

    if 60 <= serum_iron <= 170:
        st.success(f"Serum Iron : {serum_iron} µg/dL → Normal")

    elif serum_iron < 60:
        st.warning(f"Serum Iron : {serum_iron} µg/dL → Low")

    else:
        st.warning(f"Serum Iron : {serum_iron} µg/dL → High")


# Ferritin
if ferritin > 0:

    if 30 <= ferritin <= 300:
        st.success(f"Ferritin : {ferritin} ng/mL → Normal")

    elif ferritin < 30:
        st.warning(f"Ferritin : {ferritin} ng/mL → Low")
        st.info("Low ferritin may indicate reduced iron stores.")

    else:
        st.warning(f"Ferritin : {ferritin} ng/mL → High")


# TIBC
if tibc > 0:

    if 250 <= tibc <= 450:
        st.success(f"TIBC : {tibc} µg/dL → Normal")

    elif tibc < 250:
        st.warning(f"TIBC : {tibc} µg/dL → Low")

    else:
        st.warning(f"TIBC : {tibc} µg/dL → High")
#-------------------
st.subheader("🦴 Inflammatory & Autoimmune Analysis")

# CRP
if crp > 0:

    if crp <= 5:
        st.success(f"CRP : {crp} mg/L → Normal")

    elif crp <= 10:
        st.warning(f"CRP : {crp} mg/L → Mildly Elevated")
        st.info("May indicate mild inflammation or infection.")

    else:
        st.error(f"CRP : {crp} mg/L → High")
        st.info("High CRP may suggest significant inflammation, infection or autoimmune disease.")

# Rheumatoid Factor

if rf > 0:

    if rf < 20:
        st.success(f"Rheumatoid Factor : {rf} IU/mL → Normal")

    else:
        st.warning(f"Rheumatoid Factor : {rf} IU/mL → Positive")
        st.info("Positive RF may occur in Rheumatoid Arthritis and some other autoimmune disorders.")

# Anti CCP

if anti_ccp > 0:

    if anti_ccp < 20:
        st.success(f"Anti-CCP : {anti_ccp} U/mL → Negative")

    else:
        st.error(f"Anti-CCP : {anti_ccp} U/mL → Positive")
        st.info("Positive Anti-CCP strongly supports Rheumatoid Arthritis in the appropriate clinical setting.")

# ASO

if aso > 0:

    if aso <= 200:
        st.success(f"ASO Titre : {aso} IU/mL → Normal")

    else:
        st.warning(f"ASO Titre : {aso} IU/mL → Elevated")
        st.info("Raised ASO titre may indicate a recent Streptococcal infection.")

# ANA

if ana=="Positive":

    st.warning("ANA Result : Positive")
    st.info("A positive ANA test may be associated with autoimmune diseases such as systemic lupus erythematosus (SLE), but must be interpreted with clinical findings.")

elif ana=="Negative":

    st.success("ANA Result : Negative")
#-------------------
st.subheader("🩸 Coagulation Profile Analysis")

# PT
if pt > 0:

    if 11 <= pt <= 13.5:
        st.success(f"PT : {pt} sec → Normal")

    elif pt > 13.5:
        st.warning(f"PT : {pt} sec → Prolonged")
        st.info("A prolonged PT may occur with liver disease, vitamin K deficiency or anticoagulant therapy.")

    else:
        st.warning(f"PT : {pt} sec → Slightly Low")


# INR
if inr > 0:

    if 0.8 <= inr <= 1.2:
        st.success(f"INR : {inr} → Normal")

    elif inr > 1.2:
        st.warning(f"INR : {inr} → Elevated")
        st.info("An elevated INR may increase bleeding risk depending on the clinical situation.")

    else:
        st.warning(f"INR : {inr} → Low")


# aPTT
if aptt > 0:

    if 25 <= aptt <= 35:
        st.success(f"aPTT : {aptt} sec → Normal")

    else:
        st.warning(f"aPTT : {aptt} sec → Abnormal")
        st.info("Abnormal aPTT may indicate a coagulation disorder or anticoagulant effect.")
#-------------------
st.subheader("❤️ Cardiac Marker Analysis")

# Troponin
if troponin > 0:

    if troponin < 0.04:
        st.success(f"Troponin I : {troponin} ng/mL → Normal")

    else:
        st.error(f"Troponin I : {troponin} ng/mL → Elevated")
        st.warning("Elevated troponin may indicate heart muscle injury. Urgent medical evaluation is recommended.")


# CK-MB
if ckmb > 0:

    if ckmb <= 5:
        st.success(f"CK-MB : {ckmb} ng/mL → Normal")

    else:
        st.warning(f"CK-MB : {ckmb} ng/mL → Elevated")
        st.info("An elevated CK-MB may be associated with heart muscle injury.")


# BNP
if bnp > 0:

    if bnp < 100:
        st.success(f"BNP : {bnp} pg/mL → Normal")

    elif bnp <= 400:
        st.warning(f"BNP : {bnp} pg/mL → Elevated")
        st.info("An elevated BNP may be associated with heart failure and requires clinical assessment.")

    else:
        st.error(f"BNP : {bnp} pg/mL → Markedly Elevated")
        st.warning("Please seek prompt medical evaluation.")
#--------------------
st.divider()

st.subheader("🦠 Infection Profile Analysis")

# Dengue NS1
if dengue_ns1 == "Positive":
    st.error("🦟 Dengue NS1 : Positive")
    st.info("A positive Dengue NS1 result may indicate an early dengue infection. Please consult a qualified healthcare professional.")

elif dengue_ns1 == "Negative":
    st.success("🦟 Dengue NS1 : Negative")


# Dengue IgM
if dengue_igm == "Positive":
    st.warning("🦟 Dengue IgM : Positive")
    st.info("A positive Dengue IgM may suggest a recent dengue infection.")

elif dengue_igm == "Negative":
    st.success("🦟 Dengue IgM : Negative")


# Dengue IgG
if dengue_igg == "Positive":
    st.warning("🦟 Dengue IgG : Positive")
    st.info("A positive Dengue IgG may indicate past exposure or a secondary dengue infection.")

elif dengue_igg == "Negative":
    st.success("🦟 Dengue IgG : Negative")


# Malaria
if malaria == "Positive":
    st.error("🦟 Malaria Antigen : Positive")
    st.info("A positive malaria test requires prompt medical evaluation and appropriate treatment.")

elif malaria == "Negative":
    st.success("🦟 Malaria Antigen : Negative")


# Typhoid
if typhoid == "Positive":
    st.warning("🧫 Typhoid Test : Positive")
    st.info("A positive typhoid screening test should be interpreted together with symptoms and, when appropriate, confirmatory testing.")

elif typhoid == "Negative":
    st.success("🧫 Typhoid Test : Negative")


# Hepatitis B
if hbsag == "Positive":
    st.error("🦠 HBsAg : Positive")
    st.info("A positive HBsAg suggests hepatitis B infection and requires evaluation by a qualified healthcare professional.")

elif hbsag == "Negative":
    st.success("🦠 HBsAg : Negative")


# Hepatitis C
if anti_hcv == "Positive":
    st.error("🦠 Anti-HCV : Positive")
    st.info("A positive Anti-HCV screening test should be confirmed with additional testing as advised by a healthcare professional.")

elif anti_hcv == "Negative":
    st.success("🦠 Anti-HCV : Negative")


# HIV
if hiv == "Positive":
    st.error("🦠 HIV Screening : Reactive / Positive")
    st.info("A reactive HIV screening result requires confirmatory testing and consultation with a qualified healthcare professional.")

elif hiv == "Negative":
    st.success("🦠 HIV Screening : Negative")
#-------------------
st.subheader("🧬 Tumor Marker Analysis")

# PSA
if psa > 0:

    if psa <= 4:
        st.success(f"PSA : {psa} ng/mL → Within Common Reference Range")

    else:
        st.warning(f"PSA : {psa} ng/mL → Above Common Reference Range")
        st.info("An elevated PSA may occur with prostate enlargement, prostatitis or prostate cancer. Further medical evaluation is required.")

# CEA
if cea > 0:

    if cea <= 5:
        st.success(f"CEA : {cea} ng/mL → Within Common Reference Range")

    else:
        st.warning(f"CEA : {cea} ng/mL → Elevated")
        st.info("CEA may increase in several cancers and also in some non-cancerous conditions such as smoking or inflammation.")

# CA-125
if ca125 > 0:

    if ca125 <= 35:
        st.success(f"CA-125 : {ca125} U/mL → Within Common Reference Range")

    else:
        st.warning(f"CA-125 : {ca125} U/mL → Elevated")
        st.info("An elevated CA-125 may be associated with ovarian disorders or other benign and malignant conditions.")

# CA19-9
if ca199 > 0:

    if ca199 <= 37:
        st.success(f"CA 19-9 : {ca199} U/mL → Within Common Reference Range")

    else:
        st.warning(f"CA 19-9 : {ca199} U/mL → Elevated")
        st.info("CA 19-9 may be elevated in pancreatic or biliary diseases and other conditions.")

# AFP
if afp > 0:

    if afp <= 10:
        st.success(f"AFP : {afp} ng/mL → Within Common Reference Range")

    else:
        st.warning(f"AFP : {afp} ng/mL → Elevated")
        st.info("AFP may be elevated in liver disease, pregnancy and some cancers. Clinical correlation is necessary.")
#-----------------
st.divider()

st.subheader("🧬 Hormone Profile Analysis")

# Testosterone
if testosterone > 0:
    if 300 <= testosterone <= 1000:
        st.success(f"Testosterone: {testosterone} ng/dL → Within Common Adult Male Reference Range")
    else:
        st.warning(f"Testosterone: {testosterone} ng/dL → Outside Common Adult Male Reference Range")
        st.info("Reference ranges differ by sex and age. Clinical interpretation is required.")

# FSH
if fsh > 0:
    if 1 <= fsh <= 12:
        st.success(f"FSH: {fsh} mIU/mL → Within Common Reference Range")
    else:
        st.warning(f"FSH: {fsh} mIU/mL → Outside Common Reference Range")
        st.info("FSH interpretation depends on age, sex and menstrual status.")

# LH
if lh > 0:
    if 1 <= lh <= 9:
        st.success(f"LH: {lh} mIU/mL → Within Common Reference Range")
    else:
        st.warning(f"LH: {lh} mIU/mL → Outside Common Reference Range")
        st.info("LH reference values vary with age, sex and menstrual cycle.")

# Prolactin
if prolactin > 0:
    if 5 <= prolactin <= 25:
        st.success(f"Prolactin: {prolactin} ng/mL → Within Common Reference Range")
    else:
        st.warning(f"Prolactin: {prolactin} ng/mL → Outside Common Reference Range")
        st.info("Prolactin may be affected by pregnancy, medications and pituitary disorders.")

# Estradiol
if estradiol > 0:
    st.info(f"Estradiol: {estradiol} pg/mL")
    st.write("Interpretation depends on sex, age and menstrual cycle phase.")

# Progesterone
if progesterone > 0:
    st.info(f"Progesterone: {progesterone} ng/mL")
    st.write("Interpretation depends on menstrual cycle phase or pregnancy status.")

# Cortisol
if cortisol > 0:
    if 5 <= cortisol <= 25:
        st.success(f"Cortisol: {cortisol} µg/dL → Within Common Morning Reference Range")
    else:
        st.warning(f"Cortisol: {cortisol} µg/dL → Outside Common Morning Reference Range")
        st.info("Cortisol levels vary with time of day and clinical conditions.")

#----------

#---------------

st.divider()

#-----------------------#
st.divider()

with st.expander("🩸 Importance of Diabetes Profile"):

    st.write("""
The Diabetes Profile helps evaluate blood glucose control and supports the screening and monitoring of diabetes mellitus.

• Fasting Blood Sugar measures blood glucose after at least 8 hours without food.

• Post Meal Blood Sugar assesses how the body handles glucose approximately 2 hours after eating.

• Random Blood Sugar provides a glucose measurement at any time and may support evaluation when symptoms are present.

• HbA1c reflects the average blood glucose level over the previous 2–3 months and is widely used for long-term monitoring.

Results should always be interpreted together with symptoms, medical history and advice from a qualified healthcare professional.
""")

#-------

with st.expander("📚 About CBC Tests"):
    st.write("""
**Hemoglobin (Hb):** Carries oxygen in the blood.

**WBC:** Helps fight infections.

**RBC:** Carries oxygen from the lungs to body tissues.

**Platelets:** Help blood clot and prevent excessive bleeding.

**ESR:** A general marker of inflammation; it is not specific for any one disease.
""")
  #--------
st.divider()

with st.expander("❤️ Importance of Lipid Profile"):

    st.write("""
The Lipid Profile measures fats in your blood that are associated with cardiovascular health.

• Total Cholesterol gives an overall picture of blood cholesterol.

• HDL ("good cholesterol") helps remove excess cholesterol from the bloodstream.

• LDL ("bad cholesterol") can contribute to plaque buildup in arteries when elevated.

• Triglycerides are a type of fat that may increase cardiovascular risk when persistently high.

Maintaining a balanced diet, engaging in regular physical activity, avoiding tobacco, and following your healthcare provider's advice can help support healthy lipid levels.
""")
  #-------------
st.divider()

with st.expander("🧪 Importance of Liver Function Test"):

    st.write("""
Liver Function Tests (LFTs) help assess how well your liver is working.

• ALT (SGPT) and AST (SGOT) are enzymes that may increase when liver cells are damaged.

• Bilirubin is produced when red blood cells break down. High levels may cause jaundice.

• Albumin is a protein made by the liver and reflects liver function as well as nutritional status.

• Alkaline Phosphatase (ALP) may increase in certain liver or bone conditions.

These tests should always be interpreted together with your symptoms, medical history and your healthcare provider's assessment.
""")

 #--------------
st.divider()

with st.expander("🩺 Importance of Kidney Function Test"):

    st.write("""
Kidney Function Tests (KFT) help evaluate how effectively the kidneys filter waste products and maintain the body's fluid and electrolyte balance.

• Serum Creatinine is a key indicator of kidney filtration.

• Blood Urea reflects protein metabolism and may rise with dehydration or reduced kidney function.

• Uric Acid is associated with gout, kidney stones and some metabolic conditions when elevated.

• eGFR estimates how well the kidneys are filtering blood and is commonly used to stage chronic kidney disease.

Abnormal KFT results should always be interpreted together with symptoms, medical history and advice from a qualified healthcare professional.
""")
#-------------------
st.divider()

with st.expander("🦋 Importance of Thyroid Profile"):

    st.write("""
The Thyroid Profile evaluates how well the thyroid gland is functioning.

• TSH (Thyroid Stimulating Hormone) is the primary screening test for thyroid disorders.

• T3 (Triiodothyronine) is an active thyroid hormone involved in metabolism, heart rate and energy production.

• T4 (Thyroxine) is the main hormone produced by the thyroid gland and is converted into T3 in the body.

Abnormal thyroid hormone levels may contribute to symptoms such as fatigue, weight changes, heat or cold intolerance, hair loss, constipation, palpitations or mood changes.

Thyroid test results should always be interpreted together with symptoms and by a qualified healthcare professional.
""")
#-------------------
st.divider()

with st.expander("⚡ Importance of Electrolytes & Minerals"):

    st.write("""
Electrolytes and minerals are essential for normal body function.

• Sodium helps regulate body fluid balance and nerve function.

• Potassium is important for heart rhythm, muscle contraction and nerve transmission.

• Chloride helps maintain acid-base balance and hydration.

• Calcium supports bone health, muscle contraction and blood clotting.

• Magnesium is involved in hundreds of enzyme reactions and supports muscles, nerves and the heart.

• Phosphorus is essential for healthy bones, teeth and energy production.

Abnormal values should always be interpreted together with symptoms, medical history and by a qualified healthcare professional.
""")
#-------------------
st.divider()

with st.expander("💊 Importance of Vitamin & Iron Profile"):

    st.write("""
Vitamin and Iron Profile helps evaluate nutritional status and detect common deficiencies.

• Vitamin D supports bone health, muscle strength and immune function.

• Vitamin B12 is important for red blood cell production and normal nerve function.

• Serum Iron measures circulating iron in the blood.

• Ferritin reflects the body's stored iron and is useful for detecting iron deficiency.

• TIBC (Total Iron Binding Capacity) helps assess how well iron is transported in the blood.

Abnormal results should always be interpreted together with symptoms, medical history and by a qualified healthcare professional.
""")
#-------------------
st.divider()

with st.expander("🦴 Importance of Inflammatory & Autoimmune Tests"):

    st.write("""

CRP measures inflammation in the body and is commonly used to monitor infections and inflammatory conditions.

Rheumatoid Factor (RF) is frequently used during the evaluation of Rheumatoid Arthritis.

Anti-CCP antibody has higher specificity than RF for Rheumatoid Arthritis and may support the diagnosis when interpreted with symptoms and examination.

ASO Titre helps identify a recent Streptococcal infection and may assist in evaluating complications such as Rheumatic Fever.

ANA (Antinuclear Antibody) is used when autoimmune connective tissue diseases are suspected. A positive result alone does not establish a diagnosis.

These tests should always be interpreted together with symptoms, physical examination and other investigations by a qualified healthcare professional.

""")
#-------------------
st.divider()

with st.expander("❤️ Importance of Coagulation & Cardiac Markers"):

    st.write("""
Coagulation Profile evaluates how well your blood clots.

• PT measures the extrinsic clotting pathway.

• INR standardizes PT and is commonly used to monitor warfarin therapy.

• aPTT evaluates the intrinsic clotting pathway.

Cardiac Markers help assess possible heart muscle injury.

• Troponin is the most specific blood marker for myocardial injury.

• CK-MB may increase after damage to heart muscle.

• BNP helps assess heart failure and cardiac stress.

Abnormal results require interpretation together with symptoms, ECG findings and other investigations by a qualified healthcare professional.
""")

#-----------------
# =====================================================
# IMPORTANCE OF INFECTION TESTS
# =====================================================

st.divider()

with st.expander("🦠 Importance of Infection Profile"):

    st.write("""
The Infection Profile includes commonly used screening tests for infectious diseases.

• Dengue NS1 is useful during the early stage of dengue fever.

• Dengue IgM usually indicates a recent dengue infection.

• Dengue IgG may indicate previous exposure or a secondary infection.

• Malaria Antigen helps rapidly detect malaria parasites.

• Typhoid tests may support the diagnosis of typhoid fever when interpreted together with symptoms and other investigations.

• HBsAg is a screening test for Hepatitis B infection.

• Anti-HCV is a screening test for Hepatitis C infection.

• HIV screening tests help detect possible HIV infection but reactive results require confirmatory testing.

These tests should always be interpreted together with the patient's symptoms, history, physical examination and additional laboratory investigations.
""")

# =====================================================
# OVERALL INFECTION SUMMARY
# =====================================================

st.divider()

st.header("🩺 Overall Infection Summary")

positive_tests = []

if dengue_ns1 == "Positive":
    positive_tests.append("Dengue NS1")

if dengue_igm == "Positive":
    positive_tests.append("Dengue IgM")

if dengue_igg == "Positive":
    positive_tests.append("Dengue IgG")

if malaria == "Positive":
    positive_tests.append("Malaria Antigen")

if typhoid == "Positive":
    positive_tests.append("Typhoid")

if hbsag == "Positive":
    positive_tests.append("HBsAg")

if anti_hcv == "Positive":
    positive_tests.append("Anti-HCV")

if hiv == "Positive":
    positive_tests.append("HIV Screening")

if len(positive_tests) == 0:

    st.success("🟢 No Positive Infection Screening Tests Entered.")

    st.write("""
• Continue maintaining good hygiene.

• Drink safe water.

• Eat hygienic food.

• Complete recommended vaccinations.

• Consult your healthcare provider if symptoms develop despite negative screening tests.
""")

else:

    st.warning("🟡 Positive Tests Detected")

    st.write("Positive Results:")

    for test in positive_tests:
        st.write(f"• {test}")

    st.info("""
Positive screening tests do not always confirm a diagnosis.

Further clinical evaluation, confirmatory laboratory tests and medical consultation are recommended before making treatment decisions.
""")

# =====================================================
# MEDICAL DISCLAIMER
# =====================================================

st.divider()

st.warning("""
⚠️ Medical Disclaimer

This Infection Profile provides educational interpretation only.

It is NOT intended to diagnose or rule out any infectious disease.

Always consult a qualified healthcare professional for confirmation, diagnosis and treatment decisions.
""")
#------------------
st.divider()

with st.expander("🧬 Importance of Tumor Markers"):

    st.write("""
Tumor markers are substances that may be measured in blood and can assist healthcare professionals during the evaluation or monitoring of certain diseases.

• PSA is commonly used in the assessment of prostate disorders.

• CEA may be used during follow-up of some gastrointestinal and other cancers.

• CA-125 is often used during the evaluation and monitoring of certain ovarian conditions.

• CA 19-9 may be used alongside other investigations for pancreatic and biliary diseases.

• AFP may assist in the evaluation of certain liver diseases and specific tumors.

Tumor marker results alone cannot diagnose or exclude cancer. They must always be interpreted together with symptoms, physical examination, imaging studies and, when appropriate, biopsy findings by a qualified healthcare professional.
""")

#---
st.divider()

with st.expander("🧬 Importance of Hormone Profile"):

    st.write("""
Hormone tests help assess the function of endocrine glands and reproductive health.

• Testosterone supports muscle mass, bone health and reproductive function.

• FSH and LH regulate reproductive hormone production and fertility.

• Prolactin plays a role in lactation and may be elevated in pituitary disorders.

• Estradiol is an important estrogen hormone involved in reproductive health.

• Progesterone is essential for ovulation, menstrual regulation and pregnancy.

• Cortisol is produced by the adrenal glands and helps regulate metabolism, stress response and immune function.

Reference ranges vary according to age, sex, pregnancy status and, in women, the menstrual cycle. Hormone test results should always be interpreted by a qualified healthcare professional in the appropriate clinical context.
""")
#--------

#-------------

st.warning("""
⚠️ This tool is for educational purposes only and does not replace
professional medical advice or diagnosis.
""")
