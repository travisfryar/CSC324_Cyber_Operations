######################################
# Author: Travis Fryar
# Subject: CSC 324 - Named Entity Recognition
# Date: 10/8/2020
######################################

import nltk
from nltk.tag.stanford import StanfordNERTagger

PATH_TO_JAR='/media/sf_CSC324/stanford-ner-4.0.0/stanford-ner.jar'
PATH_TO_MODEL = '/media/sf_CSC324/stanford-ner-4.0.0/classifiers/english.conll.4class.distsim.crf.ser.gz'

tagger = StanfordNERTagger(model_filename=PATH_TO_MODEL,path_to_jar=PATH_TO_JAR, encoding='utf-8')
sentence='The mission marked the first time a satellite launched into a \
polar-orbiting trajectory from Florida since the 1960s. Typically, this type \
of mission launches from the West Coast because the rocket would have a clear \
path north or south, without having to avoid flying over populated areas.'
words=nltk.word_tokenize(sentence)
tagged = tagger.tag(words)

for word in tagged:
        print(word)

