from random import choice, sample
import os
import sys
from pathlib import Path
from pydub import AudioSegment
import filetype as ft
from handler import Handler
from abc import abstractmethod, ABC



from typing import Union, List, Dict


class Transform(ABC):
    def __init__(
            self,
            postprocessing_used: bool = False
    ):
        self.postprocessing_used = postprocessing_used

    @abstractmethod
    def __call__(
            self,
            input: str
    ) -> str:
        raise NotImplementedError

class Manager(Transform):
    def __init__(self):
        self.curdir = Path(__file__).parent.resolve()
        self.dir_local_path = os.path.join(self.curdir, 'tempfiles')

    def get_file_prefix(self):
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 
        name_power = 8
        shuffled_alphabet = sample(alphabet, len(alphabet))
        return ''.join(choice(shuffled_alphabet) for _ in range(name_power))

    def start(self, file):
        handler = Handler()
        prefix = self.get_file_prefix()
        mimes = {'audio/aac': 'aac', 'audio/midi': 'mid', 'audio/mpeg': 'mp3',
                 'audio/mp4': 'm4a', 'audio/ogg': 'ogg', 'audio/x-flac': 'flac',
                 'audio/x-wav': 'wav', 'audio/amr': 'amr', 'audio/x-aiff': 'aiff'}
        if type(file) == str: # and ft.guess(file):
            sound = AudioSegment.from_file(file).set_channels(1)
            file_head = os.path.basename(file)[:os.path.basename(file).rfind('.')]
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
        return handler(file)


    def __call__(self, file):
        return self.start(file)

if __name__ == '__main__':
    manager = Manager()
    # file = '../datasets/Zvonok_v_policiyu_-_Miner_(Gybka.com).mp3'
    files = [
        '46747567547.mp3',
        'Zvonok_v_policiyu_-_Miner_(Gybka.com).mp3',
        'Zvonok_v_policiyu_-_Nashli_narkotiki_vnutri_muzhchiny_v_obraze_bobra_(Gybka.com).mp3',
        'zvonok-deda-po-02-moyu-babushku-napominaet-ya-tebe-na-verevke-udavlyu....-ddd_(mp3IQ.net).mp3'
    ]
#    for file in files[1]:
#        result = manager(f'../datasets/{file}')
#        print(result)
#

    result = manager(f'../datasets/{files[1]}')
    print(result)

