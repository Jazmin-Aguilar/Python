#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


# In[ ]:


def digits():
    import string
    a_string = sys.argv[1]
    new_string = a_string.translate(str.maketrans('', '', string.punctuation))

    print(len(new_string))  
digits()


# In[ ]:




