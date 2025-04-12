import streamlit as st
import random

# Set up the Streamlit app
st.set_page_config(page_title="Number Guessing Game", layout="centered")

# Inject custom CSS for styling
st.markdown(
    """
    <style>
    /* Set background color and text color */
    .stApp {
        background-color: #f0f2f6;
        color: #333333;
    }
    /* Style the title */
    h1 {
        color: #4a90e2;
        font-size: 36px;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    /* Style buttons */
    .stButton button {
        background-color: #4a90e2;
        color: #ffffff;
        font-size: 16px;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color: #357abd;
    }
    /* Style success and warning messages */
    .stSuccess {
        color: #28a745;
        font-size: 18px;
    }
    .stWarning {
        color: #dc3545;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title("Number Guessing Game")
st.write("Guess the randomly generated number within a specified range!")

# Initialize session state
if "random_number" not in st.session_state:
    st.session_state.random_number = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Custom Range Input
st.subheader("Set Custom Range")
min_value = st.number_input("Minimum Value", value=1, step=1)
max_value = st.number_input("Maximum Value", value=100, step=1)

# Difficulty Levels
st.subheader("Select Difficulty Level")
difficulty = st.radio(
    "Choose Difficulty:",
    ["Easy (Unlimited Attempts)", "Medium (10 Attempts)", "Hard (5 Attempts)"],
)

# Generate Random Number
if st.button("Start/Restart Game"):
    st.session_state.random_number = random.randint(min_value, max_value)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.success("New game started! Guess the number.")

# Game Logic
if st.session_state.random_number is not None and not st.session_state.game_over:
    st.subheader("Make a Guess")
    guess = st.number_input("Enter your guess:", min_value=min_value, max_value=max_value, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess < st.session_state.random_number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.random_number:
            st.warning("Too high! Try again.")
        else:
            st.session_state.game_over = True
            st.success(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")

        # Check difficulty-based attempts limit
        if difficulty == "Medium (10 Attempts)" and st.session_state.attempts >= 10:
            st.session_state.game_over = True
            st.error(f"Game over! The number was {st.session_state.random_number}.")
        elif difficulty == "Hard (5 Attempts)" and st.session_state.attempts >= 5:
            st.session_state.game_over = True
            st.error(f"Game over! The number was {st.session_state.random_number}.")

    # Display Attempts
    st.write(f"**Attempts:** {st.session_state.attempts}")

# Reset Game
if st.session_state.game_over:
    if st.button("Reset Game"):
        st.session_state.random_number = None
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.success("Game reset. Start a new game!")