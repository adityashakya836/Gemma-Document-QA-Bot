import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
import json
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyPDFDirectoryLoader, Docx2txtLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

config_file_path = 'config.json'

# Open and read the JSON file
with open(config_file_path, 'r') as file:
    config_data = json.load(file)

# Load GROQ and Google API Key from the json file
GOOGLE_API_KEY = config_data['GOOGLE_API_KEY']
GROQ_API_KEY = config_data['GROQ_API_KEY']

st.title("Gemma Model Document Q&A")

llm = ChatGroq(groq_api_key = GROQ_API_KEY, model_name = 'Gemma-7b-it')

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only. 
    Please provide the most accurate response based on the question 
    <context>
    {context}
    <context>
    Questions: {input}
    """
)

def vector_embeddings():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model ='models/embedding-001', google_api_key = GOOGLE_API_KEY)
        st.session_state.loader = PyPDFDirectoryLoader("./data")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

prompt1 = st.text_input("What you want to ask from the documents")

if st.button("Creating Vector Store"):
    vector_embeddings()
    st.write("Vector Store DB is ready")

import time
if prompt1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrievar = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retrievar, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    st.write(response['answer'])

    # With a streamit expander
    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write('----------------------------------')