# Career Development Suite

A comprehensive AI-powered GenAI application that leverages large language models to assist job seekers and professionals in various aspects of their career development. This suite includes tools for generating cover letters, optimizing resumes, planning career paths, enhancing online profiles, preparing for interviews, negotiating salary, aggregating job listings, recommending skill endorsements, enhancing LinkedIn profiles, finding virtual career fairs, matchmaking for mentorships, and tracking personal development.

## Features

- **Cover Letter & Interview Prep Generator:**  
  Generate personalized cover letters, refine them with iterative feedback, receive interview preparation guides, and get a job fit score based on your profile and the job description.

- **Smart Resume Optimizer:**  
  Upload your resume to receive actionable feedback on clarity, tone, and tailoring for specific job descriptions.

- **Career Path Advisor:**  
  Get personalized career path suggestions, identify skill gaps, and receive training or certification recommendations along with a dynamic roadmap.

- **Personal Branding Assistant:**  
  Enhance your online presence with actionable tips to optimize your LinkedIn profile or other digital branding efforts.

- **Interview Follow-up Email Generator:**  
  Automatically generate professional follow-up emails post-interview based on your interview experience.

- **Networking Opportunity Finder:**  
  Discover industry events, networking opportunities, and professional groups tailored to your industry and location.

- **Salary Negotiation Advisor:**  
  Receive personalized salary negotiation strategies based on your current compensation, desired salary, and role.

- **Job Search Aggregator:**  
  Simulate a job search aggregator by generating a list of job titles, companies, and brief descriptions based on your preferences.

- **Skill Endorsement Recommender:**  
  Get recommendations on how to boost your professional endorsements and highlight key skills.

- **LinkedIn Profile Enhancer:**  
  Receive actionable tips to improve your LinkedIn profile’s clarity, impact, and SEO.

- **Virtual Career Fair Navigator:**  
  Discover upcoming virtual career fairs with event details and recommendations on which events to attend.

- **Mentorship Matchmaker:**  
  Find mentors aligned with your career goals and receive tips on how to approach potential mentors.

- **Personal Development Tracker:**  
  Create a personalized development plan with milestones, recommended courses, and suggestions for skill improvement.

## Technologies Used

- **Streamlit:** For building the interactive web application.
- **LLMPipeline:** A custom module that uses `langchain-groq` and `langchain_core` to interact with AI language models.
- **Unstructured:** For parsing and partitioning uploaded documents (with PDF support).
- **Python-dotenv:** For loading environment variables.
- **Optional:** OCR libraries such as `pytesseract` and `Pillow` (if scanned document support is needed).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AdnanSattar/career-development-suite.git
   cd career-development-suite

## Install Dependencies:

Ensure you have Python 3.8+ installed. Then, install the required dependencies:

``` bash
Copy
pip install -r requirements.txt
```
## The requirements.txt includes:

### Streamlit for the web app interface
```streamlit
```
### LLM pipeline components (adjust version numbers as appropriate)
```
langchain_core
langchain-groq
```

### Unstructured package with PDF support for processing CV files (ensure PDF extras are installed)
```
unstructured[pdf]
```
### Environment variable loader
```
python-dotenv
```
### Optional: OCR support for scanned documents
```
pytesseract
Pillow
```

## Configure Environment Variables:

Create a .env file in the project root and add your API keys. For example:

```
GROQ_API_KEY=your_groq_api_key_here
```

## Running the Application
To launch the application, run:

```bash
Copy
streamlit run main.py
```
This will start the app and open it in your default web browser. Use the sidebar to navigate between the different tools.

Project Structure

```
.
├── main.py                          # Main entry point with sidebar navigation
├── llm_pipeline.py                  # Module for LLM interactions (LLMPipeline class)
├── utils.py                         # Utility functions (e.g., text cleaning)
├── smart_resume_optimizer.py        # Smart Resume Optimizer module
├── career_path_advisor.py           # Career Path Advisor module
├── personal_branding_assistant.py   # Personal Branding Assistant module
├── interview_followup_email.py      # Interview Follow-up Email Generator module
├── networking_opportunity_finder.py # Networking Opportunity Finder module
├── salary_negotiation_advisor.py      # Salary Negotiation Advisor module
├── job_search_aggregator.py         # Job Search Aggregator module
├── skill_endorsement_recommender.py # Skill Endorsement Recommender module
├── linkedin_profile_enhancer.py     # LinkedIn Profile Enhancer module
├── virtual_career_fair_navigator.py # Virtual Career Fair Navigator module
├── mentorship_matchmaker.py         # Mentorship Matchmaker module
├── personal_development_tracker.py  # Personal Development Tracker module
├── requirements.txt                 # List of project dependencies
└── README.md                        # This file
```

### Usage
Navigation:
Use the sidebar to select one of the available tools. Each tool is designed to help you with a specific aspect of your career development.

### Example:
To generate a cover letter, select "Cover Letter & Interview Prep Generator" from the sidebar, upload your CV, enter the job description, and follow the prompts to generate and refine your cover letter.

## Contributing
Contributions are welcome! To contribute:

## Fork the repository.
```
Create a new branch: git checkout -b feature/your-feature
Commit your changes: git commit -am 'Add some feature'
Push to your branch: git push origin feature/your-feature
Create a new Pull Request.
```

## License
This project is licensed under the MIT License.

# Contact Author
Adnan Sattar
adnansattar09@gmail.com
https://www.linkedin.com/in/adnansattar09/


Happy coding and best of luck with your career development journey!