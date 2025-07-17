import speech_recognition as sr
from gpiozero import LED
from time import sleep

# Setup LED on GPIO17
led = LED(2)

# Initialize recognizer
recognizer = sr.Recognizer()

# Set the correct microphone index
mic_index = 2  # UACDemoV1.0: USB Audio

print("Say 'turn on the light' or 'turn off the light'...")

while True:
    try:
        with sr.Microphone(device_index=mic_index) as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source)

            # Use Google Speech API
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "turn on" in command or "led on" in command:
                led.on()
                print("✅ LED turned ON")

            elif "turn off" in command or "led off" in command:
                led.off()
                print("❌ LED turned OFF")

            elif "exit" in command or "stop" in command:
                print("🛑 Exiting program.")
                break

    except sr.UnknownValueError:
        print("🤷 Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"❗ Speech recognition error: {e}")
    
    sleep(1)
