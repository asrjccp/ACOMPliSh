import streamlit as st
from cb_relationaldatabase import ask_GPT
from langchain.prompts import PromptTemplate
from PIL import Image
st.set_page_config(
    page_title = "Relational Database",
    page_icon = "💻",
)
st.title('💻 Relational Database GPT')
st.caption("Click on the buttons for all the info!")
# Template
question_template = PromptTemplate(
    input_variables=['topic'],
    template=''' You are a H2 Computing Tutor in Singapore and you are teaching {topic}.
    Your role is to give a summary on {topic} and make sure its only relevant to {topic}'''
)

# Put Buttons together in Columns
col1, col2, col3 = st.columns(3)
# In Column 1
with col1:
    rd_definitions = st.button("Definitions")
if rd_definitions:
    st.markdown("**primary key:** **:red[unique identifier]** for each record in a database table")
    st.markdown("**foreign key**: column(s) in a database table that provides a **:red[link/relationship]** between data in two tables by referencing the primary key of the source table")
    st.markdown("**1NF (First Normal Form)**: **no** **:red[repeating fields/groups]**")
    st.markdown("**2NF (Second Normal Form)**: **no **:red[partial key]** dependency**.")
    st.markdown("**3NF (Third Normal Form)**: **no **:red[non-key]** dependency**.")
    
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
    response = ask_GPT(chat_box)
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
