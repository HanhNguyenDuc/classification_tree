from .base_node import *

class F0Node(BaseNode):
    def __init__(self, current_audio):
        super().__init__(current_audio)


    def preprocessing(self):
        return self.current_audio

    def update_audio(self, current_audio):
        self.current_audio = current_audio
        return self.preprocessing()
    
    def process(self, current_audio):
        preprocessed_audio = self.update_audio(current_audio)

        return AudioLabel.SOLO