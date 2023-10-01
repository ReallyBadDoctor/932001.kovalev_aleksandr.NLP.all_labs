from rnnmorph.predictor import RNNMorphPredictor
import nltk
from nltk.tokenize import word_tokenize
import re

with open('lab3.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

text = lines.replace('\n', '. ')[:-1]
text = re.sub(r'[^\w\s]', '', text)

nltk.download('punkt')

text_token = word_tokenize(text)
predictor = RNNMorphPredictor(language='ru')
text_results = predictor.predict(text_token)

# извините за этот мрак, но нормальной документации я нашел
uses = ['NOUN', 'ADJ']
d = []
for i in range(len(text_results) - 1):
    try:
        y = text_results[i].tag
        d.append(dict(x.split("=") for x in y.split("|")))
    except:
        d.append({'Очень плохо сделано': "внатуре"})

for i in range(len(text_results) - 1):
    try:
        if (text_results[i].pos in uses or text_results[i + 1].pos in uses) \
        and d[i]['Case'] == d[i+1]['Case'] and d[i]['Number'] == d[i+1]['Number'] and d[i]['Gender'] == d[i+1]['Gender']:
            print(text_results[i].normal_form, text_results[i + 1].normal_form)
    except:
        continue
