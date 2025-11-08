import streamlit as st
from datetime import datetime

# Simulated data (replace with real backend/API later)
trend_reports = [
    {
        "id": 1,
        "title": "Tech Hiring Trends",
        "description": "Latest insights into tech recruitment",
        "month": "October",
        "cover_image": "",
        "key_insights": ["Remote roles are rising", "AI skills in high demand"],
        "file_url": "#"
    }
]

resource_links = [
    {
        "id": 1,
        "title": "LinkedIn Learning",
        "description": "Courses for career development",
        "type": "course",
        "category": "skills_development",
        "is_free": True,
        "url": "https://linkedin.com/learning"
    }
]

# Search input
st.title("📚 Career Resources")
search_query = st.text_input("🔍 Search resources...")

# Tabs
tab = st.radio("Choose resource type:", ["CV Templates", "Newsletters", "Trend Reports", "External Links"])

# Trend Reports
if tab == "Trend Reports":
    filtered = [
        r for r in trend_reports
        if search_query.lower() in r["title"].lower() or search_query.lower() in r["month"].lower()
    ]
    st.subheader("📈 Career Trends")
    if filtered:
        for r in filtered:
            st.markdown(f"### {r['title']}")
            st.write(f"🗓️ Month: `{r['month']}`")
            st.write(r["description"])
            if r.get("key_insights"):
                st.markdown("**Key Insights:**")
                for insight in r["key_insights"][:2]:
                    st.write(f"- {insight}")
            st.link_button("Download Report", r["file_url"])
            st.divider()
    else:
        st.info("No trend reports available yet.")

# External Links
if tab == "External Links":
    filtered = [
        l for l in resource_links
        if search_query.lower() in l["title"].lower() or search_query.lower() in l["description"].lower()
    ]
    st.subheader("🌐 External Resources")
    if filtered:
        for l in filtered:
            st.markdown(f"### {l['title']}")
            st.write(l["description"])
            st.write(f"Type: `{l['type'].capitalize()}` | Category: `{l['category'].replace('_', ' ').capitalize()}`")
            if l["is_free"]:
                st.success("✅ Free Resource")
            st.link_button("Visit Resource", l["url"])
            st.divider()
    else:
        st.info("No external resources available yet.")