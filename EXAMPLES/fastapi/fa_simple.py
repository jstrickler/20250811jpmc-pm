from fastapi import FastAPI, HTTPException
from sqlobject import *

app = FastAPI()

# sqlhub.processConnection = connectionForURI("postgres://postgres:scripts@localhost/postgres")
sqlhub.processConnection = connectionForURI("sqlite:../../DATA/presidents.db")

class Presidents(SQLObject):
    class sqlmeta:
        fromDatabase = True

@app.get("/")
def home():
    return {'foo': 'ugh'}

@app.get("/president/{id}")
def read_president(id: int):
    return {'name': 'George Washington'}
    # try:
    #     president = Presidents.get(id)
    #     return {
    #         'first_name': president.firstname,
    #         'last_name': president.lastname,
    #         'birth_state': president.birthstate,
    #         'party': president.party,
    #     }
    # except SQLObjectNotFound:
    #     raise HTTPException(status_code=404, detail="Person not found")
