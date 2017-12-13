# coding: utf-8

# In[1]:


import os
import re
import unify




path = r'/home/tsha/Taiga/social/vk/texts/vktexts.txt'
path200 = r'/home/tsha/Taiga/social/vk/text200.txt'
taggedpath = r'/home/tsha/Taiga/social/vk/texts_tagged/vktexts.conll'


file = open(path, 'r', encoding='utf8')
text200 = unify.unify_sym(file.read())
file200 = open(path200, 'w', encoding='utf8')
file200.write(text200)
file.close()
file200.close()

os.system('/home/tsha/udpipe/src/udpipe --tokenize /home/tsha/models/syntagrus-default.udpipe  --tokenizer="normalized_spaces" ' + path200 + ' --outfile=' +taggedpath) 
    

