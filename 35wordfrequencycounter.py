from bs4 import BeautifulSoup
import requests
import operator

def frequency(url):
    word_count = []
    urldata = requests.get(url).text
    soup = BeautifulSoup(urldata,"html.parser")
    for node in soup.find_all('a',{'class' :'question-hyperlink'}):
        rawdata = node.string
        words = rawdata.lower().split()
        for each_word in words:
            print(each_word)
            word_count.append(each_word)
    cleanword(word_count)

def cleanword(word_count):
    clead_word_list = []
    for word in word_count:
        symbols = "!@#$%^&*()-_+=|\\}{[]:;<,>.?/'\""
        for i in range(0 ,len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word)>0:
            #print(word)
            clead_word_list.append(word)
    create_dictonary(clead_word_list)

def create_dictonary(clead_word_list):
    word_counter = {}
    for word in clead_word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    for key,value in sorted(word_counter.items(),key = operator.itemgetter(1)):
            print(key,value)


frequency(' INSERT url HERE')