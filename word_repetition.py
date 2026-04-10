def detect_word_repetition(text):
    words = text.split()
    
    repetitions = []
    count = 1
    prev = None

    for word in words:
        if word == prev:
            count += 1
        else:
            if count > 1:
                repetitions.append({
                    "word": prev,
                    "count": count
                })
            count = 1
        prev = word

    if count > 1:
        repetitions.append({
            "word": prev,
            "count": count
        })

    return repetitions