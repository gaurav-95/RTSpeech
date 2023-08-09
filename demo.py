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
        
    st.title("Audio to Text Converter")

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
