import os
from pathlib import Path
import filetype as ft
from recognitions import recognize
from pydub import AudioSegment


class Handler():
    def __init__(self):
        self.file_info = {} 

    def start(self, file):
        self.file_info['text'] = recognize(file)

    def __call__(self, file)
        return 


