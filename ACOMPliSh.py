import streamlit as st
st.set_page_config(
    page_title = "ACOMPliSh Home",
    page_icon = "💻",
)

st.title("ACOMPliSh")
st.caption("Developed by: Teh Kim Wee (23/25)")
st.markdown("**About**")
st.markdown("ACOMPliSh aims to be a platform for A-level students to conveniently access and interact with H2 Computing learning content")
st.markdown("**How to use?**")
st.markdown("Open the sidebar and click on the appropriate topic")
st.sidebar.success(
    '''Click on the topic you need!
    Happy (l)earning!
    ''')