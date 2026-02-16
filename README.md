# Caesar Cipher

A command-line tool to **encrypt** and **decrypt** text using the Caesar cipher with a configurable numeric key. Uses the English alphabet (26 letters).

## Table of Contents

- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Examples](#examples)

---

## Requirements

- **Python 3.6+** (no external dependencies)

---

## Project Structure

```
caesar-cipher/
├── caesar.py      # Core logic: encrypt() and decrypt() with numeric key
├── main.py        # CLI entry point (encrypt/decrypt from command line)
├── requirements.txt
├── README.md
└── tests/
    └── test_caesar.py   # Unit tests
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/caesar-cipher.git
   cd caesar-cipher
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. No extra packages are required; the project uses only the Python standard library.

---

## Usage

From the project root directory:

```bash
python main.py <action> -k <key> [-t <text>]
```

| Argument | Short | Description |
|----------|--------|-------------|
| `action` | — | `encrypt` or `decrypt` |
| `--key` | `-k` | Numeric key (0–26). Required. |
| `--text` | `-t` | Text to process (inline). |

- If `-t` is not given, text is read from **input**.
- Non-alphabetic characters (spaces, digits, punctuation) are left unchanged.

---

## Running Tests

Run all unit tests:

```bash
python -m unittest tests.test_caesar -v
```

---

## Examples

**Encrypt** the string `HOLA` with key `3`:

```bash
python main.py encrypt -k 3 -t "HOLA"
# Output: KRÑD
```

**Decrypt** the previous result:

```bash
python main.py decrypt -k 3 -t "KRÑD"
# Output: HOLA
```

**Decrypt** from input (type or paste text):

```bash
python main.py decrypt -k 7
```
