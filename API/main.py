from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from LLM.llm import LLM

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading model...")
    app.model = LLM()
    yield
    print("Model unloaded")

class Req(BaseModel):
    prompt: str

app = FastAPI(lifespan=lifespan)

@app.post("/api/v1/llm")
def llm_generate(req: Req):   
    return app.model.generate(req.prompt)


if __name__ == "__main__":    
    uvicorn.run(app, host="localhost", port=8000)
    
    