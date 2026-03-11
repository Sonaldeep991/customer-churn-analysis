import streamlit as st
import pandas as pd

df = pd.read_csv(r"C:\Users\Sonal deep Gupta\Downloads\European_Bank.csv")

# Page config
st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    
    return df

df = load_data()

st.title("📊 Customer Churn Analytics Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")

country = st.sidebar.multiselect(
    "Select Geography",
    options=df["Geography"].unique(),
    default=df["Geography"].unique()
)

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Geography"].isin(country)) &
    (df["Gender"].isin(gender))
]

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", len(filtered_df))

with col2:
    churn_rate = filtered_df["Exited"].mean() * 100
    st.metric("Churn Rate", f"{churn_rate:.2f}%")

with col3:
    active_customers = (filtered_df["Exited"] == 0).sum()
    st.metric("Active Customers", active_customers)

st.divider()

# Geography Churn
st.subheader("🌍 Churn Rate by Geography")

geo_churn = filtered_df.groupby("Geography")["Exited"].mean()

st.bar_chart(geo_churn)

# Age vs Churn
st.subheader("👥 Age vs Churn")

age_churn = filtered_df.groupby("Age")["Exited"].mean()

st.line_chart(age_churn)

# Balance vs Churn
st.subheader("💰 Average Balance by Churn")

balance = filtered_df.groupby("Exited")["Balance"].mean()

st.bar_chart(balance)
#streamlit run "C:\Users\Sonal deep Gupta\Desktop\european bank\churn analyst\webapp.py"
