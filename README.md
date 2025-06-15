# 🧠 Suicide Ideation Detection App

This project is a **real-time NLP-based suicide ideation detector** built with `Streamlit`, using a pretrained Hugging Face model to classify social media posts as **Suicidal** or **Non-Suicidal**. It supports emoji-based sentiment and shows prediction confidence.

---

## 🚀 Features

- 🧾 **Text + Emoji** input support
- 🤖 **Pretrained transformer-based model**
- 📊 **Real-time prediction** with confidence score
- 🎯 Simple and intuitive **Streamlit UI**
- 🧹 Text cleaning and preprocessing pipeline

---

## 📁 Project Structure

NLP-Suicidal-Detection/
│
├── app.py # Streamlit app
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── src/
├── init.py
└── preprocessing.py # Text cleaning logic


---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/moulik-23/Suicidal-Detection.git
cd Suicidal-Detection

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Login to Hugging Face (for private models if needed)
bash
Copy
Edit
huggingface-cli login
▶️ Running the App
bash
Copy
Edit
streamlit run app.py
Once the app starts, open http://localhost:8501 in your browser.

📦 Model Used
🤗 cardiffnlp/twitter-roberta-base-emotion

A RoBERTa-based model trained on emotion-labeled tweets.

Handles emoji-rich and short text effectively.

View on Hugging Face

✨ Example Inputs
txt
Copy
Edit
I can't take this pain anymore 😔💔
txt
Copy
Edit
I'm really happy today 😄☀️
📌 Disclaimer
This tool is for research and educational purposes only. It is not a substitute for professional mental health support. If you or someone you know is in crisis, please seek immediate help from a mental health professional or helpline.

📚 Acknowledgements
Hugging Face 🤗

Streamlit

Cardiff NLP

Feel free to contribute
Email:-moulikzinzala912@gmail.com





