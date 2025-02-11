import streamlit as st
import tempfile
from unstructured.partition.auto import partition
from llm_pipeline import LLMPipeline
from utils import clean_text

# Import separate modules for each project tool
from smart_resume_optimizer import run_smart_resume_optimizer
from career_path_advisor import run_career_path_advisor
from personal_branding_assistant import run_personal_branding_assistant
from interview_followup_email import run_interview_followup_email
from networking_opportunity_finder import run_networking_opportunity_finder
from salary_negotiation_advisor import run_salary_negotiation_advisor
from job_search_aggregator import run_job_search_aggregator
from skill_endorsement_recommender import run_skill_endorsement_recommender
from linkedin_profile_enhancer import run_linkedin_profile_enhancer
from virtual_career_fair_navigator import run_virtual_career_fair_navigator
from mentorship_matchmaker import run_mentorship_matchmaker
from personal_development_tracker import run_personal_development_tracker

def run_cover_letter_generator(llm, clean_text):
    st.header("Cover Letter & Interview Prep Generator")
    
    # Candidate uploads their CV file
    cv_file = st.file_uploader("Upload your CV", type=["pdf", "docx", "txt"])
    # Candidate enters the job description as text
    job_description_input = st.text_area("Enter the Job Description:", value="")

    generate_btn = st.button("Generate Cover Letter")
    if generate_btn:
        if cv_file is None:
            st.error("Please upload a CV file.")
            return
        if not job_description_input.strip():
            st.error("Please enter a job description.")
            return

        try:
            # Process the candidate's CV file
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(cv_file.read())
                tmp_path = tmp.name

            cv_docs = partition(filename=tmp_path)
            cv_text = " ".join([doc.text for doc in cv_docs])
            cv_text = clean_text(cv_text)

            # Extract candidate details from the CV
            candidate_details = llm.extract_cv_details(cv_text)

            # Clean and process the provided job description text
            cleaned_job_description = clean_text(job_description_input)
            job_postings = llm.extract_jobs(cleaned_job_description)
            job = job_postings[0]

            # Generate the initial cover letter
            cover_letter = llm.write_cover_letter(job, candidate_details)
            st.markdown("### Generated Cover Letter")
            st.code(cover_letter, language='markdown')

            # Feedback Loop & Iteration
            feedback = st.text_area("Provide feedback to refine the cover letter:", "")
            if st.button("Refine Cover Letter"):
                if feedback.strip() == "":
                    st.error("Please provide some feedback to refine the cover letter.")
                else:
                    refined_letter = llm.refine_cover_letter(cover_letter, feedback, job, candidate_details)
                    st.markdown("### Refined Cover Letter")
                    st.code(refined_letter, language='markdown')
                    cover_letter = refined_letter

            # Interview Preparation
            if st.button("Generate Interview Preparation Guide"):
                interview_guide = llm.generate_interview_questions(job, candidate_details)
                st.markdown("### Interview Preparation Guide")
                st.code(interview_guide, language='markdown')

            # Job Fit Score & Recommendations
            fit_score = llm.calculate_job_fit_score(job, candidate_details)
            st.markdown("### Job Fit Score and Recommendations")
            st.json(fit_score)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

def main():
    # Set page configuration
    st.set_page_config(layout="wide", page_title="Career Development Tools", page_icon="📄")
    
    # Enhanced Sidebar UI
    st.sidebar.title("🚀 Career Development Suite")
    st.sidebar.markdown(
        """
        Welcome to the Career Development Suite. Choose a tool from the list below to enhance your professional journey!
        """
    )
    
    projects = [
        "Cover Letter & Interview Prep Generator",
        "Smart Resume Optimizer",
        "Career Path Advisor",
        "Personal Branding Assistant",
        "Interview Follow-up Email Generator",
        "Networking Opportunity Finder",
        "Salary Negotiation Advisor",
        "Job Search Aggregator",
        "Skill Endorsement Recommender",
        "LinkedIn Profile Enhancer",
        "Virtual Career Fair Navigator",
        "Mentorship Matchmaker",
        "Personal Development Tracker"
    ]
    
    # Use a radio button for a clearer selection experience
    selected_project = st.sidebar.radio("Select a project", projects)
    
    # Main content container
    with st.container():
        if selected_project == "Cover Letter & Interview Prep Generator":
            llm = LLMPipeline()
            run_cover_letter_generator(llm, clean_text)
        elif selected_project == "Smart Resume Optimizer":
            run_smart_resume_optimizer()
        elif selected_project == "Career Path Advisor":
            run_career_path_advisor()
        elif selected_project == "Personal Branding Assistant":
            run_personal_branding_assistant()
        elif selected_project == "Interview Follow-up Email Generator":
            run_interview_followup_email()
        elif selected_project == "Networking Opportunity Finder":
            run_networking_opportunity_finder()
        elif selected_project == "Salary Negotiation Advisor":
            run_salary_negotiation_advisor()
        elif selected_project == "Job Search Aggregator":
            run_job_search_aggregator()
        elif selected_project == "Skill Endorsement Recommender":
            run_skill_endorsement_recommender()
        elif selected_project == "LinkedIn Profile Enhancer":
            run_linkedin_profile_enhancer()
        elif selected_project == "Virtual Career Fair Navigator":
            run_virtual_career_fair_navigator()
        elif selected_project == "Mentorship Matchmaker":
            run_mentorship_matchmaker()
        elif selected_project == "Personal Development Tracker":
            run_personal_development_tracker()
        else:
            st.header("Project Coming Soon")
            st.write("This project is under development.")

if __name__ == "__main__":
    main()
