import os
import threading
from pathlib import Path
import filetype as ft
import moviepy.editor as mp
from recognitions import recognize, read_data
from tools.postprocess import target_format, get_dicts_list
from time import time
from datetime import timedelta
from pydub import AudioSegment
import soundfile as sf


# cirrent paths for different OS
drive, path_and_file = os.path.splitdrive(Path(__file__).absolute())
path, file = os.path.split(path_and_file)
curdir = os.path.join(drive, path)

mimes = {
    'audio/aac': 'aac',
    'audio/midi': 'mid', 
    'audio/mpeg': 'mp3', 
    'audio/mp4': 'm4a', 
    'audio/ogg': 'ogg', 
    'audio/x-flac': 'flac', 
    'audio/x-wav': 'wav', 
    'audio/amr': 'amr', 
    'audio/x-aiff': 'aiff' 
}

class Handler():
    def __init__(self, data_file=None):
        self.file_info = {'data_file': data_file} 
        self.times = {
           'time': None,
        }

    def start(self, file, sem, pool):
        with sem:
            th_name = threading.current_thread().name
            print(f'Wait {th_name}')
            pool.makeActive(th_name)
            start = time()
            self.file_info['filetype'] = ft.guess(file).mime if ft.guess(file) else None       


            # need refactoring
            sound = AudioSegment.from_file(file)
            sound = sound.set_channels(1)
            
            inx = file.rfind('.')
            tmp = file[:inx]
            file = f"{''.join(tmp)}.wav"
            try:
                sound.export(file, format="wav") # wave.Error: file does not start with RIFF id
            except:
                pass 

            # ****************

            self.file_info['data_file'] = recognize(file)
            self.times['time'] = str(timedelta(seconds = time() - start))
            print(
                'Time recognition for', 
                 os.path.basename(self.file_info['data_file']).split('.')[0], 
                'is', self.times['time']
            )
            pool.makeInactive(th_name)


    def get_result(self):
        '''baseline'''
        data_file = self.file_info['data_file']
        return target_format(read_data(data_file))


