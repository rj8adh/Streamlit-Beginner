# Basic streamlit calculator
import streamlit as st

# Setting the title of the app
st.title("Calculator")

# Adding a subtitle to explain what the app does
st.write("Enter two numbers and select an operation")

# Creating two text input boxes for numbers
# st.number_input creates a number input field with up/down arrows
number1 = st.number_input("Enter first number:", value=0.0)
number2 = st.number_input("Enter second number:", value=0.0)

# Creating a dropdown menu for selecting the operation
# st.selectbox creates a dropdown with options
operation = st.selectbox(
    "Select operation:",
    options=["+", "-", "x", "/"]
)

# Creating a submit button
# st.button returns True when clicked, False otherwise
if st.button("Calculate"):
    # Does the calculation based on the selected operation
    if operation == "+":
        result = number1 + number2
        st.success(f"Result: {number1} + {number2} = {result}")
    
    elif operation == "-":
        result = number1 - number2
        st.success(f"Result: {number1} - {number2} = {result}")
    
    elif operation == "x":
        result = number1 * number2
        st.success(f"Result: {number1} x {number2} = {result}")
    
    elif operation == "/":
        # Don't forget the 0 division
        if number2 == 0:
            st.error("Can't divide by zero BUM")
        else:
            result = number1 / number2
            st.success(f"Result: {number1} / {number2} = {result}")

# Adding like a note at the bottom
st.info("This is just showing an info box")
