import json
import re
from collections import defaultdict

import math
from urllib.parse import urlparse
from bs4 import BeautifulSoup

import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))



class Search_engine():
    def __init__(self):
        self._num_of_doc
        self._unique_word = defaultdict()


    def read_file(self):
        with open("/Users/lizhang/Downloads/WEBPAGES_RAW/bookkeeping.json") as files:
            data = json.load(files)
            self._num_of_doc = 0
            for num,link in data.items():
                self._num_of_doc+=1
                with open("/Users/melaniepeng/Desktop/CS 121/WEBPAGES_RAW/" + num, encoding="utf-8") as file:
                    readfile = file.read()
                    beautiful = BeautifulSoup(readfile, "html.parser")
                    bb = beautiful.body
                    for tag in beautiful.select("style"):
                        tag.decompose
                    words = beautiful.get_text(separator="/n").lower()
                    total = re.findall("[A-Za-z0-9]+",words)
                    for eachword in total:
                        if eachword not in stop_words:
                            if eachword not in self._unique_word.keys():
                                self._unique_word[eachword] = 1
                            else:
                                self._unique_word[eachword] +=1



if __name__ == "__main__":
    token = Search_engine()
    token.read_file()












