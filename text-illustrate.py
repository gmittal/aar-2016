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
The quick brown fox jumped over the lazy dog.
'''
storyText = tb(text)

def tokenize(string):
    string = str(string.replace("\n", ""))#.replace(".", ""))
    words = string.split(" ")
    for w in range(0, len(words)): # fix contractions
        if (words[w].lower().find("'") > -1):
            if (words[w] in contractions):
                replace_contract = contractions[words[w]]
                words.pop(w)
                r = list(reversed(replace_contract.split(" ")))
                for cw in range(0, len(r)):
                    words.insert(w, r[cw])
    return words


def prepare_text(stringBlob):
    if stringBlob.detect_language() != "en": # make text is in English
        stringBlob = stringBlob.translate(to="en")
    stringBlob = tokenize(stringBlob)
    return stringBlob


def analyze_semantics(sentenceBlob):
    grammar_model = r"""
      NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
      PP: {<IN><NP>}               # Chunk prepositions followed by NP
      VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
      CLAUSE: {<NP><VP>}           # Chunk NP, VP
      """
    tagged_s = tb(" ".join(prepare_text(sentenceBlob))).tags
    parser = nltk.RegexpParser(grammar_model)
    structure_tree = parser.parse(tagged_s) # sentence structure tree
    return structure_tree

def main():
    for sentence in storyText.sentences: # split text into sentences
        print(analyze_semantics(sentence))


if __name__ == "__main__":
    main()
