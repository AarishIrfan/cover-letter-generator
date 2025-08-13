```markdown
# Cover Letter Generator with Ollama 2 (Llama2)

A Python-based tool that helps job seekers automatically generate and polish cover letters using AI. The project leverages Ollama 2 (Llama2) for natural language generation and supports both English and German cover letters. It is ideal for applicants who want tailored, professional, and error-free cover letters in minutes.

---

## Features

- Generate cover letters for any position and company.
- Supports English (EN) and German (DE) languages.
- Tailor letters with your skills, company goals, and optional job descriptions.
- Polishes existing letters using Ollama 2 AI for clarity, professionalism, and better tone.
- Saves polished letters automatically to an `output/` folder.
- Handles multiple letters efficiently with consistent formatting.

---

## Tech Stack and Tools

- Language: Python 3.11+  
- AI Model: Ollama 2 (Llama2) local model  
- Python Libraries:
  - ollama (for calling Llama2 locally)  
  - os (for file and folder management)  
- Environment: Virtual environment (venv) recommended
- IDE: VS Code (recommended for development and running scripts)

---

## Project Structure

```

cover-letter-generator/
│
├─ llm\_chain.py         # Functions to polish letters using Ollama 2
├─ main.py              # Main script for user input and letter generation
├─ output/              # Folder where polished letters are saved
├─ venv/                # Virtual environment
├─ README.md            # Project documentation
└─ requirements.txt     # Python dependencies

````

---

## How It Works

1. User Input:  
   Enter language, company, position, skills, hiring manager, company goal, your name, and optional job description.

2. Template Selection:  
   The script selects either the English or German template.

3. Letter Generation:  
   - Fills the selected template with your information.  
   - Sends the letter to Ollama 2 (Llama2) for polishing.

4. Polished Letter Output:  
   - Prints the final polished letter in the terminal.  
   - Saves it automatically to the `output/` folder as `{company}_{position}.txt`.

5. AI Polishing:  
   - The AI improves clarity, professionalism, and tone.  
   - Ensures proper grammar and formatting.  
   - Can translate to German if requested.

---

## Setup and Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd cover-letter-generator
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Pull Llama2 model via Ollama:

```bash
ollama pull llama2
```

---

## Running the Project

```bash
python main.py
```

* Follow the prompts in the terminal.
* Your polished cover letter will appear in the terminal and be saved in `output/`.

---

## Example

Input:

* Language: DE
* Company: OPS GMBH
* Position: QA Tester
* Skills: TestCafe, Playwright
* Hiring Manager: Schmark
* Company Goal: MVPs
* Name: Aarish Irfan

Output (saved in `output/OPS_GMBH_QA_TESTER.txt`):

```
Sehr geehrte/r Schmark,

Ich bin sehr begeistert, mich für die Position des QA Testers bei OPS GMBH zu bewerben. Meine Kenntnisse in TestCafe und Playwright sind ideal für das Ziel der maximalen Verfügbarkeit und Qualität (MVPs) des Unternehmens.

Vielen Dank für die Berücksichtigung meiner Bewerbung. Ich freue mich darauf, diese Gelegenheit mit Ihnen weiter zu besprechen.

Mit freundlichen Grüßen,
Aarish Irfan
```

---

## Notes and Tips

* Make sure Ollama 2 (Llama2) is installed and running locally.
* Use exactly “EN” or “DE” when prompted for language.
* Keep your `output/` folder for storing polished letters.
* Avoid entering too long job descriptions; the AI works best with concise input.

---

## Why This Project is Useful

* Saves time writing and editing cover letters manually.
* Ensures professional, clear, and persuasive content.
* Supports German and English, helping applicants in international environments.
* Easily customizable for personal templates or company-specific tweaks.



