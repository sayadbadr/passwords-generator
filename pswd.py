import random
import string
import argparse

def load_words(file_path):
    """Load words from a file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)

def generate_password(pattern, words, numbers, symbols, length=None):
    """Generate a password based on the given pattern"""
    password = []
    
    for item in pattern:
        if item == "W":
            password.append(random.choice(words))
        elif item == "N":
            password.append(random.choice(numbers))
        elif item == "S":
            password.append(random.choice(symbols))
    
    if length:
        while len("".join(password)) < length:
            password.append(random.choice(words + numbers + symbols))
    
    return "".join(password)

def random_password(words, length, mode):
    """Generate a random password based on the selected mode"""
    all_numbers = "0123456789"
    all_symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    if mode == "1":
        char_pool = words
    elif mode == "2":
        char_pool = words + list(all_numbers)
    elif mode == "3":
        char_pool = words + list(all_symbols)
    elif mode == "4":
        char_pool = words + list(all_numbers) + list(all_symbols)
    elif mode == "5":
        char_pool = list(all_numbers)
    elif mode == "6":
        char_pool = list(all_symbols)
    elif mode == "7":
        char_pool = list(all_numbers) + list(all_symbols)
    else:
        print("Invalid combination mode.")
        exit(1)

    return "".join(random.choices(char_pool, k=length))

# CLI Argument Parser with Help Manual
parser = argparse.ArgumentParser(
    description="📜 Password Generator CLI Tool",
    epilog="""
For the random mode there a combinition option:
 1. Words only
 2. Words and numbers
 3. Words and symbols
 4. Words and numbers and symbols
 5. numbers only
 6. symbols only
 7. numbers and symbols
------------------------------------------------
Examples:
---------
1️⃣ Random Mode (words + numbers + symbols, length 10, 100 passwords)
   python3 password.py -w words.txt -l 10 -m r -c 4 -g 100 -o passwords.txt

2️⃣ Custom Mode (Pattern: Word, Number, Symbol, Word, 50 passwords)
   python3 password.py -w words.txt -l 15 -m c -p W,N,S,W -g 50 -o custom_pswds.txt

3️⃣ Custom Mode with Custom Characters
   python3 password.py -w words.txt -m c -p W,N,W -g 20 --numbers 123456789 --symbols #%$ -o custom_pswds.txt
""",
    formatter_class=argparse.RawTextHelpFormatter
)

# Required Arguments
parser.add_argument("-w", "--wordslist", required=True, help="Path to the words file")
parser.add_argument("-m", "--mode", required=True, choices=["random", "custom", "r", "c"], help="Mode: 'random' (r) or 'custom' (c)")
parser.add_argument("-g", "--generate", type=int, required=True, help="Number of passwords to generate")
parser.add_argument("-o", "--output", required=True, help="Output file path")

# Optional Arguments
parser.add_argument("-l", "--length", type=int, help="Password length (optional)")

# Random Mode Arguments
parser.add_argument("-c", "--combination", type=str, help="Random mode combination type (1-7)")

# Custom Mode Arguments
parser.add_argument("-p", "--pattern", type=str, help="Custom mode password pattern (e.g., W,N,S,W)")
parser.add_argument("--words", type=str, nargs="+", help="Custom words (optional)")
parser.add_argument("--numbers", type=str, nargs="+", help="Custom numbers (optional)")
parser.add_argument("--symbols", type=str, nargs="+", help="Custom symbols (optional)")

args = parser.parse_args()

# Load words
words = load_words(args.wordslist)

# Default values for numbers and symbols
default_numbers = "0123456789"
default_symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

if args.mode in ["random", "r"]:
    if not args.combination:
        print("Error: You must specify a combination mode (-c) for random mode.")
        exit(1)

    passwords = [random_password(words, args.length or 12, args.combination) for _ in range(args.generate)]

elif args.mode in ["custom", "c"]:
    if not args.pattern:
        print("Error: You must specify a password pattern (-p) for custom mode.")
        exit(1)

    password_pattern = args.pattern.split(",")

    custom_words = args.words if args.words else words
    custom_numbers = args.numbers if args.numbers else list(default_numbers)
    custom_symbols = args.symbols if args.symbols else list(default_symbols)

    passwords = [generate_password(password_pattern, custom_words, custom_numbers, custom_symbols, args.length) for _ in range(args.generate)]

# Save passwords to file
with open(args.output, "w", encoding="utf-8") as f:
    f.write("\n".join(passwords))

print(f"Generated {args.generate} passwords and saved to {args.output}")
