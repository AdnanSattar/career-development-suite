import streamlit as st
from llm_pipeline import LLMPipeline

def run_career_path_advisor():
    st.header("Career Path Advisor")
    st.write("Enter your details to receive personalized career path suggestions and training recommendations.")

    name = st.text_input("Enter your name:")
    experience = st.text_area("Describe your work experience:")
    skills = st.text_area("List your key skills (comma-separated):")
    aspirations = st.text_area("What are your career aspirations?")

    if st.button("Get Career Path Suggestions"):
        if not name or not experience or not skills:
            st.error("Please provide your name, experience, and skills.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### CANDIDATE DETAILS:
        Name: {name}
        Experience: {experience}
        Skills: {skills}
        Aspirations: {aspirations}
        
        ### INSTRUCTION:
        Based on the above details, suggest potential career paths, identify skills gaps, and recommend relevant training courses or certifications. Provide a dynamic roadmap with milestones.
        ### CAREER PATH ADVISOR (NO PREAMBLE):
        """
        # Use the generic generate() method instead of llm.llm.invoke()
        response_content = llm.generate(prompt)
        st.markdown("### Career Path Suggestions")
        st.write(response_content)

if __name__ == "__main__":
    run_career_path_advisor()
