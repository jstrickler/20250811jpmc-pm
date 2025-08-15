from enum import Enum
from fastapi import FastAPI, Query, Header, Form
from pydantic import BaseModel, Field, UUID1
from typing import Annotated, Literal

class WombatColor(str, Enum):
    black = 'black'
    brown = 'brown'
    grey = 'grey'

class Spam(BaseModel):
    weight: float
    size: int
    model_config = {
    "json_schema_extra": {
        "examples": [
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        ]
    }
}

class WombatInfo(BaseModel):
    name: str
    age: int
    color: WombatColor
    spam: Spam

app = FastAPI()

# any(color in enum_value for enum_value in enum)

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.post("/wombats")
async def create_wombat(wombat_info: WombatInfo):
    # add new wombat to db
    return {"name": wombat_info.name}

@app.get("/wombats/{category}/{item_id}", status_code=203)
async def root(category: WombatColor, item_id: int, country: Annotated[str, Query(title="Country", description="Country where wombat lives", alias="base-country", min_length=3, max_length=12, pattern=r"^[A-Z][a-z ]+")]="Australia", doit: bool=False,  upper: bool|None = None, user_agent: Annotated[str|None, Header()]=None):
    if upper:
        category_name = category.value.upper()
    else:
        category_name = category.value
    return {
        "message": "Hello JPMC World",
        "item_id": item_id,
        "category": category_name,
        "upper": upper,
        "doit": doit,
        "user agent": user_agent,
        "country": country,
    }

@app.post("/wombats/forms")
async def forminfo(name: Annotated[str, Form()], sex: Annotated[str, Form()]):
    return {
        "name": name,
        "sex": sex,
    }