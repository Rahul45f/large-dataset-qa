# How to Run

Follow these steps to set up the environment, prepare the dataset, and execute the Research Corpus Agent.

## 1. Prerequisites
Ensure you have Python 3.10+ installed and a virtual environment activated. Install the required libraries using:
```bash
pip install -r requirements.txt
```
## 2. Dataset Collection
The project utilizes the arXiv Dataset from Kaggle.

Navigate to the [Kaggle arXiv Dataset](https://storage.googleapis.com/kaggle-data-sets/612177/15533467/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260407%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260407T151136Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=ac9ae3950d3e8e1890752437f0e34e8bae7098a8aae0038b5849f13f9cd7476c5b2f5594949260aa821d51957a32dd1f58dcd89b34ee45f0358d9ed74eb2812e84d0b9ec19cf56f87e6572845eb66167095494e594ea78bebca211910d1436f604ccc23ecb0cf825cbfd0e344016cfd29df28bf0db0f304e24a2da42f87a7375e106033ae1e0ad0c99a0d8e3ec4df6faddbb86de68081819f119aa7f3f5738361ffca47b8f4e8471b2d2a6357ccf275c1b49e38bcd0c8fbaad8d7b361b0d8295e18d102b59fc3cf769ec0b061fdec9ce32d5c734e7a2054e6091cdb35021a01ed57b5cbf54bd39bbedddc168c0a5102078da7d4a2b7dfde343ae0658f75cc5a1).

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
