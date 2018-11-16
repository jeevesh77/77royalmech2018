import speech_recognition as sr
AUDIO_FILE = ("dl1.wav")
r=sr.Recognizer() 
with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source)
try:
	print("The audio file contains:" + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Google Speech Recognizer cound not understand audio")
except sr.RequestError as e:
	print("Could not request from Google Speech Recognition service; {0}".format(e))

