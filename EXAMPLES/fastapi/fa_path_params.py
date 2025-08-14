from fastapi import FastAPI

app = FastAPI()

@app.get("/wombats/{id}")
async def get_record(id):
    return {"message": f"getting record {id}", "triple": f"{id * 3}"}