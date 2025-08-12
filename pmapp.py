import streamlit as st

# Simple password protection (change password here)
PASSWORD = "yourpassword"

def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if not st.session_state.password_correct:
        pwd = st.text_input("Enter password to access the portal:", type="password")
        if pwd == PASSWORD:
            st.session_state.password_correct = True
            st.experimental_rerun()
        elif pwd:
            st.error("Incorrect password")
        return False
    else:
        return True

def display_video_section(title, video_url, key):
    # Use Streamlit expander for toggle effect
    with st.expander(title, expanded=False):
        # Embed Canva video iframe
        st.markdown(
            f"""
            <iframe src="{video_url}" width="700" height="400" frameborder="0" allowfullscreen></iframe>
            """,
            unsafe_allow_html=True,
        )

def arrow():
    # Simple arrow icon between sections
    st.markdown(
        """
        <div style="text-align:center; font-size: 2em; margin: 10px 0;">⬇️</div>
        """,
        unsafe_allow_html=True,
    )

if check_password():
    st.title("Project Espresso: Insights from the Top Team")

    # Example data: Replace with your actual Canva embed URLs
    videos = [
        {
            "title": "Introduction: Every day, we manage projects.",
            "url": "https://www.canva.com/design/your_canva_video_embed_link_1",
        },
        {
            "title": "1st Series: Coffee & Project Traps: Brewing Success Together",
            "url": "https://www.canva.com/design/your_canva_video_embed_link_2",
        },
        {
            "title": "2nd Series: Café Success: 5 Essential Tips for Project Mastery",
            "url": "https://www.canva.com/design/your_canva_video_embed_link_3",
        },
        {
            "title": "3rd Series: Coffee Break Case Studies: Real Projects, Real Lessons",
            "url": "https://www.canva.com/design/your_canva_video_embed_link_4",
        },
        {
            "title": "4th Series: Coffee Break Roadmap: Navigating Your Project to Success",
            "url": "https://www.canva.com/design/your_canva_video_embed_link_5",
        },
    ]

    for i, video in enumerate(videos):
        display_video_section(video["title"], video["url"], key=f"video_{i}")
        if i < len(videos) - 1:
            arrow()

    st.markdown("---")
    st.caption("© 2025 Your Company Name - Internal Use Only")
