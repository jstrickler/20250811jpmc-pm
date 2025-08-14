from fastapi import FastAPI

app = FastAPI()

@app.get("/wombats/{id}")
async def get_record(id: int, report: str="short"):    
    return {
        "message": f"getting record {id}", 
        "triple": f"{id * 3}",
        "report": report,
    }

