import streamlit as st
from llm_pipeline import LLMPipeline

def run_interview_followup_email():
    st.header("Interview Follow-up Email Generator")
    st.write("Generate a personalized follow-up email after an interview.")

    interview_experience = st.text_area("Describe your interview experience:")
    interviewer_name = st.text_input("Interviewer Name:")
    company_name = st.text_input("Company Name:")

    if st.button("Generate Follow-up Email"):
        if not interview_experience or not interviewer_name or not company_name:
            st.error("Please fill all the fields.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### INTERVIEW DETAILS:
        Interviewer: {interviewer_name}
        Company: {company_name}
        Experience: {interview_experience}
        
        ### INSTRUCTION:
        Generate a polite and professional follow-up email that thanks the interviewer, reiterates your interest, and summarizes key points from the interview. Adjust tone based on the interview experience.
        ### FOLLOW-UP EMAIL (NO PREAMBLE):
        """
        # Use the new generate() method instead of directly invoking llm.llm.invoke()
        response_content = llm.generate(prompt)
        st.markdown("### Follow-up Email")
        st.write(response_content)

if __name__ == "__main__":
    run_interview_followup_email()
