import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_community.document_loaders import PyPDFLoader
from operator import itemgetter

# Use st.cache_data to cache the PDF loading and processing
@st.cache_resource
def load_and_split_pdf(path):
    loader = PyPDFLoader(path)
    pages = loader.load_and_split()
    return pages

# Use st.cache_data to cache the vector storage creation process
@st.cache_resource
def create_vector_storage(_documents):
    vectorstore = FAISS.from_documents(_documents, embedding=OpenAIEmbeddings(model="text-embedding-3-small"))
    return vectorstore

# Load, process, and create vector storage for your PDF document
pdf_path = "./documents/Relational Database.pdf"
pages = load_and_split_pdf(pdf_path)
vectorstore = create_vector_storage(pages)

# Retrieval method setup remains unchanged
retriever = vectorstore.as_retriever()

# Prompt Template
template = '''
Answer the question based only on the following context
{context}

Question: {question}
'''
prompt = ChatPromptTemplate.from_template(template)

# Connect to OpenAI (Consider sensitive data handling best practices for API keys)
llm = ChatOpenAI(api_key=st.secrets["OPENAI_API_KEY"], model="gpt-4-0125-preview")

# Define the processing chain
chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()

def answer_relational_database(question):
    response = chain.invoke(question)
    return response
