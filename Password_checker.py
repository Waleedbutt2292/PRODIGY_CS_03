import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >=8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>§~]', password))

    # Assess strength
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria or digit_criteria or special_char_criteria):
        return "Moderate"
    else:
        return "Weak"

# Main function
def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
