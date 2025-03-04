import streamlit as st
import re
import random
import string

# Common weak passwords to blacklist
COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "123abc"]

# Password strength checker
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("❌ This is a commonly used weak password. Avoid it!")

    if score >= 5:
        strength = "Strong 💪"
        color = "limegreen"
    elif score >= 3:
        strength = "Moderate 😐"
        color = "gold"
    else:
        strength = "Weak 😟"
        color = "crimson"

    return score, strength, color, feedback

# Strong password generator
def generate_strong_password():
    length = 16
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Main App
def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

    # Theme selection on main page
    theme = st.selectbox("Select Theme", ["Light", "Dark"])

    if theme == "Dark":
        background_color = "#1E1E1E"
        text_color = "#FFFFFF"
        input_bg_color = "#333333"
        label_color = "#FFFFFF"
        button_color = "#4CAF50"
        top_bar_bg_color = "#1E1E1E"
        top_bar_text_color = "#FFFFFF"
    else:
        background_color = "#F5F5F5"
        text_color = "#000000"
        input_bg_color = "#FFFFFF"
        label_color = "#000000"
        button_color = "#4CAF50"
        top_bar_bg_color = "#FFFFFF"
        top_bar_text_color = "#000000"

    # Apply theme styling to the entire app
    st.markdown(f"""
        <style>
        /* Body and main app background */
        body, .stApp {{
            background-color: {background_color};
            color: {text_color};
        }}

        /* Top bar styling */
        .stApp > header {{
            background-color: {top_bar_bg_color} !important;
            color: {top_bar_text_color} !important;
        }}

        /* Text input styling */
        .stTextInput > div > div > input {{
            background-color: {input_bg_color};
            color: {text_color};
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
        }}

        /* Button styling */
        .stButton > button {{
            background-color: {button_color};
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }}

        /* Label styling */
        label {{
            color: {label_color} !important;
            font-weight: bold;
        }}

        /* Progress bar styling */
        .stProgress > div > div > div > div {{
            background-color: {button_color};
        }}

        /* Code block styling */
        .stCodeBlock code {{
            background-color: {input_bg_color};
            color: {text_color};
            border-radius: 5px;
            padding: 10px;
        }}

        /* Success message styling */
        .stSuccess {{
            color: {text_color};
        }}

        /* Info message styling */
        .stInfo {{
            color: {text_color};
        }}
        </style>
    """, unsafe_allow_html=True)

    st.title("🔐 Password Strength Meter")
    st.write("Check your password's strength and get tips to make it stronger!")

    # Password input with styled label
    st.markdown(f"<label>Enter your password:</label>", unsafe_allow_html=True)
    password = st.text_input("", type="password", placeholder="Type your password here...")

    if password:
        score, strength, color, feedback = check_password_strength(password)

        st.subheader("Password Strength:")
        st.markdown(f"<h2 style='color: {color};'>{strength}</h2>", unsafe_allow_html=True)
        st.progress(score / 5)

        if feedback:
            st.subheader("Suggestions to improve:")
            for item in feedback:
                st.write(item)
        else:
            st.success("Your password is strong! 🚀")

    st.subheader("🔑 Generate a Strong Password")
    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password()
        st.code(strong_password, language="plaintext")
        st.success("Strong password generated! Copy it and stay secure.")

    st.markdown("---")
    st.info("Created by Areesha Kainat")


if __name__ == "__main__":
    main()