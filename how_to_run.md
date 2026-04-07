# How to Run

Follow these steps to set up the environment, prepare the dataset, and execute the Research Corpus Agent.

## 1. Prerequisites
Ensure you have Python 3.10+ installed and a virtual environment activated. Install the required libraries using:
```bash
pip install -r requirements.txt
```
## 2. Dataset Collection
The project utilizes the arXiv Dataset from Kaggle.

Navigate to the [Kaggle arXiv Dataset](https://storage.googleapis.com/kaggle-data-sets/1912571/3140615/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260407%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260407T051620Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=0ebda5c7b1d45d04c0ef4ba0c5f1b792927bf50e31faf98ee7d48a5793c07e135e9d1f8d1e9fb8134ff832773d9b9cf2b5468952291e3f0b34f6a42b863ac46af2fdc0cebeb013d59555599241c677a849f6e2dd38de59f90577b1b116f4baac28a9f78061c5e23aab3bb48b95a661c1af3902a9069479277e64d97d53796c3221082f1f2b86948da4a78129fcce8da523680b3bf70142c998bb42b40fff2999ce6da456284597a9264033763e3427f1745c13c8b9c5f6efebba8de230198601951f3fa74219fa8b2ce7d8b4ea980d8e4425ea09c22cda1ea20f5d62e3476edfa5892331ba49a8b6ba36a676ce590c60363c647b7b84c1f9d29fa2e857519b93).

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
