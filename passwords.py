import random
import string
import os

def load_words(file_path):
    """Load words from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def generate_password(pattern, words, numbers, symbols, length):
    """Generate a random password based on a pattern and length."""
    password = []
    while len("".join(password)) < length:
        for char_type in pattern:
            if len("".join(password)) >= length:
                break
            if char_type == "W":
                password.append(random.choice(words))
            elif char_type == "N":
                password.append(random.choice(numbers))
            elif char_type == "S":
                password.append(random.choice(symbols))
    return ''.join(password)[:length]  # Ensure exact length

def main():
    # 1. Get words file
    words_file = input("Enter the path to your words file: ").strip()
    if not os.path.exists(words_file):
        print("File not found! Exiting...")
        return

    words = load_words(words_file)
    if not words:
        print("No words found in the file! Exiting...")
        return

    # 2. Get password length
    password_length = int(input("Enter the password length: ").strip())

    # 3. Choose Mode
    mode = input("\nChoose Mode: 'custom' or 'random': ").strip().lower()

    if mode == "custom":
        # 4. Custom password pattern
        print("\nDefine password pattern using:")
        print("  - 'W' for a word")
        print("  - 'N' for a number")
        print("  - 'S' for a symbol")
        print("Example: 'W N W' → word + number + word")

        password_pattern = input("Enter your password pattern (e.g., 'W W', 'W N W S'): ").strip().split()

        # 5. Custom word, number, and symbol selection
        words_input = input("Enter words (comma-separated) or press Enter for default: ").strip()
        numbers_input = input("Enter numbers (comma-separated) or press Enter for default: ").strip()
        symbols_input = input("Enter symbols (comma-separated) or press Enter for default: ").strip()

        words = words_input.split(",") if words_input else words
        numbers = numbers_input.split(",") if numbers_input else list(string.digits)
        symbols = symbols_input.split(",") if symbols_input else list(string.punctuation)

    elif mode == "random":
        # 4. Choose character types
        print("\nChoose password composition:")
        print("  1 - Words only (W)")
        print("  2 - Words + Numbers (W + N)")
        print("  3 - Words + Symbols (W + S)")
        print("  4 - Words + Numbers + Symbols (W + N + S)")
        print("  5 - Numbers only (N)")
        print("  6 - Symbols only (S)")
        print("  7 - Numbers + Symbols (N + S)")

        option = input("Enter your choice (1-7): ").strip()

        numbers = list(string.digits)
        symbols = list(string.punctuation)
        patterns = {
            "1": ["W"],         # Words only
            "2": ["W", "N"],    # Words + Numbers
            "3": ["W", "S"],    # Words + Symbols
            "4": ["W", "N", "S"], # Words + Numbers + Symbols
            "5": ["N"],         # Numbers only
            "6": ["S"],         # Symbols only
            "7": ["N", "S"]     # Numbers + Symbols
        }
        password_pattern = patterns.get(option, ["W", "N", "S"])  # Default to all mixed

    else:
        print("Invalid mode! Exiting...")
        return

    # 5. Number of passwords
    num_passwords = int(input("\nHow many passwords to generate (e.g., 1000, 100000, 1000000): ").strip())

    # 6. Save location
    save_path = input("Enter the path to save the passwords file (e.g., passwords.txt): ").strip()

    # Generate passwords
    print(f"Generating {num_passwords} passwords...")
    passwords = [generate_password(password_pattern, words, numbers, symbols, password_length) for _ in range(num_passwords)]

    # Save to file
    try:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write("\n".join(passwords))
        print(f"Passwords saved to {save_path}")
    except Exception as e:
        print(f"Error saving passwords: {e}")

if __name__ == "__main__":
    main()
