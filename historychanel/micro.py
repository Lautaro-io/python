import speech_recognition as sr
import pyaudio
import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def hablar():
    mic = sr.Microphone()
    print("Deci algo")
    with mic as source :
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source )
    try:    
        text = recognizer.recognize_google(audio, language = 'ES')
        print(f"Dijiste {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        engine.say("No te entendí. Por favor, intenta de nuevo.")
        engine.runAndWait()
        return hablar()
    
    except  sr.RequestError as e:
        print(f"Error al solicitar resultados del servicio de reconocimiento de voz; {e}")
        engine.say("Error al conectar con el servicio de reconocimiento de voz.")
        engine.runAndWait()
        return ""

