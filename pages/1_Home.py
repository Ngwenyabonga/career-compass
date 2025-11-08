import streamlit as st
import random
from datetime import datetime

# Simulated user and progress data (replace with real backend/API later)
user = {"full_name": "Bonga Ngwenya"}
quiz_progress = {"completed": True, "current_step": 7}
journey = {
    "milestones": [
        {"completed": True, "title": "Completed CV", "completed_date": "2025-10-01", "id": 1},
        {"completed": True, "title": "Updated LinkedIn", "completed_date": "2025-10-05", "id": 2},
        {"completed": False, "title": "Scheduled Interview", "completed_date": None, "id": 3}
    ],
    "phase": "Growth"
}

# Motivational quotes
motivational_quotes = [
    "Excellence is not a destination, it's a continuous journey.",
    "Your career is your kingdom—build it with intention and integrity.",
    "Success is the sum of small efforts repeated day in and day out.",
    "The future belongs to those who prepare for it today.",
    "Your potential is limitless when you commit to growth."
]
quote = random.choice(motivational_quotes)

# XP and Level logic
def calculate_level():
    milestones_completed = sum(1 for m in journey["milestones"] if m["completed"])
    quiz_completed = 1 if quiz_progress["completed"] else 0
    return (milestones_completed + quiz_completed) // 2 + 1

def calculate_xp():
    milestones_completed = sum(1 for m in journey["milestones"] if m["completed"])
    quiz_xp = 100 if quiz_progress["completed"] else quiz_progress["current_step"] * 10
    return milestones_completed * 50 + quiz_xp

level = calculate_level()
current_xp = calculate_xp()
next_level_xp = level * 200
xp_progress = int((current_xp / next_level_xp) * 100)

# Next best step logic
def get_next_best_step():
    if not quiz_progress or not quiz_progress["completed"]:
        return {
            "title": "Discover Your Career Path",
            "description": "Take the 10-minute clarity quiz to unlock your profile",
            "action": "Start Quiz",
            "link": "Quiz"
        }
    if not journey or sum(1 for m in journey["milestones"] if m["completed"]) == 0:
        return {
            "title": "Begin Your Transformation",
            "description": "Track your progress and earn rewards",
            "action": "View Journey",
            "link": "Journey"
        }
    return {
        "title": "Master Career Skills",
        "description": "Explore playbook modules and level up",
        "action": "Open Playbook",
        "link": "Playbook"
    }

next_step = get_next_best_step()

# Layout
st.title(f"Welcome back, {user['full_name'].split()[0]}! 👑")
st.subheader("Building Your Kingdom of Excellence")

# Gamification stats
st.markdown(f"**Career Level:** {level}")
st.markdown(f"**Total XP:** {current_xp} / {next_level_xp}")
st.progress(xp_progress)
st.caption(f"{next_level_xp - current_xp} XP until level {level + 1}")

# Motivational quote
st.markdown(f"> 💬 *{quote}*")

# Next best step CTA
st.markdown("### 🚀 Your Next Move")
st.info(f"**{next_step['title']}**\n\n{next_step['description']}")
st.button(next_step["action"], on_click=lambda: st.switch_page(next_step["link"]))

# Career Dashboard
st.markdown("## 📊 Your Career Dashboard")
cols = st.columns(3)

with cols[0]:
    milestones = sum(1 for m in journey["milestones"] if m["completed"])
    st.metric("Milestones Achieved", milestones)
    st.button("View Journey", on_click=lambda: st.switch_page("Journey"))

with cols[1]:
    st.metric("Current Phase", journey.get("phase", "Start"))
    st.button("Continue", on_click=lambda: st.switch_page("Journey"))

with cols[2]:
    profile_strength = "100%" if quiz_progress["completed"] else "0%"
    st.metric("Profile Complete", profile_strength)
    st.button("Take Quiz" if not quiz_progress["completed"] else "Retake Quiz", on_click=lambda: st.switch_page("Quiz"))

# Recent Achievements
completed_milestones = [m for m in journey["milestones"] if m["completed"]]
if completed_milestones:
    st.markdown("## 🏆 Recent Achievements")
    for m in completed_milestones[:3]:
        date = datetime.strptime(m["completed_date"], "%Y-%m-%d").strftime("%d %b %Y")
        st.success(f"**{m['title']}** — Completed on {date} (+50 XP)")