# agri-scan-streamlite
# 🌿 AgriScanAI - Plant Disease Detection Web App

AgriScanAI is an AI-powered **plant disease detection** tool built with **TensorFlow Lite** and **Streamlit**. It allows users—especially farmers—to detect plant diseases from leaf images directly in their browser or via mobile camera. No installation, no coding, just fast and simple AI-powered diagnostics.

---

## 🚀 Live Demo

📍 Coming Soon via [Streamlit Cloud](https://streamlit.io/cloud)  
🔗 [Demo Link Here](#) (Replace with your deployed URL)

---

## 📸 Features

✅ Upload or capture a leaf image using your camera  
✅ Real-time disease prediction using a TFLite model  
✅ Mobile-friendly & offline-compatible  
✅ Fast, lightweight, and easy to deploy  
✅ Stylish and responsive interface

---

## 🧠 Model Details

- Model Type: **TensorFlow Lite (TFLite)**
- Input Size: `224x224 RGB`
- Classes Supported:
  - Pepper__bell___Bacterial_spot
  - Pepper__bell___healthy
  - Potato___Early_blight
  - Potato___healthy
  - Potato___Late_blight
  - Tomato_Bacterial_spot
  - Tomato_Early_blight
  - Tomato_healthy
  - Tomato_Late_blight
  - Tomato_Leaf_Mold

---

## 🗂️ Folder Structure

plant-disease-streamlit-app/
├── app.py # Main Streamlit app
├── plant_disease_model.tflite # Trained TFLite model
├── label_map.txt # Class labels
├── requirements.txt # Python dependencies
└── README.md # You're here

yaml
Copy
Edit

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/plant-disease-streamlit.git
cd plant-disease-streamlit
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
streamlit run app.py
Then open http://localhost:8501 in your browser.



📥 Requirements
nginx
Copy
Edit
streamlit
tensorflow
pillow
numpy
👨‍🌾 Use Case Example
A farmer takes a picture of a tomato leaf using their phone. They open the AgriScanAI web app, upload the image, and get a fast prediction like:

Disease: Tomato_Late_blight
Confidence: 95.3%

🤖 Built With
Streamlit

TensorFlow Lite

Pillow

NumPy

🛡️ License
This project is open-source under the MIT License.

🙌 Acknowledgments
Dataset: PlantVillage on Kaggle

Inspired by real-world agricultural challenges in Africa 🌍

💬 Contact & Credits
Built by [Albert sipoi]
🔗 GitHub: github.com/Dr-Alb
📧 Email:alsipoi1564@gmail.com

“Innovation starts in the field. Let AI guide your harvest.”
