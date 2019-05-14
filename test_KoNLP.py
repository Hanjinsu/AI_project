#! -*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
pprint(kkma.nouns(u'나는 사과를 먹었다'))
