from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class Threat(BaseModel):
    isThreat: Union[str, None] = None
    file: Union[str, None] = None

items = {
    "item1": {"isThreat": True, "file": ""},  
}

@app.get("/detection/{item_id}", response_model=Threat)
async def readThreat(item_id: str):
    return items[item_id]

@app.patch("/detection/{item_id}", response_model=Threat)
async def updateThreat(item_id: str, threat: Threat):
    stored_item_data = items[item_id]
    stored_item_model = Threat(**stored_item_data)
    update_data = threat.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item