
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
from sys import exit

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import  Qt
from PyQt6.QtGui import  QMovie
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUiType

from uip import Ui_MainWindow

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice


engine.setProperty('voice', voices[1].id)


def speak(audio):

        engine.say(audio) 

        engine.runAndWait() #Without this command, speech will not be audible to us.



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.operate()


    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        speak("I am Jarvis Sir. Please tell me how may I help you")  




    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
        return query

 

    def uptext():

        txt = "hii"

        return txt



    
    def operate(self):
        self.wishMe()
        while True:
        # if 1:
        
            query = self.takeCommand().lower() #Converting user query into lower case
            #query="python wikipedia"

            # Logic for executing tasks based on query
            if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')



                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)

                
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
                
            elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")



            


operate  =  MainThread()




 
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.start.clicked.connect(self.startTask)

   
    def startTask(self):
        self.ui.movie = QtGui.QMovie(".\\imgs/jar-1-unscreen.gif")
        self.ui.gif1.setMovie(self.ui.movie)

        self.ui.movie2 = QtGui.QMovie(".\\imgs/load.gif")
        self.ui.label.setMovie(self.ui.movie2)

        self.ui.movie.start()
        self.ui.movie2.start()

        self.ui.start.hide()
        operate.start()



app = QApplication(sys.argv)
ob  = Main()
ob.show()
exit(app.exec())
