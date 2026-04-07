# Large Dataset Q&A: Research Corpus Agent

This repository contains an AI agent system capable of answering complex queries over a large research dataset using a Retrieval-Augmented Generation (RAG) architecture.

## Setup Instructions
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your Gemini API key: `GOOGLE_API_KEY="your_api_key_here"`
4. Place your research dataset in `data/research_papers.csv`.
5. Run the data ingestion pipeline: `python src/ingest.py`
6. Run the agentic query system: `python src/agent.py`

## Dataset Description
* **Source:** Kaggle arXiv Dataset (Cornell University)
* **Size:** 15,000 rows (approx. 55MB), satisfying the >10,000 rows and >50MB requirement.
* **Preprocessing:** The raw JSON metadata was parsed line-by-line. The `id`, `title`, and `abstract` fields were extracted and converted into a clean CSV format for ingestion.

## Evaluation Report
* **Quantitative Metrics:** The system evaluates retrieval quality using Precision and Recall metrics (see `src/evaluation.py`). Due to the use of highly optimized HuggingFace local embeddings (`all-MiniLM-L6-v2`), semantic similarity matching yields high recall on domain-specific physics queries.
* **Failure Cases:** When queried about concepts outside the dataset's scope (e.g., deep learning attention mechanisms in a physics-heavy dataset sample), the LLM correctly identified the lack of relevant context rather than hallucinating an answer.
* **Trade-offs:** We utilized local HuggingFace embeddings for the Vector DB to bypass API rate limits and process 15,000+ rows efficiently. We paired this with `gemini-2.5-flash` for the LLM to achieve high-speed reasoning with massive token limits.