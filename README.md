markdown
# Cover Letter Generator with Ollama 2 (Llama2)

A Python-based tool that helps job seekers automatically generate and polish cover letters using AI. It supports both English and German and saves polished letters to an output folder.

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/AarishIrfan/cover-letter-generator.git
cd cover-letter-generator
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
ollama pull llama2
````

## Usage

```bash
python main.py
```

* Follow the prompts in the terminal to enter language, company, position, skills, hiring manager, company goal, and your name.
* Optionally, provide a job description for AI polishing.
* Your polished cover letter will appear in the terminal and be saved in the `output/` folder.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests or templates as appropriate.
