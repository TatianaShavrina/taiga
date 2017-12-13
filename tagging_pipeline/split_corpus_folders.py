
# coding: utf-8

# In[1]:


import os
import re
import unify


path = r'/home/tsha/Taiga/Fontanka/texts'
folders = [d[1] for d in list(os.walk(path))]
fl = []
print(folders[0])
for path, subdirs, files in os.walk(path):
    for name in files:
        if '.txt' in name:
            fl.append(os.path.join(path, name))
path = r'/home/tsha/Taiga/Fontanka/texts'
step = 500
path200 = r'/home/tsha/Taiga/Fontanka/texts200'
taggedpath = r'/home/tsha/Taiga/Fontanka/texts_tagged'
for fold in folders[0]:
    os.mkdir(os.path.join(taggedpath, fold))
steps = [i for i in range(len(fl)//step) ]
steps += [steps[-1]+1]
for i in steps:
    if i!=steps[-1]:
        filenames = fl[i*step:i*step + step]
    else:
        filenames = fl[i*step:i*step + len(fl)%step]
    text200 = []
    id200 = []
    for f in filenames:
        fpath = os.path.join(path, f)
        file = open(fpath, 'r', encoding='utf8')
        text200.append(unify.unify_sym(file.read()))
        id200.append(f)
        file.close()
    outfile = open(os.path.join(path200, str(i)+'.txt'), 'w', encoding='utf8')
    outfile.write("\n\n++++\n\n".join(text200))
    outfile.close()
    os.system('/home/tsha/udpipe/src/udpipe --tokenize /home/tsha/models/syntagrus-default.udpipe  --tokenizer="normalized_spaces" --tag --parse ' + os.path.join(path200, str(i)+'.txt') + ' --outfile=' +os.path.join(path200, str(i)+'.conll')) 
    outfile = open(os.path.join(path200, str(i)+'.conll'), 'r', encoding='utf8').read().split("""# text = ++++
1	++++	++++	SYM	_	_	0	root	_	_""")
    print(len(outfile))
    for j in range(len(outfile)):
        newdir = re.sub("/texts/", "/texts_tagged/", id200[j])
        print(newdir)
        taggedtext = open(newdir, 'w', encoding='utf8')
        taggedtext.write("# text = " + outfile[j].strip())
        taggedtext.close()






