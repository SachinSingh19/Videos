import streamlit as st

# Inject CSS for animated gradient background
def add_animated_background():
    st.markdown(
        """
        <style>
        /* Full page animated gradient background */
        body {
            margin: 0;
            height: 100vh;
            background: linear-gradient(-45deg, #6f4e37, #d2b48c, #8b5e3c, #f4f1ea);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: #333;
        }

        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        /* Make Streamlit container background transparent */
        .css-18e3th9 {
            background: transparent !important;
        }

        /* Style headers and text for better contrast */
        h1, h2, h3, .st-expanderHeader {
            color: #3e2f1c !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Style expander content background */
        .st-expander > div {
            background-color: rgba(255, 255, 255, 0.85) !important;
            border-radius: 8px;
            padding: 10px;
        }

        /* Style arrows */
        .arrow {
            text-align: center;
            font-size: 2em;
            margin: 10px 0;
            color: #6f4e37;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
            <iframe src="{video_url}" width="700" height="400" frameborder="0" allowfullscreen allow="fullscreen"></iframe>
            """,
            unsafe_allow_html=True,
        )

def arrow():
    st.markdown(
        '<div class="arrow">⬇️</div>',
        unsafe_allow_html=True,
    )

# Main app
add_animated_background()

if check_password():
    st.title("Project Espresso: Insights from the Top Team")
    st.markdown("---")

    # 1. Introduction (Canva video embed)
    st.header("1. Introduction")
    st.markdown(
        """
        <iframe src="https://www.canva.com/design/DAGqb3TtBiA/aeKE3oOyH8D3sy6f-tW-UA/embed" 
        width="700" height="400" frameborder="0" allowfullscreen allow="fullscreen"></iframe>
        """,
        unsafe_allow_html=True,
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
        if i < len(traps)
