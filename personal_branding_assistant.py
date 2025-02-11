import streamlit as st
from llm_pipeline import LLMPipeline

def run_personal_branding_assistant():
    st.header("Personal Branding Assistant")
    st.write("Enhance your online presence with personalized recommendations to optimize your digital brand.")

    profile_text = st.text_area("Enter your current online profile summary (e.g., LinkedIn About section):")

    if st.button("Optimize Personal Branding"):
        if not profile_text.strip():
            st.error("Please enter your profile summary.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### ONLINE PROFILE SUMMARY:
        {profile_text}
        
        ### INSTRUCTION:
        Analyze the provided profile summary and suggest improvements to enhance clarity, impact, and keyword optimization. Provide actionable tips.
        ### PERSONAL BRANDING ASSISTANT (NO PREAMBLE):
        """
        response_content = llm.generate(prompt)
        st.markdown("### Branding Recommendations")
        st.write(response_content)

if __name__ == "__main__":
    run_personal_branding_assistant()
