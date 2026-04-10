import librosa
import numpy as np

def detect_repetitions(y, sr):
    segment_duration = 0.3
    hop_duration = 0.15

    segment_samples = int(segment_duration * sr)
    hop_samples = int(hop_duration * sr)

    features = []
    times = []

    # Extract MFCC features + timestamps
    for i in range(0, len(y) - segment_samples, hop_samples):
        segment = y[i:i + segment_samples]
        mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=13)

        features.append(np.mean(mfcc, axis=1))
        times.append(i / sr)

    # ----------------------------
    # 🔥 Adaptive threshold
    # ----------------------------
    distances = []
    for i in range(len(features) - 1):
        d = np.linalg.norm(features[i] - features[i+1])
        distances.append(d)

    if len(distances) == 0:
        return []

    avg_distance = np.mean(distances)
    threshold = avg_distance * 0.6   # adaptive

    results = []
    visited = set()

    for i in range(len(features)):
        if i in visited:
            continue

        group = [i]

        for j in range(i+1, len(features)):
            similarity = np.linalg.norm(features[i] - features[j])

            if similarity < threshold:
                group.append(j)
                visited.add(j)

        # Only consider meaningful repetitions
        if len(group) > 2:
            start_time = times[group[0]]
            end_time = times[group[-1]] + segment_duration
            count = len(group) - 1

            # Confidence (dynamic)
            if count >= 4:
                confidence = "High"
            elif count >= 2:
                confidence = "Medium"
            else:
                confidence = "Low"

            # Pattern naming (dynamic)
            if count >= 3:
                pattern = "Strong stutter pattern"
            else:
                pattern = "Mild repetition"

            results.append({
                "pattern": pattern,
                "start": start_time,
                "end": end_time,
                "count": count,
                "confidence": confidence
            })

    return results