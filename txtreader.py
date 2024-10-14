################# Import the required Packages #######################

import spacy
import streamlit as st
import pandas as pd
from spacy import displacy
from io import StringIO

################### Load the spaCy model      ##########################
nlp = spacy.load("en_core_web_sm")

# Function to extract named entities and their labels
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities, doc

# Streamlit application
def main():
    st.title("Named Entity Recognition Visualization")

    # File uploader
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    
    if uploaded_file is not None:
        # Read the file content
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        text = stringio.read()
        
        # Extract entities
        entities, doc = extract_entities(text)
        
        # Display the original text with named entities highlighted
        html = displacy.render(doc, style="ent")
        st.write("### Named Entities Visualization")
        st.write(html, unsafe_allow_html=True)

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