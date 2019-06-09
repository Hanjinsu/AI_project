import io

summa = io.open("threeinput.txt",mode='r',encoding='utf-8')
dataset = io.open("dataset.txt",mode='r',encoding='utf-8')
articles = io.open("article.txt",mode='w',encoding='utf-8')
seqinput = io.open("seqinput.txt",mode='w',encoding='utf-8')

temp = ""
while True:
	sline = summa.readline()
	course = ""
	prf = ""
	art = ""
	if "#" in sline:
		for i in range(7) :
			sline = summa.readline()
			if "course:" in sline : 
				course = sline.replace("course: ","")
				course = course.replace("\n",",")
				seqinput.write(course)
			if "professor:" in sline : 
				prf = sline.replace("professor: ","")
				prf = prf.replace("\n",",")
				seqinput.write(prf)
			if "article:" in sline : 
				art = sline.replace("article: ","")
				art = art.replace("\n",",")
				seqinput.write(art)
	art=""
	while True: 
		dline = dataset.readline()
		if "article: " in dline : 
			dline = dline.replace(","," ")
			dline = dline.replace("\n"," ")
			art = art + dline.replace("article: ","")
		if "course:" in dline:
			if len(art) > 0:
				seqinput.write(art +'\n')
				break;
