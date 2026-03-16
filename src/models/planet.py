from pydantic import BaseModel
from typing import Optional

class Planet(BaseModel):
    id: int
    name: str
    mass: float
    radius: float
    description: Optional[str]
