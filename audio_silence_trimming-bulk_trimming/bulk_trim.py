# import the Libraries
from scipy.io.wavfile import read, write
import numpy as np
import wave
import time
from pydub.playback import play
from pydub import AudioSegment

import glob
import os

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=1):
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

def trim_audio(file_name):
    sound = AudioSegment.from_file(file_name, format="wav")

    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())

    duration = len(sound)    
    trimmed_sound = sound[start_trim:duration-end_trim]
    return trimmed_sound


wav_dir_name = '/nlp_server/TVS/audios_april/Hin/'
output_dir = '/nlp_server/TVS/audios_april/Hin/trimmed/'

wav_pattern = os.path.join(wav_dir_name, '*.wav')
file_list = glob.glob(wav_pattern)
for file in file_list:
    print("Trimming : ",file)
    trimmed_sound = trim_audio(file)
    output_file_name  = file.split("/")[-1]
    output_file_name = output_file_name.lower()
    trimmed_sound.export(output_dir +output_file_name , format="wav")