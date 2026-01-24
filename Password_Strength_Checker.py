import string

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in string.punctuation:
        has_symbol = True

length_ok = len(password) >= 8

missing = []

if not has_upper:
    missing.append("Add at least 1 UPPERCASE letter")
if not has_lower:
    missing.append("Add at least 1 lowercase letter")
if not has_digit:
    missing.append("Add at least 1 number")
if not has_symbol:
    missing.append("Add at least 1 symbol")
if not length_ok:
    missing.append("Password must be at least 8 characters long")

# Strength Rating
score = 0
if has_upper: score += 1
if has_lower: score += 1
if has_digit: score += 1
if has_symbol: score += 1
if length_ok: score += 1

print("\n--- Password Analysis ---")

if score == 5:
    print("Strength: STRONG ")
elif score >= 3:
    print("Strength: MEDIUM ")
else:
    print("Strength: WEAK ")

if len(missing) == 0:
    print("Great! Your password meets all security requirements.")
else:
    print("\nImprovements needed:")
    for msg in missing:
        print("•", msg)
