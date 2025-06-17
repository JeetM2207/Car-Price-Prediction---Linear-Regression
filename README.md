# 🚗 Car Price Prediction using Linear Regression

This project uses Linear Regression to predict car prices based on various features such as year, present price, fuel type, transmission, and more. The model is trained on a cleaned dataset and deployed using Streamlit for interactive predictions.

🔗 **Live Demo**: [Car Price Prediction App](https://car-price-prediction---linear-regression.streamlit.app/)

---

## 📁 Project Structure


---

## 📊 Dataset

- **Source**: Kaggle or publicly available car dataset
- **Features**:
  - Year
  - Present Price
  - Kms Driven
  - Fuel Type (Petrol, Diesel)
  - Seller Type (Dealer, Individual)
  - Transmission (Manual, Automatic)
  - Owner
- **Target**: Selling Price

---

## 🔍 Data Preprocessing

- Handled categorical variables using one-hot encoding
- Created a new feature: car age from current year and year of registration
- Dropped irrelevant features like car names
- Normalized/standardized where necessary

---

## 🤖 Model

- **Algorithm Used**: Linear Regression (from scikit-learn)
- **Performance Metrics**:
  - R² Score
  - MAE (Mean Absolute Error)
  - Visualization of actual vs. predicted prices

---

## 🚀 How to Use the App

You can try out the app live here:  
👉 [https://car-price-prediction---linear-regression.streamlit.app/](https://car-price-prediction---linear-regression.streamlit.app/)

### Or run it locally:

1. Clone the repository:
   git clone https://github.com/JeetM2207/Car-Price-Prediction---Linear-Regression.git
   cd Car-Price-Prediction---Linear-Regression
2.python -m venv venv
 source venv/bin/activate  # On Windows use: venv\Scripts\activate
3.pip install -r requirements.txt
4.streamlit run app.py
