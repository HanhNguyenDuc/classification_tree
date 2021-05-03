from .base_node import *
from .F0_node import F0Node
import numpy as np

class ZCRNode(BaseNode):
    def __init__(self, current_audio):
        super().__init__(current_audio)
        self.F0_child_node = F0Node(current_audio)
    

    def preprocessing(self):
        return self.current_audio

    def update_audio(self, current_audio):
        self.current_audio = current_audio
        return self.preprocessing()
    

    def process(self, current_audio):
        preprocessed_audio = self.update_audio(current_audio)

        average_zcr = np.average(librosa.feature.zero_crossing_rate(self.current_audio))

        if average_zcr < 0.03:
            return AudioLabel.SOLO
        if average_zcr < 0.05:
            return AudioLabel.DUET
        if average_zcr < 0.1:
            return AudioLabel.HARMONY

        return self.F0_childe_node.process(current_audio)
        