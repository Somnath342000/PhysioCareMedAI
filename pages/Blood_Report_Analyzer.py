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

st.header("🍯 Diabetes Profile")

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
# 1. Fasting Blood Sugar (FBS)
with st.expander("🅰️ Fasting Blood Sugar (FBS) - Code: FBS_01"):
    st.markdown("""
    ### 🩸 What is it?
    **Fasting Blood Sugar (FBS)** measures the amount of glucose (sugar) in your blood after an overnight fast of strictly 8 to 12 hours. During this time, you can only drink plain water.
    
    ### 🎯 Importance of the Test
    This is the foundational baseline test for diagnosing prediabetes and diabetes. It shows how well your body manages blood sugar without the immediate influence of food.
    - **Normal Range:** 70 - 99 mg/dL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hyperglycemia):** Indicates insulin resistance or diabetes. Symptoms include **excessive morning thirst, waking up multiple times at night to urinate, dry mouth, and blurry vision**.
    * **If Low (Hypoglycemia):** Less than 70 mg/dL. Symptoms include **shakiness, sudden cold sweats, extreme hunger, dizziness, and a racing heart**.
    """)

# 2. Post Meal Blood Sugar (PPBS)
with st.expander("🅱️ Post Meal Blood Sugar (PPBS) - Code: PPBS_02"):
    st.markdown("""
    ### 🩸 What is it?
    **Post Prandial Blood Sugar (PPBS)** measures your blood glucose exactly **2 hours after you start eating** a meal. 
    
    ### 🎯 Importance of the Test
    This test shows how effectively your body (specifically insulin) handles the carbohydrate load from your food. Sometimes fasting sugar is normal, but post-meal sugar spikes dangerously.
    - **Normal Range:** Less than 140 mg/dL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates your body isn't producing enough insulin to handle meals. Symptoms include **extreme lethargy or sleepiness after eating (food coma), persistent brain fog, and sudden intense thirst**.
    * **If Low:** Known as reactive hypoglycemia (sugar dropping too fast after a meal). Symptoms include **sudden anxiety, tremors, sweating, and confusion 1-3 hours after eating**.
    """)

# 3. Random Blood Sugar (RBS)
with st.expander("🅲 Random Blood Sugar (RBS) - Code: RBS_03"):
    st.markdown("""
    ### 🩸 What is it?
    **Random Blood Sugar (RBS)** can be measured at any time of the day, completely regardless of when you last ate.
    
    ### 🎯 Importance of the Test
    It is used as a quick screening tool, especially in emergencies, or when severe diabetes is suspected based on sudden symptoms.
    - **Normal Range:** Generally less than 140 mg/dL (A reading of 200 mg/dL or higher, accompanied by symptoms, confirms diabetes).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** You may experience the classic "Three Ps" of diabetes: **Polyuria (frequent urination), Polydipsia (excessive thirst), and Polyphagia (extreme hunger despite eating)**. Unexplained weight loss is also common.
    * **If Low:** Medical emergency. Symptoms include **severe weakness, fainting, clammy skin, and slurred speech**.
    """)

# 4. HbA1c (Glycated Hemoglobin)
with st.expander("🅳 HbA1c (3-Month Average) - Code: HBA1C_04"):
    st.markdown("""
    ### 🩸 What is it?
    **HbA1c** measures the percentage of red blood cells that have sugar attached to them (glycated). Because red blood cells live for about 3 months, this test reflects your average blood sugar level over the past 8 to 12 weeks.
    
    ### 🎯 Importance of the Test
    This is the **gold standard** for diabetes management. Unlike FBS or PPBS, which can change based on yesterday's dinner or stress, HbA1c cannot be "cheated." It does not require fasting.
    - **Normal Range:** Less than 5.7% (5.7% - 6.4% indicates Prediabetes; 6.5% or higher indicates Diabetes).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates long-term uncontrolled blood sugar, leading to organ damage. Symptoms include **frequent skin or yeast infections, slow-healing wounds, and tingling/numbness in the hands or feet (Neuropathy)**.
    * **If Low (< 4.0%):** Rare, usually caused by taking too much diabetes medication, severe anemia, or liver disease. Symptoms mirror chronic hypoglycemia (constant fatigue and dizziness).
    """)

st.divider()
st.info("💡 **Note:** Fasting Blood Sugar (FBS) requires a strict 8-12 hour fast. However, HbA1c requires absolutely no fasting and can be tested at any time of the day. If your app calculates health scores, an HbA1c > 7.0% for a known diabetic usually triggers an alert to adjust their medication.")


st.divider()
#-------------
st.header("Complete Blood Count (CBC)")

hb = st.number_input("Hemoglobin (g/dL)", min_value=0.0, value=0.0, step=0.1)
wbc = st.number_input("WBC (/µL)", min_value=0, value=0)
rbc = st.number_input("RBC (million/µL)", min_value=0.0, value=0.0, step=0.1)
platelet = st.number_input("Platelet (/µL)", min_value=0, value=0)
esr = st.number_input("ESR (mm/hr)", min_value=0, value=0)

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
with st.expander("🔴 Hemoglobin (Hb)"):
    st.write("""
    **Hemoglobin** measures the protein in your red blood cells that carries oxygen to your body's organs and tissues.
    - **Normal Range:** 12.1 - 17.2 g/dL (Varies by gender)
    - **Significance:** Low levels indicate anemia, leading to fatigue and weakness.
    """)

with st.expander("⚪ White Blood Cells (WBC)"):
    st.write("""
    **WBC** count measures the cells that fight infection in your body.
    - **Normal Range:** 4,500 - 11,000 cells/µL
    - **Significance:** High counts often indicate an ongoing infection or inflammation.
    """)

with st.expander("💉 Platelets"):
    st.write("""
    **Platelets** are cell fragments that help your blood clot to stop bleeding.
    - **Normal Range:** 150,000 - 450,000 /µL
    - **Significance:** Low platelets can lead to excessive bruising or bleeding (commonly monitored in Dengue).
    """)

with st.expander("⏳ ESR (Erythrocyte Sedimentation Rate)"):
    st.write("""
    **ESR** is a type of blood test that measures how quickly erythrocytes (red blood cells) settle at the bottom of a test tube.
    - **Normal Range:** < 15-20 mm/hr
    - **Significance:** A faster-than-normal rate can signal inflammation in the body.
    """)
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
with st.expander("❤️ Importance of Lipid Profile"):

    st.write("""
The Lipid Profile measures fats in your blood that are associated with cardiovascular health.

• Total Cholesterol gives an overall picture of blood cholesterol.

• HDL ("good cholesterol") helps remove excess cholesterol from the bloodstream.

• LDL ("bad cholesterol") can contribute to plaque buildup in arteries when elevated.

• Triglycerides are a type of fat that may increase cardiovascular risk when persistently high.

Maintaining a balanced diet, engaging in regular physical activity, avoiding tobacco, and following your healthcare provider's advice can help support healthy lipid levels.
""")
# 1. Total Cholesterol
with st.expander("📊 Total Cholesterol (Code: CHOL_01)"):
    st.markdown("""
    ### 🩸 What is it?
    **Total Cholesterol** is the overall amount of cholesterol found in your blood. It includes both "good" (HDL) and "bad" (LDL) cholesterol.
    
    ### 🎯 Importance of the Test
    It serves as a baseline screening tool to assess your overall risk of cardiovascular (heart) disease. Keeping this in a desirable range helps prevent plaque buildup in arteries.
    - **Normal/Desirable Range:** Less than 200 mg/dL
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (>240 mg/dL):** High cholesterol itself is a **"silent killer"** and typically has **no direct symptoms** until it causes a medical emergency like a heart attack or stroke. In rare, severe cases, yellowish fatty deposits called *xanthomas* may appear on the skin or tendons.
    * **If Low (<120 mg/dL):** Very low cholesterol (hypocholesterolemia) is rare but can be linked to malnutrition, hyperthyroidism, or liver disease. Symptoms usually relate to the underlying cause (e.g., chronic fatigue, unintended weight loss).
    """)

# 2. HDL Cholesterol
with st.expander("🟢 HDL Cholesterol (The 'Good' Cholesterol) - Code: HDL_02"):
    st.markdown("""
    ### 🩸 What is it?
    **HDL (High-Density Lipoprotein)** is known as the **"Good" cholesterol**. It acts as a scavenger, absorbing excess cholesterol in your blood and carrying it back to the liver, where it is flushed from the body.
    
    ### 🎯 Importance of the Test
    Higher HDL levels are protective. A high HDL level lowers your risk for heart disease and stroke, while a low level increases the risk.
    - **Optimal Range:** 60 mg/dL or higher (Below 40 mg/dL for men and 50 mg/dL for women is considered a major risk factor).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Generally has no symptoms and is highly beneficial. However, extremely abnormally high levels (due to genetic mutations) don't offer extra protection and carry no specific symptoms.
    * **If Low:** No immediate physical symptoms, but over time, it silently accelerates artery clogging (atherosclerosis), which can eventually lead to chest pain (angina) or shortness of breath during exertion.
    """)

# 3. LDL Cholesterol
with st.expander("🔴 LDL Cholesterol (The 'Bad' Cholesterol) - Code: LDL_03"):
    st.markdown("""
    ### 🩸 What is it?
    **LDL (Low-Density Lipoprotein)** is known as the **"Bad" cholesterol**. It carries cholesterol from your liver to the rest of your body. If there is too much LDL, it builds up in the walls of your arteries.
    
    ### 🎯 Importance of the Test
    This is the most critical number to watch for heart disease risk. High LDL leads to **atherosclerosis** (hardening and narrowing of arteries), which directly causes heart attacks.
    - **Optimal Range:** Less than 100 mg/dL
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** There are **no direct symptoms**. However, if it causes significant arterial blockage, you might experience chest pain (angina), leg pain when walking (Peripheral Artery Disease), or sudden numbness/weakness if brain arteries are affected.
    * **If Low:** Very low LDL is uncommon but can happen with severe illness or genetic traits. It rarely causes symptoms but can sometimes be associated with a higher risk of hemorrhagic stroke or mood disorders in rare clinical contexts.
    """)

