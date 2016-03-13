# AAR Natural Language Processing/Machine Learning Project 2015-2016
# Summarizes text using tf-idf technique
# Written by Gautam Mittal
# Mentor: Robert Cheung
# Requires Node.js and Python 2.7

from __future__ import division
import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def summarize(document1):
    document1 = tb(document1)
    bloblist = document1.sentences
    relevance_scores = []
    relevancy = {}
    for i, blob in enumerate(bloblist):
        # print "Top words in sentence " + str(i)
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        relevance = 0
        sum_relevancy = 0
        for word, score in sorted_words:
            # print "\tWord: {}, TF-IDF: {}".format(word, score)
            sum_relevancy += score
        relevance = sum_relevancy/len(sorted_words)
        relevance_scores.append(relevance)
        relevancy[str(i)] = relevance

    relevance_scores.sort(reverse=True)

    final_sentences = []
    num_top_results = 3
    for s in range(0, len(relevance_scores[:num_top_results])):
        for key in relevancy:
            if relevancy[key] == relevance_scores[s]:
                final_sentences.append(int(key))

    final_sentences.sort()
    final_text = ""
    for x in range(0, len(final_sentences)):
        if x != 0:
            final_text += " " + str(document1.sentences[final_sentences[x]]).replace('\n', '')
        else:
            final_text = str(document1.sentences[final_sentences[x]]).replace('\n', '')

    return str(final_text)
