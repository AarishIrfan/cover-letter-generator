from llm_chain import polish_letter
import os

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# English and German templates
EN_TEMPLATE = """Dear {hiring_manager},

I am excited to apply for the {position} role at {company}.
With my background in {skills}, I believe I can contribute to {company_goal}.

Sincerely,
{your_name}
"""

DE_TEMPLATE = """Sehr geehrte/r {hiring_manager},

Ich freue mich, mich für die Position {position} bei {company} zu bewerben.
Mit meinen Kenntnissen in {skills} kann ich zum Ziel beitragen: {company_goal}.

Mit freundlichen Grüßen,
{your_name}
"""

print("=== Cover Letter Generator with Ollama 2 ===")

# Collect user input
language = input("Choose language (EN/DE): ").strip().upper()
company = input("Company name: ").strip()
position = input("Position title: ").strip()
manager = input("Hiring manager name: ").strip()
skills = input("Your main skills (comma separated): ").strip()
goal = input("One company goal you like: ").strip()
your_name = input("Your name: ").strip()
job_description = input("Optional: Job description for AI polishing (press Enter to skip): ").strip()

# Select template based on language
template = DE_TEMPLATE if language == "DE" else EN_TEMPLATE

# Fill template
letter_text = template.format(
    hiring_manager=manager,
    position=position,
    company=company,
    skills=skills,
    company_goal=goal,
    your_name=your_name
)

# Polish with Ollama 2
polished = polish_letter(letter_text, job_description, language)

# Print result
print("\n=== Polished Cover Letter ===\n")
print(polished)

# Save to file
filename = f"output/{company}_{position}.txt".replace(" ", "_")
with open(filename, "w", encoding="utf-8") as f:
    f.write(polished)

print(f"\nSaved polished letter to {filename}")
