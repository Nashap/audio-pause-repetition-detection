# 🎧 Audio Pause & Repetition Detection

A Python-based system that analyzes speech audio to detect:

* ⏸️ Silent pauses in speech
* 🔁 Acoustic repetition patterns (stuttering)
* 🗣️ Word-level repetitions (e.g., "I I I")

This project combines signal processing and speech recognition to solve a real-world speech analysis problem.

---

## 🚀 Features

* Detects pause segments with timestamps
* Calculates total pause duration
* Identifies repeated acoustic patterns using MFCC
* Detects repeated words using speech recognition
* Clean and modular Python implementation

---

## 🔄 System Pipeline

```
Audio Input → Preprocessing → Feature Extraction  
→ Pause Detection + Repetition Detection → Output
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Sample Output

```
🎧 AUDIO ANALYSIS RESULTS

⏸️ Pause Segments:
[0.00s - 0.26s]
[0.58s - 0.96s]

⏱️ Total Pause Duration: 1.95s

🔁 Acoustic Repetitions:
Pattern: "Strong stutter pattern"
Count: 3

🗣️ Word-Level Repetitions:
Word: "i"
Count: 3
```

---

## 🧠 Approach

### 1. Audio Preprocessing

* Loaded using librosa
* Normalization and noise reduction applied

### 2. Pause Detection

* RMS energy thresholding used to detect silence

### 3. Acoustic Repetition Detection

* Audio split into segments
* MFCC features extracted
* Similar segments grouped as repetitions

### 4. Word-Level Repetition Detection

* SpeechRecognition API used
* Transcribed text analyzed for repeated words

---

## ⚠️ Challenges

* Handling noisy audio signals
* Choosing optimal thresholds
* Detecting repetition without full speech understanding
* Variability in speech patterns

---

## 🚀 Future Improvements

* Integrate Whisper for better accuracy
* Add waveform visualization
* Improve real-time detection

---

## 🛠️ Tech Stack

* Python
* Librosa
* NumPy
* SciPy
* SpeechRecognition

---

## 📁 Project Structure

```
audio-analysis/
│── main.py
│── utils.py
│── pause_detection.py
│── repetition_detection.py
│── speech_to_text.py
│── word_repetition.py
│── requirements.txt
│── README.md
│── samples/
```
sample.wav
[sample1.wav](https://github.com/user-attachments/files/26635719/sample1.wav)

---

## 💡 Notes

* Works best with `.wav` files
* Word detection requires internet
* Results depend on audio quality

---

## 👤 Author

**Nasha P**
