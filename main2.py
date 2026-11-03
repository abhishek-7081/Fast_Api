from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic Model
class Tea(BaseModel):
    id: int
    name: str
    origin: str


# In-memory database
teas: List[Tea] = [
    Tea(id=1, name="Green Tea", origin="China"),
                   Tea(id=2, name="Black Tea", origin="India"),
                   Tea(id=3, name="Oolong Tea", origin="Taiwan"),
                   Tea(id=4, name="White Tea", origin="China"),
                   Tea(id=5, name="Herbal Tea", origin="Various"),
                   Tea(id=6, name="Matcha", origin="Japan"),
                   Tea(id=7, name="Chai", origin="India"),
                   Tea(id=8, name="Earl Grey", origin="England")
                   ]


# 1. Home Route
@app.get("/")
def home():
    return {"message": "Welcome to Tea API"}



# 2. GET - Fetch all teas
@app.get("/teas")
def get_teas():
    return teas


# 3. GET - Fetch tea by ID
@app.get("/teas/{tea_id}")
def get_tea(tea_id: int):
    for tea in teas:
        if tea.id == tea_id:
            return tea

    raise HTTPException(status_code=404, detail="Tea not found")


# 4. POST - Add a new tea
@app.post("/teas", status_code=201)
def add_tea(tea: Tea):
    for existing_tea in teas:
        if existing_tea.id == tea.id:
            raise HTTPException(status_code=400, detail="Tea ID already exists")

    teas.append(tea)
    return {"message": "Tea added successfully", "tea": tea}


# 5. PUT - Update entire tea
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            if updated_tea.id != tea_id:
                raise HTTPException(status_code=400, detail="ID cannot be changed")

            teas[index] = updated_tea
            return {"message": "Tea updated successfully", "tea": updated_tea}

    raise HTTPException(status_code=404, detail="Tea not found")


# 6. PATCH - Partially update tea
class TeaUpdate(BaseModel):
    name: str = None
    origin: str = None


@app.patch("/teas/{tea_id}")
def partial_update_tea(tea_id: int, updates: TeaUpdate):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            updated_data = tea.model_dump()
            updated_data.update(updates.model_dump(exclude_unset=True))

            updated_tea = Tea(**updated_data)
            teas[index] = updated_tea

            return {"message": "Tea partially updated", "tea": updated_tea}

    raise HTTPException(status_code=404, detail="Tea not found")


# 7. DELETE - Delete tea
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return {"message": "Tea deleted successfully", "tea": deleted_tea}

    raise HTTPException(status_code=404, detail="Tea not found")
