
This project is an end-to-end machine learning application that classifies resumes into job categories such as Data Scientist, SQL Developer, HR, etc. Built using NLP techniques and an SVM classifier, it automates the resume screening process to reduce manual HR effort. The app is deployed with a user-friendly Streamlit interface.

---

## 🎯 Business Objective

To automate and optimize the resume classification process within HR Management by reducing manual screening time, increasing consistency, and improving accuracy with minimal human intervention.

---

## 🛠 Features

- 📄 Upload resumes in `.pdf`, `.doc`, `.docx`, or `.txt` format
- 📊 Predicts job category using a pre-trained SVM model
- ☁️ Generates word cloud from resume content
- 📦 Converts a folder of resumes into a CSV dataset for training

---

## 🗂 Folder Structure

Resume-Classification/
├── app/
    │ ├── resume_classifier_app.py # Streamlit app │
└── models/ 
│ ── svm_model.pkl │

 └── vectorizer.pkl │
├── Data/ │ ├── R-Zip/ # Zipped raw resumes │ ├── extract/ # Extracted resumes │ └── resume.csv # Structured dataset │ ├── notebooks/ │ └── model_training.ipynb # SVM + TF-IDF model building │ ├── assets/ │ ├── ui_preview.png # Screenshot of the app │ ├── run_log.png # CMD output │ ├── Problem-Statment.docx # Business overview and plan ├── README.md # Project overview (this file) ├── requirements.txt # Required packages ├── environment.yml # Conda environment setup
