import streamlit as st

st.set_page_config(
    page_title="NCV & EMG Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 NCV & EMG Assistant")

st.warning(
    "⚠️ This tool is for educational purposes only. "
    "It does NOT diagnose diseases. Always consult a Neurologist or "
    "Physiatrist for medical interpretation."
)

st.markdown("---")

st.header("Patient Information")

col1, col2 = st.columns(2)

with col1:
    patient = st.text_input("Patient Name")
    age = st.number_input("Age", 1, 120, 30)

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

st.markdown("---")

st.header("NCV Findings")

motor = st.selectbox(
    "Motor Nerve Conduction",
    [
        "Normal",
        "Reduced Velocity",
        "Reduced Amplitude",
        "Prolonged Latency",
        "Conduction Block",
        "Not Performed"
    ]
)

sensory = st.selectbox(
    "Sensory Nerve Conduction",
    [
        "Normal",
        "Reduced Velocity",
        "Reduced Amplitude",
        "Absent Response",
        "Not Performed"
    ]
)

fwave = st.selectbox(
    "F-wave",
    [
        "Normal",
        "Prolonged",
        "Absent",
        "Not Performed"
    ]
)

hreflex = st.selectbox(
    "H-reflex",
    [
        "Normal",
        "Delayed",
        "Absent",
        "Not Performed"
    ]
)

st.markdown("---")

st.header("Needle EMG Findings")

emg = st.selectbox(
    "Needle EMG",
    [
        "Normal",
        "Denervation Potentials",
        "Fibrillation Potentials",
        "Positive Sharp Waves",
        "Reduced Recruitment",
        "Large Motor Units",
        "Polyphasic MUAPs"
    ]
)

st.markdown("---")

st.header("Clinical Impression")

symptom = st.text_area(
    "Symptoms (Optional)",
    placeholder="Example: Hand numbness, foot drop, tingling..."
)

if st.button("Generate Educational Interpretation"):

    st.subheader("Report Summary")

    summary = []

    if motor == "Normal":
        summary.append("✅ Motor nerve conduction appears within expected limits.")

    elif motor == "Reduced Velocity":
        summary.append("• Reduced motor conduction velocity may be seen in demyelinating nerve disorders.")

    elif motor == "Reduced Amplitude":
        summary.append("• Reduced motor amplitude may indicate axonal involvement.")

    elif motor == "Prolonged Latency":
        summary.append("• Prolonged distal latency may occur in entrapment neuropathies.")

    elif motor == "Conduction Block":
        summary.append("• Conduction block can occur in certain demyelinating neuropathies.")

    if sensory == "Reduced Velocity":
        summary.append("• Reduced sensory velocity suggests sensory nerve involvement.")

    elif sensory == "Reduced Amplitude":
        summary.append("• Reduced sensory amplitude may reflect axonal sensory neuropathy.")

    elif sensory == "Absent Response":
        summary.append("• Absent sensory response may indicate severe sensory nerve dysfunction.")

    if fwave == "Prolonged":
        summary.append("• Prolonged F-wave may indicate proximal nerve involvement.")

    elif fwave == "Absent":
        summary.append("• Absent F-wave may occur in significant neuropathy.")

    if hreflex == "Delayed":
        summary.append("• Delayed H-reflex can be associated with S1 root involvement.")

    elif hreflex == "Absent":
        summary.append("• Absent H-reflex may occur in neuropathy or radiculopathy.")

    if emg == "Normal":
        summary.append("✅ Needle EMG appears unremarkable.")

    elif emg == "Denervation Potentials":
        summary.append("• Denervation potentials may suggest ongoing nerve injury.")

    elif emg == "Fibrillation Potentials":
        summary.append("• Fibrillation potentials may indicate active denervation.")

    elif emg == "Positive Sharp Waves":
        summary.append("• Positive sharp waves may indicate muscle denervation.")

    elif emg == "Reduced Recruitment":
        summary.append("• Reduced recruitment may be seen with neurogenic disorders.")

    elif emg == "Large Motor Units":
        summary.append("• Large motor unit potentials may indicate chronic reinnervation.")

    elif emg == "Polyphasic MUAPs":
        summary.append("• Polyphasic motor unit potentials may occur during reinnervation.")

    for item in summary:
        st.write(item)

    st.markdown("---")

    st.subheader("Possible Educational Correlations")

    possibilities = []

    if motor == "Prolonged Latency":
        possibilities.append("• Entrapment neuropathy (e.g., Carpal Tunnel Syndrome)")

    if sensory == "Reduced Velocity":
        possibilities.append("• Peripheral neuropathy")

    if sensory == "Absent Response":
        possibilities.append("• Severe sensory neuropathy")

    if hreflex == "Delayed":
        possibilities.append("• Possible S1 radicular involvement")

    if emg in [
        "Denervation Potentials",
        "Fibrillation Potentials",
        "Positive Sharp Waves"
    ]:
        possibilities.append("• Neurogenic process")

    if emg == "Large Motor Units":
        possibilities.append("• Chronic reinnervation")

    if len(possibilities) == 0:
        st.success("No specific educational correlations based on the selected findings.")

    else:
        for p in possibilities:
            st.write(p)

    st.markdown("---")

    st.info(
        "These findings are educational explanations only and "
        "should always be interpreted together with clinical history, "
        "physical examination, and the complete NCV/EMG report by a qualified physician."
    )
