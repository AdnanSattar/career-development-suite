import streamlit as st
from llm_pipeline import LLMPipeline

def run_mentorship_matchmaker():
    st.header("Mentorship Matchmaker")
    st.write("Find mentors that match your career goals and skillset.")

    industry = st.text_input("Enter your industry:")
    career_goals = st.text_area("Describe your career goals:")

    if st.button("Find Mentor"):
        if not industry or not career_goals:
            st.error("Please fill in all the fields.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### MENTORSHIP MATCH DETAILS:
        Industry: {industry}
        Career Goals: {career_goals}
        
        ### INSTRUCTION:
        Based on the above details, suggest potential mentors and explain why they would be a good match. Include tips on how to approach potential mentors.
        ### MENTORSHIP MATCHMAKER (NO PREAMBLE):
        """
        response_content = llm.generate(prompt)
        st.markdown("### Mentor Suggestions")
        st.write(response_content)

if __name__ == "__main__":
    run_mentorship_matchmaker()
