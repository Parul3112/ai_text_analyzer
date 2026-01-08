from fastapi import FastAPI
from pydantic import BaseModel
from .api_wrapper import AITextAnalyzer


app = FastAPI(title="AI Text Analyzer")

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(request: TextRequest):
    analyzer = AITextAnalyzer(request.text)
    return analyzer.analyze()
