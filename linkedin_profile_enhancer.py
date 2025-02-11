import streamlit as st
from llm_pipeline import LLMPipeline

def run_linkedin_profile_enhancer():
    st.header("LinkedIn Profile Enhancer")
    st.write("Enhance your LinkedIn profile with actionable tips and content suggestions.")

    profile_text = st.text_area("Enter your current LinkedIn profile summary:")

    if st.button("Enhance Profile"):
        if not profile_text.strip():
            st.error("Please enter your profile summary.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### LINKEDIN PROFILE:
        {profile_text}
        
        ### INSTRUCTION:
        Analyze the provided LinkedIn profile summary and suggest improvements to enhance clarity, impact, and SEO optimization. Provide actionable tips and content improvements.
        ### LINKEDIN PROFILE ENHANCER (NO PREAMBLE):
        """
        response_content = llm.generate(prompt)
        st.markdown("### Profile Enhancement Suggestions")
        st.write(response_content)

if __name__ == "__main__":
    run_linkedin_profile_enhancer()
