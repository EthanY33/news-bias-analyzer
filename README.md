# News Bias Analyzer

CLI tool that compares two or more news articles on the same topic and prints
a sentiment / framing analysis plus a neutral summary.

CS485 Build with AI project (#12).

## Dependencies

- Python 3.9+
- `google-genai` (https://pypi.org/project/google-genai/)
- A free Gemini API key from https://aistudio.google.com/app/apikey

## Setup

```
pip install -r requirements.txt
```

Set the API key:

```
export GEMINI_API_KEY=your_key       # macOS / Linux
set GEMINI_API_KEY=your_key          # Windows cmd
$env:GEMINI_API_KEY="your_key"       # PowerShell
```

## Run

```
python main.py examples/article1.txt examples/article2.txt
```

You can pass more than two files. Each file should be plain text.

## Output

Markdown to stdout, in three sections:

1. Per-Article Analysis (sentiment, tone, loaded language, framing)
2. Perspective Comparison (wording, emphasis, framing differences)
3. Balanced Summary
