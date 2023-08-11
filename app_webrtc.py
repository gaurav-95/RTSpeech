# TO DO: https://github.com/stefanrmmr/streamlit_audio_recorder

import streamlit as st
import json
import pydub
import queue
import time
from streamlit_webrtc import RTCConfiguration, WebRtcMode, webrtc_streamer
from vosk import Model, KaldiRecognizer

RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

# Set page title and logo
st.set_page_config(
    page_title="RTSR",
    page_icon="💬",
)

def main():
    st.title("Real-Time Speech Recognition App")

    # Initialize Vosk recognizer
    model = Model(lang="en-us")
    recognizer = KaldiRecognizer(model, 48000)
    
    st.info("Press START to setup webrtc, give mic permission if asked for it. Takes a minute or two to setup webRTC.")
    
    # WebRTC configuration using Google STUN servers
    webrtc_ctx = webrtc_streamer(key='speech-to-text',
        mode=WebRtcMode.SENDONLY,
        rtc_configuration = RTC_CONFIGURATION,
        media_stream_constraints={"video": False, "audio": True}) # audio_receiver_size=1024,

    status_indicator = st.empty()
    stop_button = st.button("Stop Recognition")  # Create a stop button
    
    if not webrtc_ctx.state.playing:
        return
    
    status_indicator.write("Loading...")
    # text_output = st.empty()
    
    # Create a button to start speech recognition
    # Speech recognition loop
    while not stop_button:
        if webrtc_ctx.audio_receiver:   
            sound_chunk = pydub.AudioSegment.empty()
            try:
                audio_frames = webrtc_ctx.audio_receiver.get_frames(timeout=1)
            except queue.Empty:
                time.sleep(0.2)
                status_indicator.write("No frame arrived.")
                continue

            status_indicator.write("Running. Say something!")

            for audio_frame in audio_frames:
                sound = pydub.AudioSegment(
                    data=audio_frame.to_ndarray().tobytes(),
                    sample_width=audio_frame.format.bytes,
                    frame_rate=audio_frame.sample_rate,
                    channels=len(audio_frame.layout.channels),
                )
                sound_chunk += sound
                
            if len(sound_chunk) > 0:
                sound_chunk = sound_chunk.set_channels(1).set_frame_rate(
                    48000
                )
                
                buffer_bytes = sound_chunk.raw_data # Convert audiosegment file to bytes
                
                # Recognition starts here
                recognizer.AcceptWaveform(buffer_bytes)
                result = recognizer.Result()  # returns a string dictionary
                result = json.loads(result)  # parse the string dict as dict
                text = result['text']
                
                if text != '':
                    st.write(text)
                    # text_output.markdown(f"**Text:** {result}")
        else:
            status_indicator.write("AudioReciever is not set. Abort.")
            break

if __name__ == "__main__":
    main()
