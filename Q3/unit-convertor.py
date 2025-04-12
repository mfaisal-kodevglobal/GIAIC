import streamlit as st

# Set up the Streamlit app
st.set_page_config(page_title="Unit Converter", layout="centered")

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
    /* Style subheaders */
    h2 {
        color: #4a90e2;
        font-size: 24px;
        font-family: 'Arial', sans-serif;
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
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title("Unit Converter")
st.write("Convert units for length and temperature!")

# Unit Conversion Functions
def convert_length(value, input_unit, output_unit):
    """Convert length units."""
    conversion_factors = {
        "meters": 1,
        "feet": 3.28084,
        "inches": 39.3701,
        "centimeters": 100,
    }
    return value * conversion_factors[output_unit] / conversion_factors[input_unit]

def convert_temperature(value, input_unit, output_unit):
    """Convert temperature units."""
    if input_unit == "Celsius" and output_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif input_unit == "Fahrenheit" and output_unit == "Celsius":
        return (value - 32) * 5/9
    elif input_unit == "Celsius" and output_unit == "Kelvin":
        return value + 273.15
    elif input_unit == "Kelvin" and output_unit == "Celsius":
        return value - 273.15
    elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # Same unit

# Category Selection
category = st.radio("Select Category:", ["Length", "Temperature"])

if category == "Length":
    st.subheader("Length Conversion")
    # Input value
    value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)
    # Input and output units
    input_unit = st.selectbox("Select input unit:", ["meters", "feet", "inches", "centimeters"])
    output_unit = st.selectbox("Select output unit:", ["meters", "feet", "inches", "centimeters"])
    # Perform conversion
    if st.button("Convert"):
        result = convert_length(value, input_unit, output_unit)
        st.success(f"**Converted Value:** {result:.2f} {output_unit}")

elif category == "Temperature":
    st.subheader("Temperature Conversion")
    # Input value
    value = st.number_input("Enter the value to convert:", step=0.1)
    # Input and output units
    input_unit = st.selectbox("Select input unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    output_unit = st.selectbox("Select output unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    # Perform conversion
    if st.button("Convert"):
        result = convert_temperature(value, input_unit, output_unit)
        st.success(f"**Converted Value:** {result:.2f} {output_unit}")