import os
from pathlib import Path
import filetype as ft
from tools.recognitions import recognize
from tools.punctuation import punctuate
from tools.classification import classificate
from pydub import AudioSegment
from time import time

class Handler():
    def __init__(self):
        self.file_info = {} 

    def start(self, file):

        st = time()

        text = recognize(file)
        rc = time()
        print('rec:', rc - st)

        class_text = classificate(text)
        cl = time()
        print('class:', cl - rc)

        repun_text = punctuate(text)
        rp = time()
        print('rep:', rp - cl)

        return {
            'class': class_text,
            'text': repun_text 
        }

    def __call__(self, file):
        return self.start(file)


