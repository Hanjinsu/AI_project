# -*- coding: utf-8 -*-
import io
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

r = io.open('dataset.txt',mode='r',encoding='utf-8')
f = io.open('output.txt',mode='wt',encoding='utf-8')
while 1 :
	line = r.readline()
	if not line : break

	line = line.replace("course","#\ncourse")
	if not line.find("article") or not line.find(":") :
		line = line.replace("article:","")
		arr = kkma.morphs(line)
		art = ",".join(arr)
		art = "article :" + art;
		f.write(art+"\n")
	else : f.write(line)

r.close()	 
f.close()
