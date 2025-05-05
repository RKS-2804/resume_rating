# 📄 Resume Scoring App (POC)

This is a lightweight proof-of-concept web app built with **Streamlit** and powered by **Ollama** (running a local LLM like `tinyllama`). It helps users evaluate how well a given resume aligns with a job description by generating a relevance score and feedback using local inference.

## 🚀 Features
- Upload one or more resumes in **PDF** or **TXT** format  
- Enter any job description to evaluate resumes against it  
- Uses a **local LLM** via Ollama for secure, offline evaluation  
- Simple and intuitive **Streamlit UI**  
- Converts PDF resumes to plain text using `pdfplumber`

## 🛠️ Tech Stack
| Component       | Technology             |
|----------------|------------------------|
| UI              | Streamlit              |
| LLM Backend     | Ollama (e.g., TinyLLaMA) |
| PDF Parsing     | pdfplumber             |
| HTTP Requests   | requests               |
| Language        | Python 3.8+            |


