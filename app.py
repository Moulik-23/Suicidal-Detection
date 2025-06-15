# app.py

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from src.preprocessing import clean_text

# Use GoEmotions model
model_name = "SamLowe/roberta-base-go_emotions"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# Class labels for GoEmotions (28 emotions + "neutral")
labels = [
    "admiration", "amusement", "anger", "annoyance", "approval", "caring", "confusion",
    "curiosity", "desire", "disappointment", "disapproval", "disgust", "embarrassment",
    "excitement", "fear", "gratitude", "grief", "joy", "love", "nervousness", "optimism",
    "pride", "realization", "relief", "remorse", "sadness", "surprise", "neutral"
]

# UI
st.set_page_config(page_title="Suicide-Relevant Emotion Detector", page_icon="🧠")
st.title("🧠 Suicide-Relevant Emotion Detector")
text_input = st.text_area("Enter a social media post:", height=150)

if st.button("Analyze"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        cleaned = clean_text(text_input)

        # Tokenize input
        inputs = tokenizer(cleaned, return_tensors="pt", truncation=True, padding=True, max_length=128)
        with torch.no_grad():
            outputs = model(**{k: v.to("cpu") for k, v in inputs.items()})
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
            pred = torch.argmax(probs, dim=-1).item()
            confidence = probs[0][pred].item()

        predicted_label = labels[pred]

        st.markdown(f"### 🧾 Prediction: **{predicted_label.capitalize()}**")
        st.progress(confidence)
        st.markdown(f"**Confidence:** `{confidence:.2%}`")

        if predicted_label in ["grief", "remorse", "sadness", "fear"]:
            st.error("⚠️ This message may contain suicidal or emotionally distressing intent.")
