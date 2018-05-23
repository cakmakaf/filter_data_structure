
# coding: utf-8

# In[6]:


from functools import reduce
A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

filtre = list(filter(lambda x : x % 2 == 1,A))

print(reduce(lambda x,y : x * y,filtre))

