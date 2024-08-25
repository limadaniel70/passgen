from passwordgenerator import PasswordGenerator
from config import Config


pg = PasswordGenerator(Config(32))

password = pg.gen_password()
print(password)
