import streamlit as st
from src.data_loader import load_fpl_data

st.set_page_config(page_title="FPL Team Optimizer", layout="wide")
st.title("⚽ FPL Team Optimizer")

# Load player data
df = load_fpl_data()

st.subheader("Top 10 Players by Form")
st.dataframe(df[['first_name', 'second_name', 'form', 'total_points', 'now_cost']].sort_values(by='form', ascending=False).head(10))