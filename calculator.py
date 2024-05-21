# calculator.py

import streamlit as st

# Define the calculator function
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

# Set the title and header
st.title("Calculator")
st.header("Perform simple calculations here:")

# Get user input
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
operation = st.selectbox("Select operation:", ["+", "-", "*", "/"])

# Perform the calculation and display the result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write("Result:", result)