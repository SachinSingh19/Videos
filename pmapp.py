import streamlit as st

# Password protection (change password here)
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

def display_video(title, video_url):
    with st.expander(title, expanded=False):
        st.markdown(
            f"""
            <iframe src="{video_url}" width="700" height="400" frameborder="0" allowfullscreen></iframe>
            """,
            unsafe_allow_html=True,
        )

def arrow():
    st.markdown(
        """
        <div style="text-align:center; font-size: 2em; margin: 10px 0;">⬇️</div>
        """,
        unsafe_allow_html=True,
    )

if check_password():
    st.title("Project Espresso: Insights from the Top Team")
    st.markdown("---")

    # 1. Introduction
    st.header("1. Introduction")
    display_video(
        "Every day, we manage projects. (Done)",
        "https://www.youtube.com/embed/INTRO_VIDEO_ID"  # Replace with your video URL
    )
    arrow()

    # 2. 1st Series: Coffee & Project Traps
    st.header("2. Video Series: 1st series: Coffee & Project Traps: Brewing Success Together")
    traps = [
        ("🎯 Trap #1 – Goals as Foggy as a Rainy Morning (Done)", "https://www.youtube.com/embed/VIDEO_ID_1"),
        ("⏳ Trap #2 – The “Hope-for-the-Best” Plan (Done)", "https://www.youtube.com/embed/VIDEO_ID_2"),
        ("⚠️ Trap #3 – Playing Blind to Risks (Done)", "https://www.youtube.com/embed/VIDEO_ID_3"),
        ("🪣 Trap #4 – Big Plans, No Resources (Done)", "https://www.youtube.com/embed/VIDEO_ID_4"),
        ("❄️ Trap #5 – Scope Creep Avalanche (Done)", "https://www.youtube.com/embed/VIDEO_ID_5"),
        ("🧱 Trap #6 – Talking to Walls: Communication Fail (Done)", "https://www.youtube.com/embed/VIDEO_ID_6"),
        ("🤷‍♂️ Trap #7 – A Team Out of Sync (Done)", "https://www.youtube.com/embed/VIDEO_ID_7"),
        ("🧩 Trap #8 – Surprise! Technical Troubles", "https://www.youtube.com/embed/VIDEO_ID_8"),
        ("📉 Trap #9 – Skipping Checkpoints & Deliverables", "https://www.youtube.com/embed/VIDEO_ID_9"),
        ("🎂 Trap #10 – The Final Product Flop", "https://www.youtube.com/embed/VIDEO_ID_10"),
    ]
    for i, (title, url) in enumerate(traps):
        display_video(title, url)
        if i < len(traps) - 1:
            arrow()
    arrow()

    # 3. 2nd Series: Café Success
    st.header('3. Video Series: 2nd series: "Café Success: 5 Essential Tips for Project Mastery"')
    cafe_success_videos = [
        ("Tip 1", "https://www.youtube.com/embed/CAFE_VIDEO_ID_1"),
        ("Tip 2", "https://www.youtube.com/embed/CAFE_VIDEO_ID_2"),
        ("Tip 3", "https://www.youtube.com/embed/CAFE_VIDEO_ID_3"),
        ("Tip 4", "https://www.youtube.com/embed/CAFE_VIDEO_ID_4"),
        ("Tip 5", "https://www.youtube.com/embed/CAFE_VIDEO_ID_5"),
    ]
    for i, (title, url) in enumerate(cafe_success_videos):
        display_video(title, url)
        if i < len(cafe_success_videos) - 1:
            arrow()
    arrow()

    # 4. 3rd Series: Coffee Break Case Studies
    st.header('4. Video Series: 3rd series: Coffee Break Case Studies: Real Projects, Real Lessons')
    case_studies = [
        ("Case Study 1", "https://www.youtube.com/embed/CASE_VIDEO_ID_1"),
        ("Case Study 2", "https://www.youtube.com/embed/CASE_VIDEO_ID_2"),
        ("Case Study 3", "https://www.youtube.com/embed/CASE_VIDEO_ID_3"),
    ]
    for i, (title, url) in enumerate(case_studies):
        display_video(title, url)
        if i < len(case_studies) - 1:
            arrow()
    arrow()

    # 5. 4th Series: Coffee Break Roadmap
    st.header('5. Video Series: 4th series: "Coffee Break Roadmap: Navigating Your Project to Success"')
    roadmap_videos = [
        ("Roadmap Part 1", "https://www.youtube.com/embed/ROADMAP_VIDEO_ID_1"),
        ("Roadmap Part 2", "https://www.youtube.com/embed/ROADMAP_VIDEO_ID_2"),
        ("Roadmap Part 3", "https://www.youtube.com/embed/ROADMAP_VIDEO_ID_3"),
    ]
    for i, (title, url) in enumerate(roadmap_videos):
        display_video(title, url)
        if i < len(roadmap_videos) - 1:
            arrow()

    st.markdown("---")
    st.caption("© 2025 Your Company Name - Internal Use Only")