# 4. Triglycerides
with st.expander("🟡 Triglycerides (Code: TRIG_04)"):
    st.markdown("""
    ### 🩸 What is it?
    **Triglycerides** are the most common type of fat (lipids) in your body. They come from extra calories your body doesn't need right away, which are converted and stored in fat cells.
    
    ### 🎯 Importance of the Test
    High triglycerides combined with high LDL or low HDL can increase the risk of fatty liver disease and heart disease. 
    - **Normal Range:** Less than 150 mg/dL
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (>150 mg/dL, especially >500 mg/dL):** Mildly high levels have no symptoms. However, **extremely high levels (above 500 mg/dL)** can cause severe acute **pancreatitis** (inflammation of the pancreas). Symptoms include sudden, severe abdominal pain radiating to the back, nausea, and vomiting.
    * **If Low (<50 mg/dL):** Low triglycerides are generally healthy and have no symptoms, usually resulting from a low-fat diet, regular exercise, or an overactive thyroid.
    """)

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
# 1. ALT / SGPT
with st.expander("🔸 ALT / SGPT (Code: ALT_01)"):
    st.markdown("""
    ### 🩸 What is it?
    **Alanine Aminotransferase (ALT)**, formerly known as **SGPT**, is an enzyme found primarily in the liver. It plays a crucial role in converting food into energy.
    
    ### 🎯 Importance of the Test
    ALT is the most specific biomarker for liver injury. When liver cells are damaged or inflamed, ALT leaks into the bloodstream, making it an excellent early indicator of liver problems.
    - **Normal Range:** Typically $7 - 56$ U/L (units per liter)
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates liver inflammation or damage (e.g., Fatty Liver, Hepatitis, or alcohol damage). Symptoms include **jaundice** (yellowing of skin/eyes), **dark urine**, **fatigue**, and **nausea/vomiting**.
    * **If Low:** Low ALT levels are normal and expected, signifying a healthy, undamaged liver.
    """)

# 2. AST / SGOT
with st.expander("🔸 AST / SGOT (Code: AST_02)"):
    st.markdown("""
    ### 🩸 What is it?
    **Aspartate Aminotransferase (AST)**, formerly known as **SGOT**, is an enzyme found in the liver, but it is also present in high amounts in the heart, muscles, and kidneys.
    
    ### 🎯 Importance of the Test
    While not as specific to the liver as ALT, comparing the ratio of AST to ALT helps doctors pinpoint the exact cause of liver disease (e.g., alcoholic liver disease often shows higher AST than ALT).
    - **Normal Range:** Typically $10 - 40$ U/L
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Suggests liver damage, muscle injury, or heart issues. Symptoms closely mirror high ALT (**abdominal pain**, **jaundice**, **fatigue**), but if caused by muscle/heart damage, it might be accompanied by muscle soreness or chest pain.
    * **If Low:** Perfectly normal and indicates no active cell damage in these organs.
    """)

# 3. Total Bilirubin
with st.expander("🟡 Total Bilirubin (Code: BIL_03)"):
    st.markdown("""
    ### 🩸 What is it?
    **Bilirubin** is a yellowish pigment formed during the normal breakdown of old red blood cells. The liver filters bilirubin from the blood and excretes it through bile.
    
    ### 🎯 Importance of the Test
    This test measures how well the liver is processing and excreting waste. High levels indicate either a liver disease, a blockage in the bile ducts, or rapid destruction of red blood cells (hemolysis).
    - **Normal Range:** $0.2 - 1.2$ mg/dL
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (>2.0 mg/dL):** Leads to **Jaundice**. Visible symptoms include **distinct yellowing of the eyes and skin**, **intense skin itching (pruritus)**, **pale/clay-colored stools**, and **dark tea-colored urine**.
    * **If Low:** Generally not a medical concern and has no clinical symptoms.
    """)

# 4. Albumin
with st.expander("⚪ Albumin (Code: ALB_04)"):
    st.markdown("""
    ### 🩸 What is it?
    **Albumin** is the main protein produced by your liver. It keeps fluid from leaking out of your blood vessels into surrounding tissues and carries hormones, vitamins, and enzymes throughout the body.
    
    ### 🎯 Importance of the Test
    Albumin reflects the liver's synthetic capacity (how well it creates essential proteins) and your overall nutritional status.
    - **Normal Range:** $3.5 - 5.0$ g/dL
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Typically caused by severe dehydration. Symptoms include **extreme thirst**, **dry mouth**, and **lightheadedness**.
    * **If Low:** Indicates chronic liver disease (like Cirrhosis), kidney disease, or malnutrition. Symptoms include **edema** (swelling in the legs, ankles, or feet), **ascites** (fluid buildup in the abdomen), and **muscle weakness**.
    """)

# 5. Alkaline Phosphatase (ALP)
with st.expander("🔹 Alkaline Phosphatase / ALP (Code: ALP_05)"):
    st.markdown("""
    ### 🩸 What is it?
    **ALP** is an enzyme related to the bile ducts in the liver, but it is also heavily found in bones.
    
    ### 🎯 Importance of the Test
    It is primarily used to detect diseases of the liver or bone. In the liver, it specifically flags **cholestasis**—a condition where bile flow is slowed or blocked.
    - **Normal Range:** $44 - 147$ U/L (Can be higher in growing children and pregnant individuals)
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates blocked bile ducts, gallstones, or bone disorders. Symptoms include **severe upper right abdominal pain**, **jaundice**, **nausea**, or **bone pain/frequent fractures** if it's a bone-related issue.
    * **If Low:** Rare, but can be a sign of severe malnutrition, zinc deficiency, or a rare genetic condition called hypophosphatasia. Symptoms relate to bone weakness or slow healing.
    """)
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
with st.expander("🩺 Importance of Kidney Function Test"):

    st.write("""
Kidney Function Tests (KFT) help evaluate how effectively the kidneys filter waste products and maintain the body's fluid and electrolyte balance.

• Serum Creatinine is a key indicator of kidney filtration.

• Blood Urea reflects protein metabolism and may rise with dehydration or reduced kidney function.

• Uric Acid is associated with gout, kidney stones and some metabolic conditions when elevated.

• eGFR estimates how well the kidneys are filtering blood and is commonly used to stage chronic kidney disease.

Abnormal KFT results should always be interpreted together with symptoms, medical history and advice from a qualified healthcare professional.
""")
# 1. Serum Creatinine
with st.expander("🔹 Serum Creatinine (Code: CRE_01)"):
    st.markdown("""
    ### 🩸 What is it?
    **Creatinine** is a normal waste product created by the daily breakdown of muscle tissue. Healthy kidneys filter creatinine from your blood and excrete it through urine.
    
    ### 🎯 Importance of the Test
    It is one of the most direct and reliable indicators of kidney health. If your kidneys are malfunctioning, creatinine builds up in the blood.
    - **Normal Range:** Generally $0.7 - 1.3$ mg/dL for men, and $0.6 - 1.1$ mg/dL for women.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates reduced kidney function or severe dehydration. Symptoms include **fluid retention (swelling in feet/ankles)**, **shortness of breath**, **fatigue**, **nausea**, and **changes in urination frequency**.
    * **If Low:** Uncommon and usually not a kidney problem. It is typically caused by low muscle mass (due to aging or severe weight loss) or malnutrition. Symptoms relate to muscle weakness.
    """)

# 2. Blood Urea
with st.expander("🔸 Blood Urea / BUN (Code: UREA_02)"):
    st.markdown("""
    ### 🩸 What is it?
    **Urea** (often measured as Blood Urea Nitrogen or BUN) is a waste product formed in the liver when protein is broken down. Like creatinine, it is cleared from the body by the kidneys.
    
    ### 🎯 Importance of the Test
    This test helps evaluate kidney function and liver health, as well as tracking protein intake and hydration levels. It is often looked at in tandem with creatinine (BUN-to-Creatinine ratio).
    - **Normal Range:** $7 - 20$ mg/dL (or $15 - 40$ mg/dL for total blood urea)
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Suggests kidney dysfunction, dehydration, or a high-protein diet. Symptoms of very high levels (Uremia) include a **metallic taste in the mouth**, **loss of appetite**, **fatigue**, **confusion**, and **itchy skin**.
    * **If Low:** Rare, but can indicate severe liver disease, malnutrition, or overhydration (drinking too much water). Symptoms align with the underlying cause, like chronic weakness.
    """)

# 3. Uric Acid
with st.expander("🟡 Uric Acid (Code: URIC_03)"):
    st.markdown("""
    ### 🩸 What is it?
    **Uric Acid** is a waste product created when your body breaks down chemicals called **purines**, which are found naturally in your cells and in certain foods (like red meat, seafood, and alcohol).
    
    ### 🎯 Importance of the Test
    High levels can cause uric acid to form solid crystals. This test is crucial for diagnosing **Gout** (a painful form of arthritis) and monitoring kidney stone risks.
    - **Normal Range:** $3.5 - 7.2$ mg/dL for men, and $2.6 - 6.0$ mg/dL for women.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hyperuricemia):** Causes sharp crystals to deposit in joints or kidneys. Symptoms include **sudden and intense joint pain** (most commonly in the big toe), **redness, swelling, and severe tenderness in joints**, or sharp back/side pain due to **kidney stones**.
    * **If Low:** Quite rare and generally harmless. It may be linked to certain medications, liver disease, or a rare genetic condition called Wilson's disease. Usually features no direct symptoms.
    """)

