# AAR Natural Language Processing Project 2015-2016
# Simple program that takes plaintext as input and illustrates interpretation
# Written by Gautam Mittal
# Mentor: Robert Cheung
# Requires NLTK and its respective corpora

import re
import nltk
from nltk import CFG, ChartParser, RegexpParser
from nltk.corpus import stopwords, conll2000
from textblob import TextBlob as tb
from textblob import Word as word
from textblob.parsers import PatternParser
from contractions import *

# world's greatest story
text = '''
The quick brown fox decided to jump over the lazy dog.
The boy thought the Superbowl was great.
The crowd didn't love the event.
Sometimes, programmers have trouble debugging code.
'''
storyText = tb(text)


class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)


train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP', 'VP', 'PP'])
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP', 'VP', 'PP'])
bigram_chunker = BigramChunker(train_sents)
print(bigram_chunker.evaluate(test_sents)) # chunker accuracy


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
    tagged_s = tb(" ".join(prepare_text(sentenceBlob))).tags
    return bigram_chunker.parse(tagged_s)[0]

def main():
    for sentence in storyText.sentences: # split text into sentences
        print(analyze_semantics(sentence))


if __name__ == "__main__":
    main()
