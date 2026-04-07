# System Architecture Diagram

The system follows a standard RAG flow, moving from data ingestion to the final output via a LangGraph-powered AI agent.

1. **Data Platform Layer (Ingestion):**
   * **Input:** Raw CSV data (`data/research_papers.csv`).
   * **Processing:** LangChain `DataFrameLoader` and `RecursiveCharacterTextSplitter` chunk the text.
   * **Embedding:** Local CPU-based HuggingFace model (`all-MiniLM-L6-v2`) vectorizes the chunks.
   * **Storage:** Persisted locally to a Chroma Vector DB (`chroma_db`).

2. **Agentic Layer (Retrieval & Synthesis):**
   * **Planner:** Google Gemini (`gemini-2.5-flash`) acts as the core reasoning engine via LangGraph.
   * **Tool:** A custom `create_retriever_tool` connects the agent to the Chroma DB.
   * **Execution:** The agent receives a query, decides to use the retrieval tool, fetches the top 5 semantically similar documents, and synthesizes a final, grounded answer.

3. **Output:** * The final synthesized answer is printed to the user.