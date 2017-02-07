from bs4 import BeautifulSoup
import requests

def question_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://stackoverflow.com/questions?page= " + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for node in soup.find_all('a',{'class': 'question-hyperlink'}):
            href = "http://stackoverflow.com" + node.get('href')
            print(" PAGE " + str(page))

            #print(href)
            #print(node.string)
            get_single_data(href)
        page += 1
def get_single_data(link_url):
    source_code = requests.get(link_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for node in soup.find_all('a', {'class': 'question-hyperlink'}):
        print(node.string)
    for link in soup.find_all('a'):
        href = "http://stackoverflow.com" + node.get('href')

question_spider(3)