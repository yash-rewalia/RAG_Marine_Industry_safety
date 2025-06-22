from fastapi import APIRouter
from schema import IncidentRequest
from app.services.rag import generate_rag_response

router = APIRouter()

@router.post("/generate_report")
def generate_report(request: IncidentRequest):
    return generate_rag_response(request)
