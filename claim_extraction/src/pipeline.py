from claim_extraction.src.sentence_rank import load_nlp, rank
from claim_extraction.src.claim_classifier import *
import PyPDF2

def read_pdf(path: str) -> str:
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        # read each page
        for i in range(len(reader.pages)):
            text += reader.pages[i].extract_text()
        return text

def run(text: str):
    text.replace("\n", "")
    # load models
    nlp = load_nlp()
    classifier = load_classifier()

    top_sents = rank(text, 
        nlp,
        resolution=10, # how many phrases are used for unit vector
        max_senteces=4 # how many sentences are returned
    )

    claims = predict_claims(top_sents, classifier)
    print(claims, "\n\n", len(claims))
    return claims