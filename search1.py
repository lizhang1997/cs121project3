import json
import re
from collections import defaultdict

import math
from typing import Set, Any
from urllib.parse import urlparse
from bs4 import BeautifulSoup

import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))



class Search_engine():
    def __init__(self):
        self._num_of_doc = 0
        self._unique_word = defaultdict()
        self._total_unique = 0

    def read_file(self):
        with open("/Users/lizhang/Downloads/WEBPAGES_RAWt/bookkeeping.json") as files:
            data = json.load(files)
            self._num_of_doc = 0
            self._total_unique = 0
            Informatics = 0
            Mondego = 0
            Irvine = 0
            artifical = 0
            computer = 0
            for num,link in data.items():
                self._num_of_doc+=1
                with open("/Users/lizhang/Downloads/WEBPAGES_RAWt/" + num, encoding="utf-8") as file:
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
                                self._total_unique +=1
                                #print(self._total_unique)
                            else:
                                self._unique_word[eachword] +=1
                    if "informatics" in total and Informatics < 20:
                        print("Informatics: " + link)
                        Informatics += 1
                    if "mondego" in total and Mondego < 20:
                        print("Mondego: " + link)
                        Mondego += 1
                    if "irvine" in total and Irvine <  20:
                        print("Irvine: " + link)
                        Irvine += 1
                    if "artificial" in total and "intelligence" in total and artifical < 20:
                        print("artificial intelligence: " + link)
                        artifical+=1
                    if "computer" in total and "science" in total and computer < 20:
                        print("computer science: "+ link)
                        computer+=1
        output = open("Milestone1_result","w")

        output.write("Number of docs:" + str(self._num_of_doc))
        output.write("Number of unique words"+str(self._total_unique))
        for key, value in sorted(self._unique_word.items()):
            output.write(key+": " +str(value) + "\n")







if __name__ == "__main__":
    token = Search_engine()
    token.read_file()












