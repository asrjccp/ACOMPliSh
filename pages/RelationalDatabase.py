import streamlit as st
from relationaldatabase import ask_GPT
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
    template=''' You are a H2 Computing Tutor in Singapore and you are teaching relational databases.
    Your role is to give a summary on {topic} and make sure its only relevant to {topic}'''
)

# Put Buttons together in Columns
col1, col2, col3 = st.columns(3)
# In Column 1
with col1:
    rd_definitions = st.button("Definitions")
if rd_definitions:
    st.markdown("**primary key:** Atoms of an element that have the **:red[same number of protons]** but **:red[different number of neutrons]**")
    #st.markdown("**foreign key**: The electrons in an atom are arranged in electronic shell")
    st.markdown("**1NF (First Normal Form)**: **no** **:red[repeating fields/groups]**")
    st.markdown("**2NF (Second Normal Form)**: **no **:red[partial key]** dependency**.")
    st.markdown("**3NF (Third Normal Form)**: **no **:red[non-key]** dependency**.")


st.divider()


# Show Prompt
#if question:
    #response = ask_GPT(question_template.format(topic = question))
    #st.write(response)


# with st.container():
#     question = st.chat_input("Enter your prompt here: ")
#     if question:
#         with st.chat_message("user"):
#             st.markdown(f"Q: {question}")
#             response = ask_GPT(question)
#             st.write(f"A: {response}")


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
