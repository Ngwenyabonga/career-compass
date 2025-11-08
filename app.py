import streamlit as st
import pandas as pd

# Title and intro
st.title("Career Compass")
st.write("Welcome to your personalized career growth tool!")

# Load and display CSV
try:
    df = pd.read_csv("career_paths.csv")
    st.subheader("📊 Career Path Insights")
    st.dataframe(df)
except FileNotFoundError:
    st.error("CSV file not found. Please make sure 'career_paths.csv' is in the same folder as app.py.")

# Choose Your Path
st.header("Choose Your Path")
role = st.selectbox("Pick a role you're curious about:", ["Data Analyst", "HR Manager", "Software Developer", "Financial Planner"])
st.write(f"You selected: {role}")
# Filter the CSV based on selected role
filtered_df = df[df["Role"] == role]

st.subheader(f"🔍 Details for: {role}")
st.dataframe(filtered_df)
# Evaluate Your Current Career
st.header("Evaluate Your Current Career")
satisfaction = st.slider("How satisfied are you with your current role?", 0, 10)

# Plan Your Next Step
st.header("Plan Your Next Step")
next_step = st.text_input("What’s one thing you want to improve or learn next?")