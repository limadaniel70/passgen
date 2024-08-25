class Config:

    def __init__(
        self,
        password_length: int,
        use_lowercase: bool = True,
        use_uppercase: bool = True,
        use_numbers: bool = True,
        use_symbols: bool = True,
    ) -> None:
        self.password_length = password_length 
        self.use_lowercase = use_lowercase
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols
