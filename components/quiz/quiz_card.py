import streamlit as st

def render_quiz_card(question, selected_answer, on_answer_callback):
    st.markdown(f"""
    <div style="background: linear-gradient(to right, #14b8a6, #06b6d4); padding: 1rem; border-radius: 10px; color: white;">
        <h2 style="margin: 0;">{question['question']}</h2>
    </div>
    """, unsafe_allow_html=True)

    for index, option in enumerate(question["options"]):
        is_selected = selected_answer == option["value"]
        button_style = f"""
        background: {'linear-gradient(to right, #14b8a6, #06b6d4)' if is_selected else '#f9fafb'};
        color: {'white' if is_selected else '#111827'};
        padding: 1rem;
        border-radius: 12px;
        margin-top: 0.5rem;
        width: 100%;
        text-align: left;
        font-weight: bold;
        border: none;
        box-shadow: {'0 4px 14px rgba(0,0,0,0.1)' if is_selected else 'none'};
        """

        # Use a unique key for each button
        if st.button(option["label"], key=f"{question['id']}_{option['value']}", help=option["label"]):
            on_answer_callback(question["id"], option["value"])

        # Show visual feedback
        if is_selected:
            st.markdown(f"<span style='color: #14b8a6;'>✅ Selected: {option['label']}</span>", unsafe_allow_html=True)