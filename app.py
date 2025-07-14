import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="AgriScanAI ", layout="centered")

# --- Load labels ---
with open("label_map.txt", "r") as f:
    labels = f.read().splitlines()

# --- Load TFLite model ---
interpreter = tf.lite.Interpreter(model_path="plant_disease_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# --- Helper Functions ---
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image).astype(np.float32)
    image = np.expand_dims(image, axis=0)
    return image

def predict(image):
    image = preprocess_image(image)
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])[0]
    top_index = np.argmax(output)
    confidence = output[top_index]
    return labels[top_index], confidence

# --- UI Styling ---
st.markdown("""
    <style>
    .title {
        font-size: 2.5em;
        font-weight: 600;
        text-align: center;
        color: #2E7D32;
    }
    .footer {
        font-size: 0.9em;
        text-align: center;
        margin-top: 40px;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# --- App UI ---
st.markdown('<div class="title">🌿 AgriScanAI - Plant Disease Detector</div>', unsafe_allow_html=True)
st.write("Upload or capture a leaf image to detect diseases using a machine learning model.")

# --- File Upload or Camera ---
image_input = st.file_uploader("Choose or take a photo", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

# Camera input (for mobile users)
if not image_input:
    image_input = st.camera_input("Or take a photo using your camera")

# --- Prediction Logic ---
if image_input:
    image = Image.open(image_input)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    with st.spinner("🧠 Analyzing..."):
        label, confidence = predict(image)

    st.success(f"🌱 **Prediction:** {label}")
    st.info(f"📊 Confidence: {confidence * 100:.2f}%")

# --- Footer ---
st.markdown('<div class="footer">Built with ❤️ using TensorFlow Lite and Streamlit</div>', unsafe_allow_html=True)
