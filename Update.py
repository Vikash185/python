################# Import the required Packages #######################
import spacy
import streamlit as st
import pandas as pd
from spacy import displacy
from io import StringIO
import PyPDF2  # For reading PDF files

################### Load the spaCy model ##########################
nlp = spacy.load("en_core_web_sm")

# Function to extract named entities and their labels
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities, doc

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Streamlit application
def main():
    st.title("Named Entity Recognition Visualization")

    # File uploader: supports both .txt and .pdf files
    uploaded_file = st.file_uploader("Choose a PDF or text file", type=["pdf", "txt"])
    
    if uploaded_file is not None:
        # Check if the uploaded file is a PDF
        if uploaded_file.name.endswith(".pdf"):
            text = extract_text_from_pdf(uploaded_file)
        else:
            # Handle .txt files with different encodings
            try:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            except UnicodeDecodeError:
                stringio = StringIO(uploaded_file.getvalue().decode("ISO-8859-1"))
            text = stringio.read()

        # Extract named entities
        entities, doc = extract_entities(text)

        # Display the original text with named entities highlighted
        html = displacy.render(doc, style="ent")
        st.write("### Named Entities Visualization")
        st.markdown(html, unsafe_allow_html=True)

        # Create a DataFrame for the entities
        df = pd.DataFrame(entities, columns=["Entity", "Label"])

        # Display the DataFrame
        st.write("### Entity Table")
        st.write(df)

        # Download button for the entity table
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Entity Table as CSV",
            data=csv,
            file_name='entity_table.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    main()


