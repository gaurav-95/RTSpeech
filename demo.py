import streamlit as st
import pyaudio
import json

from vosk import Model, KaldiRecognizer

def main():
    st.title("Real-Time Speech Recognition App")

    # Create a button to start speech recognition
    if st.button("Start Recognition"):
        st.text("Listening...")

        # Initialize Vosk recognizer
        model = Model(lang="en-us")
        recognizer = KaldiRecognizer(model, 16000)

        # Initialize PyAudio
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

        # Speech recognition loop
        while True:
            data = stream.read(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result() # returns a string dictionary
                result = json.loads(result) # parse the string dict as dict
                
                st.text(result['text'])
   
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
