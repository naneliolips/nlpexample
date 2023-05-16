import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
# Import the necessary libraries for NLP
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required resources for NLP
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))



############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Preprocess the text
############################################################
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words and lemmatize the tokens
    preprocessed_tokens = [
        lemmatizer.lemmatize(token.lower())
        for token in tokens
        if token.lower() not in stop_words and token.isalpha()
    ]

    # Join the preprocessed tokens back into a string
    preprocessed_text = ' '.join(preprocessed_tokens)

    return preprocessed_text


############################################################
# Answer questions about science
############################################################
def answer_science_questions(text):

    # Example: Answer specific science questions
    if "what is the speed of light" in text:
        return "The speed of light in a vacuum is approximately 299,792,458 meters per second."
    elif "who discovered gravity" in text:
        return "Sir Isaac Newton is credited with discovering the law of universal gravitation."
    elif "what is the structure of DNA" in text:
        return "DNA (deoxyribonucleic acid) is a double helix structure made up of nucleotides."
    else:
        return "I'm sorry, but I don't have the answer to that question at the moment."
############################################################
# Callback function called on each execution pass
############################################################


def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        # Preprocess the input text
        preprocessed_text = preprocess_text(text)

        # Answer science questions
        response = answer_science_questions(preprocessed_text)
        output.append(response)

    return SimpleText(dict(text=output))
