# RealTime Speech Recognition

Streamlit app that uses vosk library to perform real time speech recognition.
Recognition can be a bit off is audio spoken is not clear enough but works great most of the time with clear audio.

<p align="center">
    <img src="https://github.com/gaurav-95/RTSpeech/blob/be34fedf3cdfb254bda78cd65f975bb1faa69439/demo/RTS-Demo.gif"/>
</p>

## Installation

1. Clone the repository:

```bash
git clone https://github.com/gaurav-95/RTSpeech.git

```

2. Install requirements from requirements.txt

```bash
pip install -r requirements.txt
```

3. Run using Streamlit!

```bash
python -m streamlit run app.py
```

To use better gradio version that uses whisper run with: 
```bash
python gr_app.py
```

## References:
- https://github.com/alphacep/vosk-api/tree/master/python
- https://github.com/openai/whisper