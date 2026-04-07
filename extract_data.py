import json
import pandas as pd
import os

def create_csv_from_arxiv(json_path, output_csv_path, num_rows):
    data = []
    
    with open(json_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= num_rows:
                break
            
            doc = json.loads(line)
            data.append({
                'id': doc.get('id'),
                'title': doc.get('title'),
                'abstract': doc.get('abstract').replace('\n', ' ')
            })
            
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    
    df = pd.DataFrame(data)
    df.to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    create_csv_from_arxiv(
        json_path="data/arxiv-metadata-oai-snapshot.json", 
        output_csv_path="data/research_papers.csv", 
        num_rows=15000
    )