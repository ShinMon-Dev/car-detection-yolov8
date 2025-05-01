import streamlit as st
from PIL import Image
from ultralytics import YOLO

# Load the trained YOLO model
MODEL_PATH = 'filtered_dataset/runs/detect/train/weights/best.pt'  
model = YOLO(MODEL_PATH)

# Streamlit UI
st.title("🚗 Car Detection App")
st.write("Upload an image of a car to detect its type and get prediction accuracy.")

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Run detection
    with st.spinner("Detecting..."):
        results = model.predict(image, conf=0.8)

    result_img = results[0].plot()
    st.image(result_img, caption='Detection Result', use_container_width=True)

    # Show class names and confidence
    for box in results[0].boxes.data:
        cls_id = int(box[5].item())
        conf = float(box[4].item())
        class_name = model.names[cls_id]
        st.write(f"**Detected:** {class_name} — Confidence: {conf:.2%}")
