
## using stremlit

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function for different operations
def calculate(num, operation):
    if operation == "Square":
        return num ** 2
    elif operation == "Cube":
        return num ** 3
    elif operation == "Square Root":
        return np.sqrt(num) if num >= 0 else "Invalid (Negative Number)"
    else:
        return 0  # Default return in case of unexpected input

# Streamlit App
st.set_page_config(page_title="Advanced Calculator", layout="centered")

st.markdown("<h1 style='text-align: center; color: blue;'>Advanced Calculator</h1>", unsafe_allow_html=True)

num = st.number_input("Enter a number:", value=0)

operation = st.radio("Choose an operation:", ["Square", "Cube", "Square Root"])

if st.button("Calculate"):
    result = calculate(num, operation)
    
    if isinstance(result, str):  # Check if result is an error message
        st.error(result)
    else:
        st.success(f"The {operation.lower()} of {num} is {result}")

        # Visualization (Bar Chart)
        fig, ax = plt.subplots()
        ax.bar(["Original", operation], [num, result], color=['gray', 'blue'])
        st.pyplot(fig)

# Dark Mode Toggle
if st.checkbox("Enable Dark Mode"):
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )
