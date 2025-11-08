import streamlit as st

# Simulated module data (replace with real backend/API later)
modules = [
    {"id": 1, "title": "Build a Skills Matrix", "category": "skills", "completed": True},
    {"id": 2, "title": "Expand Your Network", "category": "networking", "completed": False},
    {"id": 3, "title": "Optimize Your Resume", "category": "resume", "completed": False},
    {"id": 4, "title": "Ace the Interview", "category": "interview", "completed": True},
    {"id": 5, "title": "Mindset Reset", "category": "mindset", "completed": False},
    {"id": 6, "title": "Career Strategy Map", "category": "strategy", "completed": True}
]

categories = ["all", "skills", "networking", "resume", "interview", "mindset", "strategy"]

# Session state
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "all"

# Header
st.title("📘 Career Playbook")
st.caption("Your step-by-step guide to career success")

# Progress
completed_count = sum(1 for m in modules if m["completed"])
st.subheader("Modules Completed")
st.markdown(f"**{completed_count} / {len(modules)}**")
st.progress(int((completed_count / len(modules)) * 100))

# Category filter
st.subheader("Filter by Category")
selected = st.selectbox("Choose category", categories, index=categories.index(st.session_state.selected_category))
st.session_state.selected_category = selected

# Filtered modules
filtered_modules = modules if selected == "all" else [m for m in modules if m["category"] == selected]

# Module cards
st.subheader("Modules")
if filtered_modules:
    for m in filtered_modules:
        with st.expander(f"{m['title']}"):
            st.write(f"Category: **{m['category'].capitalize()}**")
            st.checkbox("Mark as complete", value=m["completed"], key=f"module_{m['id']}")
else:
    st.info("No modules in this category yet.")