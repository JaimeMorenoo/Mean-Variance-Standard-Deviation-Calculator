#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[113]:


def calculate(array):
    if len(array) != 9:
        raise ValueError( "List must contain nine numbers.")
    else:
        
        np_array = np.reshape(array,(3,3))
        dictionary = {'mean': [np.mean(np_array, axis=0).tolist(), np.mean(np_array, axis=1).tolist(), np.mean(np.mean(np_array, axis=0).tolist())] ,
                      'variance' : [np.var(np_array, axis=0).tolist(),np.var(np_array, axis=1).tolist(),np.var(np_array).tolist()],
                      'standard deviation' : [np.std(np_array,axis=0).tolist(),np.std(np_array,axis=1).tolist(),np.std(np_array).tolist()],
                      'max' : [np.max(np_array,axis=0).tolist(),np.max(np_array,axis=1).tolist(),np.max(np_array).tolist()],
                      'min' : [np.min(np_array,axis=0).tolist(),np.min(np_array,axis=1).tolist(),np.min(np_array).tolist()],
                      'sum' : [np.sum(np_array,axis=0).tolist(),np.sum(np_array,axis=1).tolist(),np.sum(np_array).tolist()]
                     }
        for k, v in dictionary.items():
            print(k, v)


# In[ ]:




