# voice_led.py
import speech_recognition as sr
from gpiozero import LED
from time import sleep

led = LED(17)
recognizer = sr.Recognizer()

def listen_and_control():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Speak now.")
        recognizer.adjust_for_ambient_noise(source)
        
        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")

                if "turn on" in command or "led on" in command:
                    led.on()
                    print("LED turned ON.")
                elif "turn off" in command or "led off" in command:
                    led.off()
                    print("LED turned OFF.")
                elif "exit" in command or "stop" in command:
                    print("Exiting program.")
                    break
                else:
                    print("Command not recognized.")
            except sr.UnknownValueError:
                print("Sorry, I could not understand.")
            except sr.WaitTimeoutError:
                print("Listening timed out, try again.")
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    listen_and_control()

