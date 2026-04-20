import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="FarmCare Intelligence", layout="wide")

st.title("Surgeons FarmCare | Territory Intelligence System")

st.write("Upload your sales file or use default dataset")

# -----------------------------
# DATA INPUT LAYER
# -----------------------------
uploaded_file = st.file_uploader("Upload Sales CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    # Default dataset (fallback)
    df = pd.DataFrame({
        "Product": ["Maclik Super", "Nilzan", "Kupakula", "Triatix", "Maclik Super"],
        "Region": ["Embu", "Embu", "Meru", "Kirinyaga", "Meru"],
        "Sales": [120, 90, 150, 70, 110],
        "Profit": [30, 20, 45, 18, 28],
        "Month": ["Jan", "Jan", "Feb", "Feb", "Mar"]
    })

# -----------------------------
# FILTERS
# -----------------------------
st.sidebar.header("Control Panel")

region = st.sidebar.selectbox("Select Region", df["Region"].unique())
product = st.sidebar.selectbox("Select Product", df["Product"].unique())

filtered_df = df[(df["Region"] == region) & (df["Product"] == product)]

# -----------------------------
# KPI ENGINE
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", filtered_df["Sales"].sum())

with col2:
    st.metric("Total Profit", filtered_df["Profit"].sum())

with col3:
    if len(filtered_df) > 0:
        st.metric("Avg Sales per Transaction", round(filtered_df["Sales"].mean(), 2))
    else:
        st.metric("Avg Sales per Transaction", 0)

# -----------------------------
# DATA VIEW
# -----------------------------
st.subheader("Filtered Sales Dataset")
st.dataframe(filtered_df)

# -----------------------------
# SALES TREND
# -----------------------------
st.subheader("Sales Trend by Month")

trend = df[df["Product"] == product].groupby("Month")["Sales"].sum()

fig, ax = plt.subplots()
ax.plot(trend.index, trend.values, marker="o")
ax.set_ylabel("Sales")
ax.set_xlabel("Month")

st.pyplot(fig)

# -----------------------------
# BUSINESS INSIGHT ENGINE
# -----------------------------
st.subheader("Key Insight")

if filtered_df["Sales"].sum() > 100:
    st.success("High performing product in selected segment")
else:
    st.warning("Low sales performance detected — review distribution or pricing strategy")
