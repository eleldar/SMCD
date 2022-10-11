from random import choice, sample
import os
import sys
from pathlib import Path
from pydub import AudioSegment
import filetype as ft
# from handler import Handler


class Manager():
    def __init__(self):
        self.curdir = Path(__file__).parent.resolve()
        self.dir_local_path = os.path.join(self.curdir, 'tempfiles')

    def get_file_prefix(self):
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 
        name_power = 8
        shuffled_alphabet = sample(alphabet, len(alphabet))
        return ''.join(choice(shuffled_alphabet) for _ in range(name_power))

    def start(self, file):
#        handler = Handler()
        prefix = self.get_file_prefix()
        mimes = {'audio/aac': 'aac', 'audio/midi': 'mid', 'audio/mpeg': 'mp3',
                 'audio/mp4': 'm4a', 'audio/ogg': 'ogg', 'audio/x-flac': 'flac',
                 'audio/x-wav': 'wav', 'audio/amr': 'amr', 'audio/x-aiff': 'aiff'}
        if type(file) == str and ft.guess(file):
            sound = AudioSegment.from_file(file).set_channels(1)
            file_head = os.path.basename(file)[:os.path.basename(file).rfind('.')]
            print(file_head)
            file = os.path.join(self.dir_local_path, f'{file_head}_{prefix}_converted.wav')
            sound.export(file, format="wav")
        else:
            file_path = os.path.join(self.dir_local_path, file.filename)
            file.save(file_path)
            if ft.guess(file_path): 
                sound = AudioSegment.from_file(file_path).set_channels(1)
                file_head = file_path[:file_path.rfind('.')]
                file = f'{file_head}_{prefix}_converted.wav'
                sound.export(file, format="wav")
#        try:
#            return handler(file)
#        except Exception as e:
#            return f'Error: {e}, file: {file}'
        try:
            return file
        except Exception as e:
            return f'Error: {e}, file: {file}'


    def __call__(self, file):
        return self.start(file)

if __name__ == '__main__':
    manager = Manager()
    print(manager('../datasets/Zvonok_v_policiyu_-_Nashli_narkotiki_vnutri_muzhchiny_v_obraze_bobra_(Gybka.com).mp3'))



