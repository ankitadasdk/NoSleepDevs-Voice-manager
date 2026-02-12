import os
import whisper

def main():
    print("NoSleepDevs Voice Manager Initialized")
    try:
        print("Loading Whisper Model")
        model = whisper.load_model("base")
        print("AI Model Loaded Successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
    current_dir = os.getcwd()
    print(f"Current Directory: {current_dir}")
    print("Files found:", os.listdir(current_dir))
if __name__ == "__main__":
    main()
    