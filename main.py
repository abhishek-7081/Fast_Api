from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class hu(BaseModel):
    id: int 
    name : str 
    origin : str
    
teas: List[hu] = []



