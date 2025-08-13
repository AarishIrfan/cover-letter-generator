from ollama import chat

def polish_letter(letter_text, job_description=None, language="EN"):
    """
    Polishes a cover letter using Ollama 2 (Llama2) locally.
    Supports English and German letters based on the 'language' parameter.
    Correctly extracts content from ChatResponse.
    """
    # Instruction tailored to language
    instruction = "Polish the following cover letter in English"
    if language.upper() == "DE":
        instruction = "Polish the following cover letter in German"

    prompt = f"""
{instruction} to make it clear, professional,
and tailored to the job description if provided.

Cover Letter:
{letter_text}

Job Description (optional):
{job_description or ""}
"""

    try:
        response = chat(
            model="llama2",
            messages=[{"role": "user", "content": prompt}]
        )

        # Correctly access content
        if response and hasattr(response, "message") and hasattr(response.message, "content"):
            return response.message.content.strip()
        else:
            return "Error: No response from the model."

    except Exception as e:
        return f"Error: Exception occurred while calling Ollama: {e}"
