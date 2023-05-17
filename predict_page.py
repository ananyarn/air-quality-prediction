import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()
regressor = data["model"]
le_day = data["le_day"]
le_hour = data["le_hour"]


def show_predict_page():
    st.title("Air Quality Prediction")
    st.write(
        """### Predict fine particulate matter air pollutant level in air in India!""")
    year = ('Choose an Option', 2017, 2018, 2019, 2020, 2021, 2022)
    month = ('Choose an Option', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, )
    day = ('Choose an Option', 'Start days of the Month', 'Mid days of the Month',
           'Late days of the Month',)
    hour = ('Choose an Option', 'Early Morning', 'Morning',
            'Afternoon', 'Evening', 'Night', 'Late Night',)
    y = st.selectbox("Year", year)
    m = st.slider("Month", 1, 12, 1)
    d = st.selectbox("Day", day)
    h = st.selectbox("Hour", hour)
    ok = st.button("Calculate PM2.5")
    if ok:
        z = np.array([[y, m, d, h]])
        z[:, 2] = le_day.transform(z[:, 2])
        z[:, 3] = le_hour.transform(z[:, 3])
        z = z.astype(int)
        quality = regressor.predict(z)
        st.subheader(
            f"The predicted fine particulate matter air pollutant level is {quality[0]:.2f}")
