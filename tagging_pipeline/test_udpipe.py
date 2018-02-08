# coding: utf-8

from numpy import median

from nltk import word_tokenize, sent_tokenize
import os
import re
import unify
from tqdm import tqdm
import ufal.udpipe
global model

def ensure_dir(directory):
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def tag(text, model):
    tokenizer.setText(text)
    tokenizer.nextSentence(sentence, error)
    model.tag(sentence, model.DEFAULT)
    model.parse(sentence, model.DEFAULT)
    return conlluOutput.writeSentence(sentence)

model = ufal.udpipe.Model.load('/home/tsha/models/syntagrus-default.udpipe')

tokenizer = model.newTokenizer(model.DEFAULT)
conlluOutput = ufal.udpipe.OutputFormat.newOutputFormat("conllu")
sentence = ufal.udpipe.Sentence()
error = ufal.udpipe.ProcessingError()


WDIR = r'/home/tsha/Taiga' 
wallpath = os.path.join(WDIR, 'texts')
taggedpath = ensure_dir(os.path.join(WDIR, 'tagged_texts'))


for path, subdirs, files in tqdm(os.walk(wallpath)):
    for name in files:
        file = os.path.join(path, name)
        
        if ".txt" in file:
            print(file)
            f = open( file, 'r', encoding='utf8').read()
            newpath = ensure_dir(re.sub('texts', 'tagged_texts', path))
            print(os.path.join(newpath, name))
            out = open(os.path.join(newpath, name), 'w', encoding='utf8')
            text = unify.unify_sym(f)
            slist = sent_tokenize(text)
            for s in slist:
                s = tag(s, model)
                out.write(s)
            out.close()

