import streamlit as st
import pandas as pd
import numpy as np
import joblib
import zipfile
import os

# Page title
st.title("Network Intrusion Detection System")

st.info(
    "Upload a Network Traffic / Network Flow CSV file with the same features as the training dataset. "
    "If no file is uploaded, a sample dataset from datasets.zip will be used."
)

# Load trained model
model = joblib.load("models/cicids_model.pkl")

# File uploader
uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV file",
    type=["csv"]
)

# Load data
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("User CSV file loaded successfully")

else:
    zip_path = "datasets.zip"

    if not os.path.exists(zip_path):
        st.error("datasets.zip not found")
        st.stop()

    with zipfile.ZipFile(zip_path) as z:
        csv_files = [f for f in z.namelist() if f.endswith(".csv")]

        if len(csv_files) == 0:
            st.error("No CSV files found inside datasets.zip")
            st.stop()

        with z.open(csv_files[0]) as f:
            data = pd.read_csv(f)

    st.success("Sample dataset loaded from datasets.zip")

# Remove label columns if present
if " Label" in data.columns:
    data = data.drop(" Label", axis=1)

if "Label" in data.columns:
    data = data.drop("Label", axis=1)

# Clean data
data = data.replace([np.inf, -np.inf], np.nan)
data = data.dropna()

# Prediction
predictions = model.predict(data)

data["Prediction"] = predictions
data["Prediction"] = data["Prediction"].map({
    0: "Normal",
    1: "Attack"
})

# Show results
st.subheader("Prediction Result")
st.dataframe(data.head())

# Traffic summary
st.subheader("Traffic Summary")

result = data["Prediction"].value_counts()
st.write(result)

total = result.sum()
attack_percent = (result.get("Attack", 0) / total) * 100

st.write(f"Attack Traffic Percentage: {attack_percent:.2f}%")

# Alert
if "Attack" in result:
    st.error("⚠️ Intrusion Detected in Network Traffic")
else:
    st.success("✅ Network Traffic Looks Normal")