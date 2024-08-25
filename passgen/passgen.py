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

import argparse

from passwordgenerator import PasswordGenerator
from config import Config

class App:

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            prog="passgen",
            description="A CLI password generator made with python"
        )
        self.parser.add_argument("-l", 
                                "--length",
                                type=int,
                                dest="length",
                                required=True,
                                help="The password length")
        self.parser.add_argument("--no-numbers", 
                                action="store_false",
                                dest="use_numbers",
                                help="Don't use numbers")
        self.parser.add_argument("--no-uppercase",
                                action="store_false",
                                dest="use_uppercase",
                                help="Don't use uppercase")
        self.parser.add_argument("--no-lowercase",
                                action="store_false",
                                dest="use_lowercase",
                                help="Don't use lowercase")
        self.parser.add_argument("--no-symbols",
                                action="store_false",
                                dest="use_symbols",
                                help="Don't use symbols")

    def run(self) -> None:
        args = self.parser.parse_args()
        pg: object = PasswordGenerator(Config(
            args.length,
            args.use_lowercase,
            args.use_uppercase,
            args.use_numbers,
            args.use_symbols
        ))

        password = pg.gen_password()
        print(f"Generated password: {password}")

if __name__ == "__main__":
    app = App()
    app.run()