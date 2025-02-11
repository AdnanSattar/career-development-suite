import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class LLMPipeline:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED JOB DESCRIPTION TEXT:
            {page_data}
            ### INSTRUCTION:
            The text above is from a job description.
            Your task is to extract the job posting details and return them in JSON format with the following keys: `role`, `experience`, `skills`, and `description`.
            Only return valid JSON without any preamble.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res_parsed = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse job details.")
        return res_parsed if isinstance(res_parsed, list) else [res_parsed]

    def extract_cv_details(self, cv_text):
        prompt_cv = PromptTemplate.from_template(
            """
            ### CANDIDATE CV TEXT:
            {cv_text}
            ### INSTRUCTION:
            Extract the candidate's key details from the CV. Return the information in JSON format with the following keys: 
            "name" (if available), "skills", "projects", "experience", and "education". 
            Only return valid JSON without any preamble.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_cv = prompt_cv | self.llm
        res = chain_cv.invoke(input={"cv_text": cv_text})
        try:
            json_parser = JsonOutputParser()
            cv_details = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Unable to extract candidate details from CV.")
        return cv_details

    def write_cover_letter(self, job, candidate_details):
        prompt_cover_letter = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### CANDIDATE DETAILS:
            {candidate_details}

            ### INSTRUCTION:
            You are writing a cover letter for a candidate applying for the above job. 
            Using the candidate's details, craft a personalized and professional cover letter addressed to the recruiter.
            Highlight the matching skills, projects, and experiences that align with the job requirements.
            Do not include any preamble or explanations.
            ### COVER LETTER (NO PREAMBLE):
            """
        )
        chain_cover = prompt_cover_letter | self.llm
        res = chain_cover.invoke({
            "job_description": str(job),
            "candidate_details": str(candidate_details)
        })
        return res.content

    def refine_cover_letter(self, original_cover_letter, feedback, job, candidate_details):
        prompt_refine = PromptTemplate.from_template(
            """
            ### ORIGINAL COVER LETTER:
            {original_cover_letter}

            ### CANDIDATE FEEDBACK:
            {feedback}

            ### JOB DESCRIPTION:
            {job_description}

            ### CANDIDATE DETAILS:
            {candidate_details}

            ### INSTRUCTION:
            Based on the above feedback, please refine the cover letter to better suit the candidate's needs. 
            Provide the improved cover letter without any preamble.
            ### REFINED COVER LETTER (NO PREAMBLE):
            """
        )
        chain_refine = prompt_refine | self.llm
        res = chain_refine.invoke({
            "original_cover_letter": original_cover_letter,
            "feedback": feedback,
            "job_description": str(job),
            "candidate_details": str(candidate_details)
        })
        return res.content

    def generate_interview_questions(self, job, candidate_details):
        prompt_interview = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### CANDIDATE DETAILS:
            {candidate_details}

            ### INSTRUCTION:
            Based on the above job description and candidate's background, generate a list of potential interview questions that the candidate might be asked during an interview for this position. Also provide tips and guidance on how the candidate can best discuss their key skills and projects.
            Return the result in a clear, numbered format.
            ### INTERVIEW PREPARATION GUIDE (NO PREAMBLE):
            """
        )
        chain_interview = prompt_interview | self.llm
        res = chain_interview.invoke({
            "job_description": str(job),
            "candidate_details": str(candidate_details)
        })
        return res.content

    def calculate_job_fit_score(self, job, candidate_details):
        prompt_fit = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### CANDIDATE DETAILS:
            {candidate_details}

            ### INSTRUCTION:
            Evaluate the fit of the candidate for the given job. Calculate a job fit score on a scale of 0 to 100 based on the matching of candidate skills, experience, and projects to the job requirements. Additionally, provide personalized recommendations for improvement.
            Return the result in JSON format with keys: "job_fit_score" (number) and "recommendations" (text).
            ### JOB FIT EVALUATION (NO PREAMBLE):
            """
        )
        chain_fit = prompt_fit | self.llm
        res = chain_fit.invoke({
            "job_description": str(job),
            "candidate_details": str(candidate_details)
        })
        try:
            json_parser = JsonOutputParser()
            result = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Unable to parse job fit evaluation output.")
        return result

    def generate(self, prompt: str) -> str:
        """
        A generic method to generate content from any prompt.
        This can be used by modules that need to generate custom responses.
        """
        response = self.llm.invoke({"prompt": prompt})
        return response.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
