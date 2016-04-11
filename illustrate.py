# AAR Natural Language Processing/Machine Learning Project 2015-2016
# Takes plaintext as input and illustrates interpretation
# Written by Gautam Mittal
# Mentor: Robert Cheung
# Requires Node.js and Python 2.7
# $ npm install && pip install -r requirements.txt


import os, json, uuid, urllib, errno, requests
from os.path import join, dirname
from subprocess import check_output as call
from dotenv import load_dotenv
import text_parse as textEngine
import summarize as summaryEngine
from images2gif import writeGif
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SEARCH_KEY = os.environ.get("BING_SEARCH_KEY")
dl = urllib.URLopener()

def getImageFromString(s):
    r = call(["node", "image_search.js", SEARCH_KEY, s])
    r = str(r)
    r = r.replace("\n", "")
    return(r)


def generateGIF(file_names, size, uid):
    for fn in file_names:
        im = Image.open("./tmp_images/"+uid+"/"+fn)
        im = im.resize(size, Image.ANTIALIAS)
        im.save("./tmp_images/"+uid+"/"+fn, "JPEG")

    images = [Image.open("./tmp_images/"+uid+"/"+fn) for fn in file_names]
    writeGif("./tmp_images/"+uid+".gif", images, duration=0.5)

def make_dir(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def genTextMetrics(raw_text):
    summary = summaryEngine.summarize(raw_text)
    svo = textEngine.extract(summary)

    final_text_data = {
        "summary": summary,
        "svo_data": []
    }

    for scene in svo:
        # print scene
        sent_subject = scene["raw_subject"] if len(scene["simple_subject"]) == 0 else scene["simple_subject"]
        sent_object = scene["raw_object"] if len(scene["simple_object"]) == 0 else scene["simple_object"]
        sent_predicate = scene["predicate"]

        file_urls = {}

        file_urls["subject"] = getImageFromString(sent_subject)
        file_urls["verb"] = getImageFromString(sent_predicate)
        if len(sent_object) != 0:
            # print "OBJECT"
            file_urls["object"] = getImageFromString(sent_object)

        sent_data = {
            "subject": {
                "text": sent_subject,
                "image": file_urls["subject"]
            },
            "verb": {
                "text": sent_predicate,
                "image": file_urls["verb"]
            },
            "object": {
                "text": sent_object,
                "image": file_urls["object"] if len(sent_object) != 0 else None
            }
        }

        final_text_data["svo_data"].append(sent_data)

    return final_text_data
