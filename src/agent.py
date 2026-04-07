import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.tools import create_retriever_tool
from langgraph.prebuilt import create_react_agent

load_dotenv()

def setup_agent(persist_directory, collection_name):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory=persist_directory, 
        embedding_function=embeddings, 
        collection_name=collection_name
    )
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    
    retriever_tool = create_retriever_tool(
        retriever,
        "research_paper_search",
        "Search the research corpus for cross-document reasoning and summarization."
    )
    tools = [retriever_tool]
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    agent_executor = create_react_agent(llm, tools)
    
    return agent_executor

if __name__ == "__main__":
    agent = setup_agent("chroma_db", "research_corpus")
    
    query = "What do the research papers say about neutrino beams or silicon wafers? Summarize the findings."
    response = agent.invoke({
        "messages": [
            ("system", "You are a Research Corpus Agent. Plan your search, retrieve relevant papers, and synthesize a comprehensive answer."),
            ("user", query)
        ]
    })
    
    final_message = response["messages"][-1].content
    if isinstance(final_message, list):
        print(final_message[0].get("text", final_message))
    else:
        print(final_message)