from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="DealMind AI Demo", version="0.2.1")

class DemoRequest(BaseModel):
    text: str = Field(min_length=1, max_length=12000)

@app.get("/api/health")
def health():
    return {"status": "ok", "product": "DealMind AI", "mode": "demo"}

@app.post("/api/analyze")
def analyze(payload: DemoRequest):
    # Демонстрационный ответ: это НЕ настоящая AI-обработка.
    lines = [line.strip() for line in payload.text.splitlines() if line.strip()]
    return {
        "mode": "demo",
        "notice": "Подключите AI-провайдера для настоящего извлечения позиций.",
        "extracted_lines": lines[:50],
        "count": min(len(lines), 50)
    }
