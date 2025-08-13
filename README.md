```markdown
# Cover Letter Generator with Ollama 2 (Llama2)

A Python-based tool that helps job seekers automatically generate and polish cover letters using AI. The project leverages Ollama 2 (Llama2) for natural language generation and supports both English and German. It saves polished letters to an output folder for easy access.

---

## Features

- Generate professional cover letters in minutes.  
- Supports English (EN) and German (DE).  
- Tailors letters to your skills, company goals, and job descriptions.  
- Polishes existing letters with AI for clarity, grammar, and tone.  
- Saves output automatically to the `output/` folder.  

---

## Project Structure

```

cover-letter-generator/
├─ llm\_chain.py      # AI polishing logic with Ollama 2
├─ main.py           # Main script for user interaction
├─ output/           # Generated and polished letters
├─ README.md         # Documentation
└─ requirements.txt  # Dependencies

````

---

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/AarishIrfan/cover-letter-generator.git
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

## What This Project Solves

* Saves time writing and editing cover letters manually.
* Ensures professional, clear, and persuasive content.
* Supports German and English, helping applicants in international environments.
* Easy to customize for personal templates or company-specific tweaks.
