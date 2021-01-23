import aiml
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
import os
import webbrowser
from time import sleep
import pyautogui
from PIL import Image


kernel=aiml.Kernel()
kernel.bootstrap(learnFiles = "startup.xml")

r=sr.Recognizer()
mic=sr.Microphone(device_index=1)

rate = engine.getProperty('rate')   
engine.setProperty('rate', 140) 


print("Bot: Hi! I am Curo the Cobot.")
engine.say("Hi! I am Curo, the Co-Bot!")
engine.runAndWait()
sleep(0.3)
print("Bot: Enter Y if you want to enable voice inputs along with the typed ones and I will speak out the answers, else press any other key and enter: ")
engine.say("Enter Y if you want to enable voice inputs along with the typed ones and I will speak out the answers, else press any other key and enter: ")
engine.runAndWait()
X=input("You: ")
if X=='Y' or X=="YES" or X=="yes" or X=="Yes" or X=="y":

   print("Bot: Enter WORLD to get the total no of COVID cases and recoveries in the world.")
   engine.say("Enter world to get the total number of kovid cases and recoveries in the world.")
   engine.runAndWait()
   sleep(0.3)

   print("Bot: Enter INDIA to get the total no of COVID cases and recoveries in India.")
   engine.say("Enter India to get the total number of kovid cases and recoveries in India.")
   engine.runAndWait()
   sleep(0.3)

   print("Bot: Enter HOSPITAL to get the list of nearby hospitals.")
   engine.say("Enter hospital to get the list of nearby hospitals.")
   engine.runAndWait()
   sleep(0.3)

   print("Bot: Enter MED to know about Medical Shops near you.")
   engine.say("Enter med to know about Medical Shops near you.")
   engine.runAndWait()
   sleep(0.3)

   print("Bot: Enter PIC to get an informative poster about COVID-19.")
   engine.say("Enter pick to get an informative poster about covid-19.")
   engine.runAndWait()
   sleep(0.3)

   print("Bot: Enter E for emergency")
   engine.say("Enter E for emergency")
   engine.runAndWait()
   sleep(0.3)

   print("Bot: Feel free to ask any other query and I will try my best to answer you.")
   engine.say("Feel free to ask any other query and I will try my best to answer you.")
   engine.runAndWait()
   sleep(0.3)


   print("Enter LOAD to proceed...  ")
   engine.say("Enter load to proceed")
   engine.runAndWait()

   with mic as source:   
      audio=r.listen(source, timeout=8)
      said=r.recognize_google(audio)
   I= format(said)
   I=I.upper()
   print("You :" + format(said))
   pyautogui.press('enter')

   while I!="exit" and I!="bye" and I!="end" and I!="leave":
      if I=="WORLD" or I=="world" or I=="World":
         webbrowser.open("https://www.worldometers.info/coronavirus/")
      elif I=="INDIA" or I=="india" or I=="India":
         webbrowser.open("https://www.worldometers.info/coronavirus/country/india/")
      elif I=="HOSPITAL" or I=="hospital" or I=="Hospital":
         webbrowser.open("https://www.google.com/search?q=hospitals+near+me")
      elif I=="MED" or I=="med" or I=="Med" :
        webbrowser.open("https://www.google.com/search?q=medical+shops+near+me") 
      elif I=="PIC" or I =="pic" or I=="Pic":
         im = Image.open(r'1.jpg')
         im.show()    
      elif I=='E':
         print("Call govt helpline no: 91-11-23978046")
         engine.say("Call govt helpline no: 91-11-23978046")
         engine.runAndWait()
      else:
         print("Bot:",kernel.respond(I))
         engine.say(kernel.respond(I))
         engine.runAndWait()   
      with mic as source:   
         audio=r.listen(source, timeout=40)
         said=r.recognize_google(audio)
      I= format(said)
      I=I.upper()
      print("You :" + format(said))
      pyautogui.press('enter')

else      

   print("Bot: Enter WORLD to get the total no of COVID cases and recoveries in the world")
   sleep(0.5)
   print("Bot: Enter INDIA to get the total no of COVID cases and recoveries in India")
   sleep(0.5)
   print("Bot: Enter HOSPITAL to get the list of nearby hospitals")
   sleep(0.5)
   print("Bot: Enter MED to know about Medical Shops near you.")
   sleep(0.5)
   print("Bot: Enter PIC to get an informative poster about COVID-19.")
   sleep(0.5)
   print("Bot: Enter E for emergency")
   sleep(0.5)

   print("Bot: Feel free to ask any other query and I will try my best to answer you.")
   sleep(0.5)
   print("Enter LOAD to proceed...  ")
   I=input("You: ")
   I=I.upper()
   while I!="EXIT" and I!="BYE" and I!="END" and I!="LEAVE":
      if I=="WORLD":
         webbrowser.open("https://www.worldometers.info/coronavirus/")
      elif I=="INDIA":
         webbrowser.open("https://www.worldometers.info/coronavirus/country/india/")
      elif I=="HOSPITAL":
         webbrowser.open("https://www.google.com/search?q=hospitals+near+me")
      elif I=="PIC" or I =="pic" or I=="Pic":
         im = Image.open(r'1.jpg')
         im.show()  
      elif I=='E':
         print("Call govt helpline no: 91-11-23978046")
      else:
         print("Bot:",kernel.respond(I))
      I=input("You: ")
      I=I.upper()

print("Bot:",kernel.respond(I))
if X=='Y' or X=="YES" or X=="yes" or X=="Yes" or X=='y':
    engine.say(kernel.respond(I))
    engine.runAndWait()

#kernel.saveBrain("bot_brain.brn")

