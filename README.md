# 📸 Photo Metadata Extractor

*A lightweight Flask + Docker web application that extracts and displays EXIF metadata from uploaded images.*

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Flask-blue" />
  <img src="https://img.shields.io/badge/Language-Python%203-green" />
  <img src="https://img.shields.io/badge/Container-Docker-orange" />
  <img src="https://img.shields.io/badge/Metadata-EXIF-purple" />
</p>

This project allows users to upload a photo and instantly view its embedded **EXIF metadata**—including camera model, shutter speed, aperture, ISO, focal length, and more.
Built using **Flask**, **Pillow**, and **Docker**, the application is simple, portable, and easy to extend.

---

## 🛠️ Features

* Upload JPEG or PNG images
* Extract EXIF metadata using **Pillow (PIL)**
* Clean, responsive HTML/CSS UI
* Organized backend using Flask blueprints
* Dockerized for easy deployment
* Optional support for cloud storage (Azure Blob Storage)

---

## 📁 Project Structure

```
photo-metadata-site/
│
├── src/                     # Main Flask application code
│   ├── app.py               # Application entry point
│   └── utils/               # Optional helpers for metadata extraction
│
├── templates/               # Jinja2 HTML templates
│   ├── index.html
│   └── result.html
│
├── static/                  # CSS, images, client-side assets
│   └── style.css
│
├── assets/                  # Additional project assets (optional)
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker image configuration
├── .gitignore
└── README.md
```

---

## 🚀 Running the Application

### ▶️ Local Setup

#### 1. Clone the repository

```bash
git clone https://github.com/romancgilbert/photo-metadata-site
cd photo-metadata-site
```

#### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the app

```bash
python src/app.py
```

#### 5. Open your browser:

👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

### 🐳 Running with Docker

#### 1. Build the image

```bash
docker build -t photo-metadata-site .
```

#### 2. Run the container

```bash
docker run -p 5000:5000 photo-metadata-site
```

#### 3. Visit:

👉 [http://localhost:5000/](http://localhost:5000/)

---

## 📸 How It Works

1. User uploads a photo
2. Flask saves the file temporarily
3. Pillow reads the file and extracts EXIF metadata
4. Metadata is parsed into human-readable fields
5. Data is rendered using HTML templates on the results page

The result is a fast, intuitive tool for photographers, developers, and anyone needing to inspect image metadata.

---

## ☁️ Optional Azure Blob Storage Extension (Not Enabled by Default)

This application can be extended to store uploaded images in **Azure Blob Storage** instead of the local filesystem.

### Why add Blob Storage?

* Persistent cloud-based image storage
* Easier deployment to Azure App Service
* Scalable architecture for larger applications
* Integrates cleanly with CI/CD via GitHub Actions

### Example integration (future work)

* Configure a Blob container
* Upload files using `azure-storage-blob` Python SDK
* Replace local `uploads/` path with cloud URL references

> This is an optional enhancement — not required to run the local app.

If you want, I can generate a full Blob Storage integration script and instructions.

---

## 🔮 Future Improvements

* Image histogram display
* Map rendering if GPS EXIF is available
* Drag-and-drop upload UI
* Multi-image batch processing
* Deeper metadata formatting (lens info, exposure mode, etc.)
* Deployment (Azure, Render, Railway)

---

## 👤 Author

**Roman Gilbert**
University of Virginia — Data Science + Civil Engineering 2nd year
Photographer • UI/UX • Data Engineering
GitHub: [romancgilbert](https://github.com/romancgilbert)
LinkedIn: [https://www.linkedin.com/in/roman-gilbert-377bb6325/](https://www.linkedin.com/in/roman-gilbert-377bb6325/)
Photography Portfolio:[https://www.instagram.com/rchristian.digital/]
---
