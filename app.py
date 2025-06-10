import streamlit as st


# Define the calculator function
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operator!"

# Streamlit app layout
st.title("Simple Calculator")

# Input fields for numbers
number1 = st.number_input("Enter the first number:", format="%.2f")
number2 = st.number_input("Enter the second number:", format="%.2f")

# Dropdown for operator selection
operator = st.selectbox("Select an operator:", ['+', '-', '*', '/'])

# Button to calculate
import streamlit as st

# Define the calculator function
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operator!"

# Streamlit app layout
st.title("Simple Calculator")

# Input fields for numbers
number1 = st.number_input("Enter the first number:", format="%.2f")
number2 = st.number_input("Enter the second number:", format="%.2f")

# Dropdown for operator selection
operator = st.selectbox("Select an operator:", ['+', '-', '*', '/'])

# Button to calculate
if st.button("Calculate"):
    result = calculator(number1, number2, operator)
    st.write(f"The result is: {result}")
