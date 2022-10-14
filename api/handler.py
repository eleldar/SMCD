import os
from pathlib import Path
import filetype as ft
from tools.recognitions import recognize
from tools.punctuation import punctuate
from tools.classification import classificate
from pydub import AudioSegment


class Handler():
    def __init__(self):
        self.file_info = {} 

    def start(self, file):
        text = recognize(file)
        text = punctuate(text)
        result = classificate(text)
        return result

    def __call__(self, file):
        return self.start(file)


