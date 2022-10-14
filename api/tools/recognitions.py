#!/usr/bin/env python3
import os
from vosk import Model, KaldiRecognizer, SetLogLevel
from pathlib import Path
import wave
import json


curdir = Path(__file__).parent.resolve()
models_path = os.path.join(curdir, 'models')
SetLogLevel(-1) # keep init message
models = {
    'ru': Model(os.path.join(models_path, 'ru')),
}

def get_words(dct_lst):
    text = dct_lst.get('text') 
    return text if text else ''

    
def recognize(file_path, language='ru'):
    '''giperparameters, recognize, save, read and split text file'''
    wf = wave.open(file_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)
    model = models[language]
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    result = []
    while True:
        frame = wf.readframes(4000)
        if len(frame) == 0:
            break
        if rec.AcceptWaveform(frame):
            output = json.loads(rec.Result())
            result.append(get_words(output))
    output = json.loads(rec.FinalResult())
    result.append(get_words(output))
    return " ".join(result) 