# 4. eGFR (Estimated Glomerular Filtration Rate)
with st.expander("🟢 eGFR (The Ultimate Kidney Score) - Code: EGFR_04)"):
    st.markdown("""
    ### 🩸 What is it?
    **eGFR** is not a direct waste product; it is a **calculated score** based on your blood creatinine level, age, body size, and gender. It estimates how many milliliters of blood your kidneys clean per minute.
    
    ### 🎯 Importance of the Test
    This is considered the **gold standard** for determining the stage of Chronic Kidney Disease (CKD). While creatinine tells you something is wrong, eGFR tells you exactly *how well* the kidneys are performing.
    - **Normal Range:** $90$ mL/min/1.73m² or higher. (A score below 60 for over 3 months indicates kidney disease).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** A high score is excellent! It means your kidneys are filtering blood at an optimal rate. There are no negative symptoms.
    * **If Low (<60):** Indicates declining kidney function. Early stages often have **no symptoms** (the silent phase). As it drops significantly lower (below 30 or 15), symptoms manifest as **severe swelling (edema)**, **foamy urine**, **persistent nausea**, **severe anemia**, and **uamic frost (itched, flaky skin)**.
    """)

st.divider()
st.info("💡 **Note:** A sudden spike in Creatinine and Urea can sometimes be temporary, caused by intense exercise, heavy red meat consumption the night before, or dehydration. Advise users to consult a nephrologist for persistent abnormal values.")

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
with st.expander("🦋 Importance of Thyroid Profile"):

    st.write("""
The Thyroid Profile evaluates how well the thyroid gland is functioning.

• TSH (Thyroid Stimulating Hormone) is the primary screening test for thyroid disorders.

• T3 (Triiodothyronine) is an active thyroid hormone involved in metabolism, heart rate and energy production.

• T4 (Thyroxine) is the main hormone produced by the thyroid gland and is converted into T3 in the body.

Abnormal thyroid hormone levels may contribute to symptoms such as fatigue, weight changes, heat or cold intolerance, hair loss, constipation, palpitations or mood changes.

Thyroid test results should always be interpreted together with symptoms and by a qualified healthcare professional.
""")
# 1. TSH (Thyroid Stimulating Hormone)
with st.expander("🔹 TSH (Thyroid Stimulating Hormone) - Code: TSH_01"):
    st.markdown("""
    ### 🩸 What is it?
    **TSH** is not actually produced by your thyroid; it is released by the **pituitary gland** in your brain. It acts as a manager, telling your thyroid gland how much T3 and T4 hormones to make and release.
    
    ### 🎯 Importance of the Test
    This is the primary and most sensitive screening test for thyroid dysfunction. It runs on a negative feedback loop: if your thyroid is sluggish, TSH goes up to push it harder; if your thyroid is overactive, TSH drops.
    - **Normal Range:** Typically $0.4 - 4.5$ mIU/L (milli-international units per liter).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hypothyroidism / Underactive Thyroid):** Your brain is screaming at the thyroid to work. Symptoms include **unexplained weight gain**, **chronic fatigue**, **feeling constantly cold**, **dry skin**, **hair loss**, and **depression**.
    * **If Low (Hyperthyroidism / Overactive Thyroid):** Your brain has stopped stimulating the thyroid because there are already too many hormones. Symptoms include **sudden weight loss**, **rapid or irregular heart rate (palpitations)**, **excessive sweating & heat intolerance**, **anxiety/nervousness**, and **hand tremors**.
    """)

# 2. Total T4 (Thyroxine)
with st.expander("🔸 Total T4 (Thyroxine) - Code: T4_02"):
    st.markdown("""
    ### 🩸 What is it?
    **T4** is the primary hormone produced directly by the thyroid gland. It is mostly inactive and acts as a reservoir, which your body converts into the active T3 hormone when needed. "Total T4" measures both bound and free T4 in your blood.
    
    ### 🎯 Importance of the Test
    It helps confirm whether an abnormal TSH level is due to an actual thyroid gland problem (like Graves' disease or Hashimoto's thyroiditis) or an issue with the pituitary gland.
    - **Normal Range:** Typically $5.0 - 12.0$ µg/dL (micrograms per deciliter).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates an overactive thyroid. Symptoms match **Hyperthyroidism**: **high anxiety**, **weight loss despite increased appetite**, **frequent bowel movements**, and **sleep disturbances**.
    * **If Low:** Indicates an underactive thyroid. Symptoms match **Hypothyroidism**: **extreme sluggishness**, **brain fog**, **muscle weakness**, **constipation**, and **puffiness in the face**.
    """)

# 3. Total T3 (Triiodothyronine)
with st.expander("🟡 Total T3 (Triiodothyronine) - Code: T3_03"):
    st.markdown("""
    ### 🩸 What is it?
    **T3** is the active form of the thyroid hormone. While the thyroid gland produces some T3 directly, most of it comes from the body converting T4 into T3 in tissues like the liver and kidneys.
    
    ### 🎯 Importance of the Test
    T3 is highly useful for diagnosing and monitoring **Hyperthyroidism** (overactive thyroid). Sometimes, in severe hyperthyroidism, T4 levels might look normal but T3 will be significantly elevated.
    - **Normal Range:** Typically $80 - 200$ ng/dL (nanograms per deciliter).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Accelerates your body's metabolism drastically. Symptoms include **muscle weakness**, **irritability**, **thinning skin**, **brittle hair**, and a **noticeable swelling in the neck (Goiter)**.
    * **If Low:** Slows down body functions. Symptoms include **bradycardia (slow heart rate)**, **severe fatigue**, **menstrual irregularities in women**, and **high cholesterol levels**.
    """)

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
# 1. Sodium (Na+)
with st.expander("🧂 Sodium (Na+) - Code: SOD_01"):
    st.markdown("""
    ### 🩸 What is it?
    **Sodium** is the primary electrolyte found in the fluid outside your cells. It works closely with your kidneys to regulate the total amount of water in your body.
    
    ### 🎯 Importance of the Test
    It is crucial for maintaining blood pressure, fluid balance, and ensuring that your nerves and muscles function properly.
    - **Normal Range:** $135 - 145$ mEq/L (milliequivalents per liter).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hypernatremia):** Usually caused by severe dehydration. Symptoms include **extreme thirst**, **dry mucous membranes**, **restlessness**, **confusion**, and in severe cases, muscle twitching or seizures.
    * **If Low (Hyponatremia):** Often caused by drinking too much water, kidney failure, or heart failure. Symptoms include **headache**, **nausea/vomiting**, **brain fog/lethargy**, **muscle weakness**, and confusion.
    """)

# 2. Potassium (K+)
with st.expander("🍌 Potassium (K+) - Code: POT_02"):
    st.markdown("""
    ### 🩸 What is it?
    **Potassium** is the primary electrolyte found *inside* your cells. Small changes in blood potassium levels can have massive effects on your body.
    
    ### 🎯 Importance of the Test
    It controls electrical activity in the heart muscle. Monitoring potassium is vital for patients taking blood pressure medications, or those with heart and kidney diseases.
    - **Normal Range:** $3.5 - 5.2$ mEq/L.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hyperkalemia):** **Extremely dangerous for the heart.** Severe high levels can cause the heart to stop beating. Symptoms include **heart palpitations (irregular heartbeat)**, **chest pain**, **severe muscle weakness**, and numbness.
    * **If Low (Hypokalemia):** Often caused by prolonged vomiting, diarrhea, or diuretics. Symptoms include **muscle cramps (especially in calves)**, **fatigue**, **constipation**, and abnormal heart rhythms.
    """)

# 3. Chloride (Cl-)
with st.expander("🧪 Chloride (Cl-) - Code: CHL_03"):
    st.markdown("""
    ### 🩸 What is it?
    **Chloride** is an electrolyte that typically binds with Sodium or Potassium. It helps maintain the proper balance of fluids and acid-base (pH) levels in your body.
    
    ### 🎯 Importance of the Test
    It is rarely evaluated alone. It helps diagnose kidney diseases, high blood pressure, or acid-base imbalances in the body.
    - **Normal Range:** $96 - 106$ mEq/L.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hyperchloremia):** Usually matches symptoms of dehydration or kidney issues. Includes **excessive fatigue**, **muscle weakness**, **deep/rapid breathing**, and severe thirst.
    * **If Low (Hypochloremia):** Often due to heavy sweating or prolonged vomiting (losing stomach acid). Symptoms include **prolonged dehydration**, **shallow breathing**, and muscle twitching.
    """)

# 4. Calcium (Ca)
with st.expander("🦴 Calcium (Total) - Code: CAL_04"):
    st.markdown("""
    ### 🩸 What is it?
    **Calcium** is one of the most important minerals in the body. While 99% is stored in bones and teeth, the tiny fraction circulating in the blood is vital for blood clotting and nerve transmission.
    
    ### 🎯 Importance of the Test
    It screenings for bone diseases, kidney disease, parathyroid gland disorders, or certain types of neurological conditions.
    - **Normal Range:** $8.5 - 10.2$ mg/dL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hypercalcemia):** Think of the classic phrase: *"Stones, bones, groans, and psychiatric overtones."* Symptoms include **kidney stones**, **bone pain**, **abdominal pain/constipation**, and **lethargy or confusion**.
    * **If Low (Hypocalcemia):** Often caused by Vitamin D deficiency. Symptoms include **muscle spasms/tetany**, **tingling in fingers and lips**, **muscle cramps**, and hyperactive reflexes.
    """)

# 5. Magnesium (Mg)
with st.expander("🔩 Magnesium (Mg) - Code: MAG_05"):
    st.markdown("""
    ### 🩸 What is it?
    **Magnesium** is an essential mineral required for more than 300 biochemical reactions in the body, including protein synthesis, muscle/nerve function, and blood glucose control.
    
    ### 🎯 Importance of the Test
    Low levels can impair calcium and potassium regulation. It is checked when a patient has chronic muscle cramps, neurological issues, or cardiac arrhythmias.
    - **Normal Range:** $1.7 - 2.2$ mg/dL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hypermagnesemia):** Rare, usually happens in kidney failure patients taking magnesium-containing antacids. Symptoms include **flushing**, **low blood pressure (hypotension)**, **nausea**, and **diminished reflexes**.
    * **If Low (Hypomagnesemia):** Common in chronic alcoholism or malnutrition. Symptoms include **muscle tremors/twitches**, **insomnia**, **irregular heart rate**, and personality changes.
    """)

