import streamlit as st
from llm_pipeline import LLMPipeline

def run_networking_opportunity_finder():
    st.header("Networking Opportunity Finder")
    st.write("Find recommendations for networking opportunities, events, and professional groups.")

    industry = st.text_input("Enter your industry:")
    location = st.text_input("Enter your location (or leave blank for remote opportunities):")

    if st.button("Find Networking Opportunities"):
        if not industry:
            st.error("Please enter your industry.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### CANDIDATE DETAILS:
        Industry: {industry}
        Location: {location}
        
        ### INSTRUCTION:
        Recommend networking opportunities, industry events, and professional groups that would benefit someone in the specified industry and location. Provide event names, dates, and participation details.
        ### NETWORKING OPPORTUNITY FINDER (NO PREAMBLE):
        """
        response_content = llm.generate(prompt)
        st.markdown("### Networking Opportunities")
        st.write(response_content)

if __name__ == "__main__":
    run_networking_opportunity_finder()
