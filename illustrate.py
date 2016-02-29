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

def getImageFromString(s):
    r = call(["node", "image_search.js", SEARCH_KEY, s])
    r = str(r)[:-3][2:]
    return(r)


def main():
    svo = textEngine.extract("Even aside from the rain and wind it hadn't been a happy practice session. Fred and George, who had been spying on the Slytherin team, had seen for themselves the speed of those new Nimbus Two Thousand and Ones. They reported that the Slytherin team was no more than seven greenish blurs, shooting through the air like missiles.")

    for scene in svo:
        print(scene)

if __name__ == "__main__":
    main()
