import faiss
import numpy as np
import os
from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer
from langchain.llms import OpenAI
from app.services.sop_loader import get_all_sop_chunks
from schema import IncidentRequest

load_dotenv()

# Initialize embedding model and LLM
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
llm = OpenAI(temperature=0.3, openai_api_key=os.getenv("OPENAI_API_KEY"),max_tokens=200)

# Load and embed SOP documents once
sop_docs = get_all_sop_chunks("data/sops")
texts = [doc.page_content for doc in sop_docs]
index = faiss.IndexFlatL2(embedding_model.encode([texts[0]])[0].shape[0])
index.add(embedding_model.encode(texts))

# Retrieve top-K relevant SOPs
def retrieve_docs(query, top_k=5):
    q_embed = embedding_model.encode([query])
    D, I = index.search(np.array(q_embed), top_k)
    return [texts[i] for i in I[0]]

# Format all incidents into a single summary string
def summarize_all_incidents(incidents):
    summary = []
    for i, inc in enumerate(incidents, 1):
        item = f"""Incident {i}:
- Event: {inc.event}
- Date: {inc.eventdate}
- Description: {inc.longdesc}
- Vessel Type: {inc.veseltype}
- Root Cause: {inc.rootcause}"""
        summary.append(item)
    return "\n\n".join(summary)

# Construct LLM prompt and generate report
def generate_report(incident_summary, sop_context):
    prompt = f"""You are a maritime safety analyst.
You will receive a list of multiple incidents and relevant SOP context.
Generate a structured report with the following sections:

1. INCIDENT REPORT
   - High-level summary of incidents
   - Any noticeable trends, correlations, or repeated issues
   - Any patterns across vessel type, causes, or time

2. PLAN OF ACTION
   - Preventive and corrective measures based on SOPs
   - Clear and practical steps the crew/management should take

INCIDENTS:
{incident_summary}

RELEVANT SOP CONTEXT:
{sop_context}

Ensure the report uses clear bullet points and headers.
Avoid repeating raw input — interpret and synthesize the information."""
    
    return llm(prompt)

# Main callable from FastAPI
def generate_rag_response(request: IncidentRequest):
    # Step 1: Summarize all incidents
    summary = summarize_all_incidents(request.incidents)

    # Step 2: Retrieve relevant SOP content
    sop_context = "\n\n".join(retrieve_docs(summary))

    # Step 3: Generate report using LLM
    report = generate_report(summary, sop_context)
    print({
        "incident_summary": summary,
        "sop_context": sop_context,
        "report": report
    })

    # Step 4: Return full result (flat, not grouped)
    return {
        "incident_summary": summary,
        "sop_context": sop_context,
        "report": report
    }
