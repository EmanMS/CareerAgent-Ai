# 🚀 Agentic Career Architect v4.0

An autonomous **multi-agent AI system** designed to bridge the gap between **Fresh Graduates** and **high-standard Job Descriptions**.  
The system leverages **Agentic AI** to perform deep resume auditing, factual gap analysis, and professional CV tailoring — **without AI hallucinations**.

---

## 🌟 Key Features

- **PDF Resume Parsing**  
  Automatically extracts and cleans text from professional PDF resumes.

- **Multi-Agent Orchestration**  
  Utilizes specialized AI agents (Auditor, Strategist, Writer) to handle complex career workflows.

- **Factual Gap Analysis**  
  Compares candidate skills against Job Description requirements to generate a **Hard Gap Report** (technologies, experience years, tools).

- **Personalized Study Roadmap**  
  Generates a realistic **4-week learning plan** focused on missing technical stacks.

- **Anti-Hallucination Engine**  
  Implements strict negative constraints and low-temperature settings to ensure **100% factual accuracy**.

- **ATS Optimization**  
  Tailors professional summaries and project descriptions to align with **Applicant Tracking Systems (ATS)**.

---

## 🛠 Tech Stack

- **Language:** Python 3.x  
- **Framework:** CrewAI (Agentic Orchestration)  
- **LLM Provider:** Groq Cloud  
  - Llama-3.3-70B  
  - Llama-3.1-8B  
- **Libraries:**  
  - LangChain  
  - PyPDF2  
  - python-dotenv  
  - LiteLLM  

---

## 🚧 Engineering Challenges & Solutions

Building this project involved solving real-world AI and software engineering problems:

### 1️⃣ The Hallucination Problem
**Challenge:**  
Agents occasionally embellished resumes by adding technologies not present in the CV.

**Solution:**  
- Implemented **Strict Role Prompting**
- Added **Negative Constraints**
- Introduced a dedicated **Technical Auditor Agent**
- Reduced LLM temperature to `0.1` for deterministic outputs

---

### 2️⃣ Dependency & Version Conflicts
**Challenge:**  
Severe conflicts between `openai`, `litellm`, and `mcp` libraries.

**Solution:**  
- Isolated environment using `venv`
- Manually pinned compatible versions  
  (e.g., `mcp==1.16.0`)
- Ensured a stable orchestration layer

---

### 3️⃣ Redundancy in Multi-Agent Communication
**Challenge:**  
Agents repeated CV summaries or JD descriptions in final outputs.

**Solution:**  
- Shifted to a **Sequential Process**
- Implemented **Context Management**
- Defined strict `expected_output` formats so each agent contributes only **new value**

---

### 4️⃣ API Rate Limiting
**Challenge:**  
High-reasoning 70B models quickly hit rate limits.

**Solution:**  
- Optimized token usage
- Used **Llama-3.1-8B-Instant** for lightweight tasks
- Reserved **70B models** for deep auditing and reasoning

---

## 🏗 System Architecture (Agent Roles)

- **Technical Fact-Checker (Auditor)**  
  Compares CV vs. JD with zero assumptions and identifies **Hard Gaps**.

- **Learning Path Architect (Strategist)**  
  Converts gaps into a structured and realistic learning roadmap.

- **Technical CV Surgeon (Writer)**  
  Refines CV language while strictly adhering to the candidate’s actual experience.

---

## 🚀 Getting Started

### Clone the Repository
```bash
git clone https://github.com/EmanSalem/CareerAgent.git
cd CareerAgent

## 📄 Resume Input Requirement

To run the system correctly, the user **must add their CV as a PDF file** inside the project directory.

### Instructions:
1. Prepare your resume in **PDF format only**.
2. Place the file inside the project root (or the designated `resumes/` folder if configured).
3. Update the file path in the configuration or `main.py` if required.

⚠️ **Important Notes**
- Only **PDF resumes** are supported.
- The system will strictly analyze **only the content inside the provided PDF**.
- Any skills or technologies not explicitly mentioned in the CV **will NOT be assumed or added**.


## 🚀 Getting Started

### Setup Virtual Environment
Create and activate a virtual environment:

```bash
python -m venv venv

### activate a virtual environment
Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

###Install Dependencies
```bash
pip install -r requirements.txt

Configure API Key

###Create a .env file and add:
```bash
GROQ_API_KEY=your_api_key_here
