import os
import shutil
from pathlib import Path

def move_file_to_folder(filename, destination_folder):
    current_dir = os.getcwd() 
    source_path = os.path.join(current_dir, filename)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created new folder: {destination_folder}")
    destination_path = os.path.join(destination_folder, filename)
    try:
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print(f"SUCCESS: Moved '{filename}' to '{destination_folder}'")
            return True
        else:
            print(f"ERROR: File '{filename}' not found in {current_dir}")
            return False
    except Exception as e:
        print(f"System Error: {e}")
        return False
if __name__ == "__main__":
    with open("test_file.txt", "w") as f:
        f.write("Hackathon testing")
    move_file_to_folder("test_file.txt", "Organized_Files")
def smart_organizer(voice_text):
  """
  Scans the voice text for keywords and decides what to move.
  """
  current_dir = os.getcwd()
  all_files = os.listdir(current_dir)
  if "image" in voice_text or "photo" in voice_text:
      target_folder = "My_Images"
      extension = (".png", ".jpg", ".jpeg")
  elif "document" in voice_text or "pdf" in voice_text:
      target_folder = "My_Documents"
      extension = (".pdf", ".docx", ".txt")
  else:
      print("Logic Error: I heard you, but I don't know which files to move.")
      return False
  moved_count = 0
  for file in all_files:
      if file.lower().endswith(extension):
          move_file_to_folder(file, target_folder)
          moved_count += 1       
  print(f"Total files organized: {moved_count}")
  return True