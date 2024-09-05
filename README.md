# 🚀 Gemma Model Document Q&A

## 📖 Overview
The **Gemma Model Document Q&A** is a project designed to read and process documents, convert them into vectors, and perform question answering based on the document's content. This project leverages several key technologies such as **Langchain**, **FAISS**, **Streamlit**, and others to enable efficient vector search and natural language understanding.
![Gemma Document Q&A Screenshot](https://github.com/adityashakya836/Gemma-Document-QA-Bot/blob/main/Screenshot%202024-09-05%20170246.png)
## ✨ Features
- 📝 **Document Processing**: Reads documents and extracts their content for processing.
- 🔍 **Vector Embedding**: Converts document text into vector representations using embedding models.
- ❓ **Question Answering**: Answers user queries by retrieving the most relevant parts of the document using vector-based search.
- 💻 **Interactive User Interface**: Provides an easy-to-use web interface via **Streamlit**.

## 🛠️ Key Technologies
- **[Faiss CPU](https://github.com/facebookresearch/faiss)**: ⚡ An efficient vector search library for performing fast similarity search.
- **[Groq](https://groq.com/)**: 🚀 High-performance hardware acceleration for AI workloads.
- **[Langchain](https://github.com/hwchase17/langchain)**: 🤖 A framework for building language model applications.
- **[PyPDF2](https://pypi.org/project/PyPDF2/)**: 📄 A library for working with PDF files, used for document reading and text extraction.
- **[Streamlit](https://streamlit.io/)**: 🌐 A Python-based framework for creating web applications, used to build the user interface for querying documents.
- **[Google GenAI](https://cloud.google.com/ai)**: 🤯 Google’s Generative AI tool, integrated for enhanced language processing.

## 📦 Dependencies

This project uses the following Python packages:
- `faiss-cpu`: ⚡ Efficient similarity search and clustering of dense vectors.
- `groq`: 🚀 For optimized AI performance on custom hardware.
- `langchain_groq`: 🤖 Langchain integration with Groq hardware.
- `PyPDF2`: 📄 To extract text data from PDF documents.
- `langchain`: 🧠 Framework for developing language models and chain-of-thought reasoning.
- `streamlit`: 🌐 To create an interactive web interface.
- `langchain_community`: 👥 Community-based extensions for Langchain.
- `pypdf`: 📂 Alternative PDF processing library for handling different PDF types.
- `langchain_google_genai`: 🔍 Integration with Google’s Generative AI models for enhanced question-answering capabilities.

## 🛠️ How It Works
1. **📥 Document Input**: Read and processed the document using **PyPDF2**.
2. **🔗 Vectorization**: The document is converted into vector embeddings using **Langchain** and **FAISS** for efficient searching.
3. **❓ Question Answering**: The user inputs a query, which is processed by the system. Relevant document sections are retrieved based on vector similarity, and the answer is provided.
4. **💻 Web Interface**: The **Streamlit** interface allows the user to interact with the system, upload documents, and ask questions.

## 🛠️ Setup
1. Clone The Repository
   ```bash
   git clone https://github.com/adityashakya836/Gemma-Document-QA-Bot.git
    cd Gemma-Document-QA-Bot
2. Create Virtual Environment
   ```bash
   python -m venv venv
3. Activate Virtual Environment
   ```bash
   venv\Scripts\activate
4. Install requirements.txt
   ```bash
   pip install requirements.txt
5. Run app.py file
   ```bash
   streamlit run app.py

## 🌱 Future Enhancements
- 📂 Adding support for more document formats (Word, Excel, etc.).
- 🤖 Expanding the language models for more precise answers.
- 🌟 Improving the interface for better user experience.
