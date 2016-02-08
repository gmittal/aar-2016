# AAR Natural Language Processing Project 2015-2016
# Simple program that takes plaintext as input and illustrates interpretation
# Written by Gautam Mittal
# Mentor: Robert Cheung
# Requires NLTK and its respective corpora

import re
import nltk
from nltk import CFG, ChartParser, RegexpParser
from nltk.corpus import stopwords
from textblob import TextBlob as tb
from textblob import Word as word
from textblob.parsers import PatternParser
from contractions import *

text = '''
In New York, The New York Times published their first article.
'''
storyText = tb(text)

def tokenize(string):
    string = str(string.replace("\n", "").replace(".", "")).lower()
    words = string.split(" ")
    for w in range(0, len(words)): # fix contractions
        if (words[w].find("'") > -1):
            if (words[w] in contractions):
                replace_contract = contractions[words[w]]
                words.pop(w)
                r = list(reversed(replace_contract.split(" ")))
                for cw in range(0, len(r)):
                    words.insert(w, r[cw])
    return words


def prepare_text(stringBlob):
    if stringBlob.detect_language() != "en":
        stringBlob = stringBlob.translate(to="en")
    stringBlob = tokenize(stringBlob)
    return stringBlob


def analyze_semantics(sentenceBlob):
    simple_grammar = "NP: {<DT>?<JJ>*<NN>}"
    tagged_s = tb(" ".join(prepare_text(sentenceBlob))).tags
    parser = nltk.RegexpParser(simple_grammar)
    print(parser.parse(tagged_s))


def main():
    for sentence in storyText.sentences: # split text into sentences
        print(analyze_semantics(sentence))


if __name__ == "__main__":
    main()
