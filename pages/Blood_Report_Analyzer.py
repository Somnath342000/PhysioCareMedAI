import streamlit as st

st.set_page_config(
    page_title="Blood Report Analyzer",
    page_icon="🩸",
    layout="wide"
)

st.title("🩸 Blood Report Analyzer")
st.info("Enter available blood test values. Leave the others as 0.")

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
#-------------------
if st.button("🔍 Analyze Report"):

    st.header("📋 CBC Analysis")

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
#-------------------

st.divider()

#-----------------------#
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
#-------------------

st.warning("""
⚠️ This tool is for educational purposes only and does not replace
professional medical advice or diagnosis.
""")
