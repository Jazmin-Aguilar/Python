#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


# In[ ]:


def capCount():
    x = sys.argv[1]
    total = 0
    for letter in x:
        if(letter.isupper()):
            total = total + 1
    print(total)
    print(sum([ i for i, c in enumerate(x) if c.isupper()]))
capCount()

