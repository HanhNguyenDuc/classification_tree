from node import *

def classify():
    # Load file
    y, sr = librosa.load('../irmas_dataset/don_tau/' + "[cla][cla]0150__1.wav")
    # Process file
    root_node = ZCRNode(y)
    label = root_node.process(y)

    print(label)
    

if __name__ == '__main__':
    classify()