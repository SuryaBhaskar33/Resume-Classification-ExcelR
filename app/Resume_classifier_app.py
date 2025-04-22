import streamlit as st
import joblib
from PyPDF2 import PdfReader
from docx import Document
import pythoncom
import win32com.client as win32
import tempfile
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io

# Load the saved TfidfVectorizer and SVM model
vectorizer = joblib.load(r'C:\Users\surya\Downloads\Resume-Classification\app\models\vectorizer.pkl')
model = joblib.load(r'C:\Users\surya\Downloads\Resume-Classification\app\models\svm_model.pkl')

# Debugging: Check the vectorizer and model
print(f"Loaded vectorizer vocabulary size: {len(vectorizer.get_feature_names_out())}")
print(f"Model expects {model.n_features_in_} features.")

# Function to predict resume category
def predict_resume_category(resume_text):
    if not resume_text.strip():
        raise ValueError("The resume text is empty.")
    
    resume_tfidf = vectorizer.transform([resume_text])
    print(f"Shape of resume_tfidf: {resume_tfidf.shape}")
    
    num_features = len(vectorizer.get_feature_names_out())
    
    if resume_tfidf.shape[1] != num_features:
        raise ValueError(f"Feature mismatch: Model expects {num_features} features but got {resume_tfidf.shape[1]}.")
    
    prediction = model.predict(resume_tfidf)
    return prediction[0]

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# Function to extract text from DOCX
def extract_text_from_docx(uploaded_file):
    doc = Document(uploaded_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to extract text from DOC using win32com
def extract_text_from_doc(uploaded_file):
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix='.doc') as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Initialize Word application
    pythoncom.CoInitialize()  # Required when working with COM in a thread
    word = win32.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(temp_file_path)
    
    # Extract the text
    text = doc.Content.Text
    doc.Close()
    word.Quit()
    
    # Clean up the temporary file
    os.remove(temp_file_path)
    
    return text

# Function to generate and display a word cloud
def display_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Streamlit UI
st.title('Resume Classification App')

# File uploader for resume
uploaded_file = st.file_uploader("Upload a resume", type=["txt", "pdf", "doc", "docx"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()
    
    # Extract text based on file type
    if file_type == 'txt':
        resume_text = uploaded_file.read().decode('utf-8')
    elif file_type == 'pdf':
        resume_text = extract_text_from_pdf(uploaded_file)
    elif file_type == 'docx':
        resume_text = extract_text_from_docx(uploaded_file)
    elif file_type == 'doc':
        resume_text = extract_text_from_doc(uploaded_file)
    else:
        st.error("Unsupported file type.")
        resume_text = ""

    if resume_text:
        try:
            # Predict category
            category = predict_resume_category(resume_text)
            st.write(f"Predicted Category: {category}")
            
            # Generate and display word cloud
            st.write("Word Cloud of the Resume:")
            buf = display_wordcloud(resume_text)
            st.image(buf, use_column_width=True)
            
        except ValueError as e:
            st.error(f"Error in prediction: {e}")
    else:
        st.error("No text extracted from the file.")
