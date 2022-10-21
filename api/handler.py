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
        self.info = {}

    def start(self, file):

        st = time()
        text = recognize(file)
        rc = time()

        self.info['recognition_time'] = rc - st

        class_text = classificate(text)
        cl = time()

        self.info['classification_time'] = cl - rc

        repun_text = punctuate(text)
        rp = time()

        self.info['punctuation_time'] = rp - cl

        result = {
            'class': class_text,
            'text': repun_text,
        }
        result.update(self.info)
        return result

    def __call__(self, file):
        return self.start(file)


