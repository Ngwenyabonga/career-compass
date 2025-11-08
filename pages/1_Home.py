import streamlit as st
from components.quiz.quiz_card import render_quiz_card
from components.quiz.quiz_results import render_quiz_results
from components.journey.journey_timeline import render_journey_timeline
from components.playbook.playbook_card import render_playbook_card
from components.home.kingdom_quote_carousel import render_kingdom_quote

# 🔧 Page config
st.set_page_config(page_title="JoyTee Academy", page_icon="👑", layout="wide")

# 🌿 Branding Background
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom right, #d4edda, #fdf6e3);
}
.main {
    background-color: transparent;
}
</style>
""", unsafe_allow_html=True)

# 🎨 Welcome Banner
st.markdown("""
<div style='background: linear-gradient(to right, #a2cf9b, #f7e9b7); padding: 1rem; border-radius: 10px; color: #333; text-align: center; font-weight: bold;'>
  <h2>Welcome back, Bonga 👑</h2>
  <p>Building Your Kingdom of Excellence — Powered by JoyTee Holdings</p>
</div>
""", unsafe_allow_html=True)

# 💬 Quote Carousel
render_kingdom_quote()

# 🎮 Career Progress
st.markdown("### 🎮 Career Progress")
st.progress(0.5, text="200 XP until level 3")
st.write("Career Level: 2")
st.write("Total XP: 200 / 400")

# 🚀 Your Next Move
st.markdown("### 🚀 Your Next Move")
st.write("Let’s find your career phase and unlock your next step.")

# 🧠 Quiz Section
if "selected_answer" not in st.session_state:
    st.session_state["selected_answer"] = None

question = {
    "id": "q1",
    "question": "What motivates you most in your career?",
    "options": [
        {"label": "Growth & Learning", "value": "growth"},
        {"label": "Stability & Security", "value": "stability"},
        {"label": "Freedom & Flexibility", "value": "freedom"},
        {"label": "Impact & Legacy", "value": "legacy"}
    ]
}

results = {
    "careerProfile": "visionary",
    "recommendedPhase": "pivot",
    "affirmation": "You were made for more — rise and reign.",
    "topStrengths": ["Creative thinking", "Resilience", "Empathy"],
    "recommendations": [
        "Reflect on your values and redefine your goals.",
        "Update your CV and LinkedIn to match your new direction.",
        "Explore new industries or roles that align with your strengths."
    ]
}

def handle_answer(question_id, answer_value):
    st.session_state["selected_answer"] = answer_value

if st.session_state["selected_answer"] is None:
    render_quiz_card(question, st.session_state["selected_answer"], handle_answer)
else:
    render_quiz_results(results)

# 🛤️ Journey Timeline
st.markdown("### 🛤️ Your Journey")
render_journey_timeline({
    "milestones": [
        {"title": "Completed Quiz", "completed": True},
        {"title": "Defined Career Profile", "completed": True},
        {"title": "Explored Playbook", "completed": False},
        {"title": "Scheduled Coaching", "completed": False}
    ]
})

# 📘 Playbook CTA
render_playbook_card()

# 🔗 Top Navigation Buttons
st.markdown("""
<style>
.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
}
.gradient-button {
    background: linear-gradient(to right, #a2cf9b, #f7e9b7);
    color: #333;
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1rem;
    cursor: pointer;
    transition: transform 0.2s ease;
}
.gradient-button:hover {
    transform: scale(1.05);
}
</style>
<div class="button-container">
    <form action="pages/3_Journey.py"><button class="gradient-button">🛤️ Journey</button></form>
    <form action="pages/4_Playbook.py"><button class="gradient-button">📘 Playbook</button></form>
    <form action="pages/5_Profile.py"><button class="gradient-button">👤 Profile</button></form>
    <form action="pages/6_Resources.py"><button class="gradient-button">📚 Resources</button></form>
    <form action="pages/10_Contact.py"><button class="gradient-button">💬 Contact</button></form>
</div>
""", unsafe_allow_html=True)