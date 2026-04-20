
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="FarmCare Dashboard", layout="wide")

st.title("Surgeons FarmCare | Sales Intelligence Dashboard")

# -----------------------------
# SAMPLE BUSINESS DATA
# -----------------------------
data = {
    "Product": ["Maclik Super", "Nilzan", "Kupakula", "Triatix", "Maclik Super", "Nilzan"],
    "Region": ["Embu", "Embu", "Meru", "Kirinyaga", "Meru", "Embu"],
    "Sales": [120, 90, 150, 70, 110, 95],
    "Profit": [30, 20, 45, 18, 28, 22]
}

df = pd.DataFrame(data)

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region", df["Region"].unique())

filtered_df = df[df["Region"] == region]

# -----------------------------
# KPI SECTION
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", filtered_df["Sales"].sum())

with col2:
    st.metric("Total Profit", filtered_df["Profit"].sum())

# -----------------------------
# DATA TABLE
# -----------------------------
st.subheader("Sales Performance Table")
st.dataframe(filtered_df)

# -----------------------------
# VISUALIZATION
# -----------------------------
st.subheader("Sales Distribution")

fig, ax = plt.subplots()
ax.bar(filtered_df["Product"], filtered_df["Sales"])
ax.set_ylabel("Sales Volume")
ax.set_xlabel("Products")

st.pyplot(fig)
