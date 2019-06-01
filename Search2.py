import json
import sys
import re
from collections import defaultdict

import math
from typing import Set, Any
from urllib.parse import urlparse
from bs4 import BeautifulSoup

import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))



class Search_engine():
    def __init__(self):
        self._num_of_doc = 0
        self.savedData = defaultdict()
        self.jsonCount = 0
        self._total_unique = 0


    def read_file(self):
        with open("/Users/lizhang/Downloads/WEBPAGES_RAWt/bookkeeping.json") as files:
            data = json.load(files)
            self._total_unique = 0
            Informatics = 0
            Mondego = 0
            Irvine = 0
            artifical = 0
            computer = 0
            # write the savedData into a json file
            with open('/Users/lizhang/PycharmProjects/cs121project3_milestone1/savedDict.json', 'w') as saveJson:
                for rel_path,link in data.items():
                    with open("/Users/lizhang/Downloads/WEBPAGES_RAWt/" + rel_path, encoding="utf-8") as file:
                        readfile = file.read()
                        beautiful = BeautifulSoup(readfile, "html.parser")
                        bb = beautiful.body
                        for tag in beautiful.select("style, script"):
                            tag.decompose
                        words = beautiful.get_text(separator="/n").lower()
                        total = re.findall("[A-Za-z0-9]+",words)
                        for eachword in total:
                            if eachword not in stop_words:
                                self.jsonCount += 1
                                if eachword not in self.savedData.keys():
                                    newUrlDict = {rel_path:link}
                                    self.savedData[eachword] = newUrlDict
                                elif eachword in self.savedData.keys():
                                    newUrlDict[rel_path] = link
                                    self.savedData[eachword] = newUrlDict
                                #print(self.savedData)
                    # saved 100 urls to json
                    if self.jsonCount > 100:
                        json.dump(self.savedData, saveJson,indent=4)
                        sys.exit()













                    # if "informatics" in total and Informatics < 20:
                    #     print("Informatics: " + link)
                    #     Informatics += 1
                    # if "mondego" in total and Mondego < 20:
                    #     print("Mondego: " + link)
                    #     Mondego += 1
                    # if "irvine" in total and Irvine <  20:
                    #     print("Irvine: " + link)
                    #     Irvine += 1
                    # if "artificial" in total and "intelligence" in total and artifical < 20:
                    #     print("artificial intelligence: " + link)
                    #     artifical+=1
                    # if "computer" in total and "science" in total and computer < 20:
                    #     print("computer science: "+ link)
                    #     computer+=1
                    #
    #     output = open("Milestone1_result","w")
    #
    #     output.write("Number of docs:" + str(self._num_of_doc))
    #     output.write("Number of unique words"+str(self._total_unique))
    #     for key, value in sorted(self._unique_word.items()):
    #         output.write(key+": " +str(value) + "\n")
    #
    #
    #
    #
    # def get_doc_num(self):
    #     with open("/Users/lizhang/Downloads/WEBPAGES_RAWt/bookkeeping.json") as files:
    #         data = json.load(files)
    #         self._num_of_doc = 0
    #         for num,link in data.items():
    #             self._num_of_doc+=1
    #     return self._num_of_doc



if __name__ == "__main__":
    token = Search_engine()
    token.read_file()












