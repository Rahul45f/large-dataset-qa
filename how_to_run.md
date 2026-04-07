# How to Run

Follow these steps to set up the environment, prepare the dataset, and execute the Research Corpus Agent.

## 1. Prerequisites
Ensure you have Python 3.10+ installed and a virtual environment activated. Install the required libraries using:
```bash
pip install -r requirements.txt
```
## 2. Dataset Collection
The project utilizes the arXiv Dataset from Kaggle.

Navigate to the Kaggle arXiv Dataset.

Download the dataset archive.

Extract the archive to find the arxiv-metadata-oai-snapshot.json file.

Move this JSON file into the root directory of the project.

## 3. Environment Configuration
Create a .env file in the root directory to store your API credentials:
```bash
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

## 4. Data Extraction
Run the extraction script to convert the raw JSON metadata into a structured CSV format for the processing pipeline:
```bash
python extract_data.py
```
This script will generate data/research_papers.csv.

## 5. Data Ingestion
Vectorize the extracted research papers and populate the local vector database. This step uses local HuggingFace embeddings to process the large dataset efficiently:
```bash
python src/ingest.py
```

## 6. Running the Agent
Once the vector database is ready, you can run the agent to perform Q&A:
```bash
python src/agent.py
```
