import streamlit as st
import pandas as pd

df = pd.read_csv(r"C:\Users\Sonal deep Gupta\Downloads\European_Bank.csv")

st.title("Customer Churn Analytics Dashboard")

st.metric("Overall Churn Rate", round(df["Exited"].mean()*100,2))

geo = df.groupby("Geography")["Exited"].mean()

st.bar_chart(geo)
#streamlit run "C:\Users\Sonal deep Gupta\Desktop\european bank\churn analyst\webapp.py"
