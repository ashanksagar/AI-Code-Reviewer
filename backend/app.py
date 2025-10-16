from fastapi import FastAPI, UploadFile, File
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from review.analyzer import analyze_code
import os
from review.openai_client import gpt_chat
from fastapi.responses import FileResponse
from fastapi import Form


app = FastAPI()

frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/static", StaticFiles(directory=frontend_dir), name="frontend")


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8")
    result = analyze_code(code)
    return {"analysis": result}

@app.get("/")
async def root():
    return FileResponse(os.path.join(frontend_dir, "frontend.html"))


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}


    
@app.post("/review")
async def review_code(file: UploadFile = File(...)):
    content = await file.read()
    code_text = content.decode("utf-8")
    feedback = analyze_code(code_text)
    return {"feedback": feedback}

@app.post("/chat")
async def chat_with_ai(message: str = Form(...)):
    response = gpt_chat(message)
    return {"reply": response}