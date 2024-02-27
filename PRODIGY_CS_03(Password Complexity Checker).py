import re

def password_strength(password):
    length = len(password)
    if length < 8:
        return "Weak: Password should be at least 8 characters long."

    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'\d', password))
    special_char = bool(re.search(r'[^A-Za-z0-9]', password))

    missing_elements = []
    if not uppercase:
        missing_elements.append("uppercase letters")
    if not lowercase:
        missing_elements.append("lowercase letters")
    if not digit:
        missing_elements.append("numbers")
    if not special_char:
        missing_elements.append("special characters")

    if missing_elements:
        return f"Password should include {', '.join(missing_elements)} to be stronger."
    else:
        return "Excellent: Password is very strong."


password = input("Enter your password: ")
strength = password_strength(password)
print(strength)