from transformers import pipeline

class MedicalDiagnoser:
    def __init__(self):
        self.model = pipeline(
            "text-classification",
            model="microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
        )
    
    def analyze(self, symptoms: str):
        result = self.model(symptoms)[0]
        return {
            "condition": result["label"],
            "confidence": f"{result['score']*100:.2f}%",
            "recommendation": self._generate_recommendation(result["label"])
        }

    def _generate_recommendation(self, condition: str):
        return f"Immediately consult a licensed {condition.split('_')[0]} specialist."
