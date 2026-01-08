import speech_recognition as sr
# import pyttsx3
import time

# def SpeakText(command):
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()


r = sr.Recognizer()

# List available microphones
print("Available microphones:")
mic_list = sr.Microphone.list_microphone_names()
for i, microphone_name in enumerate(mic_list):
    print(f"  {i}: {microphone_name}")

# Use the first microphone (index 0) - MacBook Air Microphone
mic_index = 0
print(f"\nUsing microphone: {mic_list[mic_index]} (index {mic_index})\n")

# Test microphone access
print("Testing microphone access...")
test_mic = sr.Microphone(device_index=mic_index)
with test_mic as test_source:
    time.sleep(0.1)
    if test_source.stream is None:
        raise Exception("Microphone stream is None - check permissions")
print("Microphone access successful!\n")


while True:
    try:
        # Explicitly use device_index=0 for the microphone
        mic = sr.Microphone(device_index=mic_index)
        with mic as source2:
            # Wait a moment to let the microphone initialize
            time.sleep(0.5)
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source2, duration=0.2)

            print("Listening...")
            audio2 = r.listen(source2, timeout=5, phrase_time_limit=5)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say:", MyText, "\n")
    except sr.WaitTimeoutError:
        print("No speech detected. Waiting again...\n")
        continue
    except sr.UnknownValueError:
        print("Could not understand audio\n")
        continue 
    