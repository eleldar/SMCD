from random import choice, sample
import os
import sys
from pathlib import Path
from handler import Handler
from abc import abstractmethod, ABC
import time
import platform


from pydub import AudioSegment
if platform.system() == 'Windows':
    # https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
    curdir = Path(__file__).parent.resolve()
    ffmpeg_path = os.path.join(os.path.dirname(curdir), 'win_venv', 'Lib', 'ffmpeg', 'bin')
    AudioSegment.converter = os.path.join(ffmpeg_path, 'ffmpeg.exe')
    AudioSegment.ffmpeg = os.path.join(ffmpeg_path, 'ffmpeg.exe')
    AudioSegment.ffprobe = os.path.join(ffmpeg_path, 'ffprobe.exe')

class Interface(ABC):
    @abstractmethod
    def __call__(
            self,
            input: str
    ) -> str:
        raise NotImplementedError

class Manager(Interface):
    def __init__(self):
        self.curdir = Path(__file__).parent.resolve()
        self.dir_local_path = os.path.join(os.path.dirname(self.curdir), 'input_data')
        self.info = {}


    def get_file_prefix(self):
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 
        name_power = 8
        shuffled_alphabet = sample(alphabet, len(alphabet))
        return ''.join(choice(shuffled_alphabet) for _ in range(name_power))

    def start(self, file):
        handler = Handler()
        prefix = self.get_file_prefix()

        if type(file) == str: # and ft.guess(file):
            sound = AudioSegment.from_file(file).set_channels(1)
            file_head = Path(file).stem
            file = os.path.join(self.dir_local_path, f'{file_head}_{prefix}_converted.wav')
            sound.export(file, format="wav")
        else:
            file_path = os.path.join(self.dir_local_path, file.filename)
            start_save_file = time.time()
            file.save(file_path)
            end_save_file = time.time()
            self.info['save_file_time'] = end_save_file - start_save_file

            try:
                start_conv_file = time.time()
                sound = AudioSegment.from_file(file_path).set_channels(1)
                file_head = Path(file_path).stem
                file = os.path.join(self.dir_local_path, f'{file_head}_{prefix}_converted.wav')
                sound.export(file, format="wav")
                end_conv_file = time.time()
                self.info['save_convert_time'] = end_conv_file - start_conv_file
            except Exception as e:
                print(e)
        self.info.update(handler(file))
        return self.info


    def __call__(self, file):
        try:
            result = self.start(file)
            return result
        except Exception as e:
            return f'Error: {e}'


