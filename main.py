import argparse
import sys
from caesar import encrypt, decrypt


def main():
    parser = argparse.ArgumentParser(
        description="Caesar cipher: encrypt or decrypt text with a numeric key."
    )
    parser.add_argument(
        "action",
        choices=["encrypt", "decrypt"],
        help="Action to perform: encrypt or decrypt",
    )
    parser.add_argument(
        "-k",
        "--key",
        type=int,
        required=True,
        metavar="N",
        help="Numeric key (0-26). Example: -k 3",
    )
    parser.add_argument(
        "-t",
        "--text",
        type=str,
        default=None,
        metavar="TEXT",
        help="Text to process (if omitted, read from stdin)",
    )

    args = parser.parse_args()

    if args.text is not None:
        text = args.text
    else:
        text = input("Enter the text to process: ")

    if not text:
        print("No text provided to process.", file=sys.stderr)
        sys.exit(1)

    if args.action == "encrypt":
        result = encrypt(text, args.key)
    else:
        result = decrypt(text, args.key)

    print(result)


if __name__ == "__main__":
    main()
