from dotenv import load_dotenv, find_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import openai
import os
from tools.llm import LlmEngine


def get_pdf_text(pdf):
  pdf_reader = PdfReader(pdf)
  text = ""
  for page in pdf_reader.pages:
    text += page.extract_text()
  return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        # chunk_size=768,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""],
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# # 保存
# def save_vector_store(textChunks):
#     db = FAISS.from_texts(textChunks, OpenAIEmbeddings())
#     db.save_local('faiss')
 
 
# # 加载
# def load_vector_store():
#     return FAISS.load_local('faiss', OpenAIEmbeddings())

def st_first():
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")



def main():
  st_first()
  # upload file
  pdf = st.file_uploader("Upload your PDF", type="pdf")
  openai.api_key = get_openai_key()
  print(openai.api_key)
  if pdf is not None:
    text = get_pdf_text(pdf)
    chunks = get_text_chunks(text)
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    user_question = st.text_input("Ask a question about your PDF:")
    if user_question:

        docs = knowledge_base.similarity_search(user_question)
        llm = LlmEngine()
        chain = llm.get_qa_chain(knowledge_base)
        with get_openai_callback() as cb:
           response = chain({"query": user_question})
           print(cb)
            
        st.write(response['result'])

    

if __name__ == '__main__':
    main()
