import os
from dotenv import load_dotenv
from crewai import LLM, Agent, Task, Crew, Process
from PyPDF2 import PdfReader 

load_dotenv()

my_llm = LLM(
    model="groq/llama-3.3-70b-versatile", 
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1 
)

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

cv_content = read_pdf("cv.pdf") 

print("\n" + "="*50)
print("Agentic Auditor v4.0 ")
print("==================================================")
print("Paste the JD below (type 'DONE' on a new line):")
lines = []
while True:
    line = input()
    if line.strip().upper() == 'DONE': break
    lines.append(line)
job_description = "\n".join(lines)


auditor = Agent(
    role='Technical Fact-Checker',
    goal='Identify exactly what is present and what is MISSING without any fluff.',
    backstory='You are a senior technical auditor. You believe ONLY in the CV text. If a skill like "Angular" is not in the CV, you mark it as a "CRITICAL GAP".',
    llm=my_llm,
    verbose=True
)

strategist = Agent(
    role='Learning Path Architect',
    goal='Create a realistic study plan to fill technical gaps.',
    backstory='You do not over-index on problem-solving scores. You focus on hands-on tools like .NET Core, Microservices, and SQL optimization that the candidate MUST learn.',
    llm=my_llm,
    verbose=True
)

task1 = Task(
    description=f"""
    1. Extract ALL technologies from the CV: {cv_content}.
    2. Compare them with the JD: {job_description} and mention the match score .
    3. List the 'Hard Gaps' (Technologies in JD but NOT in CV). 
    DO NOT assume she knows anything not written. and mention the Experience Gap , If JD asks for 4 years and she has 1, state: 'Experience Gap: 3 Years'.
    """,
    expected_output="A factual Gap Analysis table (Tech, Status, Action Needed).",
    agent=auditor
)

task2 = Task(
    description=f"""
    Based on the 'Hard Gaps' from the previous task, create a 4-week study roadmap.
    Focus on:
    - The .NET frameworks she hasn't used yet.
    - Architectural patterns (Microservices/Design Patterns) missing.
    Stop mentioning the 1200 PS score as a magic solution; treat it only as a proof of basic logic.
    """,
    expected_output="A 4-week learning plan to match the JD requirements.",
    agent=strategist,
    context=[task1]
)

task3 = Task(
    description=f"""
    Rewrite the CV 'Professional Summary' using ONLY the following facts:
    - Tech Stack: C#, .NET, ASP.NET, SQL Server, Entity Framework.
    - Experience: Fresh Graduate / Internships DEPI.
    - Achievements: ECPC Finalist.
    CRITICAL: If a technology (like React/Angular/VB) is NOT in the CV, do NOT mention it. Keep it 100% honest.
    """,
    expected_output="A clean, honest Professional Summary and a list of 5 'Honest Interview Questions' for the HR.",
    agent=auditor,
    context=[task1, task2]
)


career_crew = Crew(
    agents=[auditor, strategist],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    verbose=True
)

print("\n### System is auditing your profile factually... ###\n")
result = career_crew.kickoff()
print(result)