import streamlit as st
import tempfile
from unstructured.partition.auto import partition
from llm_pipeline import LLMPipeline

def run_smart_resume_optimizer():
    st.header("Smart Resume Optimizer")
    st.write("Upload your resume to receive actionable feedback on how to improve its clarity, style, and job-tailoring.")

    resume_file = st.file_uploader("Upload your Resume", type=["pdf", "docx", "txt"])

    if st.button("Optimize Resume"):
        if resume_file is None:
            st.error("Please upload a resume file.")
            return

        try:
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(resume_file.read())
                tmp_path = tmp.name

            resume_docs = partition(filename=tmp_path)
            resume_text = " ".join([doc.text for doc in resume_docs])
            resume_text = clean_text(resume_text)

            llm = LLMPipeline()
            prompt = f"""
            ### RESUME TEXT:
            {resume_text}
            
            ### INSTRUCTION:
            Provide actionable feedback on how to improve this resume in terms of clarity, tone, and tailoring for specific job descriptions. Suggest specific improvements, rephrasing, and highlight any missing skills.
            ### FEEDBACK (NO PREAMBLE):
            """
            # Use the generic generate() method instead of direct invocation
            response_content = llm.generate(prompt)
            st.markdown("### Resume Optimization Feedback")
            st.write(response_content)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    run_smart_resume_optimizer()
