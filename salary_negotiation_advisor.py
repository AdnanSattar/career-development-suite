import streamlit as st
from llm_pipeline import LLMPipeline

def run_salary_negotiation_advisor():
    st.header("Salary Negotiation Advisor")
    st.write("Receive personalized salary negotiation strategies based on your role and current compensation.")

    current_salary = st.text_input("Enter your current salary:")
    desired_salary = st.text_input("Enter your desired salary:")
    role = st.text_input("Enter your job role:")

    if st.button("Get Negotiation Advice"):
        if not current_salary or not desired_salary or not role:
            st.error("Please fill all the fields.")
            return

        llm = LLMPipeline()
        prompt = f"""
        ### SALARY NEGOTIATION DETAILS:
        Current Salary: {current_salary}
        Desired Salary: {desired_salary}
        Role: {role}
        
        ### INSTRUCTION:
        Provide personalized salary negotiation advice, including market insights, effective negotiation tactics, and additional recommendations to help bridge the gap between current and desired salary.
        ### SALARY NEGOTIATION ADVISOR (NO PREAMBLE):
        """
        response_content = llm.generate(prompt)
        st.markdown("### Negotiation Advice")
        st.write(response_content)

if __name__ == "__main__":
    run_salary_negotiation_advisor()
