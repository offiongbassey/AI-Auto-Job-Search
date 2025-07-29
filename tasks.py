from crewai import Task
from agents import JobSearchAgent, AnalysisAgent, MessageWriterAgent

JobSearch = Task(
    description="Search and return 5–10 recent remote {title} job postings ({years} yrs experience) as structured JSON.",
    expected_output="A JSON list with job title, company, location, description, and application link.",
    agent=JobSearchAgent,
    output_file="./job-posts/job-results-2.json"
)

Analysis = Task(
    description="Analyze the job data to find best matches for a {level} {title} candidate, common skills, and standout roles.",
    expected_output="3-paragraph summary with top roles, required skills, and any red flags.",
    agent=AnalysisAgent,
    output_file="./job-posts/new-job-analysis-2.md"
)

MessageWriting = Task(
    description="Write LinkedIn messages and cold emails for 3-5 top job entries. Include job title, company, location, tools/stack, and application link in a formatted daily digest.",
    expected_output="A job digest with 2–3 job entries, each containing a recruiter message and cold email.",
    agent=MessageWriterAgent,
    output_file="./job-posts/new-job-post-2.md"
)