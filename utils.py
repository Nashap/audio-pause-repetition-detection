import librosa
import numpy as np

def load_audio(file_path):
    try:
        y, sr = librosa.load(file_path, sr=16000)
        y = y / max(abs(y))  # normalize
        return y, sr
    except Exception as e:
        print("Error loading audio:", e)
        return None, None

def remove_noise(y, threshold=0.01):
    return np.where(abs(y) < threshold, 0, y)