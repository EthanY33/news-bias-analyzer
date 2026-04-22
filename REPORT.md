# Project Report — News Bias Analyzer

## Goal and Design

The goal is to help a reader see how different news outlets cover the same
event differently — what sentiment they carry, what language they load,
and what framing they push — and then get a single neutral summary that
strips those biases out.

The design is intentionally minimal: one Python script, one LLM call.

1. Read 2+ article text files passed on the command line.
2. Concatenate them into a single prompt with clear delimiters.
3. Ask Gemini 1.5 Flash (free tier) to produce a structured markdown
   report: per-article analysis, perspective comparison, balanced summary.
4. Print the result.

Keeping it to one LLM call is a deliberate choice — the model can reason
across all the articles at once, which is exactly what "perspective
comparison" requires. Splitting the analysis into separate calls per
article would lose that cross-article context.

## Assumptions

- User provides articles as plain text files (no scraping).
- Articles are on the same topic — the tool does not verify this.
- Article length fits comfortably in the model's context window
  (Gemini 1.5 Flash handles 1M tokens, so this is not a practical limit).
- User has a Gemini API key set in the `GEMINI_API_KEY` environment variable.
- English-language content (the model can handle others, but prompts were
  tuned for English).

## Sample Input / Output

**Input:** Two bundled sample articles about a Federal Reserve rate hike
written with opposite framing — one pro-business ("responsible", "prudent",
"measured"), one labor-focused ("squeezing working families", "tone-deaf").

**Command:**

```bash
python main.py examples/article1.txt examples/article2.txt
```

**Output (abridged):**

```
## Per-Article Analysis
- article1.txt: positive sentiment, reassuring/confident tone. Loaded
  phrases: "responsible", "prudent", "disciplined action". Framing:
  Fed as competent steward of the economy.
- article2.txt: negative sentiment, outraged/sympathetic tone. Loaded
  phrases: "squeezing working families", "crushing mortgage costs",
  "tone-deaf". Framing: Fed as out-of-touch actor harming workers.

## Perspective Comparison
- Article 1 centers Wall Street, investors, economists. Article 2
  centers workers, renters, small businesses.
- Article 1 emphasizes low unemployment; Article 2 emphasizes housing
  collapse and recession risk. Both cite the same rate hike and the
  same Chair Powell quote but frame them oppositely.

## Balanced Summary
The Federal Reserve raised its benchmark interest rate by 0.25
percentage points on Wednesday as part of its ongoing effort to reduce
inflation. The move was expected by markets. Supporters argue it
protects long-term stability; critics warn it worsens affordability
pressures on lower-income households and raises recession risk.
```

## Challenges

- **Prompt stability:** early drafts returned free-form prose that was
  hard to read. Fixed by specifying the exact markdown section
  structure in the prompt.
- **Avoiding meta-commentary:** Gemini sometimes added a preamble like
  "Here is your analysis:". Removed by tightening the prompt's opening
  instruction ("respond in this exact markdown structure").
- **Keeping the balanced summary actually balanced:** the model
  occasionally leaned toward whichever article appeared last. Fixed by
  explicitly instructing it to strip loaded language rather than to
  "average" the tone.
- **API key handling:** keeping the key out of the repo. Solved with an
  environment variable plus `.gitignore` for `.env`.
