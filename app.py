import streamlit as st
import requests
import pdfplumber
import io

class OllamaClient:
    def __init__(self, model: str = "llama2", base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        self.model = model

    def score_resume(self, job_description, resume_text):

        prompt = (
            f"Job Description:\n{job_description}\n\n"
            f"Resume:\n{resume_text}\n\n"
            "On a scale of 1–10, rate how well this resume matches the JD."
        )


        payload = {
            "model": self.model,
            "prompt": prompt,
            "max_tokens": 200,
            "temperature": 0.3,
            "stream": False
        }


        resp = requests.post(f"{self.base_url}/api/generate", json=payload)
        resp.raise_for_status()
        return resp.json().get("response", "").strip()

def pdf_to_txt(file_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                text += txt + "\n"
    return text

def main():
    st.title("Resume POC")

    st.write("Upload one or more resumes and enter a Job Description to get a score & feedback.")

    jd = st.text_area("Job Description", height=100)

    uploaded_files = st.file_uploader("Upload resume", type=["pdf", "txt"], accept_multiple_files=True)

    if st.button("Score Resumes"):

        if not jd.strip():
            st.error("Please enter a job description.")
            return
        if not uploaded_files:
            st.error("Please upload at least one resume.")
            return

        client = OllamaClient(model="tinyllama")

        for f in uploaded_files:
            st.subheader(f.name)
            raw = f.read()
            resume_text = pdf_to_txt(raw)
            

            with st.spinner(f"Scoring {f.name}..."):
                try:
                    feedback = client.score_resume(jd, resume_text)
                except Exception as e:
                    st.error(f"Error scoring resume: {e}")
                    continue
            
            st.markdown("Score and feedback of the resume:")
            
            st.write(feedback)
            

if __name__ == "__main__":
    main()
