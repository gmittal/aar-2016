# AAR Natural Language Processing/Machine Learning Project 2015-2016
# Takes plaintext as input and illustrates interpretation
# Written by Gautam Mittal
# Mentor: Robert Cheung

from os.path import join, dirname
from dotenv import load_dotenv
import text_parse as textEngine
from image_search import BingSearchAPI

SEARCH_KEY = os.environ.get("BING_SEARCH_KEY")

def main():
    query_string = "cat"
    bing = BingSearchAPI(SEARCH_KEY)
    params = {'ImageFilters':'"Face:Face"', '$format': 'json', '$top': 10, '$skip': 0}
    print(bing.search('image',query_string,params).json()) # requests 1.0+
    # print(textEngine.extract("The quick brown fox jumped over the lazy dog. The story was amazing."))

if __name__ == "__main__":
    main()
