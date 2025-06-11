import streamlit as st
import nltk
import re
from deep_translator import GoogleTranslator
from langdetect import detect

# Download tokenizer
nltk.download('punkt')

# Function to fix run-on sentences in Hindi
def fix_run_on_sentence_hindi(text):
    text = re.sub(r'(?<=[\u0900-\u097F]) (?=(मैं|तू|वह|यह|हम|आप|वे|लेकिन|और|क्योंकि|इसलिए|जब|फिर|तो|कि|जो|अगर|यदि|जिस|क्या|कैसे|कब|कौन|कहाँ|क्यों))', '। ', text)
    text = re.sub(r'([।]+)', '।', text)  # Remove duplicate "।"
    
    if text and not text.endswith("।"):
        text += "।"

    sentences = re.split(r'। ', text)
    sentences = [s.strip().capitalize() for s in sentences if s.strip()]
    fixed_text = "। ".join(sentences)

    return fixed_text.strip()

# Function to fix run-on sentences in Tamil
def fix_run_on_sentence_tamil(text):
    text = re.sub(r'(?<=[\u0B80-\u0BFF]) (?=(நான்|நீ|அவன்|அவள்|அது|நாங்கள்|நீங்கள்|அவர்கள்|ஆனால்|மற்றும்|ஏனெனில்|எப்போது|அப்பொழுது|அதனால்|எனவே|பின்|அதை|அவர்கள்|எப்படி|ஏன்|எங்கே|யார்))', '. ', text)
    text = re.sub(r'([.]+)', '.', text)  # Remove duplicate "."

    if text and not text.endswith("."):
        text += "."

    sentences = re.split(r'\. ', text)
    sentences = [s.strip().capitalize() for s in sentences if s.strip()]
    fixed_text = ". ".join(sentences)

    return fixed_text.strip()

# Function to fix run-on sentences in English
def fix_run_on_sentence_english(text):
    # Add punctuation where required
    text = re.sub(r'(?<=\w) (?=(I|You|He|She|It|We|They|But|And|Because|So|Then|That|Which|If|Who|What|How|When|Where|Why))', '. ', text)

    # Fix spaces before punctuation
    text = re.sub(r'\s+([.,!?])', r'\1', text)

    # Ensure commas before conjunctions when necessary
    text = re.sub(r'\b(and|but|so|because|yet|although)\b', r', \1', text)

    # Ensure full stop at the end
    if text and not text.endswith("."):
        text += "."

    # Capitalize sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip().capitalize() for s in sentences if s.strip()]
    fixed_text = " ".join(sentences)

    return fixed_text.strip()

# Function to detect language
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# Function to translate text
def translate_text(text, target_lang):
    detected_lang = detect_language(text)
    if detected_lang == target_lang:
        return text  # No translation needed
    try:
        return GoogleTranslator(source=detected_lang, target=target_lang).translate(text)
    except:
        return "❌ Translation failed. Please try again."

# Streamlit UI
st.set_page_config(page_title="Sentence Fixer", page_icon="📝", layout="centered")

st.title("📝 Sentence Fixer & Translator")
st.write("Enter a run-on sentence in English, Hindi, or Tamil, and we will correct it with proper punctuation. Optionally, you can also translate it into another language.")

# Language selection
indian_languages = {
    "Hindi (हिन्दी)": "hi",
    "Tamil (தமிழ்)": "ta",
    "Telugu (తెలుగు)": "te",
    "Bengali (বাংলা)": "bn",
    "Marathi (मराठी)": "mr",
    "Malayalam (മലയാളം)": "ml",
    "Kannada (ಕನ್ನಡ)": "kn",
    "Punjabi (ਪੰਜਾਬੀ)": "pa",
    "Gujarati (ગુજરાતી)": "gu",
    "English (English)": "en"
}
selected_language = st.selectbox("🔄 Select Output Language:", list(indian_languages.keys()))

# User input
user_text = st.text_area("✍️ Enter your sentence:", "")

# Checkbox for translation
enable_translation = st.checkbox("🔀 Translate to selected language")

if st.button("✅ Fix Sentence"):
    if user_text.strip():
        detected_lang = detect_language(user_text)
        
        if detected_lang == "hi":
            fixed_sentence = fix_run_on_sentence_hindi(user_text)
        elif detected_lang == "ta":
            fixed_sentence = fix_run_on_sentence_tamil(user_text)
        elif detected_lang == "en":
            fixed_sentence = fix_run_on_sentence_english(user_text)
        else:
            fixed_sentence = user_text  # No correction for other languages

        st.success("### ✅ Fixed Sentence:")
        st.write(fixed_sentence)

        if enable_translation:
            translated_sentence = translate_text(fixed_sentence, indian_languages[selected_language])
            st.info(f"### 🌎 Translated to {selected_language}:")
            st.write(translated_sentence)
    else:
        st.warning("⚠️ Please enter a sentence.")
