import gradio as gr
import time
import whisper

model = whisper.load_model("base.en")

def transcribe_whisper(audio, state=""):
    time.sleep(0.5)
    result = model.transcribe(audio)
    text = result["text"]
    state += text + " "
    return state, state

gr.Interface(
    fn=transcribe_whisper, 
    inputs=[
        gr.components.Audio(source="microphone", type="filepath", streaming=True),
        'state'
    ],
    outputs=[
        "textbox",
        "state"
    ],
    live=True).launch()