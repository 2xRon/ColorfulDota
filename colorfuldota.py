"""Colorful Dota. Replaces markers with special codes that correspond to certain text colors in Dota 2's chatbox. DEPRECATED. Volvo PLS."""

import sys, re, argparse

try:
    import pyperclip
except ImportError:
    HASCLIP = False
else:
    HASCLIP = True

colordict = {
    "olive": "\x10",
    "pink": "\x11",
    "red": "\x12",
    "orange": "\x13",
    "darkyellow": "\x14",
    "lightgreen": "\x15",
    "purple": "\x16",
    "grey": "\x17",
    "green": "\x18",
    "blue": "\x19",
    "white": "\x0B",
    "limegreen": "\x0C",
    "hotpink": "\x0E",
    "violet": "\x1A",
    "magenta": "\x1C",
    "yellow": "\x1F",
    "default": "\x06",
}
description = __doc__ + "\nAvalible colors: " + ", ".join(colordict.keys())

delimiter_match = {
    "(": ("((", "))"),
    ")": ("((", "))"),
    "[": ("[[", "]]"),
    "]": ("[[", "]]"),
    "{": ("{{", "}}"),
}


def main():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-d",
        "--delimiter",
        type=str,
        help="Set the delimiter for color names. Uses a matched delimiter for (, [ or {. Delimiters should be used like '[[color]]' or '//color//'.",
    )
    parser.add_argument(
        "-c",
        "--copy",
        action="store_true",
        help="Copy output to system clipboard. Requires pyperclip.",
    )
    parser.add_argument(
        "-t",
        "--entrytext",
        type=str,
        nargs=argparse.REMAINDER,
        required=True,
        help="Message to process",
    )
    args = parser.parse_args()
    entrytext = " ".join(args.entrytext)

    if args.delimiter:
        # for delimiters without a matching pair, use the same symbol twice
        default_d = (args.delimiter + args.delimiter, args.delimiter + args.delimiter)
        d = delimiter_match.get(args.delimiter, default_d)
    else:
        d = delimiter_match["("]

    pattern = re.compile(rf"{re.escape(d[0])}(.*?){re.escape(d[1])}", flags=re.DOTALL)
    outtext = pattern.sub(lambda x: colordict.get(x.group(0)[2:-2], None), entrytext)
    print(outtext)
    if HASCLIP and args.copy:
        pyperclip.copy(outtext)


if __name__ == "__main__":
    main()
