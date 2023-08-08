from bs4 import BeautifulSoup
import requests

def search(inp):
    noun = []
    preposition = []
    verb = []
    adverb = []
    article = []
    
    sentence,sentence1,sentence2,sentence3,sentence4 = "","","","",""
    url = f'https://www.wordnik.com/words/{inp}'

    req = requests.get(url=url)
    soup = BeautifulSoup(req.text,'html.parser')
    
    A = soup.find('div',{'class':'word_page'})
    b = A.find_all('div',class_="guts active")
    c = b[0].find('ul')
    d = c.find_all('li')
    for a in d:
        if "noun" in a.text.split()[0]:
            split = a.text.split(" ")
            split.pop(0)
            for i in split:
                sentence += f" {i}"
            sentence.lstrip()
            noun.append(sentence.lstrip())
            sentence = ""
        if "intransitive" in a.text.split()[0]:
            split1 = a.text.split(" ")
            split1.pop(0)
            split1.pop(0)
            for i in split1:
                sentence1 += f" {i}"
            verb.append(sentence1.lstrip())
            sentence1 = ""
        if "preposition" in a.text.split()[0]:
            split2 = a.text.split(" ")
            split2.pop(0)
            for i in split2:
                sentence2 += f" {i}"
            preposition.append(sentence2.lstrip())
            sentence2 = ""
        if "adverb" in a.text.split()[0]:
            split3 = a.text.split(" ")
            split3.pop(0)
            for i in split3:
                sentence3 += f" {i}"
            adverb.append(sentence3.lstrip())
            sentence3 = ""
        if "definite" in a.text.split()[0]:
            split4 = a.text.split(" ")
            split4.pop(0)
            split4.pop(0)
            for i in split4:
                sentence4 += f" {i}"
            article.append(sentence4.lstrip())
            sentence4 = ""
        
    return noun,verb,preposition,adverb,article