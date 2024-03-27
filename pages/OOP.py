import streamlit as st
from cb_oop import answer_oop
from PIL import Image
st.set_page_config(
    page_title = "Object-Oriented Programming",
    page_icon = "💻",
)
st.title('💻 OOP Computing tutor')
st.caption("Ask me anything! :)")

col1, col2, col3 = st.columns(3)

# In Column 1 (Definition)
with col1:
    pt_definitions = st.button("Definitions")
if pt_definitions:
    st.markdown("**class:** **:red[blueprint/template]** for creating objects")
    st.markdown("**object**: **:red[runtime instantiation]** of a class")
    st.markdown("**encapsulation**: **bundling of data and methods within a class entity;** **:red[private data]** are accessible via **:red[public methods]**")
    st.markdown("**inheritance**: **ability of a **:red[subclass]** to **:red[adopt data and methods]** from a **:red[superclass]**; **:red[subclass can define its own data and method]**")
    st.markdown("**polymorphism**: ability to **:red[invoke different methods]** in different classes **:red[using the same name]** at **:red[program runtime]**")
    
st.divider()

# Initialise a state to keep track of person response"
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

chat_box = st.chat_input("Enter your question")
if chat_box:
    with st.chat_message("user"):
        st.markdown(chat_box)
    st.session_state.messages.append({"role": "user", "content": chat_box})
    response = answer_oop(chat_box)
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
