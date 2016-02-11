# AAR Natural Language Processing/Machine Learning Project 2015-2016
# Takes plaintext as input and illustrates interpretation
# Written by Gautam Mittal
# Mentor: Robert Cheung

import os
from os.path import join, dirname
from dotenv import load_dotenv
import text_parse as textEngine
import google as Google

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SEARCH_KEY = os.environ.get("BING_SEARCH_KEY")

def main():


    # request = urllib3.Request(url)
    # request.add_header('Authorization', credentialBing)
    # requestOpener = urllib2.build_opener()
    # response = requestOpener.open(request)

    # results = json.load(response)
    # print(textEngine.extract("The quick brown fox jumped over the lazy dog. The story was amazing."))

if __name__ == "__main__":
    main()
