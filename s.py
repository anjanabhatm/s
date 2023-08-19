import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app title
st.title("Normal Distribution Generator")

# Sidebar inputs
st.sidebar.header("Parameters")
mean = st.sidebar.number_input("Mean", value=0.0)
std_dev = st.sidebar.number_input("Standard Deviation", value=1.0)
num_samples = st.sidebar.number_input("Number of Samples", value=1000)

# Generate normal distribution data
data = np.random.normal(mean, std_dev, num_samples)

# Display histogram
st.header("Histogram of Generated Data")
plt.hist(data, bins=30, density=True)
plt.xlabel("Value")
plt.ylabel("Frequency")
st.pyplot(plt)

# Download data as CSV
if st.button("Download Data as CSV"):
    df = pd.DataFrame(data, columns=["Value"])
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="generated_data.csv",
        mime="text/csv",
    )
