from math import nan

import gensim
from gensim.utils import simple_preprocess


def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

# Remove Stop Words
def doc_to_words_split(docs):
    for doc in docs:
        sentences = doc.split('.')
        result = []
        for sentence in sentences:
            result.extend(gensim.utils.simple_preprocess(str(sentence), deacc=False))
            result.extend(['.'])
        yield(result)  # deacc=True removes punctuations



def remove_stopwords(texts, stop_words):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]


def make_bigrams(texts,bigram_mod):
    return [bigram_mod[doc] for doc in texts]


def make_trigrams(texts,trigram_mod):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]


def lemmatization(texts, nlp, allowed_postags=['NOUN']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out

