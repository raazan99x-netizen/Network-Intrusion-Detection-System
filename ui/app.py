import streamlit as st
import pandas as pd
import numpy as np
import joblib
import zipfile
import os

st.title("Network Intrusion Detection System")

model = joblib.load("../models/cicids_model.pkl")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    data = pd.read_csv(file)

else:
    zip_path = "../datasets.zip"

    if not os.path.exists(zip_path):
        st.error("datasets.zip not found")
        st.stop()

    with zipfile.ZipFile(zip_path) as z:
        csv_files = [f for f in z.namelist() if f.endswith(".csv")]

        if len(csv_files) == 0:
            st.error("No CSV files found in datasets.zip")
            st.stop()

        with z.open(csv_files[0]) as f:
            data = pd.read_csv(f)

if " Label" in data.columns:
    data = data.drop(" Label", axis=1)

if "Label" in data.columns:
    data = data.drop("Label", axis=1)

data = data.replace([np.inf, -np.inf], np.nan)
data = data.dropna()

predictions = model.predict(data)

data["Prediction"] = predictions
data["Prediction"] = data["Prediction"].map({0: "Normal", 1: "Attack"})

st.subheader("Prediction Result")
st.write(data.head())

st.subheader("Traffic Summary")

result = data["Prediction"].value_counts()
st.write(result)

total = result.sum()
attack_percent = (result.get("Attack", 0) / total) * 100

st.write(f"Attack Traffic Percentage: {attack_percent:.2f}%")

if "Attack" in result:
    st.error("⚠️ Intrusion Detected in Network Traffic")
else:
    st.success("✅ Network Traffic Looks Normal")