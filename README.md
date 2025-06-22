
# 🚢 Maritime Incident Report Generator (RAG-based)

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** system that generates structured maritime **incident reports** and **plans of action** based on historical incident data and Standard Operating Procedure (SOP) documents.

It leverages:
- 🔍 **FAISS + Sentence Transformers** for semantic retrieval of relevant SOPs  
- 🧠 **OpenAI LLM (via LangChain)** for intelligent report generation  
- ⚙️ **FastAPI** backend to handle RAG processing and embedding pipeline  
- 💡 **Streamlit** frontend for a simple UI with one-click summarization

---

## 🧩 Features

- Accepts multiple maritime incident entries (JSON format)
- Retrieves the most relevant SOP content using semantic similarity
- Summarizes incidents and SOPs into a unified report
- Generates a clear **Incident Report** and **Plan of Action**
- Provides a Streamlit UI for easy interaction

---

## 🗂️ Project Structure

```
rag_incident_report/
├── app/
│   ├── main.py                # FastAPI app entry
│   ├── api.py                 # API routes
│   └── services/
│       ├── rag.py             # RAG logic (embedding, retrieval, generation)
│       └── sop_loader.py      # SOP loading from PDFs/DOCX/TXT
│   
│               
├── frontend/
│   └── streamlit_app.py       # Streamlit frontend app
├── data/
│   └── sops/                  # Folder containing SOP documents
├── .env                       # API keys and environment configs
└── schema.py                  # Pydantic request models                     
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yash-rewalia/RAG_Marine_Industry_safety.git
cd 'your-folder-name'
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Place your SOPs

Put `.pdf`, `.docx`, or `.txt` files inside the `data/sops/` folder.

---

## 🧪 Running the App

### Start the FastAPI backend:

```bash
uvicorn app.main:app --reload
```

### Run the Streamlit frontend:

```bash
streamlit run frontend/streamlit_app.py
```

---

## 📸 UI Preview

> Streamlit shows:
- Incident Summary
- Retrieved SOP Context
- Generated Report & Plan of Action

---

## 📄 Sample Input Format

```json
{
  "incidents": [
    {
      "event": "Fire in engine room",
      "eventdate": "12-07-2023",
      "longdesc": "A fire broke out in the engine room due to overheating of machinery.",
      "veseltype": "Tanker",
      "rootcause": "Lack of maintenance"
    }
  ]
}
```


---

## 🙌 Acknowledgements

- [OpenAI](https://openai.com/)
- [LangChain](https://www.langchain.com/)
- [Sentence-Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)

---

> Made with ❤️ for safer seas and smarter incident handling.
