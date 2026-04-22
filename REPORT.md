# Project Report

## Goal and Design

Show how different outlets cover the same story differently (sentiment,
loaded language, framing), and produce a neutral summary that strips the
bias out.

The tool is one Python script with one LLM call:

1. Read 2+ article text files from the command line.
2. Build a single prompt that includes all of them with delimiters.
3. Send it to Gemini 2.5 Flash and print the response.

I kept it to one call so the model can compare across articles in the same
context. Splitting into separate calls would lose that.

## Assumptions

- Articles are provided as plain text files. No web scraping.
- Articles are about the same topic. The tool does not check this.
- Combined article length fits in the model context window.
- `GEMINI_API_KEY` is set in the environment.
- Content is in English.

## Sample Input / Output

Two bundled sample articles about a Federal Reserve rate hike, one written
in pro-business framing ("responsible", "prudent") and one in labor framing
("squeezing working families", "tone-deaf").

Command:

```
python main.py examples/article1.txt examples/article2.txt
```

Abridged output:

```
## Per-Article Analysis
- article1.txt: positive, reassuring tone. Loaded phrases: "responsible",
  "prudent", "disciplined action". Frames the Fed as a competent steward.
- article2.txt: negative, outraged tone. Loaded phrases: "squeezing
  working families", "crushing mortgage costs", "tone-deaf". Frames the
  Fed as harming workers.

## Perspective Comparison
Article 1 centers investors and business leaders. Article 2 centers
workers, renters, and small businesses. Article 1 emphasizes low
unemployment; Article 2 emphasizes housing and recession risk. Both
quote Powell but frame the quote oppositely.

## Balanced Summary
The Federal Reserve raised its benchmark interest rate by 0.25 percentage
points to continue addressing inflation. Supporters see it as a step
toward stability; critics warn it worsens affordability pressure on
lower-income households and raises recession risk.
```

A third sample article (`examples/article3.txt`) with neutral framing is
also included for testing the N-article path.

## Challenges

- Early prompts produced free-form prose. Fixed by specifying the exact
  three-section markdown structure in the prompt.
- The model sometimes added a "Here is your analysis:" preamble. Removed
  by tightening the opening instruction.
- The balanced summary occasionally leaned toward whichever article came
  last. Fixed by telling the model to strip loaded language rather than
  average the tone.
- The Gemini SDK I started with (`google-generativeai`) is deprecated and
  the `gemini-1.5-flash` name no longer resolves. Migrated to
  `google-genai` and `gemini-2.5-flash`.
- Keeping the API key out of the repo. Used an environment variable and
  added `.env` to `.gitignore`.
