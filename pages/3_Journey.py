import streamlit as st

# Simulated user journey data (replace with real backend/API later)
default_milestones = {
    "discover": [
        {"id": "self_assessment", "title": "Complete self-assessment", "completed": False},
        {"id": "explore_paths", "title": "Explore 3+ career paths", "completed": False},
        {"id": "informational_interviews", "title": "Conduct informational interviews", "completed": False},
        {"id": "skills_audit", "title": "Audit your current skills", "completed": False},
        {"id": "vision_board", "title": "Create career vision board", "completed": False}
    ],
    "validate": [
        {"id": "goal_setting", "title": "Set SMART career goals", "completed": False},
        {"id": "performance_review", "title": "Request performance feedback", "completed": False},
        {"id": "skill_development", "title": "Enroll in skill development course", "completed": False},
        {"id": "network_expansion", "title": "Expand professional network", "completed": False},
        {"id": "mentor_connection", "title": "Connect with a mentor", "completed": False}
    ],
    "pivot": [
        {"id": "decision_clarity", "title": "Gain clarity on pivot decision", "completed": False},
        {"id": "transition_plan", "title": "Create transition plan", "completed": False},
        {"id": "skills_gap", "title": "Identify skills gap", "completed": False},
        {"id": "financial_plan", "title": "Build financial safety net", "completed": False},
        {"id": "network_rebuild", "title": "Rebuild network in new field", "completed": False}
    ]
}

# Session state
if "phase" not in st.session_state:
    st.session_state.phase = "discover"
if "milestones" not in st.session_state:
    st.session_state.milestones = default_milestones[st.session_state.phase]
if "affirmations" not in st.session_state:
    st.session_state.affirmations = ["You're taking control of your career journey."]

# Header
st.title("Your Journey")
st.caption("Track your career transformation")

# Phase selector
st.subheader("Current Phase")
phases = {
    "discover": "Discover",
    "validate": "Validate",
    "pivot": "Pivot"
}
selected_phase = st.radio("Choose your phase:", list(phases.keys()), format_func=lambda x: phases[x])
if selected_phase != st.session_state.phase:
    st.session_state.phase = selected_phase
    st.session_state.milestones = default_milestones[selected_phase]

# Progress bar
milestones = st.session_state.milestones
completed_count = sum(1 for m in milestones if m["completed"])
progress = int((completed_count / len(milestones)) * 100)
st.subheader("Your Progress")
st.progress(progress)
st.caption(f"{completed_count} of {len(milestones)} milestones completed")

# Milestone toggles
st.subheader("Milestones")
for m in milestones:
    toggled = st.checkbox(m["title"], value=m["completed"], key=m["id"])
    m["completed"] = toggled

# Affirmations
if st.session_state.affirmations:
    st.subheader("Your Affirmations")
    for a in st.session_state.affirmations:
        st.markdown(f"> 💬 *{a}*")