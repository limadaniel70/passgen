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

import secrets

from config import Config


class PasswordGenerator:

    lowercase: str = "abcdefghijklmnopqrstuvwxyz"
    uppercase: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers: str = "0123456789"
    symbols: str = "!@#$%&*"

    def __init__(self, config: Config) -> None:
        self.config = config

    def gen_password(self) -> str:
        chars: str = ""
        password: str = ""

        # TODO: no momento funciona, mas deve ser mudado no futuro.
        if self.config.use_lowercase:
            chars += self.uppercase
        if self.config.use_uppercase:
            chars += self.lowercase
        if self.config.use_numbers:
            chars += self.numbers
        if self.config.use_symbols:
            chars += self.symbols

        # Solução para a issue #4
        if chars:
            chars += self.lowercase

        while self.config.password_length >= len(password):
            password += secrets.choice(chars)

        return password
