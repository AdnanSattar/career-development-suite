import streamlit as st
from llm_pipeline import LLMPipeline

def run_job_search_aggregator():
    st.header("Job Search Aggregator")
    st.write("Aggregate job listings based on your preferences and receive personalized recommendations.")

    keywords = st.text_input("Enter job keywords:")
    location = st.text_input("Enter preferred location:")

    if st.button("Search Jobs"):
        if not keywords:
            st.error("Please enter job keywords.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### JOB SEARCH DETAILS:
        Keywords: {keywords}
        Location: {location}
        
        ### INSTRUCTION:
        Simulate a job search aggregator by generating a list of job titles, companies, and brief descriptions based on the provided keywords and location.
        ### JOB SEARCH AGGREGATOR (NO PREAMBLE):
        """
        response_content = llm.generate(prompt)
        st.markdown("### Job Listings")
        st.write(response_content)

if __name__ == "__main__":
    run_job_search_aggregator()
