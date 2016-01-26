# AAR Natural Language Processing Project 2015-2016
# Simple program that takes plaintext as input and illustrates interpretation
# Written by Gautam Mittal
# Mentor: Robert Cheung

from textblob import TextBlob as tb
from textblob import Word as word

text = '''
The quick brown fox jumped over the lazy dog. He was very good.
'''
storyText = tb(text)

# does simple relational analysis
def analyze_semantics(sentenceBlob): # requires tb(STRING) to be passed
    # make sure the string is in English
    if sentenceBlob.detect_language() != "en":
        sentenceBlob = sentenceBlob.translate(to="en")
    # print(sentenceBlob)

    for w in range(0, len(sentenceBlob.words)):
        lemmWord = sentenceBlob.words[w].lemmatize("v")
        print(lemmWord)

# breaks the large text up into blob sized chunks
for sentence in storyText.sentences:
    analyze_semantics(sentence)
