import streamlit as st
import spacy
from spacy import displacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

st.title("Named Entity Recognition (NER) with SpaCy")

# Initialize session state for text if it doesn't exist
if 'text_area' not in st.session_state:
    st.session_state.text_area = ""

# Text area for input
st.session_state.text_area = st.text_area("Enter text here", st.session_state.text_area)

text = st.session_state.text_area

if text.strip():
    doc = nlp(text)

    # Display entities with colors using displaCy HTML
    html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown("**Detected Entities:**", unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)

    # Optional: show entity table
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    if entities:
        st.markdown("**Entity Table:**")
        st.table(entities)
    else:
        st.info("No named entities found.")
else:
    st.info("Paste or type some text above to see NER results.")
