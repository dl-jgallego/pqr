import re
import spacy
import nltk
nltk.download('stopwords')
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.collocations import *
nlp = spacy.load('es_core_news_md')

def text_normalization(text):
    stop_words = list(stopwords.words('spanish'))
    no_value_words = ['fecha', 'valor']
    for w in no_value_words:
        stop_words.append(w)
    text = str(text)
    text = text.lower()
    text = ' '.join(re.findall(r'[a-záéíóúñ]{2,}', text))
    text = word_tokenize(text)
    for w in stop_words:
        while w in text: text.remove(w)
    return ' '.join(list(dict.fromkeys(text)))

