import sys
import re

URL_REGEX = r'''^.*?("|')(https?://[a-zA-Z0-9.-]+)?(/[\w\d.~:/?#@!$&()*+,;%=[{}\]-]*?)(\1).*?$'''

HELP = """Usage: {} [FILE...]

Extract endpoints (relative URLs) from either stdin or file(s) passed as
arguments. If files are passed, stdin is ignored."""


def decode_and_sanitize(bs):
    content = bs.decode("ascii", "replace")
    content = re.sub(r";\s*$", "\n", content)
    return content


def extract_endpoints(content):
    content = decode_and_sanitize(content)

    endpoints = set()

    for line in content.splitlines():
        for url in re.findall(URL_REGEX, line):
            endpoints.add(url[2])

    return endpoints


def main():
    if sys.argv[1] in ["-h", "--help"]:
        print(HELP.format(sys.argv[0]))
        sys.exit(0)

    endpoints = set()

    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            with open(path, "rb") as file:
                endpoints.update(extract_endpoints(file.read()))
    else:
        endpoints.update(extract_endpoints(sys.stdin.buffer.read()))

    endpoints.discard("/")

    for endpoint in sorted(endpoints):
        print(endpoint)
