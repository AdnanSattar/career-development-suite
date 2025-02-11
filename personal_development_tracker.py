import streamlit as st
from llm_pipeline import LLMPipeline

def run_personal_development_tracker():
    st.header("Personal Development Tracker")
    st.write("Track your goals, certifications, and skill development progress.")

    current_goals = st.text_area("List your current development goals:")
    completed_courses = st.text_area("List any completed courses or certifications:")

    if st.button("Get Development Plan"):
        llm = LLMPipeline()
        prompt = f"""
        ### DEVELOPMENT DETAILS:
        Goals: {current_goals}
        Completed Courses/Certifications: {completed_courses}
        
        ### INSTRUCTION:
        Based on the provided information, generate a personalized development plan with milestones, recommended courses, and suggestions for skill improvement.
        ### PERSONAL DEVELOPMENT TRACKER (NO PREAMBLE):
        """
        # Use the generic generate() method to get the response
        response_content = llm.generate(prompt)
        st.markdown("### Development Plan")
        st.write(response_content)

if __name__ == "__main__":
    run_personal_development_tracker()