# 6. Phosphorus
with st.expander("🫧 Phosphorus / Phosphate - Code: PHO_06"):
    st.markdown("""
    ### 🩸 What is it?
    **Phosphorus** works in a tight inverse relationship with Calcium. It is vital for energy production (forming ATP) and building bone structure.
    
    ### 🎯 Importance of the Test
    Abnormal levels are a hallmark sign of advanced kidney disease or severe Vitamin D and parathyroid imbalances.
    - **Normal Range:** $2.5 - 4.5$ mg/dL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hyperphosphatemia):** Mostly asymptomatic on its own, but because it binds to calcium, it causes symptoms of low calcium like **muscle cramps**, **joint pain**, and **severe skin itching**.
    * **If Low (Hypophosphatemia):** Often seen in severe malnutrition or diabetic ketoacidosis recovery. Symptoms include **extreme muscle weakness**, **bone pain/fragility**, **appetite loss**, and respiratory failure in extreme cases.
    """)
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
# 1. Vitamin D (25-Hydroxy Vitamin D)
with st.expander("☀️ Vitamin D3 - Code: VITD_01"):
    st.markdown("""
    ### 🩸 What is it?
    **Vitamin D** is a fat-soluble vitamin that your body produces naturally when exposed to sunlight. It acts more like a hormone, helping your gut absorb calcium and phosphorus.
    
    ### 🎯 Importance of the Test
    It is crucial for maintaining bone density, supporting immune function, and reducing inflammation. Low levels are incredibly common globally due to indoor lifestyles.
    - **Optimal Range:** $30 - 100$ ng/mL (Below 20 ng/mL is considered deficient).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Toxicity):** Usually caused by mega-doses of supplements, not sunlight. Symptoms include **nausea, vomiting, frequent urination, kidney stones**, and muscle weakness due to calcium buildup (hypercalcemia).
    * **If Low (Deficiency):** Causes poor bone mineralization. Symptoms include **chronic fatigue, persistent bone or lower back pain, muscle weakness**, frequent infections, and mood changes (depression).
    """)

# 2. Vitamin B12 (Cobalamin)
with st.expander("🧠 Vitamin B12 - Code: B12_02"):
    st.markdown("""
    ### 🩸 What is it?
    **Vitamin B12** is a water-soluble vitamin found primarily in animal products (meat, fish, eggs, dairy). It is essential for red blood cell production, DNA synthesis, and proper nerve function.
    
    ### 🎯 Importance of the Test
    It helps diagnose unexplained nerve issues (neuropathy) or a specific type of large-cell anemia (Megaloblastic Anemia). Vegans and vegetarians are at high risk for deficiency.
    - **Normal Range:** $200 - 900$ pg/mL (picograms per milliliter).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Uncommon, as excess is usually flushed through urine. However, highly elevated levels without supplements can sometimes flag underlying liver disease or myeloproliferative disorders.
    * **If Low (Deficiency):** Leads to nerve damage and anemia. Symptoms include **tingling or numbness in hands/feet ("pins and needles")**, **brain fog/memory loss**, smooth/red tongue, severe fatigue, and difficulty walking.
    """)

# 3. Serum Iron
with st.expander("🔩 Serum Iron - Code: IRON_03"):
    st.markdown("""
    ### 🩸 What is it?
    **Serum Iron** measures the actual amount of iron circulating in your blood liquid (serum) at that exact moment, bound to a transport protein called transferrin.
    
    ### 🎯 Importance of the Test
    Iron is the core building block of hemoglobin, which carries oxygen. This test is looked at alongside Ferritin and TIBC to get a clear picture of iron-deficiency anemia or iron overload.
    - **Normal Range:** Generally $60 - 170$ µg/dL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Suggests excessive iron absorption or frequent blood transfusions. Symptoms include **joint pain, abdominal pain, chronic fatigue**, and skin darkening.
    * **If Low:** Indicates an inadequate supply of iron. Symptoms include **pale skin, constant feeling of coldness, shortness of breath, dizziness**, and brittle nails.
    """)

# 4. Ferritin
with st.expander("📦 Ferritin (Iron Storage) - Code: FER_04"):
    st.markdown("""
    ### 🩸 What is it?
    While serum iron is the iron floating in your blood, **Ferritin** is a protein that stores iron inside your cells. Think of Serum Iron as the cash in your wallet, and Ferritin as your savings bank account.
    
    ### 🎯 Importance of the Test
    This is the **most sensitive test** for iron deficiency. Your serum iron can fluctuate daily based on what you ate, but Ferritin shows your true long-term iron reserves.
    - **Normal Range:** $20 - 300$ ng/mL for men; $15 - 150$ ng/mL for women.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Can signify **Hemochromatosis** (genetic iron overload) or act as an acute phase reactant, meaning it spikes during **active inflammation or infections**. Symptoms include unexplained liver issues, heart palpitations, and fatigue.
    * **If Low:** Means your body's iron banks are completely empty. Symptoms match classic iron deficiency: **severe fatigue, pica (craving non-food items like ice or dirt)**, hair loss, and restless leg syndrome.
    """)

# 5. TIBC (Total Iron-Binding Capacity)
with st.expander("🔄 TIBC (Total Iron-Binding Capacity) - Code: TIBC_05"):
    st.markdown("""
    ### 🩸 What is it?
    **TIBC** measures how well a protein called transferrin can bind and transport iron in your blood. It essentially tells you how much "empty space" is available for iron to ride on.
    
    ### 🎯 Importance of the Test
    TIBC has an **inverse relationship** with iron stores. When your body is starved of iron, the liver produces *more* transport proteins to catch every bit of iron it can find, causing TIBC to go UP.
    - **Normal Range:** $240 - 450$ µg/dL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Directly points to **Iron Deficiency Anemia**. The symptoms are those of low iron: **extreme fatigue, pale skin, weakness, and a rapid heart rate**.
    * **If Low:** Indicates that your transport proteins are fully packed or your liver isn't making them. This happens in **iron overload** or chronic liver/kidney diseases. Symptoms include joint pain and chronic lethargy.
    """)
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
with st.expander("🦴 Importance of Inflammatory & Autoimmune Tests"):

    st.write("""

CRP measures inflammation in the body and is commonly used to monitor infections and inflammatory conditions.

Rheumatoid Factor (RF) is frequently used during the evaluation of Rheumatoid Arthritis.

Anti-CCP antibody has higher specificity than RF for Rheumatoid Arthritis and may support the diagnosis when interpreted with symptoms and examination.

ASO Titre helps identify a recent Streptococcal infection and may assist in evaluating complications such as Rheumatic Fever.

ANA (Antinuclear Antibody) is used when autoimmune connective tissue diseases are suspected. A positive result alone does not establish a diagnosis.

These tests should always be interpreted together with symptoms, physical examination and other investigations by a qualified healthcare professional.

""")
#------------------
# 1. C-Reactive Protein (CRP)
with st.expander("🔴 C-Reactive Protein (CRP) - Code: CRP_01"):
    st.markdown("""
    ### 🩸 What is it?
    **CRP** is a protein produced by your liver. Its level rises drastically in response to acute inflammation, infections, or tissue injury anywhere in the body.
    
    ### 🎯 Importance of the Test
    It is a general but highly sensitive marker for inflammation. While it doesn't tell *where* the problem is, a high CRP tells doctors that something is actively causing inflammation (like a bacterial infection, injury, or chronic disease flare-up).
    - **Normal Range:** Less than $3.0$ mg/L (Values > 10 mg/L usually indicate significant infection or inflammation).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates active inflammation. Symptoms depend on the cause but commonly include **fever, unexplained muscle aches, fatigue, rapid heart rate**, and localized redness or swelling.
    * **If Low:** Low or undetectable CRP is ideal, indicating no major active inflammation or infection in the body.
    """)

# 2. Rheumatoid Factor (RF)
with st.expander("🦴 Rheumatoid Factor (RF) - Code: RF_02"):
    st.markdown("""
    ### 🩸 What is it?
    **Rheumatoid Factor** is an autoantibody—a protein produced by your own immune system that mistakenly attacks healthy tissues in your joints and glands.
    
    ### 🎯 Importance of the Test
    It is primarily used to help diagnose **Rheumatoid Arthritis (RA)**, a chronic autoimmune disease that causes joint damage. However, it can sometimes be positive in healthy individuals or other conditions.
    - **Normal Range:** Less than $14$ IU/mL (International Units per milliliter).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Strongly associated with autoimmune arthritis. Symptoms include **symmetrical joint pain (e.g., both wrists or both knees), severe morning stiffness lasting over 30 minutes, swelling and warmth in small joints**, and chronic fatigue.
    * **If Low/Negative:** Normal result. However, a negative result does not completely rule out Rheumatoid Arthritis, as some patients have "seronegative" RA.
    """)

# 3. Anti-CCP Antibody (Anti-Cyclic Citrullinated Peptide)
with st.expander("🎯 Anti-CCP Antibody - Code: ACCP_03"):
    st.markdown("""
    ### 🩸 What is it?
    Like RF, **Anti-CCP** is an autoantibody produced by the immune system that targets joints. However, it is far more specific and precise than the Rheumatoid Factor.
    
    ### 🎯 Importance of the Test
    This is the **gold standard** test for diagnosing Rheumatoid Arthritis. If a patient has both high RF and high Anti-CCP, the diagnosis of RA is nearly certain. It can even detect the disease years before physical symptoms appear.
    - **Normal Range:** Less than $20$ Units.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Points directly to Rheumatoid Arthritis and often predicts a more aggressive form of joint damage. Symptoms include **persistent joint pain, joint deformities over time, limited range of motion**, and nodules under the skin.
    * **If Low/Negative:** Normal. It indicates a very low likelihood of having Rheumatoid Arthritis, though early-stage disease is still a minor possibility.
    """)

