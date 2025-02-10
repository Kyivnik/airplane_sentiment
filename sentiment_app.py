import streamlit as st
import joblib
import re

# Завантаження збереженої моделі та TF-IDF векторизатора
model = joblib.load("model.pkl")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Функція для базового очищення тексту
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Заголовок додатку
st.title("Sentiment analysis for airlines")
st.write("Enter the text of the tweets to determine his mood.")

# Текстове поле для введення користувачем
user_input = st.text_area("Enter the text here:")

# Кнопка для запуску аналізу
if st.button("Analyze"):
    if user_input:
        # Очищення тексту
        cleaned_text = clean_text(user_input)
        # Перетворення тексту за допомогою TF-IDF
        transformed_text = tfidf_vectorizer.transform([cleaned_text])
        # Прогнозування настрою
        prediction = model.predict(transformed_text)[0]
        st.write(f"Predicted mood: **{prediction}**")
    else:
        st.write("Please enter the text for analysis.")
