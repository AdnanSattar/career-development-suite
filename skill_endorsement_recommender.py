import streamlit as st
from llm_pipeline import LLMPipeline

def run_skill_endorsement_recommender():
    st.header("Skill Endorsement Recommender")
    st.write("Get recommendations on how to boost your professional endorsements.")

    skills = st.text_area("Enter your key skills (comma-separated):")

    if st.button("Get Endorsement Recommendations"):
        if not skills:
            st.error("Please enter your skills.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### SKILL DETAILS:
        Skills: {skills}
        
        ### INSTRUCTION:
        Analyze the provided skills and recommend strategies to improve your professional endorsements. Include tips on how to request endorsements and highlight which skills to focus on.
        ### SKILL ENDORSEMENT RECOMMENDER (NO PREAMBLE):
        """
        response_content = llm.generate(prompt)
        st.markdown("### Endorsement Recommendations")
        st.write(response_content)

if __name__ == "__main__":
    run_skill_endorsement_recommender()
