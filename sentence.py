# -*- coding: utf-8 -*-
import io
from konlpy.tag import Kkma
from konlpy.utils import pprint
from collections import Counter

kkma = Kkma()

class Sentence :
	def co_occurence(sentence1, sentence2) :
		p = sum((sentence1.bow & sentence2.bow).values())
		q = sum((sentence1.bow | sentence2.bow).values())
		return p / q if q else 0

	def __init__(self, text, index = 0) :
		self.index = index
		self.text = text
		self.nouns = kkma.nouns(self.text)
		self.bow = Counter(self.nouns)

	def __eq__(self, another) :
		return hasattr(another, 'index') and self.index == another.index

	def __hash__(self) :
		return self.index

	def get_sentences(text) :
		candidates = xplit('.','?','!','\n','.\n')(text.strip())
		sentence = []
		index = 0

		for candidate in candidates :
			candidate = candidate.strip()
			if len(candidate) :
				sentences.append(Sentence(candidate, index))
				index += 1
		return sentences

	def build_graph(sentences) :
		graph = networkx.Graph()
		graph.add_nodes_from(sentences)
		pairs = list(itertools.combinations(sentences,2))
		for eins, zwei in pairs :
			graph.add_edge(eins, zwei, weight=Sentence.co_occurence(eins, zwei))
		return graph

	r = io.open('dataset.txt',mode='r',encoding='utf-8')
	i = 50
	text = ""

	while i > 0 : 
		line = r.readline()
		if not line : break

		if not line.find("article") :
			line = line.replace("article:","")
			text = text + "."
	sentences = get_sentences(text)
	graph = build_graph(sentences)
	pagerank = networkx.pagerank(graph, weight='weight')
	reordered = sorted(pagerank, key = pagerank.get, reverse=True)
