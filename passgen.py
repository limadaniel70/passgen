#!/usr/bin/env python3
import string
import secrets
import sys

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
NUMBERS = string.digits
SYMBOLS = string.punctuation

USAGE = """
Password Generator
Usage:
    python passgen.py [options]

Options:
    -nl, --no-lowercase    Exclude lowercase letters
    -nu, --no-uppercase    Exclude uppercase letters
    -nn, --no-numbers      Exclude numbers
    -ns, --no-symbols      Exclude symbols
    -l <length>            Specify the length of the password (default: 32)
    -h, --help             Show this help message
"""


def gen_password(chars: str, length: int) -> str:
    return "".join(secrets.choice(chars) for _ in range(length))


def parse_args(argv: list[str]) -> tuple[str, int]:
    chars = [LOWERCASE, UPPERCASE, NUMBERS, SYMBOLS]
    length = 32

    i = 1
    argc = len(argv)

    if argc < 2:
        return "".join(chars), length
    while i < argc:
        arg = argv[i]
        if arg in ("-h", "--help"):
            print(USAGE)
            sys.exit(0)
        elif arg in ("-nl", "--no-lowercase"):
            chars.remove(LOWERCASE)
            i += 1
        elif arg in ("-nu", "--no-uppercase"):
            chars.remove(UPPERCASE)
            i += 1
        elif arg in ("-nn", "--no-numbers"):
            chars.remove(NUMBERS)
            i += 1
        elif arg in ("-ns", "--no-symbols"):
            chars.remove(SYMBOLS)
            i += 1
        elif arg == "-l":
            if i + 1 >= argc:
                print("Error: missing value for -l\n")
                print(USAGE)
                sys.exit(1)
            try:
                length = int(argv[i + 1])
                if length <= 0:
                    raise ValueError()
            except ValueError:
                print("Error: invalid value for -l. Must be a positive integer.\n")
                print(USAGE)
                sys.exit(1)
            i += 2
        else:
            print(f"Error: unknown argument {arg}\n")
            print(USAGE)
            sys.exit(1)

    if not chars:
        print("Error: no character sets selected. At least one must be enabled.")
        sys.exit(1)

    return "".join(chars), length


def main():
    args = sys.argv
    charset, length = parse_args(args)
    psswrd = gen_password(charset, length)
    print("\n Generated Password:")
    print("-" * (length + 4))
    print(f" {psswrd}")
    print("-" * (length + 4))


if __name__ == "__main__":
    main()
