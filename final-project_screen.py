# Simple text-based "screen recorder" example without modules

def record_screen():
    print("Recording screen...")
    recorded_text = []
    while True:
        user_input = input("Enter text (type 'exit' to stop recording): ")
        if user_input.lower() == 'exit':
            break
        recorded_text.append(user_input)
    
    print("\nRecorded text:")
    for line in recorded_text:
        print(line)

if __name__ == "__main__":
    record_screen()
import os

def record_audio(filename, duration):
    # Define the command to execute
    command = f"SoundRecorder /FILE {filename} /DURATION {duration}"
    
    print("Recording audio...")
    os.system(command)
    print(f"Audio recorded and saved as '{filename}'")

if __name__ == "__main__":
    filename = "recorded_audio.wav"
    duration = 5  # Recording duration in seconds

    record_audio(filename, duration)
