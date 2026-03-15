# AI DDR Report Generator 
An AI-powered system that converts site inspection reports and thermal inspection reports into a structured Detailed Diagnostic Report (DDR) using LangChain, LangGraph, Gemini, and RAG.

The system automatically extracts observations from raw inspection documents, combines them logically, and generates a client-ready diagnostic report.


# Features 
1.  Inspection Report PDF
2. Upload Thermal Report PDF
3. Extract text and images from PDFs
4. Perform semantic search using FAISS
5. Use RAG (Retrieval Augmented Generation) for contextual reasoning
6. Generate a structured DDR report
7. Simple Streamlit UI
8. Modular architecture using LangChain + LangGraph

# System Architecture 

```bash
User Uploads Reports
        │
        ▼
PDF Processing
(Text + Image Extraction)
        │
        ▼
Text Chunking
        │
        ▼
Embeddings 
        │
        ▼
FAISS Vector Database
        │
        ▼
RAG Retrieval
        │
        ▼
LangGraph Workflow
        │
        ▼
Gemini LLM
        │
        ▼
Structured DDR Report
```
# Installation 

### step-1 Clone the repository
```bash 
git clone https://github.com/rishabh6900/DDR

cd DDR
```
### step-2 Create virtual environment
```bash
conda create --name DDR python=3.11 
```

```bash 
conda activate DDR
````

### step-3 Install dependencies
```bash 
pip install -r requirements.txt
```
### step-4 Environment Variables 
Create a .env file in the project root. 
```bash
GEMINI_API_KEY="your_api_key_here"
```

### step-5 Run the Application 
```bash
streamlit run app.py
```  

### Tech Stack 
Google Gemini, Langchain,LangGraph,Faiss,PyMuPDF,Streamlit,python
