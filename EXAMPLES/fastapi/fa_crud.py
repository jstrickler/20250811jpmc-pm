from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

CREATE = """
create table if not exists wombats (
    id integer primary key,
    name varchar(32),
    age integer
)
"""

QUERY_ALL = "select * from wombats"
QUERY_ONE = "select * from wombats where name = ?"
QUERY_COUNT = "select count(*) from wombats where name = ?"
INSERT = "insert into wombats (name, age) values (?, ?)"
DELETE = "delete from wombats where name = ?"

conn = sqlite3.connect("wombats.db")
cursor = conn.cursor()
cursor.execute(CREATE)

class Wombat(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/wombats", status_code=201)
async def add_wombat(wombat: Wombat):
    cursor.execute(QUERY_COUNT, [wombat.name])
    results = cursor.fetchall()
    if results[0] == 0:
        raise HTTPException(status_code=400, detail="Duplicate wombat name")
    cursor.execute(INSERT, [wombat.name, wombat.age])
    conn.commit()
    return wombat

@app.get("/wombats")
async def get_wombats():
    return cursor.execute(QUERY_ALL).fetchall()

@app.get("/wombats/{name}")
async def get_wombat(name: str):
    return cursor.execute(QUERY_ONE, [name]).fetchone()

@app.delete("/wombats/{name}")
async def delete_wombat(name: str):
    cursor.execute(DELETE, [name])
    conn.commit()
