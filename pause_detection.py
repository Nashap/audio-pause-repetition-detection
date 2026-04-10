import librosa

def detect_pauses(y, sr, threshold=0.02):
    rms = librosa.feature.rms(y=y)[0]
    times = librosa.frames_to_time(range(len(rms)), sr=sr)

    pauses = []
    start = None

    for i, energy in enumerate(rms):
        if energy < threshold:
            if start is None:
                start = times[i]
        else:
            if start is not None:
                end = times[i]
                pauses.append((start, end))
                start = None

    # Handle last pause
    if start is not None:
        pauses.append((start, times[-1]))

    total_pause = sum(end - start for start, end in pauses)

    return pauses, total_pause