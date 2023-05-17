import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def organize_days_in_a_month(x):
    if x >= 1 and x <= 10:
        return 'Start days of the Month'
    elif x >= 11 and x <= 20:
        return 'Mid days of the Month'
    elif x >= 21 and x <= 31:
        return 'Late days of the Month'


def organize_hours_in_a_day(x):
    if x >= 7 and x <= 11:
        return 'Morning'
    elif x >= 12 and x <= 15:
        return 'Afternoon'
    elif x >= 16 and x <= 19:
        return 'Evening'
    elif x >= 20 and x <= 23:
        return 'Night'
    elif x >= 0 and x <= 3:
        return 'Late Night'
    elif x >= 4 and x <= 6:
        return 'Early Morning'


@st.cache_data
def load_data():
    df = pd.read_csv("air-quality-india.csv")
    df = df[["Year", "Month", "Day", "Hour", "PM2.5"]]
    df = df[df["PM2.5"].notnull()]
    df = df.dropna()
    df['Day'] = df['Day'].apply(organize_days_in_a_month)
    df['Hour'] = df['Hour'].apply(organize_hours_in_a_day)
    return df


df = load_data()


def show_explore_page():
    st.title("Explore PM2.5 Levels")
    st.write(""" ### Air Quality Data in India (2017 - 2022)""")
    data = df['Year'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%",
            shadow=True, startangle=90)
    ax1.axis("equal")
    st.write(""" ### Percentage of data from different years: """)
    st.pyplot(fig1)
    st.write(""" ### Mean PM2.5 based on year:""")
    data = df.groupby(['Year'])['PM2.5'].mean().sort_values(ascending=True)
    st.bar_chart(data)
    st.write(""" ### Mean PM2.5 based on hour of the day:""")
    data = df.groupby(['Hour'])['PM2.5'].mean().sort_values(ascending=True)
    st.line_chart(data)
