import nltk
from nltk.tokenize import word_tokenize
import pymorphy2
import re

with open('lab1.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

text = lines.replace('\n', '. ')[:-1]
text = re.sub(r'[^\w\s]', '', text)

nltk.download('punkt')

text_token = word_tokenize(text)
ma = pymorphy2.MorphAnalyzer()

pos = []
gender = []
number = []
case = []
text_result = []
for i in text_token:
    got_pa = ma.parse(i)[0]
    text_result.append(got_pa.normal_form)
    pos.append(got_pa.tag.POS)
    gender.append(got_pa.tag.gender)
    number.append(got_pa.tag.number)
    case.append(got_pa.tag.case)

uses = ['NOUN', 'ADJF', 'ADJS']
for i in range(len(pos) - 1):
    if gender[i] == gender[i + 1] and number[i] == number[i + 1] and case[i] == case[i + 1] and (pos[i] in uses or pos[i + 1] in uses):
        print(text_result[i], text_result[i + 1])
