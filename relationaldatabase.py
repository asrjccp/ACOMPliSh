from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
# from apikey import apikey
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Read the PDF File:
reader = PdfReader("./documents/RelationalDatabase.pdf")

# Read Data from Text:
raw_text = ''

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

# Split Text Data:
text_splitter = CharacterTextSplitter(
    separator= "\n",
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function = len
)
texts = text_splitter.split_text(raw_text)

# OpenAI Embeddings
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(texts, embeddings)

# Chain with LangChain
llm = ChatOpenAI(temperature=0.0, openai_api_key = st.secrets("OPENAI_API_KEY"))
chain = load_qa_chain(llm = llm, chain_type="stuff")

# Ask Questions
def ask_GPT(question):
    query = question
    docs = docsearch.similarity_search(query)
    response = chain.run(input_documents = docs, question=query)
    return response
