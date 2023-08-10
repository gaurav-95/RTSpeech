# https://github.com/whitphx/streamlit-stt-app/blob/main/app_deepspeech.py
# https://stackoverflow.com/questions/75973228/speech-recognition-with-streamlit
# https://www.youtube.com/watch?v=2kSPbH4jWME
# https://realpython.com/python-speech-recognition/
# https://github.com/Uberi/speech_recognition#readme
# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/#:~:text=Translation%20of%20Speech%20to%20Text%3A,function%20may%20take%202%20arguments.&text=After%20initialization%2C%20we%20will%20make,may%20also%20take%202%20arguments.


import streamlit as st
import speech_recognition as sr

def main():
    st.title("Real-time Speech Recognition App")

    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio input from microphone
    with sr.Microphone() as source:
        st.write("Say something...")
        audio = recognizer.listen(source, timeout=None)

    try:
        st.write("Transcribing...")
        text = recognizer.recognize_google(audio, show_all=False)
        st.success("You said: " + text)
    except sr.UnknownValueError:
        st.error("Sorry, could not understand audio.")
    except sr.RequestError as e:
        st.error(f"Error connecting to Google Speech Recognition service: {e}")
        
    # st.title("Audio to Text Converter")

    # # Upload the audio file
    # audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])

    # if audio_file is not None:
    #     # Split the audio file into 5-minute chunks
    #     CHUNK_DURATION = 5 * 60 # 5 minutes
    #     r = sr.Recognizer()
    #     with sr.AudioFile(audio_file) as source:
    #         audio_duration = math.ceil(source.DURATION)
    #         num_chunks = math.ceil(audio_duration / CHUNK_DURATION)
    #         for i in range(num_chunks):
    #             chunk_start = i * CHUNK_DURATION
    #             chunk_end = min((i + 1) * CHUNK_DURATION, audio_duration)
    #             audio_text = r.record(source, offset=chunk_start, duration=chunk_end-chunk_start)
    #             text = r.recognize_google(audio_text)

    #             # Display the text for this chunk
    #             st.header(f"Text from Audio (Chunk {i+1}/{num_chunks})")
    #             st.write(text)

if __name__ == "__main__":
    main()
