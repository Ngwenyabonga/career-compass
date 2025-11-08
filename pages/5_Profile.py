import streamlit as st
from datetime import datetime

# Simulated user and progress data (replace with real backend/API later)
user = {
    "full_name": "Bonga Ngwenya",
    "email": "bonga@example.com",
    "created_date": "2023-06-01T00:00:00"
}
quiz_progress = {
    "results": {
        "careerProfile": "transformer",
        "recommendedPhase": "pivot",
        "affirmation": "It takes courage to reinvent yourself. You're brave."
    }
}
journey = {
    "phase": "pivot",
    "milestones": [{"completed": True}, {"completed": False}, {"completed": True}],
    "affirmations": ["You're taking control of your career journey."]
}
modules = [
    {"title": "Resume Optimization", "completed": True},
    {"title": "Interview Prep", "completed": False},
    {"title": "Networking Strategy", "completed": True}
]

# Header
st.title("👤 Profile Overview")
st.subheader(user["full_name"])
st.caption(f"📧 {user['email']}")
st.markdown(f"🗓️ Member Since: {datetime.strptime(user['created_date'], '%Y-%m-%dT%H:%M:%S').strftime('%b %Y')}")

# Career Profile Badge
if quiz_progress.get("results", {}).get("careerProfile"):
    st.markdown(f"**Career Profile:** `{quiz_progress['results']['careerProfile'].capitalize()}`")

# Stats Grid
st.subheader("📊 Your Stats")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Current Phase", journey.get("phase", "Not Started").capitalize())
with col2:
    st.metric("Milestones", sum(1 for m in journey["milestones"] if m["completed"]))
with col3:
    st.metric("Modules", sum(1 for m in modules if m["completed"]))

# Journey Summary
st.subheader("🛤️ Journey Overview")
st.write(f"Completed Milestones: {sum(1 for m in journey['milestones'] if m['completed'])} / {len(journey['milestones'])}")
st.write(f"Collected Affirmations: {len(journey['affirmations'])}")
st.write(f"Completed Modules: {sum(1 for m in modules if m['completed'])} / {len(modules)}")

# Quiz Results
if quiz_progress.get("results"):
    st.subheader("🧠 Quiz Results")
    st.write(f"Career Profile: `{quiz_progress['results']['careerProfile'].capitalize()}`")
    st.write(f"Recommended Phase: `{quiz_progress['results']['recommendedPhase'].capitalize()}`")
    st.markdown(f"> 💬 *{quiz_progress['results']['affirmation']}*")

# Logout Button (simulated)
st.subheader("🔒 Actions")
if st.button("Sign Out"):
    st.warning("You’ve been signed out (simulated).")