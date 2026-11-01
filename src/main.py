from fastapi import FastAPI

app = FastAPI()

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

@app.get("/health")
def health_check():
    return {"status":"ok"}