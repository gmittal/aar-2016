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

document1 = tb("""Python is a 2000 made-for-TV horror movie directed by Richard
Clabaugh. The film features several cult favorite actors, including William
Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
Whalen. The film concerns a genetically engineered snake, a python, that
escapes and unleashes itself on a small town. It includes the classic final
girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
 California and Malibu, California. Python was followed by two sequels: Python
 II (2002) and Boa vs. Python (2004), both also made-for-TV films.""")

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
print relevance_scores

for s in range(0, len(relevance_scores[:3])):
    for key in relevancy:
        if relevancy[key] == relevance_scores[s]:
            print document1.sentences[int(key)]
