import streamlit as st
# From the Retrieval Augmented Generation Notebook
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_community.document_loaders import PyPDFLoader
from operator import itemgetter

# Load in our PDF
loader = PyPDFLoader("./documents/NoSQL.pdf")
# Split the text in the file for it to be digestible for the LLM
pages = loader.load_and_split()
# Set-Up our Vector Storage
vectorstore = FAISS.from_documents(pages, embedding = OpenAIEmbeddings())
# Retrieval Method
retriever = vectorstore.as_retriever()
# Prompt Template
template = '''
Answer the question based only on the following context
{context}

Question: {question}
'''
prompt = ChatPromptTemplate.from_template(template)
# Connection with OpenAI
llm = ChatOpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Chain
chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()

def answer_nosql(question):
    response = chain.invoke(question)
    return response