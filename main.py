import datetime
import speech_recognition as sr
import pyttsx3
import wolframalpha
import webbrowser
import wikipedia


# Speech engine initialisation
engine = pyttsx3.init()
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[0])    # 0 = male, 1 = female
activation_word = "iva"     # 'iva' stands for "Intelligent Virtual assistant"


def parse_command():
    listener = sr.Recognizer()
    print("Listening...")

    with sr.Microphone as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print("Recognizing command...")
        query_1 = listener.recognize_google(input_speech, language='en_gb')
        print("The command was {0}".format(query_1))

    except Exception as exception:
        print("Could not hear you")
        speak("Could not hear you")
        print(exception)
        return 'None'

    return query


def speak(text, rate=150):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


# Main Loop
if __name__ == '__main__':
    speak("Hey there. What can I do for you?", 190)

    while True:     # Parse as list
        query = parse_command().lower().split()

        if query[0] == activation_word:
            query.pop(0)

            if query[0] == 'say':
                if 'hello'.lower() in query:
                    speak('Greetings')
                else:
                    query.pop(0)    # Remove 'Say' from the list
                    speech = '  '.join(query)
                    speak(speech)
