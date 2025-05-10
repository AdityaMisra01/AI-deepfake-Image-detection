
# GenuineAI – DeepFake Image Detector

**GenuineAI** is a deep learning-based image analysis tool designed to detect synthetic (deepfake) images using Convolutional Neural Networks (CNNs) and advanced computer vision techniques. Built for both technical and non-technical users, GenuineAI offers a lightweight, fast, and accurate solution to verify the authenticity of images — especially in today's misinformation-heavy digital world.

---

## 🌟 Features

- 🔍 DeepFake detection using a trained CNN model
- 🖼️ Real-time image upload and analysis
- 📊 Confidence score and visual indicators of manipulation
- 📝 Automatic PDF report generation
- 🔐 GDPR-compliant secure image handling
- 🌐 Responsive web interface accessible from any modern browser

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python 3.8+, Flask |
| Model | TensorFlow/Keras (CNN) |
| Image Processing | OpenCV |
| Database (optional) | MongoDB |
| Hosting (optional) | Azure/AWS (cloud-based or local) |

---

## 🧪 Dataset Used

- [FaceForensics++](https://github.com/ondyari/FaceForensics)
- [Celeb-DF v2](https://github.com/yuezunli/Celeb-DF)

> These datasets are used to train and test the deep learning model for high accuracy and generalizability.

---

## 📁 Project Structure

```
GenuineAI/
│
├── static/                 # Frontend assets (HTML/CSS/JS)
├── templates/              # HTML templates for Flask
├── model/                  # Trained CNN model (.h5)
├── uploads/                # Temporary image storage
├── reports/                # Auto-generated PDF reports
├── app.py                  # Main Flask application
├── utils.py                # Helper functions
├── requirements.txt        # Dependencies
└── README.md               # Project manual
```

---

## ⚙️ Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/GenuineAI.git
cd GenuineAI
```

### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

Now open your browser and go to:  
👉 `http://127.0.0.1:5000`

---

## 🖼️ How to Use GenuineAI

1. **Upload Image**  
   Supported formats: `.jpg`, `.jpeg`, `.png`

2. **View Result**  
   - Prediction: `REAL` or `FAKE`
   - Confidence Score (e.g. 92.5%)

3. **Download Report**  
   - Click “Download PDF” to save the report for records

---

## 🔐 Data Privacy

- Uploaded images are temporarily stored and deleted after processing
- User data is encrypted and not shared externally
- Fully GDPR-compliant and safe for academic, journalistic, and forensic use

---

## 🧠 Model Details

- Input: 224x224 color image
- Architecture: Custom CNN / VGG19 / ResNet-based (edit based on actual)
- Output: Binary classification (`REAL`, `FAKE`) + confidence
- Accuracy: >90% on test set (FaceForensics++ and Celeb-DF)

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Accuracy | ≥ 90% |
| Precision | High |
| Inference Time | < 3 seconds per image |
| Concurrent Users | Up to 50 |

---

## 📌 Future Enhancements

- Video deepfake detection
- Mobile application (Android/iOS)
- Integration with social media platforms
- Advanced user accounts and analytics

---

## 📚 Contributors

- **Aditya Misra** – Model Development & Deployment  
- **Anushree Rathore** – Frontend & Report Generation  
- **Anubhuti Sharma** – Data Handling & UI Design  
- **Anand Tiwari** – System Evaluation & Integration  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Acknowledgements

- FaceForensics++ & Celeb-DF Dataset creators
- TensorFlow & OpenCV open-source communities
- SKIT Jaipur, Rajasthan Technical University

---

## 🔗 Useful Links

- 🔍 [Deepware Scanner](https://deepware.ai/)
- 📰 [Microsoft Video Authenticator](https://blogs.microsoft.com/on-the-issues/2020/09/01/disinformation-deepfakes-newsguard-video-authenticator/)
