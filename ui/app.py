import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Network Intrusion Detection System")

model = joblib.load("models/cicids_model.pkl")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    data = pd.read_csv(file)

    if " Label" in data.columns:
        data = data.drop(" Label", axis=1)

    if "Label" in data.columns:
        data = data.drop("Label", axis=1)

    import numpy as np
    data = data.replace([np.inf, -np.inf], np.nan)
    data = data.dropna()

    # Make predictions
    predictions = model.predict(data)

    data["Prediction"] = predictions
    data["Prediction"] = data["Prediction"].map({0: "Normal", 1: "Attack"})

    st.subheader("Prediction Result")
    st.write(data.head())

    # Traffic summary
    st.subheader("Traffic Summary")
    result = data["Prediction"].value_counts()
    st.write(result)

    # Show attack percentage
    total = result.sum()
    attack_percent = (result.get("Attack", 0) / total) * 100

    st.write(f"Attack Traffic Percentage: {attack_percent:.2f}%")
    if "Attack" in result:
        st.error("⚠️ Intrusion Detected in Network Traffic")
    else:
        st.success("✅ Network Traffic Looks Normal")