# 4. ASO Titre (Anti-Streptolysin O)
with st.expander("🦠 ASO Titre - Code: ASO_04"):
    st.markdown("""
    ### 🩸 What is it?
    **ASO Titre** measures the level of antibodies against *Streptolysin O*, a toxin produced by **Group A Streptococcus** bacteria (the bacteria responsible for strep throat).
    
    ### 🎯 Importance of the Test
    It checks if you had a recent, undetected, or poorly treated strep infection. If left untreated, this infection can lead to serious post-streptococcal complications like **Rheumatic Fever** (which affects the heart and joints) or kidney inflammation.
    - **Normal Range:** Typically less than $200$ IU/mL (Varies slightly between adults and children).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates a recent or ongoing strep infection that has triggered an immune response. Symptoms of complications can include **migrating joint pain (pain moving from one joint to another), chest pain/palpitations, shortness of breath, skin rashes**, or dark urine.
    * **If Low:** Normal result. It means there is no evidence of a recent Group A Strep infection.
    """)

# 5. ANA Test (Antinuclear Antibody)
with st.expander("🧬 ANA Test (Screening for Autoimmune Disease) - Code: ANA_05"):
    st.markdown("""
    ### 🩸 What is it?
    **ANA** targets the "nucleus" (the command center) of your own cells. It is the primary screening tool used when your body's immune system turns against itself.
    
    ### 🎯 Importance of the Test
    This is the master gateway test for detecting systemic autoimmune diseases, most notably **Lupus (SLE)**, Sjogren's syndrome, and Scleroderma. A positive result is usually followed by more specific antibody tests.
    - **Normal Range:** Reported as Negative or as a low ratio/titre (e.g., less than 1:40 or 1:80).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Positive):** Indicates your body is producing autoantibodies. Symptoms of diseases like Lupus include a **butterfly-shaped rash across the cheeks and nose, extreme fatigue, unexplained hair loss, joint pain with swelling**, sensitivity to sunlight, and fingers turning blue/pale in the cold (Raynaud's phenomenon).
    * **If Low (Negative):** Highly reassuring. A negative ANA strongly rules out major systemic autoimmune diseases like Lupus.
    """)
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
# 1. Prothrombin Time (PT)
with st.expander("⏳ Prothrombin Time (PT) - Code: PT_01"):
    st.markdown("""
    ### 🩸 What is it?
    **Prothrombin Time (PT)** measures the exact number of seconds it takes for the liquid portion of your blood (plasma) to clot after specific substances are added. It primarily evaluates the "extrinsic" pathway of blood coagulation.
    
    ### 🎯 Importance of the Test
    It checks for bleeding problems, liver damage (since the liver produces clotting proteins), or Vitamin K deficiency. It is also used before surgeries to ensure you won't bleed excessively.
    - **Normal Range:** Typically $11 - 13.5$ seconds.
    
    ### ⚠️ Symptoms: High (Prolonged) vs. Low (Shortened)
    * **If High (Prolonged / Takes longer to clot):** Your blood is too thin. Symptoms include **frequent or prolonged nosebleeds, bleeding gums after brushing, easy bruising (bruises appearing without injury)**, and heavy menstrual cycles.
    * **If Low (Shortened / Clots too fast):** Rare, but indicates a higher tendency for blood to clot. Symptoms could relate to an active blood clot, such as unexplained leg swelling or pain (Deep Vein Thrombosis).
    """)

# 2. INR (International Normalized Ratio)
with st.expander("🌍 INR (International Normalized Ratio) - Code: INR_02"):
    st.markdown("""
    ### 🩸 What is it?
    **INR** is not a separate test; it is a **standardized calculation** based on your PT result. Because different labs use different testing chemicals, the INR was created so that a clotting score in one country means the exact same thing in another.
    
    ### 🎯 Importance of the Test
    This is the **gold standard** for monitoring patients on oral blood thinners/anticoagulants like **Warfarin (Coumadin)**. 
    - **Normal Range:** $0.8 - 1.1$ for a healthy individual. (For patients on blood thinners, doctors usually target a higher therapeutic range of $2.0 - 3.0$).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (>3.0 or >5.0 in critical states):** The blood is dangerously thin, placing you at a high risk for internal bleeding. Symptoms include **blood in the urine or stool (dark, tarry stools), severe dizziness, sudden unprovoked severe headaches**, or bleeding from cuts that won't stop.
    * **If Low (<0.8 or below therapeutic target):** The blood is too thick or the medicine isn't working. This significantly increases the risk of **unwanted blood clots, stroke, or heart attack**. Symptoms include sudden shortness of breath, chest pain, or weakness on one side of the body.
    """)

# 3. aPTT (Activated Partial Thromboplastin Time)
with st.expander("⏱️ aPTT (Activated Partial Thromboplastin Time) - Code: APTT_03"):
    st.markdown("""
    ### 🩸 What is it?
    **aPTT** measures the time it takes for blood to clot, but it focuses on a different set of clotting proteins (the "intrinsic" and common pathways) compared to PT.
    
    ### 🎯 Importance of the Test
    It is primarily used to monitor patients who are receiving **intravenous (IV) Heparin therapy** (an in-hospital blood thinner). It also helps screen for genetic bleeding disorders like **Hemophilia** or certain autoimmune conditions (like Antiphospholipid Syndrome).
    - **Normal Range:** Typically $25 - 35$ seconds.
    
    ### ⚠️ Symptoms: High (Prolonged) vs. Low (Shortened)
    * **If High (Prolonged):** Indicates a deficiency in clotting factors or heavy heparin use. Symptoms include **excessive bleeding from small cuts, joint pain and swelling (caused by internal bleeding into joints)**, and large hematomas (blood pooling under the skin).
    * **If Low (Shortened):** Can be seen in early stages of severe conditions like DIC (Disseminated Intravascular Coagulation) or advanced cancers where the body is in a hypercoagulable (over-clotting) state. Symptoms involve a high risk of blood clots.
    """)

st.info("💡 **Note:** Coagulation tests are highly time-sensitive. The blood sample must be processed quickly in the lab for accurate results. If your app flags critical values, any INR above 4.5 or aPTT above 70 seconds usually warrants immediate medical notification.")

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
import streamlit as st

st.subheader("🧪 Cardiac Markers & Heart Health Information")
st.write("Understand the critical biomarkers used to detect heart muscle injury, heart attacks, and heart failure.")

# 1. Troponin (Troponin I or T)
with st.expander("🚨 Troponin (The Heart Attack Marker) - Code: TROP_01"):
    st.markdown("""
    ### 🩸 What is it?
    **Troponin** is a type of protein found specifically in your heart muscle cells. Under normal conditions, troponin stays inside the heart, and virtually none is found in the blood.
    
    ### 🎯 Importance of the Test
    This is the **gold standard and most critical test** for diagnosing a **Heart Attack (Myocardial Infarction)**. When heart muscle cells die due to a lack of oxygen/blood flow, they rupture and leak troponin into the bloodstream. It can stay elevated for up to 1-2 weeks after a heart attack.
    - **Normal Range:** Extremely low, typically less than $0.04$ ng/mL (depending on the specific high-sensitivity assay used).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates active heart muscle damage. Emergency symptoms include **crushing chest pain or pressure (often radiating to the left arm, jaw, or back), sudden shortness of breath, excessive cold sweating (diaphoresis), dizziness, and severe anxiety**.
    * **If Low/Normal:** Reassuring, meaning there is likely no acute, major damage to the heart muscle.
    """)

# 2. CK-MB (Creatine Kinase-MB)
with st.expander("⏱️ CK-MB (Creatine Kinase-MB) - Code: CKMB_02"):
    st.markdown("""
    ### 🩸 What is it?
    **CK-MB** is an enzyme found primarily in heart muscle cells, though small amounts exist in skeletal muscles. 
    
    ### 🎯 Importance of the Test
    While Troponin is now preferred for initial diagnoses, CK-MB rises and falls much quicker (returning to normal within 2-3 days). Therefore, it is highly useful for detecting a **re-infarction** (a second heart attack that happens shortly after the first one).
    - **Normal Range:** Typically $3 - 5$ ng/mL or less than 5% of total CK.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Points to recent heart damage or intense skeletal muscle trauma. Symptoms mirror a heart attack: **chest tightness, nausea, lightheadedness, and unexplained fatigue**.
    * **If Low:** Normal. It indicates that no significant heart muscle injury has occurred within the last 24 to 48 hours.
    """)

# 3. BNP (B-Type Natriuretic Peptide)
with st.expander("🫁 BNP (The Heart Failure Marker) - Code: BNP_03"):
    st.markdown("""
    ### 🩸 What is it?
    **BNP** is a hormone produced and released by the heart’s left ventricle when it is overworked, stretched, or under too much pressure.
    
    ### 🎯 Importance of the Test
    This test is the primary tool used to diagnose and monitor **Heart Failure**. It helps doctors quickly differentiate whether a patient's shortness of breath is caused by a heart problem (Heart Failure) or a lung problem (like Asthma or COPD).
    - **Normal Range:** Less than $100$ pg/mL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Indicates that the heart is struggling to pump blood efficiently, causing fluid to back up in the body. Symptoms include **severe shortness of breath (especially when lying flat on the back), persistent coughing or wheezing, extreme fatigue, and sudden swelling (edema) in the legs, ankles, or abdomen**.
    * **If Low:** Highly reassuring. A low BNP level almost completely rules out heart failure as the cause of a patient's breathing difficulties.
    """)
st.error("🚨 **CRITICAL NOTE:** Troponin and CK-MB are time-critical emergency tests. If app processes live data, any significant elevation in Troponin must be flagged with a high-priority red alert instructing the user to call emergency services (e.g., 999/911) immediately.")

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
# 1. Dengue NS1 Antigen
with st.expander("🦟 Dengue NS1 Antigen - Code: DEN_NS1"):
    st.markdown("""
    ### 🩸 What is it?
    **Dengue NS1** is a test that detects the Non-Structural Protein 1 (NS1) of the Dengue virus. This protein is secreted into the blood by the virus during its replication phase.
    
    ### 🎯 Importance of the Test
    It is used for the **early detection** of Dengue fever. It can detect the virus from the **very 1st day of fever** up to day 5–7. After day 7, this antigen disappears from the blood.
    - **Normal Result:** Negative (Non-reactive).
    
    ### ⚠️ Symptoms if Positive (Reactive)
    Indicates an active, early-stage Dengue infection. Symptoms include **sudden high fever ($103-104^{\circ}\text{F}$), severe headache (especially behind the eyes), severe muscle and joint pain ("breakbone fever"), and skin rashes**.
    """)

