import secrets
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    character_sets = []

    if use_upper:
        character_sets.append(string.ascii_uppercase)
    if use_lower:
        character_sets.append(string.ascii_lowercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("Select at least one character type.")

    all_characters = "".join(character_sets)

    # Ensure selected character types are represented when possible.
    password_chars = [secrets.choice(chars) for chars in character_sets]

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars[:length])


def main():
    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter desired password length: "))

        if length < 4:
            print("Please enter a length of at least 4.")
            return

        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
        use_digits = input("Include numbers? (y/n): ").strip().lower() == "y"
        use_special = input("Include special characters? (y/n): ").strip().lower() == "y"

        selected_types = sum([use_upper, use_lower, use_digits, use_special])

        if selected_types == 0:
            print("Error: Select at least one character type.")
            return

        if length < selected_types:
            print(f"Please choose a length of at least {selected_types}.")
            return

        password = generate_password(
            length, use_upper, use_lower, use_digits, use_special
        )

        print("\nGenerated Password:", password)
        print("Password Length:", len(password))

    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
