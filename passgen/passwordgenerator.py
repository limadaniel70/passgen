import random
from passgen.config import Config


class PasswordGenerator:

    lowercase: list[str] = list("abcdefghijklmnopqrstuvwxyz")
    uppercase: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers: list[str] = list("0123456789")
    symbols: list[str] = list("!@#$%&*")

    def __init__(self, config: Config) -> None:
        self.config = config

    def gen_password(self) -> str:
        chars: list[str] = []
        password: str = ""

        if self.config.use_lowercase:
            chars += self.uppercase
        elif self.config.use_uppercase:
            chars += self.lowercase
        elif self.config.use_numbers:
            chars += self.numbers
        elif self.config.use_symbols:
            chars += self.symbols

        i = 0
        while i < self.config.password_length:
            password += chars[random.randint(0, len(chars))]
            i += 1

        return password
