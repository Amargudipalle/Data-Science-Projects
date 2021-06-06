#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path


# In[2]:


import spacy


# In[4]:


output_dir=Path('hindi_model/')


# In[5]:


nlp=spacy.load(output_dir) 


# In[6]:


nlp.to_disk(output_dir)


# In[7]:


# Load the saved model and predict
print("Loading from", output_dir)
nlp_updated = spacy.load(output_dir)
doc = nlp_updated("मैं बैंगलोर जा रहा हूं" )
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




