import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += "!@#$%^&*"

    password = []
    if use_upper: password.append(random.choice(string.ascii_uppercase))
    if use_digits: password.append(random.choice(string.digits))
    if use_symbols: password.append(random.choice("!@#$%^&*"))

    password += [random.choice(chars) for _ in range(length - len(password))]
    random.shuffle(password)
    return ''.join(password)

print("=" * 35)
print("   Password Generator")
print("=" * 35)

try:
    length = int(input("\nEnter password length (default 12): ") or 12)
    upper = input("Include uppercase? (y/n, default y): ").lower() != 'n'
    digits = input("Include digits? (y/n, default y): ").lower() != 'n'
    symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
    count = int(input("How many passwords to generate? (default 3): ") or 3)
except ValueError:
    print("Invalid input. Using defaults.")
    length, upper, digits, symbols, count = 12, True, True, True, 3

print(f"\nGenerated {count} password(s):")
print("-" * 35)
for i in range(count):
    print(f"  {i+1}. {generate_password(length, upper, digits, symbols)}")
print("-" * 35)
