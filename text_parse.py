# AAR Natural Language Processing Project 2015-2016
# Takes plaintext as input and illustrates interpretation
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
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP', 'VP', 'PP'])
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP', 'VP', 'PP'])

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
    # if str(stringBlob.detect_language()) != "en": # make text is in English
    #     print("["+stringBlob.detect_language()+"] Non-English string found. Translating...")
    #     stringBlob = stringBlob.translate(to="en")
    stringBlob = tokenize(stringBlob)
    return stringBlob

def treeToJSON(t):
    json = []
    for p in list(t):
        if str(type(p)) != "<class 'tuple'>":
            phraseJSON = {
                'label': p.label(),
                'text': list(p)
            }
            json.append(phraseJSON)
    return json

def stringifyTree(t):
    s = []
    for x in range(0, len(t)):
        s.append(t[x][0])
    return " ".join(s)

def simplifyTree(t):
    if t.label() == "NP":
        for x in list(t):
            if x[1].find("NN") == -1:
                t.remove(x)
        return stringifyTree(t)
    elif t.label() == "VP":
        # print(list(t))
        for x in list(t):
            if x[1].find("VB") == -1:
                t.remove(x)
        return stringifyTree(t)

def analyze_sent_semantics(sentenceBlob):
    tagged_s = tb(" ".join(prepare_text(sentenceBlob))).tags
    sent_tree = bigram_chunker.parse(tagged_s)
    sent_tree = treeToJSON(sent_tree) # convert to format that we can work with

    # verify the verb phrases
    for p in range(0, len(sent_tree)):
        phrase = sent_tree[p]
        if phrase["label"] == "VP":
            verbCount = 0
            for w in phrase["text"]:
                if w[1].find("VB") > -1:
                    verbCount += 1
            if verbCount == 0:
                phrase["label"] = "PSEUDO-VP"

    # print(sent_tree)

    predicted_subject = []
    for ph in range(0, len(sent_tree)):
        p = sent_tree[ph]
        # print(sent_tree[ph]["label"])
        # print(sent_tree[ph-1]["label"])

        if p["label"] == "NP" or (p["label"] == "PP" and (sent_tree[ph-1]["label"] == "NP" and ph-1 > -1)):
            for t in p["text"]:
                predicted_subject.append(t)
        if p["label"] == "VP":
            break;

    print("Subject: " + stringifyTree(predicted_subject)) # what we think the subject might be

def extract(storyString):
    storyText = tb(storyString)
    results = []
    for sentence in storyText.sentences: # split text into sentences
        results.append(analyze_sent_semantics(sentence))

    return results
