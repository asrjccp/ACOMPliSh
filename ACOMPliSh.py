import streamlit as st
st.set_page_config(
    page_title = "ACOMPliSh Home",
    page_icon = "💻",
)

st.title("ACOMPliSh")
st.caption("Credits: Initiated and developed by Mr Teh Kim Wee, alumni, Anderson Serangoon Junior College (class of 23/25)")
st.markdown("**About**")
st.markdown("ACOMPliSh aims to be a platform for A-level students to conveniently access and interact with H2 Computing learning content.")
st.markdown("**How to use?**")
st.markdown("Click on the appropriate topic on the left sidebar.")
st.sidebar.success(
    '''Happy (l)earning!
    ''')