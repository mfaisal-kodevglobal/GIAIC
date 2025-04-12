import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    length_check = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*]', password))

    # Assign score
    if length_check:
        score += 1
    else:
        feedback.append("❌ At least 8 characters")
    
    if has_upper:
        score += 1
    else:
        feedback.append("❌ Uppercase letter (A-Z)")
    
    if has_lower:
        score += 1
    else:
        feedback.append("❌ Lowercase letter (a-z)")
    
    if has_digit:
        score += 1
    else:
        feedback.append("❌ At least one digit (0-9)")
    
    if has_special:
        score += 1
    else:
        feedback.append("❌ Special character (!@#$%^&*)")

    # Strength classification
    if score <= 2:
        strength = "Weak ❌"
    elif score <= 4:
        strength = "Moderate ⚠️"
    else:
        strength = "Strong ✅"

    return strength, feedback

def generate_strong_password():
    import random
    import string
    length = 12
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    st.title("🔒 Password Strength Meter")
    password = st.text_input("Enter your password:", type="password")

    if st.button("Check Strength"):
        if not password:
            st.warning("Please enter a password!")
            return

        # Check common passwords
        common_passwords = ["password", "123456", "qwerty", "admin"]
        if password.lower() in common_passwords:
            st.error("❌ This password is too common. Choose a stronger one!")
            return

        strength, feedback = check_password_strength(password)
        st.subheader(f"Password Strength: **{strength}**")
        
        if strength != "Strong ✅":
            st.warning("**Suggestions to improve:**")
            for suggestion in feedback:
                st.write(suggestion)
        else:
            st.success("✅ Your password is strong and secure!")

    # Optional: Password Generator
    if st.button("Generate Strong Password"):
        strong_pass = generate_strong_password()
        st.code(f"Generated Password: {strong_pass}")

if __name__ == "__main__":
    main()