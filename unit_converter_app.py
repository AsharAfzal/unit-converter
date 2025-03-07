import streamlit as st

# Conversion factors
conversion_factors = {
    'meters': 1,
    'kilometers': 1000,
    'miles': 1609.34,
    'feet': 0.3048,
    'inches': 0.0254
}

def convert_units(length, unit_from, unit_to):
    """Convert length from one unit to another."""
    if unit_from in conversion_factors and unit_to in conversion_factors:
        meters = length * conversion_factors[unit_from]  # Convert to meters
        return meters / conversion_factors[unit_to]  # Convert to target unit
    return None

# Streamlit UI
st.title("Unit Converter 🌍📏")

# User input
length = st.number_input("Enter length:", min_value=0.0, format="%.2f")
unit_from = st.selectbox("From Unit", list(conversion_factors.keys()))
unit_to = st.selectbox("To Unit", list(conversion_factors.keys()))

# Convert button
if st.button("Convert"):
    result = convert_units(length, unit_from, unit_to)
    if result is not None:
        st.success(f"Converted Value: {result:.4f} {unit_to}")
    else:
        st.error("Invalid conversion. Please check the units.")

