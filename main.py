from dotenv import load_dotenv
load_dotenv()
import time

from crewai import Crew
from agents import JobSearchAgent, AnalysisAgent, MessageWriterAgent
from tasks import JobSearch, Analysis, MessageWriting
from litellm import RateLimitError

crew = Crew(
    agents=[JobSearchAgent, AnalysisAgent, MessageWriterAgent],
    tasks=[JobSearch, Analysis, MessageWriting],
    verbose=True,
    planning=True
)

for attempts in range(3):
    try:
        result = crew.kickoff()

        print("✅ Crew completed successfully.")
        break
    except RateLimitError as e:
        print(f"Rate Limit hit. Retrying in 20s.... (Attempt: {attempts+1})")
        time.sleep(20)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        break