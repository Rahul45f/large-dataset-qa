class RetrievalEvaluator:
    def __init__(self):
        self.metrics_log = []

    def calculate_metrics(self, retrieved_ids, ground_truth_ids):
        if not retrieved_ids or not ground_truth_ids:
            return {"precision": 0.0, "recall": 0.0}

        retrieved_set = set(retrieved_ids)
        truth_set = set(ground_truth_ids)
        
        true_positives = len(retrieved_set.intersection(truth_set))
        
        precision = true_positives / len(retrieved_set)
        recall = true_positives / len(truth_set)
        
        metrics = {"precision": precision, "recall": recall}
        self.metrics_log.append(metrics)
        return metrics

    def get_average_metrics(self):
        if not self.metrics_log:
            return {"avg_precision": 0.0, "avg_recall": 0.0}
            
        avg_precision = sum(m["precision"] for m in self.metrics_log) / len(self.metrics_log)
        avg_recall = sum(m["recall"] for m in self.metrics_log) / len(self.metrics_log)
        return {"avg_precision": avg_precision, "avg_recall": avg_recall}

if __name__ == "__main__":
    evaluator = RetrievalEvaluator()
    
    sample_retrieved = ["doc_1", "doc_3", "doc_5", "doc_7"]
    sample_ground_truth = ["doc_1", "doc_2", "doc_3"]
    
    print("Evaluating Query 1...")
    metrics = evaluator.calculate_metrics(sample_retrieved, sample_ground_truth)
    print(f"Precision: {metrics['precision']:.2f}, Recall: {metrics['recall']:.2f}")
    print(f"Aggregated System Metrics: {evaluator.get_average_metrics()}")