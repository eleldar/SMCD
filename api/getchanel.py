from pydub import AudioSegment
sound = AudioSegment.from_wav("path2.wav")
sound = sound.set_channels(2)
sound.export("output_path2_2.wav", format="wav")
