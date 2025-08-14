from uuid import uuid4, UUID
from fastapi import FastAPI

app = FastAPI()

@app.get("/wombats/{id}")
async def get_record(id: int):    
    return {"message": f"getting record {id}", "triple": f"{id * 3}"}

