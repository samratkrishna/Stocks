import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

import pandas as pd

data = pd.read_excel("alldatacombined.xlsx", engine='openpyxl')


companies = data["Company Name"].unique()
models = {}

for company in companies:
    data_company = data[data["Company Name"] == company]
    X = data_company[["Open", "High", "Low"]]
    y = data_company["Close"]
    model = LinearRegression()
    model.fit(X, y)
    models[company] = model


st.title("Stock Close Price Predictor")


company = st.selectbox("Select Company", companies)


open_val = st.number_input("Enter Open Price", min_value=0.0, step=0.01)
high_val = st.number_input("Enter High Price", min_value=0.0, step=0.01)
low_val = st.number_input("Enter Low Price", min_value=0.0, step=0.01)

if st.button("Predict Close Price"):
    model = models[company]
    new_data = np.array([[open_val, high_val, low_val]])
    predicted_close = model.predict(new_data)[0]
    st.markdown(
        f"<p style='color:blue; font-size:20px;'>Predicted Close Price for {company}: {predicted_close:.2f}</p>",
        unsafe_allow_html=True
    )
