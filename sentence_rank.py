import spacy
import pytextrank

from math import sqrt
from operator import itemgetter


def load_nlp():
    # load spaCy model.
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank", last=True)
    return nlp


def unit_vector(doc, sent_bounds, limit_phrases=10):
    phrase_id = 0
    unit_vector = []

    for p in doc._.phrases:
        unit_vector.append(p.rank)
        for chunk in p.chunks:
            for sent_start, sent_end, sent_vector in sent_bounds:
                if chunk.start >= sent_start and chunk.end <= sent_end:
                    sent_vector.add(phrase_id)
                    break

        phrase_id += 1

        if phrase_id == limit_phrases:
            break

    sum_ranks = sum(unit_vector)
    unit_vector = [ rank/sum_ranks for rank in unit_vector ]
    return unit_vector

def sent_rank(sent_bounds, unit_vector):
    sent_rank = {}
    sent_id = 0

    for sent_start, sent_end, sent_vector in sent_bounds:
        sum_sq = 0.0
        for phrase_id in range(len(unit_vector)):
            if phrase_id not in sent_vector:
                sum_sq += unit_vector[phrase_id]**2.0

        sent_rank[sent_id] = sqrt(sum_sq)
        sent_id += 1
    return sent_rank

def top_n(doc, sent_rank, max_sentences):

    sent_text = {}
    sent_id = 0

    sentences = []

    for sent in doc.sents:
        sent_text[sent_id] = sent.text
        sent_id += 1

    num_sent = 0

    for sent_id, rank in sorted(sent_rank.items(), key=itemgetter(1)):
        sentences.append(sent_text[sent_id])
        num_sent += 1

        if num_sent == max_sentences:
            break
    return sentences

def rank(text, nlp, resolution, max_senteces):
    # parse into spacy pipeline
    doc = nlp(text)

    # array with start and stop of each sentence + an empyty set per sentence
    sent_bounds = [ [s.start, s.end, set([])] for s in doc.sents ]

    # create the unit vector from phrases
    uv = unit_vector(doc, sent_bounds, limit_phrases=resolution)

    # rank the senteces in relation to unit vector
    sr = sent_rank(sent_bounds, uv)

    # return the top n most related sentences
    return top_n(doc, sr, max_senteces)
