import streamlit as st

# 🔧 Page config
st.set_page_config(
    page_title="JoyTee Academy",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🌿 JoyTee Branding Background
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
  <h2>Welcome to JoyTee Academy 👑</h2>
  <p>Leaving a Footprint of Excellence — Powered by JoyTee Holdings</p>
</div>
""", unsafe_allow_html=True)

# 🔄 Scrolling Motivation Banner
st.markdown("""
<style>
.marquee {
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
  box-sizing: border-box;
  animation: marquee 15s linear infinite;
  font-size: 1.1rem;
  color: #444;
  background: #fff8dc;
  padding: 0.75rem;
  border-radius: 8px;
  margin-bottom: 1rem;
}
@keyframes marquee {
  0%   { transform: translateX(100%); }
  100% { transform: translateX(-100%); }
}
</style>
<div class="marquee">
  💬 Excellence is not a destination — it's a continuous journey. Your career is your kingdom. Build it with intention and integrity.
</div>
""", unsafe_allow_html=True)

# 🧭 Gradient Navigation Buttons
st.markdown("""
<style>
.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-top: 1rem;
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
    <form action="pages/1_Home.py"><button class="gradient-button">🏠 Home</button></form>
    <form action="pages/2_Quiz.py"><button class="gradient-button">🧠 Quiz</button></form>
    <form action="pages/3_Journey.py"><button class="gradient-button">🛤️ Journey</button></form>
    <form action="pages/4_Playbook.py"><button class="gradient-button">📘 Playbook</button></form>
    <form action="pages/5_Profile.py"><button class="gradient-button">👤 Profile</button></form>
    <form action="pages/6_Resources.py"><button class="gradient-button">📚 Resources</button></form>
    <form action="pages/10_Contact.py"><button class="gradient-button">💬 Contact</button></form>
</div>
""", unsafe_allow_html=True)