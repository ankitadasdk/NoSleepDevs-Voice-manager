import os
import whisper

def main():
    print("--- NoSleepDevs Voice Manager Initialized ---")
    
    # Check if the AI model loads
    try:
        print("Loading Whisper Model (Base)...")
        model = whisper.load_model("base")
        print("AI Model Loaded Successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")

    # Test File Management logic
    current_dir = os.getcwd()
    print(f"Current Directory: {current_dir}")
    print("Files found:", os.listdir(current_dir))

if __name__ == "__main__":
    main()
    