from transformers import pipeline
import re

summarizer=pipeline("summarization")
sentiment_analyzer=pipeline("sentiment-analysis")

class AITextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        

    def get_summary(self):
        if len(self.text.split()) < 30:
            return self.text

        result = summarizer(
            self.text,
            max_length=130,
            min_length=30,
            do_sample=False
        )

        return result[0]["summary_text"]
    
    def get_sentiment(self):
        result=sentiment_analyzer(self.text)
        return {
            "label":result[0]["label"]
        }
    
    def get_keywords(self):
        words= re.findall(r"\b[a-zA-Z]{4,}\b", self.text.lower())
        keywords=sorted(set(words), key=words.count, reverse=True)
        return keywords[:10]

    def analyze(self):
        return {
            "summary": self.get_summary(),
            "sentiment": self.get_sentiment(),
            "keywords": self.get_keywords()
        }
    
    
        
        