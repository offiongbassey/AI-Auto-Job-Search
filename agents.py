from crewai import Agent
from tools import docs_tool, file_tool, web_rag_tool, search_tool
import os

serper_api_key = os.getenv("SEPER_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_model = os.getenv("OPENAI_MODEL")
openai_api_base = os.getenv("OPENAI_API_BASE")

JobSearchAgent = Agent(
    role="Job Researcher",
    goal="Find recent, high-quality remote {title} jobs ({years} yrs experience) using public sources.",
    backstory="""
        A focused online job researcher skilled in using search APIs and platforms like Google Jobs and RemoteOK 
        to find relevant opportunities for {level} engineers.
    """,
    tools=[search_tool],
    verbose=True,
    model=openai_model
)

AnalysisAgent = Agent(
    role="Job Analyst",
    goal="Analyze job listings and suggest best-fit roles and in-demand skills.",
    backstory="""
        A data-driven career strategist with insight into job market trends, ideal roles, and red flags 
        for early-career {title} engineers.
    """,
    tools=[docs_tool, file_tool],
    verbose=True,
    model=openai_model
)

MessageWriterAgent = Agent(
    role="Outreach Message Writer",
    goal="Write effective LinkedIn messages and cold emails for top job picks.",
    backstory="""
        A persuasive tech-savvy communicator who crafts personalized, high-converting outreach messages 
        to help job seekers stand out and connect with recruiters.
    """,
    tools=[docs_tool, file_tool],
    verbose=True,
    model=openai_model
)