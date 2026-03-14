# Network Intrusion Detection System (NIDS)

A Machine Learning based **Network Intrusion Detection System** that detects malicious network traffic and classifies it as **normal or intrusion**.
The project includes a trained ML model and a **Streamlit web application** for interactive predictions.

## 🌐 Live Web App

Try the deployed application here:
https://nisd99x.streamlit.app/

## 📌 Features

* Detects network intrusions using Machine Learning
* Interactive **Streamlit web interface**
* Data visualization for model results
* Confusion matrix and prediction outputs
* Easy to deploy and test

## 📂 Project Structure

```
Network_Intrusion_Detection_System
│
├── models/                # Trained machine learning models
├── notebooks/             # Jupyter notebooks for training and analysis
│   └── intrusion_detection.ipynb
│
├── ui/                    # Streamlit web application
│   └── app.py
│
├── datasets.zip           # Dataset used for training
├── requirements.txt       # Python dependencies
├── .gitignore
└── .gitattributes
```

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

## 🚀 Running the Project Locally

### 1. Clone the repository

```
git clone https://github.com/raazan99x-netizen/Network-Intrusion-Detection-System.git
```

### 2. Navigate to the project

```
cd Network-Intrusion-Detection-System
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```
streamlit run ui/app.py
```

The application will open at:

```
http://localhost:8501
```

## 📊 Machine Learning Model

The project uses a **classification model** trained on network traffic data to detect intrusion patterns.

Model pipeline includes:

* Data preprocessing
* Feature selection
* Model training
* Evaluation using confusion matrix

## 📷 Web App Preview

Access the deployed application to test predictions:
https://nisd99x.streamlit.app/

## 👨‍💻 Author

**Raaz An**

GitHub:
https://github.com/raazan99x-netizen
