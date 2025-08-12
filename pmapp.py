import streamlit as st

# Simple password protection (change password here)
PASSWORD = "yourpassword"

def check_password():
    """Returns True if the user enters the correct password."""
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

if check_password():
    st.title("Project Espresso: Insights from the Top Team")

    st.header("Introduction")
    st.video("https://www.youtube.com/watch?v=INTRO_VIDEO_ID")
    st.write("Every day, we manage projects.")

    st.header("1st Series: Coffee & Project Traps: Brewing Success Together")
    traps = [
        ("🎯 Trap #1 – Goals as Foggy as a Rainy Morning", "VIDEO_ID_1"),
        ("⏳ Trap #2 – The “Hope-for-the-Best” Plan", "VIDEO_ID_2"),
        ("⚠️ Trap #3 – Playing Blind to Risks", "VIDEO_ID_3"),
        ("🪣 Trap #4 – Big Plans, No Resources", "VIDEO_ID_4"),
        ("❄️ Trap #5 – Scope Creep Avalanche", "VIDEO_ID_5"),
        ("🧱 Trap #6 – Talking to Walls: Communication Fail", "VIDEO_ID_6"),
        ("🤷‍♂️ Trap #7 – A Team Out of Sync", "VIDEO_ID_7"),
        ("🧩 Trap #8 – Surprise! Technical Troubles", "VIDEO_ID_8"),
        ("📉 Trap #9 – Skipping Checkpoints & Deliverables", "VIDEO_ID_9"),
        ("🎂 Trap #10 – The Final Product Flop", "VIDEO_ID_10"),
    ]
    for title, vid in traps:
        st.subheader(title)
        st.video(f"https://www.youtube.com/watch?v={vid}")

    st.header("2nd Series: Café Success: 5 Essential Tips for Project Mastery")
    tips = [
        ("Tip 1", "TIP_VIDEO_ID_1"),
        ("Tip 2", "TIP_VIDEO_ID_2"),
        ("Tip 3", "TIP_VIDEO_ID_3"),
        ("Tip 4", "TIP_VIDEO_ID_4"),
        ("Tip 5", "TIP_VIDEO_ID_5"),
    ]
    for title, vid in tips:
        st.subheader(title)
        st.video(f"https://www.youtube.com/watch?v={vid}")

    st.header("3rd Series: Coffee Break Case Studies: Real Projects, Real Lessons")
    case_studies = [
        ("Case Study 1", "CASE_VIDEO_ID_1"),
        ("Case Study 2", "CASE_VIDEO_ID_2"),
        ("Case Study 3", "CASE_VIDEO_ID_3"),
    ]
    for title, vid in case_studies:
        st.subheader(title)
        st.video(f"https://www.youtube.com/watch?v={vid}")

    st.header("4th Series: Coffee Break Roadmap: Navigating Your Project to Success")
    roadmap = [
        ("Roadmap Part 1", "ROADMAP_VIDEO_ID_1"),
        ("Roadmap Part 2", "ROADMAP_VIDEO_ID_2"),
        ("Roadmap Part 3", "ROADMAP_VIDEO_ID_3"),
    ]
    for title, vid in roadmap:
        st.subheader(title)
        st.video(f"https://www.youtube.com/watch?v={vid}")

    st.markdown("---")
    st.caption("© 2025 Your Company Name - Internal Use Only")
