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
    st.title("Project Espresso: Coffee & Project Traps: Brewing Success Together")

    traps = [
        ("🎯 Trap #1 – Goals as Foggy as a Rainy Morning (Done)", "https://www.canva.com/design/your_canva_video_embed_link_1"),
        ("⏳ Trap #2 – The “Hope-for-the-Best” Plan (Done)", "https://www.canva.com/design/your_canva_video_embed_link_2"),
        ("⚠️ Trap #3 – Playing Blind to Risks (Done)", "https://www.canva.com/design/your_canva_video_embed_link_3"),
        ("🪣 Trap #4 – Big Plans, No Resources (Done)", "https://www.canva.com/design/your_canva_video_embed_link_4"),
        ("❄️ Trap #5 – Scope Creep Avalanche (Done)", "https://www.canva.com/design/your_canva_video_embed_link_5"),
        ("🧱 Trap #6 – Talking to Walls: Communication Fail (Done)", "https://www.canva.com/design/your_canva_video_embed_link_6"),
        ("🤷‍♂️ Trap #7 – A Team Out of Sync (Done)", "https://www.canva.com/design/your_canva_video_embed_link_7"),
        ("🧩 Trap #8 – Surprise! Technical Troubles", "https://www.canva.com/design/your_canva_video_embed_link_8"),
        ("📉 Trap #9 – Skipping Checkpoints & Deliverables", "https://www.canva.com/design/your_canva_video_embed_link_9"),
        ("🎂 Trap #10 – The Final Product Flop", "https://www.canva.com/design/your_canva_video_embed_link_10"),
    ]

    for i, (title, url) in enumerate(traps):
        display_video_section(title, url, key=f"trap_{i}")
        if i < len(traps) - 1:
            arrow()

    st.markdown("---")
    st.caption("© 2025 Your Company Name - Internal Use Only")
