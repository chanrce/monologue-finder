from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic validation
class MonologueResponse(BaseModel):
    id: int
    character: str
    play: str
    playwright: str


# ROUTES

@app.get("/")
def root():
    return {"message": "Monologue Finder API"}

@app.get("/monologues")
def get_monologues():
    monologues=[{"id":1,
                "character":"Hamlet",
                "play":"Hamlet",
                "playwright":"William Shakespeare"}]
    return monologues

@app.get("/monologues/{monologue_id}", response_model=MonologueResponse)
def get_monologue(monologue_id: int):
    for monologue in get_monologues():
        if monologue["id"] == monologue_id:
            return monologue
    raise HTTPException(status_code=404, detail="Monologue not found")

@app.get("/health")
def health_check():
    return {"status":"ok"}

