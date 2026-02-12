import speech_recognition as sr

def record_voice():
    recognizer = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening, speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            with open("command.wav", "wb") as f:
                f.write(audio.get_wav_data())
            print("Successfully recorded to command.wav")   
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    record_voice()
    