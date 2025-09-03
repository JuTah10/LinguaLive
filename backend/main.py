from fastapi import FastAPI
from routes import stt, translate, tts

app = FastAPI(title="LinguaLive")

# Routes
app.include_router(stt.router, prefix="/api/stt", tags=["Speech-to-Text"])
# app.include_router(translate.router, prefix="/api/translate", tags=["Translation"])
# app.include_router(tts.router, prefix="/api/tts", tags=["Text-to-Speech"])


@app.get("/")
def root():
    return {"message": "LinguaLive API is running"}