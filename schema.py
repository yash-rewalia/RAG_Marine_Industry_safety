from pydantic import BaseModel
from typing import List

class Incident(BaseModel):
    event: str
    eventdate: str
    longdesc: str
    veseltype: str
    rootcause: str

class IncidentRequest(BaseModel):
    incidents: List[Incident]
