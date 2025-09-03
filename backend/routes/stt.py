from fastapi import APIRouter, UploadFile, File
import whisper

router = APIRouter()

# Load Whisper model once (small = faster, large = more accurate)
whisper_model = whisper.load_model("small")

@router.post("/")
async def speech_to_text(file: UploadFile = File(...)):
    
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    result = whisper_model.transcribe(file_location)
    text = result["text"]

    return {"transcription": text}
