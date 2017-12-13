
# coding: utf-8

# In[1]:


import os
import re
import unify




path = r'/home/tsha/Taiga/Magazines/texts'
fl = os.listdir(path)
step = 500
path200 = r'/home/tsha/Taiga/Magazines/texts200'
taggedpath = r'/home/tsha/Taiga/Magazines/texts_tagged'
steps = [i for i in range(len(fl)//step) ]
steps += [steps[steps.index(max(steps))]+1]
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
        id200.append(f.strip('.txt'))
        file.close()
    outfile = open(os.path.join(path200, str(i)+'.txt'), 'w', encoding='utf8')
    outfile.write("\n\n++++\n\n".join(text200))
    outfile.close()
    os.system('/home/tsha/udpipe/src/udpipe --tokenize /home/tsha/models/syntagrus-default.udpipe  --tokenizer="normalized_spaces" --tag --parse ' + os.path.join(path200, str(i)+'.txt') + ' --outfile=' +os.path.join(path200, str(i)+'.conll')) 
    outfile = open(os.path.join(path200, str(i)+'.conll'), 'r', encoding='utf8').read().split("""# text = ++++
1	++++	++++	SYM	_	_	0	root	_	_""")
    print(len(outfile))
    for j in range(len(outfile)):
        newdir = os.path.join(taggedpath, id200[j] + '.txt')
        print(newdir)
        taggedtext = open(newdir, 'w', encoding='utf8')
        taggedtext.write("# text = " + outfile[j].strip())
        taggedtext.close()






