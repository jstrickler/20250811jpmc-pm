from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.get("/wombats")
async def root():
    return {"message": "Welcome to Wombat World"}

# @app.get("/wombats")    get all wombats
# @app.post("/wombats")   add wombat

# @app.get("/wombats/{id}")  get specific wombat
# @app.put("/wombats/{id}")  replace wombat
# @app.patch("/wombats/{id}") update wombat
# @app.delete("/wombats/{id}") delete wombat
