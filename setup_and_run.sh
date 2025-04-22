#!/bin/bash

# Resume Classification Project Setup Script

echo "🔧 Setting up Python environment..."
python -m venv venv
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🚀 Launching Streamlit app..."
streamlit run app/resume_classifier_app.py
