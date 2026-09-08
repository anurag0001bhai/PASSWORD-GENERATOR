import secrets
import string
import streamlit as st


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

    if length < len(character_sets):
        raise ValueError(
            f"Password length must be at least {len(character_sets)}."
        )

    all_characters = "".join(character_sets)

    # Make sure every selected character type is represented
    password_chars = [
        secrets.choice(chars) for chars in character_sets
    ]

    # Fill the remaining length
    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars[:length])


# -------------------------------
# Streamlit Web Interface
# -------------------------------

st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Generator")
st.write("Generate a strong and secure password instantly.")

st.divider()

# Password length
length = st.slider(
    "Password Length",
    min_value=4,
    max_value=64,
    value=12
)

st.subheader("Character Types")

use_upper = st.checkbox(
    "Include uppercase letters (A-Z)",
    value=True
)

use_lower = st.checkbox(
    "Include lowercase letters (a-z)",
    value=True
)

use_digits = st.checkbox(
    "Include numbers (0-9)",
    value=True
)

use_special = st.checkbox(
    "Include special characters (!@#$...)",
    value=True
)

st.divider()

if st.button("🔑 Generate Password", use_container_width=True):

    if not any([use_upper, use_lower, use_digits, use_special]):
        st.error("Please select at least one character type.")

    else:
        password = generate_password(
            length,
            use_upper,
            use_lower,
            use_digits,
            use_special
        )

        st.success("Password generated successfully!")

        st.subheader("Your Password")

        st.code(password, language=None)

        st.write(f"**Password Length:** {len(password)} characters")

        st.info(
            "💡 Tip: Use a different strong password for every account."
        )