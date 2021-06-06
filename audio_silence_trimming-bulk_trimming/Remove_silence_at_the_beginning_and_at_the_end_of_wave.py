#!/usr/bin/env python
# coding: utf-8

# In[4]:


import warnings
warnings.filterwarnings('ignore')


# In[5]:


# import the Libraries
from scipy.io.wavfile import read, write
import numpy as np
import wave
import time
from pydub.playback import play
from pydub import AudioSegment
import warnings
warnings.filterwarnings('ignore')


# In[6]:


from pydub import AudioSegment

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=1):
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


# In[7]:


sound = AudioSegment.from_file("C:\\Users\\amit amar\\Desktop\\Gnani.ai\\New Project AV\\BAJAJ_initial_message.wav", format="wav")

start_trim = detect_leading_silence(sound)
end_trim = detect_leading_silence(sound.reverse())

duration = len(sound)    
trimmed_sound = sound[start_trim:duration-end_trim]


# In[8]:


trimmed_sound.export("new.wav", format="wav")


# In[9]:


obj = wave.open('new.wav','r')


# In[10]:


a = read("new.wav")


# In[11]:


a


# In[ ]:




