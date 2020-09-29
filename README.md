# About

This is a simple tool to extract potential web endpoints (relative URLs) from
a file or stdin, based on some heuristics. Useful when bug hunting.

It's similar to jobertabma's [relative-url-extractor][relative-url-extractor],
except it's written in Python and can also receive input from stdin, since
I often use commands in a pipeline. It also allows some additional characters
which are valid in an URL so it will catch some additional endpoints.

[relative-url-extractor]:
<https://github.com/jobertabma/relative-url-extractor>

# Usage

- `relative-urls some-file.js another-file.js`
- `curl https://some-url.com/ | relative-urls`
