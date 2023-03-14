from transformers import pipeline

def load_classifier():
    classifier = pipeline(
        "text-classification", 
        model="Nithiwat/bert-base_claimbuster"
    )
    return classifier

def predict_claims(sents, classifier):
    claims = []
    for sent in sents:
        pred = classifier(sent)[0]

        if pred["label"] == "LABEL_1":
            claims.append(sent)
 
    return claims
