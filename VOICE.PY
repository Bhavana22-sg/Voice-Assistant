import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            print("No voice detected.")
            return ""

        except sr.UnknownValueError:
            speak("I could not understand you.")
            return ""

        except sr.RequestError:
            speak("Speech recognition is unavailable.")
            return ""


# Applications
apps = {
    "calculator": "start calc",
    "notepad": "start notepad",
    "paint": "start mspaint",
    "word": "start winword",
    "excel": "start excel",
    "powerpoint": "start powerpnt",
    "chrome": "start chrome",
    "edge": "start msedge",
    "file explorer": "start explorer",
    "command prompt": "start cmd",
    "task manager": "start taskmgr"
}


# Websites
websites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "whatsapp": "https://web.whatsapp.com",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "chatgpt": "https://chatgpt.com"
}


def open_app(command):

    # Check applications
    for app in apps:
        if app in command:
            speak("Opening " + app)
            os.system(apps[app])
            return

    # Check websites
    for website in websites:
        if website in command:
            speak("Opening " + website)
            webbrowser.open(websites[website])
            return

    speak("Sorry, I could not find that application.")


# Main program
speak("Hello. I am ready. Tell me an application to open.")

while True:

    command = listen()

    if command == "":
        continue

    # Stop
    if "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye")
        break

    # Open whatever application was spoken
    open_app(command)
