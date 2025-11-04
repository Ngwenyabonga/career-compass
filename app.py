import streamlit as st

st.title("Career Compass")
st.write("Welcome to your personalized career growth tool!")

st.header("Choose Your Path")
role = st.selectbox("Pick a role you're curious about:", ["Data Analyst", "HR Manager", "Software Developer", "Financial Planner"])
st.write(f"You selected: {role}")

st.header("Evaluate Your Current Career")
st.slider("How satisfied are you with your current role?", 0, 10)

st.header("Plan Your Next Step")
st.text_input("What’s one thing you want to improve or learn next?")