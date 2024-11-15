#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2024 Daniel Lima
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import string
import secrets
import sys

lowercase: str = string.ascii_lowercase
uppercase: str = string.ascii_uppercase
numbers: str = string.digits
symbols: str = string.punctuation


def gen_password(chars: str, length: int) -> str:
    return "".join([secrets.choice(chars) for _ in range(length)])


def parser() -> tuple[str, int]:
    chars = [lowercase, uppercase, numbers, symbols]
    length = 32

    if len(sys.argv) < 2:
        print("Error: ")
        sys.exit(1)

    if sys.argv[1] in ["-h", "--help"]:
        print("""
Password Generator
Usage:
    python script.py [options]

Options:
    --no-lowercase    Exclude lowercase letters
    --no-uppercase    Exclude uppercase letters
    --no-numbers      Exclude numbers
    --no-symbols      Exclude symbols
    -l <length>       Specify the length of the password (default: 32)
    -h, --help        Show this help message
    """)
        sys.exit(0)

    # Options
    options = {
        "--no-lowercase": lowercase,
        "--no-uppercase": uppercase,
        "--no-numbers": numbers,
        "--no-symbols": symbols,
    }
    for option, char_set in options.items():
        if option in sys.argv:
            chars.remove(char_set)

    # Password Lenght
    if "-l" in sys.argv:
        index = sys.argv.index("-l")
        try:
            length = int(sys.argv[index + 1])
        except IndexError:
            print("Error: null password lenght.")
            sys.exit(1)
        except ValueError:
            print("Error: invalid password lenght.")
            sys.exit(1)

    if length <= 0:
        print("Error: Password length must be a positive integer.")
        sys.exit(1)

    if not chars:
        print("Error: No character types selected.")
        sys.exit(1)

    return ("".join(chars), length)


def main() -> None:
    chars, length = parser()
    password = gen_password(chars, length)
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
