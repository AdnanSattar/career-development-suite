import streamlit as st
from llm_pipeline import LLMPipeline

def run_virtual_career_fair_navigator():
    st.header("Virtual Career Fair Navigator")
    st.write("Discover upcoming virtual career fairs and get recommendations on which events to attend.")

    industry = st.text_input("Enter your industry:")

    if st.button("Find Career Fairs"):
        if not industry:
            st.error("Please enter your industry.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### CAREER FAIR DETAILS:
        Industry: {industry}
        
        ### INSTRUCTION:
        Based on the provided industry, generate a list of upcoming virtual career fairs including event names, dates, and participation recommendations. Provide brief summaries for each event.
        ### VIRTUAL CAREER FAIR NAVIGATOR (NO PREAMBLE):
        """
        response_content = llm.generate(prompt)
        st.markdown("### Virtual Career Fairs")
        st.write(response_content)

if __name__ == "__main__":
    run_virtual_career_fair_navigator()
