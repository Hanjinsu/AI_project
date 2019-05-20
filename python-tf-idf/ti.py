from tfidf import TfIdf
import io
import re

def find_sim(doc_name):
    doc_name=doc_name.split(' ')
#    print(doc_name)
#    numart = doc_name[1]
#    numppl = doc_name[4]

    simil=1.0-abs(int(doc_name[7][0])-3.96)
    return simil

r= io.open('parsing.txt',mode='r', encoding='utf-8')

title =r.readline()
print(title)

tag = ['NNG','MAG','W','VA','NNP']

line=r.readline()
line=r.readline()
cntart=0
doc_name=""

table= TfIdf()

while True:
    if "<article" in line:
        name=line
      #  print(name)
    if "FINISH" in line:
        break
    list_of_words=[]
    while True:
        line=r.readline()
        if "#" in line:
            doc_name=name[:-1]+line[1:-1]
            line=r.readline()
        elif line=="\n":
        #    print(doc_name)
        #    print(list_of_words)
            simil = find_sim(doc_name)
            table.add_document(doc_name,list_of_words,simil)
            list_of_words=[]
        elif "<article" in line:
            break
        elif "FINISH" in line:
            break
        else:
            line=line.replace('\t',' ').split()
            for words in line:
                if any(t in words for t in tag):
                    tmp=words.split('/')
                    list_of_words.append(tmp[0])


sim=table.similarities(["수업", "학점", "출첵"])
for m in sim:
    print(m)
