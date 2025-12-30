# 🍎🍊 Fruit Image Classification (Apple vs Orange)

Aplikasi **klasifikasi citra buah** berbasis **Machine Learning** yang mampu
membedakan gambar **apel** dan **jeruk** menggunakan pendekatan
**Transfer Learning** dengan **MobileNetV2** sebagai feature extractor
dan **Logistic Regression** sebagai algoritma klasifikasi.

Project ini dikembangkan secara end-to-end, mulai dari pemodelan di
**Jupyter Notebook** hingga deployment ke aplikasi web menggunakan **Flask**.

---

## 🎯 Tujuan Project
- Membangun sistem klasifikasi citra buah berbasis machine learning
- Menerapkan konsep **transfer learning** untuk ekstraksi fitur visual
- Mengimplementasikan model ke dalam aplikasi web interaktif
- Menjadi project pembelajaran/portofolio di bidang **Computer Vision**

---

## 🧠 Metodologi

### 1. Dataset
- Sumber dataset: Hugging Face (`Suru/Fruit`)
- Kelas:  
  - Apple  
  - Orange
- Dataset telah dibagi menjadi:
  - Train
  - Validation
  - Test

### 2. Preprocessing
- Resize gambar menjadi **224 × 224**
- Normalisasi nilai pixel (0–1)
- Konversi ke array NumPy

### 3. Feature Extraction
- Model: **MobileNetV2**
- Pretrained weights: **ImageNet**
- Konfigurasi:
  - `include_top=False`
  - `pooling='avg'`
- Model digunakan sebagai **feature extractor (freeze weights)**

### 4. Classification
- Algoritma: **Logistic Regression**
- Training dilakukan menggunakan fitur hasil ekstraksi MobileNetV2
- Evaluasi menggunakan:
  - Accuracy
  - Precision
  - Recall
  - F1-Score

### 5. Deployment
- Backend: **Flask**
- Frontend: **HTML + Tailwind CSS**
- Sistem menerima **1 gambar** dan menampilkan hasil klasifikasi secara real-time

---

## 🚀 Fitur Aplikasi
- Upload satu gambar buah (apel atau jeruk)
- Preview gambar sebelum diproses
- Prediksi hasil klasifikasi secara real-time
- Tampilan UI modern dan responsif
- Model inference tanpa training ulang (inference only)

---

## 📂 Struktur Project
```

fruit-image-classification-mobilenet-logreg/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   ├── classifier.pkl
│   └── mobilenet_feature_extractor.h5
│
├── notebooks/
│   └── modeling.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   └── preview.js
│
└── venv/

````

---

## ⚙️ Instalasi & Menjalankan Aplikasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/fruit-image-classification-cnn.git
cd fruit-image-classification-cnn
````

### 2️⃣ Buat dan Aktifkan Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

### 4️⃣ Jalankan Aplikasi Flask

```bash
python app.py
```

### 5️⃣ Akses Aplikasi

Buka browser dan akses:

```
http://127.0.0.1:5000
```

---

## 📊 Contoh Output

* Input: Gambar apel → **Apple**
* Input: Gambar jeruk → **Orange**

---

## 🛠️ Teknologi yang Digunakan

* Python
* Flask
* TensorFlow / Keras
* NumPy
* Pillow
* Scikit-learn
* Joblib
* Tailwind CSS

---

## 📌 Catatan

* Model disimpan dalam format `.h5` dan `.pkl`
* Aplikasi dijalankan dalam mode development
* Dataset relatif kecil sehingga akurasi dapat tinggi
* Cocok untuk project akademik, praktikum, atau portofolio

---

## 👨‍💻 Author

**Hardika Setiyawan**
Informatics Student | Computer Vision & Machine Learning