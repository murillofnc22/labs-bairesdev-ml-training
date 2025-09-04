from gtts import gTTS
import speech_recognition as sr
import os
from datetime import datetime
import playsound
import wikipedia
import webbrowser

def get_audio():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 1
    audio = r.listen(source)
    said = ""
    try:
      said = r.recognize_google(audio, language = "pt-BR")
      print(said)
    except sr.UnknownValueError:
      print("Não entendi")
    except sr.RequestError:
      print("Erro ao conectar")
  return said

def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

def respond(text):
    text = text.lower()
    if 'youtube' in text:
        speak("O que você quer pesquisar?")
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Veja o que eu encontrei para {keyword} no youtube")
    elif 'buscar' in text:
        speak("O que você quer que eu busque?")
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("De acordo com a wikipedia")
            print(result)
            speak(result)    
    elif 'que horas' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)    
    elif 'sair' in text:
        speak("Adeus, até a próxima!")
        exit()

while True:
  print("Estou ouvindo...")
  text = get_audio()
  respond(text)