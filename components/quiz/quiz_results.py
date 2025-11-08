import streamlit as st

def render_quiz_results(results):
    phase_colors = {
        "discover": "#d946ef",  # purple-pink
        "validate": "#3b82f6",  # blue-cyan
        "pivot": "#f97316"      # orange-red
    }

    phase_messages = {
        "discover": "Explore career paths aligned with your values and strengths.",
        "validate": "Optimize your current career path and deepen your expertise.",
        "pivot": "Reinvent yourself with clarity and confidence."
    }

    color = phase_colors.get(results["recommendedPhase"], "#6b7280")
    message = phase_messages.get(results["recommendedPhase"], "Keep growing with intention.")

    # 🌟 Hero Section
    st.markdown(f"""
    <div style="text-align:center; margin-top:2rem;">
        <div style="width:96px; height:96px; margin:auto; border-radius:50%; background:{color}; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 14px rgba(0,0,0,0.2);">
            <span style="font-size:2rem; color:white;">🎯</span>
        </div>
        <h2 style="margin-top:1rem;">Your Career Profile</h2>
        <p style="font-size:1.2rem; font-weight:bold;">{results['careerProfile'].capitalize()}</p>
    </div>
    """, unsafe_allow_html=True)

    # ✨ Affirmation Card
    st.markdown(f"""
    <div style="background:{color}; color:white; padding:1rem; border-radius:10px; text-align:center; margin-top:2rem;">
        <p style="font-style:italic;">"{results['affirmation']}"</p>
    </div>
    """, unsafe_allow_html=True)

    # 🎯 Recommended Phase
    st.markdown("### Recommended Phase")
    st.markdown(f"""
    <div style="background:#f3f4f6; padding:1rem; border-radius:10px;">
        <p style="font-size:1.1rem; font-weight:bold; color:{color};">{results['recommendedPhase'].capitalize()}</p>
        <p style="color:#4b5563;">{message}</p>
    </div>
    """, unsafe_allow_html=True)

    # 💪 Top Strengths
    if results.get("topStrengths"):
        st.markdown("### Your Top Strengths")
        for strength in results["topStrengths"]:
            st.markdown(f"""
            <div style="display:flex; align-items:center; gap:0.5rem;">
                <div style="width:8px; height:8px; border-radius:50%; background:{color};"></div>
                <span>{strength}</span>
            </div>
            """, unsafe_allow_html=True)

    # 📋 Recommendations
    if results.get("recommendations"):
        st.markdown("### Next Steps")
        for i, rec in enumerate(results["recommendations"], start=1):
            st.markdown(f"""
            <div style="display:flex; align-items:flex-start; gap:0.5rem; margin-bottom:0.5rem;">
                <div style="width:24px; height:24px; border-radius:50%; background:#e0e7ff; display:flex; align-items:center; justify-content:center;">
                    <span style="font-size:0.8rem; font-weight:bold; color:#6366f1;">{i}</span>
                </div>
                <span>{rec}</span>
            </div>
            """, unsafe_allow_html=True)

    # 🚀 CTA Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start Your Journey 🚀"):
            st.switch_page("Journey")
    with col2:
        if st.button("Explore Playbook 📘"):
            st.switch_page("Playbook")