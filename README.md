# Sentence-Fixer-Translator
Perfect! Since your **Sentence-Fixer-Translator** project uses:

* `streamlit` for the UI,
* `nltk` for tokenization,
* `re` for regex-based processing,
* `deep_translator` for translation,
* `langdetect` for language detection,

here’s an **updated `README.md`** that reflects your actual setup:

---

````markdown
# 🌐 Sentence-Fixer-Translator

**Sentence-Fixer-Translator** is a simple and interactive NLP-based web app built with Streamlit. It detects the language of a sentence, corrects its grammar using basic NLP and regex logic, and translates it to your preferred language using the Google Translator API.

---

## 🚀 Features

- 🧠 Tokenizes and processes text using `nltk`
- 🔍 Detects input language with `langdetect`
- 🛠 Fixes common sentence issues (e.g., casing, spacing)
- 🌍 Translates text with `deep_translator` and Google Translate
- 🖥 Built with a clean Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NLTK (Natural Language Toolkit)
- deep-translator
- langdetect
- Regular Expressions (`re`)

---

## 📦 Installation

Make sure you have Python 3.7+ installed.

```bash
# Clone the repository
git clone https://github.com/harshii-02/Sentence-Fixer-Translator.git
cd Sentence-Fixer-Translator

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

---

## 🧪 Run the App

```bash
streamlit run main.py
```

You’ll see the app running in your default web browser at `http://localhost:8501`.

---



---

## 📌 Example Usage

* **Input:** `i go school everyday`
* **Fixed:** `I go to school every day`
* **Translated to French:** `Je vais à l'école tous les jours`

---

## 🔧 Dependencies (requirements.txt)

```
streamlit
nltk
deep-translator
langdetect
```

You should also download NLTK tokenizers at runtime:

```python
import nltk
nltk.download('punkt')
```

---