# 2. Dengue IgM & IgG Antibodies
with st.expander("🦟 Dengue IgM & IgG - Code: DEN_AB"):
    st.markdown("""
    ### 🩸 What is it?
    This test looks for antibodies (**IgM** and **IgG**) produced by your immune system to fight the Dengue virus.
    
    ### 🎯 Importance of the Test
    * **IgM:** Appears around day 4–5 of the fever and indicates a **current or very recent infection**.
    * **IgG:** Appears later (after a week) or indicates a **past Dengue infection** in your life, giving you long-term immunity to that specific serotype.
    - **Normal Result:** Negative.
    
    ### ⚠️ Symptoms if Positive (Reactive)
    * **If IgM is Positive:** Active infection. Watch out for severe warning signs like **persistent vomiting, severe abdominal pain, bleeding gums/nose, and a sudden drop in blood platelets**.
    * **If IgG is Positive (with negative IgM):** You had Dengue in the past; no immediate treatment is needed unless currently symptomatic.
    """)

# 3. Malaria Antigen (Pv/Pf)
with st.expander("🦟 Malaria Antigen (Pv/Pf) - Code: MAL_AG"):
    st.markdown("""
    ### 🩸 What is it?
    This rapid diagnostic test detects specific proteins produced by the *Plasmodium* parasites (specifically *Plasmodium vivax* and *Plasmodium falciparum*) transmitted through Anopheles mosquitoes.
    
    ### 🎯 Importance of the Test
    It helps quickly identify malaria. Identifying *P. falciparum (Pf)* is critical because it causes cerebral malaria, which can be fatal if not treated immediately.
    - **Normal Result:** Negative.
    
    ### ⚠️ Symptoms if Positive (Reactive)
    Indicates active Malaria. Symptoms typically include **high fever with severe shaking chills (shivering), profuse sweating as the fever drops, intense headaches, and body aches**. In severe *Pf* cases, it can cause confusion or altered consciousness.
    """)

# 4. Typhoid IgM (Widal / Typhidot)
with st.expander("🥣 Typhoid IgM (Typhidot) - Code: TYP_IGM"):
    st.markdown("""
    ### 🩸 What is it?
    This test detects **IgM antibodies** against the *Salmonella typhi* bacteria, which enters the body through contaminated food or water and causes Typhoid fever.
    
    ### 🎯 Importance of the Test
    The Typhidot (IgM) test is much faster and more accurate in the early phase (after 3-4 days of fever) compared to the traditional Widal test.
    - **Normal Result:** Negative.
    
    ### ⚠️ Symptoms if Positive (Reactive)
    Indicates active Typhoid fever. Symptoms include **step-ladder fever (fever that increases gradually day by day), severe stomach pain, diarrhea or severe constipation, extreme weakness, and a coated white tongue**.
    """)

# 5. HBsAg (Hepatitis B Surface Antigen)
with st.expander("🟡 HBsAg (Hepatitis B Screening) - Code: HBSAG"):
    st.markdown("""
    ### 🩸 What is it?
    **HBsAg** is the surface antigen of the Hepatitis B virus (HBV). It is the earliest marker of a Hepatitis B infection, which affects the liver.
    
    ### 🎯 Importance of the Test
    It screens for both acute and chronic Hep B. If it remains positive for more than 6 months, it indicates that the person has chronic Hepatitis B, which can lead to liver cirrhosis or liver cancer.
    - **Normal Result:** Negative (Non-reactive).
    
    ### ⚠️ Symptoms if Positive (Reactive)
    * **Acute Stage:** May cause **jaundice (yellow skin/eyes), dark tea-colored urine, extreme fatigue, loss of appetite, and nausea**.
    * **Chronic Stage:** Often **completely silent with zero symptoms** for years, quietly damaging the liver.
    """)

# 6. Anti-HCV (Hepatitis C Antibody)
with st.expander("🟠 Anti-HCV (Hepatitis C Screening) - Code: HCV_AB"):
    st.markdown("""
    ### 🩸 What is it?
    This test detects antibodies produced by the body in response to a **Hepatitis C Virus (HCV)** infection, which is transmitted through infected blood or needles.
    
    ### 🎯 Importance of the Test
    It is used to screen for exposure to Hep C. Unlike Hep B, there is no vaccine for Hep C, but it is highly curable with modern oral medications if caught early.
    - **Normal Result:** Negative (Non-reactive).
    
    ### ⚠️ Symptoms if Positive (Reactive)
    Most people with Hep C have **no symptoms** for decades. When symptoms finally appear, they indicate advanced liver scarring (Cirrhosis) and include **swelling in the legs/abdomen (ascites), easy bruising, skin itching, and confusion**.
    """)

# 7. HIV 1 & 2 Screening (ELISA / Rapid)
with st.expander("🧬 HIV 1 & 2 Screening - Code: HIV_SCR"):
    st.markdown("""
    ### 🩸 What is it?
    This test screens for antibodies and/or the p24 antigen against **Human Immunodeficiency Virus (HIV) types 1 and 2**, the viruses that cause AIDS.
    
    ### 🎯 Importance of the Test
    Early diagnosis allows patients to start **Antiretroviral Therapy (ART)** immediately, ensuring they live a normal, healthy life expectancy and preventing the virus from spreading.
    - **Normal Result:** Negative (Non-reactive).
    
    ### ⚠️ Symptoms if Positive (Reactive)
    * **Early Stage (Acute HIV):** Occurs 2-4 weeks after exposure, presenting with **flu-like symptoms: fever, sore throat, swollen lymph nodes, and mouth ulcers**.
    * **Latent Stage:** The virus can remain active but asymptomatic for 10+ years without medicine.
    """)

st.warning("⚠️ **CRITICAL NOTE:** A 'Positive' or 'Reactive' screening result for HBsAg, Anti-HCV, or HIV *does not* constitute a final diagnosis. These are screening tests and **MUST** always be followed by confirmatory molecular tests (like HBV DNA PCR, HCV RNA PCR, or Western Blot/HIV Viral Load) before confirming diagnosis.")

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
# 1. PSA (Prostate-Specific Antigen)
with st.expander("🎗️ PSA (Prostate-Specific Antigen) - Code: PSA_01"):
    st.markdown("""
    ### 🩸 What is it?
    **PSA** is a protein produced exclusively by the cells of the prostate gland in men. Small amounts of PSA normally circulate in the blood.
    
    ### 🎯 Importance of the Test
    It is primarily used to screen for **Prostate Cancer** in men. It is also highly valuable for monitoring how well prostate cancer treatment is working or if the cancer has returned.
    - **Normal Range:** Generally less than $4.0$ ng/mL (Increases slightly with age).
    
    ### ⚠️ Symptoms if the Level is High
    An elevated PSA indicates prostate inflammation or abnormal growth (which can be benign or cancerous). Symptoms include **frequent urination (especially at night), difficulty starting or stopping urination, a weak urine stream**, or blood in the urine or semen.
    """)

# 2. CEA (Carcinoembryonic Antigen)
with st.expander("🎗️ CEA (Carcinoembryonic Antigen) - Code: CEA_02"):
    st.markdown("""
    ### 🩸 What is it?
    **CEA** is a type of protein normally found in embryonic tissue during development. After birth, it drops to very low levels, but certain cancers can cause it to spike.
    
    ### 🎯 Importance of the Test
    It is mainly used to track **Colorectal Cancer (Colon Cancer)**. It is not an ideal standalone screening tool because non-cancerous conditions (and heavy smoking) can raise it, but it is the gold standard for tracking treatment success.
    - **Normal Range:** Less than $2.5$ ng/mL (Up to $5.0$ ng/mL can be normal for heavy smokers).
    
    ### ⚠️ Symptoms if the Level is High
    Highly elevated levels usually track with advanced colorectal or gastrointestinal cancers. Symptoms include **unexplained weight loss, persistent change in bowel habits (chronic diarrhea or constipation), blood in the stool**, and constant abdominal discomfort.
    """)

# 3. CA-125 (Cancer Antigen 125)
with st.expander("🎗️ CA-125 (Ovarian Cancer Marker) - Code: CA125_03"):
    st.markdown("""
    ### 🩸 What is it?
    **CA-125** is a protein found on the surface of most ovarian cancer cells. It is also found in small amounts in normal tissue.
    
    ### 🎯 Importance of the Test
    It is used to monitor treatment for **Ovarian Cancer** and detect recurrence. It can also be checked if a woman has an ovarian mass or high genetic risk. (Note: Menstruation, pregnancy, and pelvic inflammatory disease can also cause spikes).
    - **Normal Range:** Less than $35$ U/mL.
    
    ### ⚠️ Symptoms if the Level is High
    Significantly high levels correlate with ovarian malignancy or severe pelvic inflammation. Symptoms include **persistent abdominal bloating or swelling, feeling full quickly when eating, pelvic pain**, and a frequent, urgent need to urinate.
    """)

# 4. CA-19-9 (Cancer Antigen 19-9)
with st.expander("🎗️ CA-19-9 (Pancreatic Cancer Marker) - Code: CA199_04"):
    st.markdown("""
    ### 🩸 What is it?
    **CA-19-9** is a tumor-associated antigen that is heavily shed by pancreatic and biliary tract cancer cells.
    
    ### 🎯 Importance of the Test
    It is the premier biomarker for managing and monitoring **Pancreatic Cancer** and bile duct cancers. It helps evaluate if a tumor is surgically removable or responding to chemotherapy.
    - **Normal Range:** Less than $37$ U/mL.
    
    ### ⚠️ Symptoms if the Level is High
    Correlates strongly with pancreatic or gallbladder disease. Symptoms include **severe upper abdominal pain radiating to the back, unexplained weight loss, new-onset diabetes in older adults, and obstructive jaundice** (yellowing of skin/eyes with pale stools).
    """)

