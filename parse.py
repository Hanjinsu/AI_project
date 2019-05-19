# -*- coding: utf-8 -*-
import io
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

r = io.open('dataset.txt',mode='r',encoding='utf-8')
f = io.open('output2.txt',mode='wt',encoding='utf-8')
while 1 :
	line = r.readline()
	if not line : break

	if not line.find("article"):
		line = line.replace("article:","")
		line = line + "."
		arr = kkma.morphs(line)
		art = ",".join(arr)
		art = "article :" + art;
		f.write(art+"\n")
	elif not line.find("course") :
		line = line.replace("course","#\ncourse");
		f.write(line)
	elif not line.find("professor") :
		f.write(line)
	elif not line.find("star") :
		f.write(line)
	elif not line.find("assignment") :
		f.write(line)
	elif not line.find("teamproject") :
		f.write(line)
	elif not line.find("percentage") :
		f.write(line)
	elif not line.find("attendance") :
		f.write(line)
	elif not line.find("testnum") :
		f.write(line)
	elif not line.find("semester") :
		f.write(line)
	elif not line.find("starnum") :
		f.write(line)
	elif not line.find("\n") : 
		f.write(line)
	else :
		line = line.replace("article:","")
		arr = kkma.morphs(line)
		art = ",".join(arr)
		f.write(art+"\n")

r.close()	 
f.close()
