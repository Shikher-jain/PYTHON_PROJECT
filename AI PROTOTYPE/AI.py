from MouduleInstall import check
# from MouduleInstall import check
check("speech_recognition")
check("pyttsx3")
check("pywhatkit")
check("datetime")
check("wikipedia")
check("pyjokes")
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice to a specific one (e.g., second voice in the list, often female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Selects the second voice in the list

# Function to speak out the text
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to commands from the user
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')  # Remove 'jarvis' from the command
                print(f"Command received: {command}")
    except:
        print("Sorry, I could not understand that.")
        command = ""
    return command

# Function to execute commands
def run_jarvis():
    command = listen()

    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'The time is {time}')

    elif 'tell me about' in command:
        query = command.replace('tell me about', '')
        summary = wikipedia.summary(query, sentences=1)
        talk(summary)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    else:
        talk("Sorry, I didn't understand that command.")

# Main execution loop
if __name__ == "__main__":
    while True:
        run_jarvis()
