import math
import json
from bs4 import BeautifulSoup
import re



class Calculation():
    def __init__(self):
        self._tf = 0
        self._urlNum = 0


    def count_tf(self, file, userinput):
        with open("/Users/lizhang/Downloads/WEBPAGES_RAWt/" + file, encoding="utf-8") as file:
            readfile = file.read()
            beautiful = BeautifulSoup(readfile, "html.parser")
            bb = beautiful.body
            for tag in beautiful.select("style, script"):
                tag.decompose
            words = beautiful.get_text(separator="/n").lower()
            total = re.findall("[A-Za-z0-9]+", words)
            for word in total:
                if word == userinput:
                    self._tf += 1


    #def calculate_tfidf():


    def run(self):
        #with open("/Users/lizhang/PycharmProjects/cs121project3_milestone1/savedDict.json") as savedUrl:
        with open("/Users/lizhang/PycharmProjects/cs121project3_milestone1/savedDict.json", 'r') as savedUrl:
           #print(type(savedUrl))
            data = json.load(savedUrl)
            userinput = input("Enter the keyword you want to search: ")
            print(data[userinput])
            for file, url in data[userinput].items():
                self._urlNum += 1
            for file, url in data[userinput].items():
                # count tf
                self.count_tf(file, userinput)
                print("urlnum:"+str(self._urlNum))
                print("tf:"+str(self._tf))
                tfidf = self._tf*math.log(37497/self._urlNum)

                print("tfidf: "+str(tfidf) + "/n" +"URL: " +"url")






if __name__ == "__main__":
    token = Calculation()
    token.run()



