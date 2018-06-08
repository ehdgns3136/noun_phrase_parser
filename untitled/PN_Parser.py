import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

sentences = [
    "hello, my name is donghoon kim",
    "nice to meet you! Where are you from?",
    "I'm from Korean. What about you?"
]

for sentence in sentences:
    nltk.pos_tag_sents(sentence)
    token = word_tokenize(sentence)
    print(token)
    tag = nltk.pos_tag(token)
    print(tag)

