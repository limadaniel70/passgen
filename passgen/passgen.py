#!/usr/bin/env python
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

def gen_password(chars: str, len: int) -> str:
    return ''.join([secrets.choice(chars) for _ in range(len)])

def parser() -> tuple[str, int]:
    chars = [lowercase, uppercase, numbers, symbols]
    lenght = 32
    if len(sys.argv) < 2:
        print("Error: ")
        sys.exit(1)

    if sys.argv[1] in ["-h", "--help"]:
        print("Usage: ")
        sys.exit(0)

    if "--no-lowercase" in sys.argv:
        chars.remove(lowercase)
    if "--no-uppercase" in sys.argv:
        chars.remove(uppercase)
    if "--no-numbers" in sys.argv:
        chars.remove(numbers)
    if "--no-symbols" in sys.argv:
        chars.remove(symbols)

    if not chars:
        print("")
        sys.exit(1)

    return (''.join(chars), lenght)

def main() -> None:
    chars, lenght = parser()
    password = gen_password(chars, lenght)
    print(f"Generated password: {password!r}")

if __name__ == "__main__":
    main()