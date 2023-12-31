# RealTime Speech Recognition

Streamlit and Gradio app that uses 'vosk' and 'whisper' libraries respectively to perform real time speech recognition.

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

3. Run app using Gradio or Streamlit!

To use the better Gradio version that uses whisper recognizer run with: 
```bash
python gr_app.py
```
(You need to press stop recording in order to view the results in the gradio version of the app.)

For Streamlit version that uses vosk recognizer:
```bash
python -m streamlit run app.py
```

## References:
- https://github.com/alphacep/vosk-api/tree/master/python
- https://github.com/openai/whisper