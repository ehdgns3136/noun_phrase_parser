import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize

def parse_np():
    grammar = """
        EPN: {<DT|PRP.>?<JJ.*|CD>*<NN.*|CD|PRP>+} # element noun phrase
        BPN: {<EPN>(<IN><EPN>)*} # bunch of element noun phrase
        GPN: {<VBG><VBN>?(<BPN>|<TO|IN><BPN>)} # greund noun phrase
        TPN: {<TO><VB>(<BPN>|<TO|IN><BPN>)} # to noun phrase
        
        NP: {<BPN>*}
            {<GPN>} 
            {<TPN>}
            {<BPN><GPN|TPN>*}
    """
    the man
    the pretty man
    if word == DT:
        if word2 == NN:
            명사구다!
        if word2 == JJ:
            if word3 == NN:
                명사구디!

    with open('sentences.txt') as file:
        sentences = file.readlines()

    for sentence in sentences:
        sentence = sentence.replace("\n", "")
        token = word_tokenize(sentence)
        tag = nltk.pos_tag(token)
        cp = nltk.RegexpParser(grammar)
        tree = cp.parse(tag)

        terms = []
        for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
            terms.append(subtree.leaves())

        print(sentence)
        for term in terms:
            print(term)
        print()

parse_np()
