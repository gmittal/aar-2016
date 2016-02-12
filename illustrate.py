# AAR Natural Language Processing/Machine Learning Project 2015-2016
# Takes plaintext as input and illustrates interpretation
# Written by Gautam Mittal
# Mentor: Robert Cheung
# Requires Node.js and Python 3.4.6
# $ npm install && pip install -r requirements.txt

import os
from os.path import join, dirname
from subprocess import check_output as call
from dotenv import load_dotenv
import text_parse as textEngine
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SEARCH_KEY = os.environ.get("BING_SEARCH_KEY")

def main():
    query = "brown fox"
    r = call(["node", "image_search.js", SEARCH_KEY, query])
    r = str(r)[2:][:-3]
    print(r)
    image_json = json.loads(r)

    # print(image_json)
    # print(textEngine.extract("The quick brown fox jumped over the lazy dog. The story was amazing."))

if __name__ == "__main__":
    main()
