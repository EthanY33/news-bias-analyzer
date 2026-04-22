# AI Usage Report

## Tools Used

- Cursor for in-editor code assistance during development.
- Gemini 2.5 Flash via the Google AI Studio free tier as the runtime LLM
  the tool calls to do the analysis.
- `google-genai` Python SDK as the client library.

## Example Prompts (to the coding assistant)

1. "Write a small Python CLI that takes N article file paths as arguments
   and reads them. Standard library only for I/O."
2. "Show the minimum code to call Gemini via the `google-genai` SDK with
   one text prompt and print the response."
3. "Write a prompt that forces the model to output exactly three markdown
   sections: per-article analysis, perspective comparison, balanced
   summary."
4. "The model keeps prefixing 'Here is your analysis:'. How do I stop it?"
5. "The summary leans toward whichever article comes last. What prompt
   change makes it strip loaded language instead of averaging tone?"
6. "Give me two short fake news articles on the same event with opposite
   framing so I can test the analyzer."
7. "What's the safe way to handle an API key in a small Python repo I'm
   pushing to GitHub?"
8. "I'm getting `404 models/gemini-1.5-flash is not found`. What's the
   current model name and SDK?"

## What AI Helped With

- Getting the Gemini SDK call right without reading the full docs.
- Iterating quickly on the prompt wording, which is what most of the
  output quality depends on.
- Writing two contrasting sample articles to test against without having
  to find real ones.
- Boilerplate like `.gitignore` and the README skeleton.

## What I Modified or Fixed

- The first scaffold used `argparse` with named flags. Replaced with
  positional `sys.argv` because the tool only takes a list of files.
- The first prompt was long and chatty. Trimmed to just the structure
  the model needed to follow.
- The assistant suggested wrapping the API call in try/except with
  retries. Removed it, since for a one-shot CLI a plain crash is more
  useful than a silent retry.
- Added an explicit `GEMINI_API_KEY` check up front so the tool fails
  fast with a clear message instead of failing inside the SDK.
- Sample articles were too long initially. Shortened them so the demo
  runs in a couple of seconds.
- The first version used `google-generativeai` and `gemini-1.5-flash`,
  both of which are now deprecated. Migrated to `google-genai` and
  `gemini-2.5-flash`.

## What I Learned

- The output is mostly a function of the prompt. Specifying the exact
  output structure helped much more than describing what I wanted in
  prose.
- The assistant adds things I don't need by default (retries, argparse,
  logging). A lot of the work was deleting that.
- For libraries I haven't used, the assistant got me to a working call
  faster than reading the docs would have.
- AI suggestions can be outdated. The first SDK and model name it gave
  me were both deprecated and I had to debug the 404 myself.
- The output of the analyzer needs human checking. The model's idea of
  "balanced" sometimes wasn't, and I only caught it because I read it.
