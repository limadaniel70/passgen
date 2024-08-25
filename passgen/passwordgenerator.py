import random
from config import Config


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

        # TODO: no momento funciona, mas deve ser mudado no futuro.
        if self.config.use_lowercase:
            chars += self.uppercase
        if self.config.use_uppercase:
            chars += self.lowercase
        if self.config.use_numbers:
            chars += self.numbers
        if self.config.use_symbols:
            chars += self.symbols

        while self.config.password_length >= len(password):
            password += chars[random.randint(0, len(chars) - 1)]

        return password
