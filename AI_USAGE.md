# AI Usage Report

## Tools Used

- **Cursor** — editor with inline AI for scaffolding, refactoring,
  and debugging during development.
- **Google Gemini 1.5 Flash** — runtime LLM used by the tool itself
  to analyze articles (free tier via Google AI Studio).
- **`google-generativeai`** Python SDK — client library for calling
  the Gemini API.

## Example Prompts

Prompts I used during development (to the coding assistant, not to Gemini
at runtime):

1. "Scaffold a small Python CLI that takes N article file paths as
   arguments and reads them into memory. Use only the standard library
   for the I/O."
2. "Show me the minimum code to call Gemini 1.5 Flash via the
   `google-generativeai` SDK with a single text prompt and print the
   response."
3. "Write a prompt that makes the model output exactly three markdown
   sections: per-article analysis, perspective comparison, and balanced
   summary. Constrain the structure tightly."
4. "The model keeps prefixing responses with 'Here is your analysis:'.
   How do I suppress that?"
5. "My balanced summary is echoing the tone of the last article. What
   prompt change would force it to strip loaded language instead of
   averaging it?"
6. "Give me two short sample news articles on the same fictional event
   with clearly opposed framing — one pro-business, one labor-focused —
   so I can test the analyzer."
7. "What's a safe pattern for handling an API key in a small Python
   project that I'm pushing to GitHub?"
8. "Write a concise README that explains how to install dependencies,
   set the API key on Windows and Unix, and run the tool."

## What AI Helped With

- Getting the Gemini SDK call right on the first try (easy to miss
  `genai.configure` or the model name format).
- Iterating on the system prompt — the analysis quality is almost
  entirely a function of prompt wording, and fast iteration with an
  AI was the fastest way to converge.
- Drafting the two sample articles with deliberately opposed framing,
  which made it possible to sanity-check the output without scraping
  real news.
- Writing boilerplate docs (README sections, .gitignore).

## What I Modified or Fixed

- The AI's first scaffold used `argparse` with three named flags — I
  replaced it with positional `sys.argv` because the tool only takes
  a list of files and doesn't need flags.
- The AI's initial prompt was long and chatty; I trimmed it to the
  exact markdown structure and dropped hedging language so the model
  would stop adding meta-commentary.
- The AI suggested wrapping the API call in a try/except and retrying
  on failure. I removed that — for a one-shot CLI, a plain crash is
  more useful than a silent retry loop.
- I added an explicit check for the `GEMINI_API_KEY` env var up front
  so the tool fails fast with a clear message instead of deep inside
  the SDK.
- Sample articles were originally too long; I shortened them so the
  end-to-end demo runs under a couple of seconds.

## What I Learned About Using AI

- **Tight prompts beat long prompts.** The single biggest quality jump
  came from specifying the exact markdown structure rather than
  describing what I wanted in prose.
- **The AI over-engineers by default.** It added retries, argparse,
  logging, and exception handling I didn't need. Stripping those out
  was most of the editing work.
- **AI is great for the unfamiliar parts.** I hadn't used the Gemini
  SDK before — getting the first working call took maybe a minute with
  AI assistance instead of a trip through the docs.
- **Verify, don't trust.** When the balanced summary came back leaning
  one way, I only noticed because I read it. An AI won't flag its own
  bias — you have to test with adversarial inputs (which is why the
  sample articles are deliberately opposed).
- **AI-generated code is a starting point, not a finish line.** Most
  of what the assistant produced needed at least one round of
  simplification before it matched what the project actually needs.
