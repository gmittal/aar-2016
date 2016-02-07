# AAR Natural Language Processing Project 2015-2016
# Simple program that takes plaintext as input and illustrates interpretation
# Written by Gautam Mittal
# Mentor: Robert Cheung
# Requires nltk.download()

import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob as tb
from textblob import Word as word
from textblob.parsers import PatternParser
from contractions import *

text = '''
The boy couldn't throw very well.
'''
storyText = tb(text)

def tokenize(string):
    string = string.replace("\n", "").replace(".", "")
    words = string.split(" ")


def prepare_text(stringBlob):
    if stringBlob.detect_language() != "en":
        stringBlob = stringBlob.translate(to="en")



    # legit_w = [w for w in words if not w in stops]
    return(tb(stringBlob))


def analyze_semantics(sentenceBlob): # requires tb(STRING) to be passed
    sentenceBlob = prepare_text(sentenceBlob)
    print(sentenceBlob)
    sentence_partsOfSpeech = sentenceBlob.tags

    for w in range(0, len(sentenceBlob.words)):
        current_word = sentenceBlob.words[w]

        # verbs
        if sentence_partsOfSpeech[w][1].find("VB") > -1:
            lemmWord = sentenceBlob.words[w].lemmatize("v")
            print(lemmWord)



# breaks the large text up into blob sized chunks
for sentence in storyText.sentences:
    print(tokenize(sentence))
    # analyze_semantics(sentence)