# 5. AFP (Alpha-Fetoprotein)
with st.expander("🎗️ AFP (Alpha-Fetoprotein) - Code: AFP_05"):
    st.markdown("""
    ### 🩸 What is it?
    **AFP** is a protein naturally produced by a developing baby's liver. In healthy non-pregnant adults, AFP levels should be extremely low or undetectable.
    
    ### 🎯 Importance of the Test
    In adults, high AFP levels are a hallmark sign of **Liver Cancer (Hepatocellular Carcinoma)** or certain **Germ Cell Tumors** (testicular or ovarian cancer). It is routinely used to screen high-risk patients (like those with Cirrhosis or Hepatitis B).
    - **Normal Range:** Less than $10$ ng/mL (for non-pregnant adults).
    
    ### ⚠️ Symptoms if the Level is High
    * **If Liver Related:** Symptoms include **pain or a lump in the upper right side of the abdomen, loss of appetite, dark urine, and fluid accumulation in the belly (ascites)**.
    * **If Testicular Related:** Symptoms include a painless lump or swelling in either testicle or a heavy feeling in the scrotum.
    """)
st.warning("⚠️ **CRITICAL CLINICAL NOTE:** Tumor markers are **NOT** definitive diagnostic tools for cancer on their own. Elevated levels can occur in non-cancerous conditions (e.g., PSA can rise due to a UTI; CA-125 can rise during a normal period). A definitive diagnosis always requires imaging (CT/MRI) and a tissue biopsy.")

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
# 1. Testosterone
with st.expander("🧬 Testosterone - Code: TEST_01"):
    st.markdown("""
    ### 🩸 What is it?
    **Testosterone** is the primary male sex hormone (androgen), though women also produce it in much smaller amounts. It regulates muscle mass, bone density, fat distribution, and sex drive.
    
    ### 🎯 Importance of the Test
    Used to diagnose erectile dysfunction and infertility in men. In women, it is primarily used to evaluate conditions like **PCOS (Polycystic Ovary Syndrome)**.
    - **Normal Range:** **Men:** $300 - 1,000$ ng/dL | **Women:** $15 - 70$ ng/dL.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** In women (common in PCOS), it causes **excessive facial/body hair (hirsutism), severe acne, male-pattern baldness, and irregular periods**. In men, abnormally high levels are rare unless caused by steroid abuse, leading to aggression and low sperm count.
    * **If Low:** In men, it causes **low sex drive (libido), chronic fatigue, loss of muscle mass, erectile dysfunction, and depression**.
    """)

# 2. FSH (Follicle-Stimulating Hormone)
with st.expander("🥚 FSH (Follicle-Stimulating Hormone) - Code: FSH_02"):
    st.markdown("""
    ### 🩸 What is it?
    **FSH** is released by the pituitary gland. In women, it stimulates the growth of ovarian follicles (eggs); in men, it triggers sperm production in the testes.
    
    ### 🎯 Importance of the Test
    Essential for evaluating infertility, irregular periods, and diagnosing the onset of **Menopause** in women or testicular failure in men.
    - **Normal Range:** Varies drastically based on the menstrual cycle phase. Highly elevated in postmenopausal women ($>30$ mIU/mL).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** In women, it signifies that the ovaries are failing to respond (e.g., **Menopause** or Primary Ovarian Insufficiency). Symptoms include **hot flashes, night sweats, mood swings, and absent periods**.
    * **If Low:** Indicates a pituitary gland problem, leading to **infertility, lack of puberty in teens, and complete absence of ovulation or sperm production**.
    """)

# 3. LH (Luteinizing Hormone)
with st.expander("⚡ LH (Luteinizing Hormone) - Code: LH_03"):
    st.markdown("""
    ### 🩸 What is it?
    Like FSH, **LH** is a pituitary hormone. In women, a sudden spike in LH (the "LH surge") triggers **ovulation** (the release of a mature egg). In men, it tells the testes to produce testosterone.
    
    ### 🎯 Importance of the Test
    Used alongside FSH to evaluate fertility issues, pituitary disorders, and PCOS (where the LH to FSH ratio is often abnormally high, like 2:1 or 3:1).
    - **Normal Range:** Fluctuates based on the menstrual cycle phase.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Often associated with PCOS or ovarian failure. Symptoms include **irregular or painful periods, pelvic discomfort, and difficulty conceiving**.
    * **If Low:** Leads to a lack of ovulation or low testosterone production. Symptoms include **amenorrhea (stopped periods) in women and low energy/erectile dysfunction in men**.
    """)

# 4. Prolactin
with st.expander("🥛 Prolactin - Code: PRL_04"):
    st.markdown("""
    ### 🩸 What is it?
    **Prolactin** is a hormone produced by the pituitary gland. Its primary biological function is to stimulate and maintain breast milk production (lactation) after childbirth.
    
    ### 🎯 Importance of the Test
    Used to investigate unexplained milk discharge from breasts, infertility, and to screen for a non-cancerous pituitary tumor called a **Prolactinoma**.
    - **Normal Range:** Less than $25$ ng/mL for non-pregnant women; less than $20$ ng/mL for men.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Hyperprolactinemia):** In women, it shuts down ovulation, causing **unexplained breast milk discharge (galactorrhea), skipped periods, and infertility**. In men, it causes **enlarged breasts (gynecomastia), severe erectile dysfunction, and low libido**.
    * **If Low:** Generally rare and typically only an issue for postpartum women who find themselves unable to produce enough breast milk.
    """)

# 5. Estradiol (E2)
with st.expander("🌸 Estradiol (E2) - Code: EST_05"):
    st.markdown("""
    ### 🩸 What is it?
    **Estradiol** is the strongest and most active form of **Estrogen**, the primary female sex hormone. It regulates the menstrual cycle, protects bone health, and maintains female physical characteristics.
    
    ### 🎯 Importance of the Test
    Used to check ovarian function, monitor fertility treatments (like IVF), and assess reasons for abnormal vaginal bleeding or early/delayed puberty.
    - **Normal Range:** Fluctuates wildly during the menstrual cycle; drops significantly after menopause.
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** Known as "Estrogen Dominance." Symptoms include **heavy/painful periods, severe PMS, breast tenderness, bloating, weight gain**, and fibroids.
    * **If Low:** Indicates low ovarian reserve or menopause. Symptoms include **vaginal dryness, painful intercourse, chronic insomnia, mood swings, and a higher long-term risk of osteoporosis (bone thinning)**.
    """)

# 6. Progesterone
with st.expander("🍂 Progesterone - Code: PROG_06"):
    st.markdown("""
    ### 🩸 What is it?
    **Progesterone** is the "pregnancy hormone." It is produced by the ovaries right after ovulation to thicken the lining of the uterus, preparing it to sustain a fertilized egg.
    
    ### 🎯 Importance of the Test
    It is used to confirm whether ovulation actually occurred during a cycle and to monitor the health of a high-risk pregnancy (especially if there is a risk of miscarriage).
    - **Normal Range:** Low before ovulation, peaks mid-way through the luteal phase (around Day 21 of a 28-day cycle).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High:** High levels are completely normal during pregnancy. Outside of pregnancy, abnormally elevated levels can cause **fatigue, severe bloating, breast swelling, and moodiness**.
    * **If Low:** Leads to a failure to maintain the uterine lining. Symptoms include **spotting before periods, irregular cycles, frequent early miscarriages, and difficulty maintaining a pregnancy**.
    """)

# 7. Morning Cortisol
with st.expander("☀️ Morning Cortisol (The Stress Hormone) - Code: CORT_07"):
    st.markdown("""
    ### 🩸 What is it?
    **Cortisol** is a steroid hormone produced by the adrenal glands (sitting on top of your kidneys). It is known as the **"stress hormone"** because it regulates the body's fight-or-flight response, blood sugar, and blood pressure.
    
    ### 🎯 Importance of the Test
    Cortisol levels follow a strict daily clock (circadian rhythm)—they are highest in the morning (around 8 AM) and lowest at midnight. A morning blood draw screens for **Cushing’s Syndrome** (too much cortisol) or **Addison’s Disease** (adrenal insufficiency).
    - **Normal Morning Range:** Typically $5 - 23$ µg/dL (micrograms per deciliter).
    
    ### ⚠️ Symptoms: High vs. Low
    * **If High (Cushing's style):** Causes fat redistribution and tissue breakdown. Symptoms include a **round "moon face," a fatty hump between the shoulders (buffalo hump), rapid weight gain in the abdomen with purple stretch marks (striae)**, high blood pressure, and fragile skin.
    * **If Low (Addison's style):** Your body cannot handle stress or maintain blood pressure. Symptoms include **severe chronic fatigue, muscle weakness, unexplained weight loss, dark patches on the skin (hyperpigmentation)**, and dangerously low blood pressure causing dizziness upon standing.
    """)

st.info("💡 **Note:** Reproductive hormones (FSH, LH, Estradiol, Progesterone) fluctuate constantly based on the day of a woman's menstrual cycle. For data accuracy, it is highly recommended to record the exact day of the cycle when the blood sample was collected (e.g., Day 3 for FSH/LH, Day 21 for Progesterone). Morning Cortisol must strictly be collected between 7:00 AM and 9:00 AM.")

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
# =====================================================


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
st.divider()

st.warning("""
⚠️ This tool is for educational purposes only and does not replace
professional medical advice or diagnosis.
""") 

# Streamlit Page Configuration (Wide layout for optimal data visibility)
st.set_page_config(page_title="Medical Lab Test Directory", layout="wide")

st.title("📊 Interactive Medical Lab Test Directory")
st.write("Search, filter, and review test codes, associated diseases, and specific timing instructions.")

