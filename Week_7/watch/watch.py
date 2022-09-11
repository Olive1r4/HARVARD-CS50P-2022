import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    url = re.search(r"^<.*https?://(?:www\.)?(youtu)be\.com/em(be)d/([a-zA-Z0-9]+)", s, re.IGNORECASE.MULTILINE)
    if url:
        return (f"https://{url.group(1)}.{url.group(2)}/{url.group(3)}")
    else:
        return None


if __name__ == "__main__":
    main()