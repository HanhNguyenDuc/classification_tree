import librosa
from enum import unique, Enum

@unique
class AudioLabel(Enum):
    SOLO = 1
    DUET = 2
    HARMONY = 3

class BaseNode:
    
    def __init__(self, current_audio):
        self.current_audio = current_audio

    def update_audio(self, current_audio):
        pass

    def preprocessing(self, current_audio):
        pass

    def process(self, current_audio):
        pass 