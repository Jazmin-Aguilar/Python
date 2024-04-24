#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


# In[ ]:


def countvowels():
    letters = sys.argv[1].lower()
    count = 0
    for vowel in 'aeiou':
        if vowel in letters:
            count += 1
    print(count)
countvowels()

