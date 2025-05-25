# Password Generator (CLI)

A simple and customizable command-line password generator written in Python.

## Features

- Generate secure, random passwords
- Choose which character sets to include (lowercase, uppercase, digits, symbols)
- Define password length
- Easy to use, no external dependencies

## Installation

Clone the repository or copy the script locally:

```bash
git clone https://github.com/limadaniel70/passgen.git
cd password-generator
```

## Usage

```bash
python passgen.py [options]
```

| Option                  | Description                       |
| ----------------------- | --------------------------------- |
| `--no-lowercase`, `-nl` | Exclude lowercase letters         |
| `--no-uppercase`, `-nu` | Exclude uppercase letters         |
| `--no-numbers`, `-nn`   | Exclude digits                    |
| `--no-symbols`, `-ns`   | Exclude symbols                   |
| `-l <length>`           | Set password length (default: 32) |
| `-h`, `--help`          | Show help message                 |

## Examples

Generate a 16-character password with all character sets:

```bash
python script.py -l 16
```

Generate a 24-character password with no symbols:

```bash
python script.py -ns -l 24
```

Generate a password with only numbers:

```bash
python script.py -nl -nu -ns -l 10
```

Show help:

```bash
python script.py --help
```

## Example Output

```bash
$ python script.py -l 20

Generated Password:
────────────────────────
 *w8iv7@-Hrw#Z^xu!wby
────────────────────────
```
