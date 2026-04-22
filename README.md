# News Bias Analyzer

A command-line tool that takes two or more news articles on the same topic and
produces a bias/perspective analysis: per-article sentiment and tone, a
side-by-side perspective comparison, and a balanced neutral summary.

Built for CS485 "Build with AI: Applied Programming Project" (Project 12).

## Dependencies

- Python 3.9+
- [`google-generativeai`](https://pypi.org/project/google-generativeai/)
- A free Gemini API key from https://aistudio.google.com/app/apikey

## Setup

```bash
pip install -r requirements.txt
export GEMINI_API_KEY=your_key_here        # macOS / Linux
set GEMINI_API_KEY=your_key_here           # Windows cmd
$env:GEMINI_API_KEY="your_key_here"        # PowerShell
```

## Run

```bash
python main.py examples/article1.txt examples/article2.txt
```

Pass as many article files as you want (minimum two). Each file should contain
plain text of one article.

## Output

The tool prints a markdown report with three sections:

1. **Per-Article Analysis** — sentiment, tone, loaded language, framing
2. **Perspective Comparison** — wording, emphasis, and framing differences
3. **Balanced Summary** — neutral combined summary
