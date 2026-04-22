import os
import sys
from google import genai


PROMPT_TEMPLATE = """You are a news bias analyzer. Below are {n} articles from different
sources covering the same topic. Analyze them and respond in this exact markdown structure:

## Per-Article Analysis
For each article, include:
- Source / filename
- Overall sentiment: positive / negative / neutral
- Emotional tone (e.g., alarming, reassuring, outraged, cautious)
- Loaded or emotional language (quote 2-4 specific phrases)
- Likely framing / perspective

## Perspective Comparison
- Key wording differences between sources
- What each source emphasizes vs downplays
- Framing differences (who is portrayed as the hero / villain / victim)

## Balanced Summary
A single neutral paragraph combining all viewpoints, with loaded language stripped out.

ARTICLES:
{articles}
"""


def read_articles(paths):
    articles = []
    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            articles.append((os.path.basename(path), f.read().strip()))
    return articles


def build_prompt(articles):
    joined = "\n\n".join(
        f"=== Article {i + 1}: {name} ===\n{text}"
        for i, (name, text) in enumerate(articles)
    )
    return PROMPT_TEMPLATE.format(n=len(articles), articles=joined)


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <article1.txt> <article2.txt> [article3.txt ...]")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: set GEMINI_API_KEY environment variable.")
        print("Get a free key at https://aistudio.google.com/app/apikey")
        sys.exit(1)

    articles = read_articles(sys.argv[1:])
    prompt = build_prompt(articles)

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print(response.text)


if __name__ == "__main__":
    main()
