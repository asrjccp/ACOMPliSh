import streamlit as st
st.set_page_config(
    page_title = "ACOMPliSh Home",
    page_icon = "💻",
)

st.title(":rainbow[🐉 ACOMPliSh🐉]")
st.caption("Developed by Mr Teh Kim Wee (class of 23/25), Anderson Serangoon Junior College.")
st.markdown("**About:**")
st.markdown("ACOMPliSh aims to be a platform for A-level students to conveniently access and interact with H2 Computing learning content.")
st.markdown("**How to use?**")
st.markdown("Click on the appropriate topic on the left sidebar and profit :)")
st.sidebar.success(
    '''Happy (l)earning!
    ''')
