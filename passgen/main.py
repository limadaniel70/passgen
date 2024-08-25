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