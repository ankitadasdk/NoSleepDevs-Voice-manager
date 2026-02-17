import whisper
import os

def process_voice_command():
    if not os.path.exists("command.wav"):
        print("Error: I don't see command.wav. Record")
        return "" 
    print("AI is thinking... (Loading Whisper)")
    model = whisper.load_model("base")
    print("Transcribing your audio")
    result = model.transcribe("command.wav") 
    text_heard = result['text'].strip()
    print(f"\n  System heard: '{text_heard}' \n")
    return text_heard.lower() 
if __name__ == "__main__":
    process_voice_command()