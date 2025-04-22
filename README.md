
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
│   ├── resume_classifier_app.py       # Streamlit application
│
├── models/
│   ├── svm_model.pkl                  # Trained SVM model
│   └── vectorizer.pkl                 # TF-IDF vectorizer
│
├── Data/
│   ├── R-Zip/                         # Original zipped resumes
│   ├── extract/                       # Extracted resume files
│   └── resume.csv                     # Final structured dataset
│
├── notebooks/
│   └── model_training.ipynb          # Model training & EDA notebook
│
├── assets/
│   ├── ui_preview.png                # Screenshot of Streamlit UI
│   └── run_log.png                   # CMD output example
│
├── Problem-Statment.docx             # Business overview and phases
├── README.md                         # Project documentation
├── requirements.txt                  # Python package requirements
└── environment.yml                   # Conda environment file




📁 Add Your Resumes
Place your resumes inside the /Data/extract/ folder to start testing or building your dataset.

🖼 Sample Outputs

-Streamlit UI 

![ui_preview](https://github.com/user-attachments/assets/0c5ff5da-c07a-4631-bbda-63d63bd309c8)
-Terminal Logs

![run_log](https://github.com/user-attachments/assets/1056cacf-6e3f-4cc2-bb26-d9a92a4f6744)



## 📚 Problem Statement

- **See Problem-Statment.docx for detailed business goals, timeline, and delivery protocols.

## 📦 Tech Stack

- **Language:** Python, Jupyter Notebook
- **Frameworks:** Streamlit, Scikit-learn
- **Libraries:** WordCloud, Matplotlib, PyPDF2, python-docx, win32com (for DOC parsing)


## 👤 Author

**Surya Bhaskar**  
Made with ❤️ and Machine Learning

