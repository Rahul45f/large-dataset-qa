import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DataFrameLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import pandas as pd

load_dotenv()

def ingest_data(file_path, collection_name, persist_directory):
    df = pd.read_csv(file_path)
    loader = DataFrameLoader(df, page_content_column="abstract")
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory=persist_directory
    )
    
    return vectorstore

if __name__ == "__main__":
    ingest_data("data/research_papers.csv", "research_corpus", "chroma_db")