# 1. Core Dataset Creation (Pandas DataFrame)
data = {
    "Test Name": [
        "FBS (Fasting Blood Sugar)", "PPBS (Post Meal Blood Sugar)", "RBS (Random Blood Sugar)", "HbA1c",
        "Hemoglobin (Hb)", "WBC Count", "RBC Count", "Platelets", "ESR",
        "Total Cholesterol", "HDL Cholesterol", "LDL Cholesterol", "Triglycerides",
        "ALT / SGPT", "AST / SGOT", "Total Bilirubin", "Albumin", "Alkaline Phosphate (ALP)",
        "Serum Creatinine", "Blood Urea", "Uric Acid", "eGFR",
        "TSH", "Total T3", "Total T4",
        "Sodium (Na+)", "Potassium (K+)", "Chloride (Cl-)", "Calcium", "Magnesium (Mg)", "Phosphorus",
        "Vitamin D3", "Vitamin B12", "Serum Iron", "Ferritin", "TIBC",
        "CRP (C-Reactive Protein)", "Rheumatoid Factor (RF)", "Anti-CCP Antibody", "ASO Titre", "ANA Test",
        "Prothrombin Time (PT) / INR", "aPTT",
        "Troponin (I or T)", "CK-MB", "BNP",
        "Dengue NS1 Antigen", "Dengue IgM & IgG", "Malaria Antigen (Pv/Pf)", "Typhoid IgM (Typhidot)",
        "HBsAg (Hepatitis B)", "Anti-HCV (Hepatitis C)", "HIV 1 & 2 Screening",
        "PSA", "CEA", "CA-125", "CA-19-9", "AFP",
        "Testosterone", "FSH", "LH", "Prolactin", "Estradiol (E2)", "Progesterone", "Morning Cortisol"
    ],
    "Test Code": [
        "FBS_01", "PPBS_02", "RBS_03", "HBA1C_04",
        "HB_01", "WBC_02", "RBC_03", "PLT_04", "ESR_05",
        "CHOL_01", "HDL_02", "LDL_03", "TRIG_04",
        "ALT_01", "AST_02", "BIL_03", "ALB_04", "ALP_05",
        "CRE_01", "UREA_02", "URIC_03", "EGFR_04",
        "TSH_01", "T3_03", "T4_02",
        "SOD_01", "POT_02", "CHL_03", "CAL_04", "MAG_05", "PHO_06",
        "VITD_01", "B12_02", "IRON_03", "FER_04", "TIBC_05",
        "CRP_01", "RF_02", "ACCP_03", "ASO_04", "ANA_05",
        "PT_01 / INR_02", "APTT_03",
        "TROP_01", "CKMB_02", "BNP_03",
        "DEN_NS1", "DEN_AB", "MAL_AG", "TYP_IGM",
        "HBSAG", "HCV_AB", "HIV_SCR",
        "PSA_01", "CEA_02", "CA125_03", "CA199_04", "AFP_05",
        "TEST_01", "FSH_02", "LH_03", "PRL_04", "EST_05", "PROG_06", "CORT_07"
    ],
    "Potential Diseases / Conditions Checked": [
        "Diabetes, Prediabetes, Insulin Resistance", "Diabetes management, Reactive Hypoglycemia", "Emergency Diabetes Screening, Hyperglycemia", "3-Month Average Diabetes Control, Prediabetes",
        "Anemia, Blood loss, Polycythemia", "Infections, Inflammation, Leukemia, Allergy", "Anemia, Hypoxia, Erythrocytosis", "Dengue, Bleeding Disorders, Thrombocytopenia", "Tuberculosis, Autoimmune Diseases, Chronic Infection",
        "Cardiovascular (Heart) Disease Risk, Hyperlipidemia", "Good Cholesterol tracking, Heart attack risk", "Atherosclerosis (Artery Clogging), Stroke Risk", "Fatty Liver, Acute Pancreatitis, Metabolic Syndrome",
        "Fatty Liver, Hepatitis, Liver Injury/Cirrhosis", "Alcoholic Liver Disease, Heart/Muscle Damage", "Jaundice, Gallstones, Hemolytic Anemia", "Cirrhosis, Nephrotic Syndrome (Kidney Disease), Malnutrition", "Bile Duct Blockage, Bone Diseases, Paget's Disease",
        "Chronic Kidney Disease (CKD), Acute Kidney Injury", "Kidney Dysfunction, Dehydration, Uremia", "Gout (Joint Pain), Kidney Stones", "Kidney Function Staging (CKD Stages)",
        "Hypothyroidism, Hyperthyroidism, Goiter", "Graves' Disease, Thyroid Function", "Hashimoto's Thyroiditis, Thyroid Function",
        "Severe Dehydration, Hyponatremia, Confusion", "Heart Arrhythmia (Palpitations), Muscle Cramps", "Acid-Base Imbalance, Severe Vomiting/Dehydration", "Bone thinning, Hyperparathyroidism, Muscle Spasms", "Chronic Muscle Twitches, Alcoholism Malnutrition", "Advanced Kidney Failure, Vitamin D disorders",
        "Osteoporosis, Chronic Fatigue, Rickets", "Pernicious Anemia, Neuropathy (Pins/Needles in feet)", "Iron Deficiency Anemia, Hemochromatosis (Iron Overload)", "Iron Storage Deficiency, Chronic Inflammation", "Iron Deficiency Anemia Differentiation",
        "Acute Bacterial Infection, Rheumatoid Flare-up", "Rheumatoid Arthritis (Severe joint pain & stiffness)", "Rheumatoid Arthritis Diagnosis (High Specificity)", "Rheumatic Fever (Migrating joint pain), Strep Throat", "Lupus (SLE), Sjogren's Syndrome, Autoimmune Screen",
        "Warfarin Medication Monitoring, Bleeding Disorders", "Heparin Monitoring, Hemophilia (Genetic bleeding)",
        "Heart Attack (Myocardial Infarction Emergency)", "Recent Heart Damage, Re-infarction Tracking", "Heart Failure (Severe shortness of breath/Edema)",
        "Early Dengue Fever (Day 1 to 5 of fever)", "Current or Past Dengue Infection status", "Malaria (Fever with violent shivering/chills)", "Typhoid Fever (Step-ladder fever, stomach pain)",
        "Hepatitis B Infection (Liver Jaundice or Silent)", "Hepatitis C Infection (Chronic Liver damage)", "HIV / AIDS screening",
        "Prostate Cancer screening, Benign Prostate Hyperplasia", "Colorectal (Colon) Cancer Monitoring", "Ovarian Cancer Monitoring, Endometriosis", "Pancreatic Cancer, Gallbladder Cancer tracking", "Liver Cancer, Testicular Cancer, Germ Cell Tumors",
        "Low Libido (Men), Infertility, PCOS (Women)", "Infertility, Menopause, PCOS evaluation", "Infertility, Ovulation Trigger Tracking", "Prolactinoma (Pituitary tumor), Galactorrhea", "Ovarian reserve, Menopause, IVF tracking", "Pregnancy maintenance, Miscarriage risk, Ovulation check", "Cushing’s Syndrome, Addison’s Disease (Adrenal)"
    ],
    "Best Test Time / Instructions": [
        "Morning (Strictly 8-12 Hours Fasting)", "2 hours after starting a main meal", "Anytime (Regardless of food)", "Anytime (No fasting required)",
        "Anytime", "Anytime", "Anytime", "Anytime", "Anytime",
        "Morning (9-12 Hours Fasting preferred)", "Morning (9-12 Hours Fasting preferred)", "Morning (9-12 Hours Fasting preferred)", "Morning (9-12 Hours Fasting Mandatory)",
        "Anytime (Avoid alcohol 48h before)", "Anytime (Avoid alcohol 48h before)", "Anytime (Morning preferred)", "Anytime", "Anytime (Fasting preferred)",
        "Anytime (Avoid heavy workout before)", "Anytime", "Anytime", "Calculated Score (No extra time needed)",
        "Morning (Due to diurnal variation)", "Morning preferred", "Morning preferred",
        "Anytime", "Anytime", "Anytime", "Anytime", "Anytime", "Morning Fasting preferred",
        "Anytime", "Anytime", "Morning (Fasting preferred)", "Morning (Fasting preferred)", "Morning (Fasting preferred)",
        "Anytime", "Anytime", "Anytime", "Anytime", "Anytime",
        "Anytime (Consistent time daily if on medicine)", "Anytime",
        "Emergency (Anytime immediately with chest pain)", "Emergency (Anytime immediately with chest pain)", "Anytime",
        "Anytime (Best within Day 1 to 5 of fever)", "Anytime (Best after Day 5 of fever)", "Anytime (Ideally during a fever spike)", "Anytime (Best after Day 3-4 of fever)",
        "Anytime", "Anytime", "Anytime (Mind the window period)",
        "Anytime (Avoid cycling 48h before)", "Anytime", "Anytime (Avoid during menstruation)", "Anytime", "Anytime",
        "Morning (Between 7 AM - 10 AM)", "Day 2 to Day 5 of the menstrual cycle", "Day 2 to Day 5 of the menstrual cycle", "Morning (3-4 hours after waking up)", "Day 2 to Day 5 of cycle preferred", "Day 21 of cycle for Progesterone check", "Strictly Morning (Between 7 AM - 9 AM)"
    ]
}

df = pd.DataFrame(data)

# 2. Search Box Filter Interface
search_query = st.text_input("🔍 Search by Test Name or Disease Name:", "")

# 3. Dynamic Filtering Logic
if search_query:
    filtered_df = df[
        df["Test Name"].str.contains(search_query, case=False) | 
        df["Potential Diseases / Conditions Checked"].str.contains(search_query, case=False)
    ]
else:
    filtered_df = df

# 4. Interactive Spreadsheet Rendering
st.dataframe(
    filtered_df,
    use_container_width=True,  # Scales elegantly across standard & ultra-wide screens
    hide_index=True           # Removes default pandas integer indexing row lines
)

