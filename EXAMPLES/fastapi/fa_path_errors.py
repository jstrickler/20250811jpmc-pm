from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/wombats/{id}")
async def get_record(id: int):
    if id < 1:
        raise HTTPException(status_code=400, detail="ID must be >= 1")
    return {"message": f"getting record {id}", "triple": f"{id * 3}"}