import streamlit as st
import numpy as np
from PIL import Image

# Title and Header
st.title("Breast Cancer Prediction Model")
st.markdown("This app predicts whether a patient is at risk for breast cancer based on the input features.")

# Display Image
img = Image.open(r"C:\Users\ASUS\Desktop\ML Projects\Cancer\images.jpg")  # Replace with the correct path to your image
st.image(img, caption="Breast Cancer Model", use_column_width=True)

# Input Features Form
st.sidebar.header("Input Breast Cancer Features")
st.sidebar.markdown("Enter the features below:")

# Input fields for the user
feature_input = st.sidebar.text_area(
    "Comma-separated numeric input features:",
    placeholder="-0.23717126, -0.64487029, -0.11382239, ...",
)

# Predict Button
if st.sidebar.button("Predict"):
    if feature_input:
        try:
            # Convert input string into a list of floats
            input_features = np.array([float(x.strip()) for x in feature_input.split(",")]).reshape(1, -1)

            # Mock prediction logic (replace this with your actual ML model logic)
            prediction = "Not Cancrouse" if input_features.sum() < 5 else "Cancrouse"

            # Display results
            st.subheader("Prediction Result")
            if prediction == "Not Cancrouse":
                st.success("**Not Cancrouse**: Don't worry! You don't have Breast Cancer Disease. Enjoy your life! 😊")
                img_not_cancer = Image.open(r"C:\Users\ASUS\Desktop\ML Projects\Cancer\img2.jpg")  # Replace with the correct path to your image
                st.image(img_not_cancer, caption="Not Cancrouse", use_column_width=True)
            else:
                st.error("**Cancrouse**: Alert! You might have Breast Cancer Disease. Please consult a doctor for further diagnosis. 🚨")
                img_cancer = Image.open(r"C:\Users\ASUS\Desktop\ML Projects\Cancer\img1.jpg")  # Replace with the correct path to your image
                st.image(img_cancer, caption="Cancrouse", use_column_width=True)
        except ValueError:
            st.error("Invalid input! Please provide numeric values separated by commas.")
    else:
        st.warning("Please enter the features before predicting.")

# Footer
st.markdown("---")
st.markdown("Developed using [Streamlit](https://streamlit.io).")

