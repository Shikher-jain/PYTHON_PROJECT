import re

def password_strength(password):
    # Initialize strength score
    strength = 0

    # Check password length
    if len(password) < 8:
        print("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for no.
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1

    # Print password strength
    if strength == 1:
        print("Password is weak.")
    elif strength == 2:
        print("Password is medium.")
    elif strength == 3:
        print("Password is strong.")
    elif strength == 4:
        print("Password is very strong.")
    else:
        print("Password is extremely strong.")

# Get password from user
password = input("Enter a password: ")

# Check password strength
password_strength(password)