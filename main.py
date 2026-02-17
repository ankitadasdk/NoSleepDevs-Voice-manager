import recorder     
import brain        
import file_logic   

def run_system():
    print("\n NOSLEEPDEVS SYSTEM ONLINE")
    recorder.record_voice()
    command = brain.process_voice_command()
    if command:
        print(f"Executing: {command}")
        file_logic.smart_organizer(command)
    else:
        print("System: I didn't hear anything.")

if __name__ == "__main__":
    run_system()