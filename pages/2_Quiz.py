import streamlit as st

# Simulated user and progress (replace with real backend/API later)
user = {"full_name": "Bonga Ngwenya", "email": "bonga@example.com"}
quiz_questions = [
    {"id": 1, "question": "What motivates you most in your work?", "options": ["Impact", "Creativity", "Growth", "Stability"]},
    {"id": 2, "question": "How do you prefer to work?", "options": ["Independently", "In teams", "Leading others", "Flexible/varied"]},
    {"id": 3, "question": "What's your ideal work environment?", "options": ["Office", "Remote", "Hybrid", "Field"]},
    {"id": 4, "question": "Which best describes your current career satisfaction?", "options": ["Fulfilled", "Satisfied", "Unsure", "Unfulfilled"]},
    {"id": 5, "question": "What's most important for your career growth?", "options": ["Skills", "Network", "Recognition", "Purpose"]},
    {"id": 6, "question": "How do you handle career challenges?", "options": ["Analytical", "Intuitive", "Seek help", "Adapt"]},
    {"id": 7, "question": "What's your biggest career concern right now?", "options": ["Direction", "Stagnation", "Balance", "Passion"]},
    {"id": 8, "question": "How would you describe your ideal career path?", "options": ["Linear", "Diverse", "Entrepreneurial", "Exploratory"]},
    {"id": 9, "question": "What's your relationship with change?", "options": ["Embrace", "Cautious", "Resist", "Depends"]},
    {"id": 10, "question": "If you could start over, what would you do differently?", "options": ["Follow passion", "Take risks", "Nothing", "Seek guidance"]}
]

# Session state
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "completed" not in st.session_state:
    st.session_state.completed = False

# Result logic
def calculate_results(answers):
    satisfaction = answers.get(4)
    concern = answers.get(7)
    change_attitude = answers.get(9)

    recommended_phase = "discover"
    career_profile = "explorer"
    affirmation = "You're on the path to career clarity."

    if satisfaction == "Unfulfilled" or concern == "Stagnation":
        recommended_phase = "pivot"
        career_profile = "transformer"
        affirmation = "It takes courage to reinvent yourself. You're brave."
    elif satisfaction in ["Satisfied", "Fulfilled"]:
        recommended_phase = "validate"
        career_profile = "optimizer"
        affirmation = "You're building on a solid foundation."

    return {
        "recommended_phase": recommended_phase,
        "career_profile": career_profile,
        "affirmation": affirmation,
        "top_strengths": ["Growth-oriented", "Self-aware", "Action-taker"],
        "recommendations": [
            "Explore career paths aligned with your values",
            "Connect with mentors in your field of interest",
            "Develop skills through online courses"
        ]
    }

# Completion screen
if st.session_state.completed:
    st.success("🎉 Quiz Complete!")
    results = calculate_results(st.session_state.answers)
    st.markdown(f"**Career Profile:** {results['career_profile']}")
    st.markdown(f"**Recommended Phase:** {results['recommended_phase']}")
    st.markdown(f"💬 *{results['affirmation']}*")
    st.markdown("### 🔝 Top Strengths")
    for s in results["top_strengths"]:
        st.write(f"- {s}")
    st.markdown("### 🎯 Recommendations")
    for r in results["recommendations"]:
        st.write(f"- {r}")
    if st.button("Retake Quiz"):
        st.session_state.current_step = 0
        st.session_state.answers = {}
        st.session_state.completed = False
    st.stop()

# Quiz flow
current_index = st.session_state.current_step
question = quiz_questions[current_index]
st.markdown(f"**Question {current_index + 1} of {len(quiz_questions)}**")
st.progress((current_index + 1) / len(quiz_questions))
answer = st.radio(question["question"], question["options"], key=f"q_{question['id']}")

# Navigation
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⬅️ Back") and current_index > 0:
        st.session_state.current_step -= 1
with col2:
    if st.button("➡️ Next") and answer:
        st.session_state.answers[question["id"]] = answer
        if current_index < len(quiz_questions) - 1:
            st.session_state.current_step += 1
        else:
            st.session_state.completed = True