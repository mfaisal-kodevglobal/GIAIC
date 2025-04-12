import streamlit as st

# Set up the Streamlit app (must be the first command)
st.set_page_config(page_title="Text Analyzer", layout="wide")

# Inject custom CSS for full-width content, background color, and heading styles
st.markdown(
    """
    <style>
    /* Set full-width layout */
    .stApp {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    /* Set background color for the entire app */
    .stApp > div {
        background-color: #e6f7ff !important;  /* Light blue background */
    }
    /* Style the title */
    h1 {
        color: #0052cc;  /* Dark blue */
        font-size: 42px;
        font-family: 'Georgia', serif;
        text-align: center;
        margin-bottom: 20px;
    }
    /* Style subheaders */
    h2 {
        color: #0052cc;  /* Dark blue */
        font-size: 28px;
        font-family: 'Georgia', serif;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    /* Style text input area */
    .stTextArea textarea {
        background-color: #ffffff;
        color: #333333;
        font-size: 16px;
        border-radius: 8px;
        border: 2px solid #0052cc;
        padding: 10px;
    }
    /* Style buttons */
    .stButton button {
        background-color: #0052cc;  /* Dark blue */
        color: #ffffff;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #003d99;  /* Darker blue on hover */
    }
    /* Style success and warning messages */
    .stSuccess {
        color: #28a745;  /* Green */
        font-size: 18px;
        font-weight: bold;
    }
    .stWarning {
        color: #dc3545;  /* Red */
        font-size: 18px;
        font-weight: bold;
    }
    /* Style general text */
    .stMarkdown {
        color: #333333;  /* Dark gray */
        font-size: 16px;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title("Text Analyzer")
st.write("Analyze your text with word count, vowel count, search and replace, and more!")

# User Input
st.subheader("Enter Your Text")
user_input = st.text_area("Type or paste your paragraph here:", height=200)

# Validate input
if not user_input.strip():
    st.error("Please enter some text to analyze.")
else:
    # Ensure the input is a string
    user_input = str(user_input)

    # 1. Word and Character Count
    st.subheader("Word and Character Count")
    word_count = len(user_input.split())
    char_count = len(user_input)
    st.write(f"**Total Words:** {word_count}")
    st.write(f"**Total Characters (including spaces):** {char_count}")

    # 2. Vowel Count
    st.subheader("Vowel Count")
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in user_input if char in vowels)
    st.write(f"**Total Vowels:** {vowel_count}")

    # 3. Search and Replace
    st.subheader("Search and Replace")
    search_word = st.text_input("Enter a word to search for:")
    replace_word = st.text_input("Enter a word to replace it with:")
    if search_word and replace_word:
        modified_text = user_input.replace(search_word, replace_word)
        st.write("**Modified Paragraph:**")
        st.write(modified_text)

    # 4. Uppercase and Lowercase Conversion
    st.subheader("Uppercase and Lowercase Conversion")
    st.write("**Uppercase Paragraph:**")
    st.write(user_input.upper())
    st.write("**Lowercase Paragraph:**")
    st.write(user_input.lower())

    # 5. Type Casting
    st.subheader("Type Casting")
    word_count_str = str(word_count)
    vowel_count_str = str(vowel_count)
    st.write(f"**Word Count as String:** {word_count_str}")
    st.write(f"**Vowel Count as String:** {vowel_count_str}")

    # 6. Operators
    st.subheader("Operators")
    # Check if the paragraph contains the word "Python"
    contains_python = "Python" in user_input
    st.write(f"**Does the text contain the word 'Python'?** {contains_python}")

    # Calculate average word length
    if word_count > 0:
        avg_word_length = char_count / word_count
        st.write(f"**Average Word Length:** {avg_word_length:.2f} characters per word")
    else:
        st.write("**Average Word Length:** Cannot calculate (no words found).")

    # 7. Python Keywords (if statement)
    st.subheader("Python Keywords")
    if "Python" in user_input:
        st.success("The text contains the word 'Python'!")
    else:
        st.warning("The text does not contain the word 'Python'.")  