import random
import string

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 8 and score == 4:
        return "Strong"
    elif length >= 6 and score >= 2:
        return "Medium"
    else:
        return "Weak"

def generate_password():
    length = 10
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User input
password = input("Enter your password: ")
print("Strength:", check_strength(password))

print("\nGenerated Strong Password:", generate_password())