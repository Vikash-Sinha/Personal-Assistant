# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:04:50 2020

@author: vikas
"""
import time
#import webbrowser 
import os
import pyttsx3
from playsound import playsound
import speech_recognition as sr

#from tkinter import *
from selenium import webdriver
#from selenium import ActionChains
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
import chromedriver_binary
#driver=webdriver.Edge('D:/software/MicrosoftWebDriver')



r=sr.Recognizer()
engine = pyttsx3.init()
#data store here
dataDis={'hai':'hello',
         'what are you doing':' its non of your business',
         'I am sad':'kya hua hai aapko',
         'open YouTube':'khool rahai hai wait kijiye',
         'play a song':'Ganna Sunna hai',
         'mood off':'don''t sad sir! What can i do for you',
         'ok bye':'bye sir! and take care',
         "it's my order":'wait sir i am trying! dheerai dheerai ho bhaisoor dheerai dheerai, hamra marwaa mai ayeah bhaisoor dheerai dheerai! kaisa laga sir',
         'sing a song':'i can''t sing a song',
         'good':'thank you sir',
         'Vinod please sing a song':'sir i can''t sing a song! i can play a song for you',
         
         }

#default setting for speeker
volume = engine.getProperty('volume')  
engine.setProperty('volume',0.1)

voices = engine.getProperty('voices')      
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')  
engine.setProperty('rate', 150)

#audio recognisationn code
engine.say("hello vikash sir,i''m Vinod, Design By you, how can i help you")
engine.runAndWait() 
def voice(say=False):
     with sr.Microphone()as source:
        if say:
             speek(say)
             print('.')
        audio=r.listen(source)
        text=''
        try:
            text=r.recognize_google(audio) 
        except:
            print("something went worng")
     return text
def speek(say):
    engine.say(say)
    engine.runAndWait()
def youtube():
    t=voice('What you want to play there')
    driver = webdriver.Chrome()
    s='https://www.youtube.com/results?search_query='+t
    driver.get(s)
    play=driver.find_elements_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')
    play[0].click()
    time.sleep(5)

    hlp=voice('any help')
    print(hlp)
    if(hlp=='play on full screen'):
        ful=driver.find_element_by_xpath('//*[@id="movie_player"]/div[32]/div[2]/div[2]/button[8]')
        ful.click()
    speek('enjoy sir') 
    
def google():
    t=voice('What you want to play there')
    driver = webdriver.Chrome()
    s='https://www.google.com/search?q='+t
    driver.get(s)
while True:
    t=voice('i''m listning')
    if t in dataDis:
        speek(dataDis[t])
    if(t=='ok bye'):
        os.exit(0)
    elif t=='open YouTube':
        youtube()
    elif t=='search on google':
        google()
        
        break;
    elif t=='play a song':
        playsound('D:/mob/apkaIntzar.mp3')
        break;
        









































'''
while True:
    
    engine.say("i'm listening ...")
    engine.runAndWait()
    with sr.Microphone()as source:
        print(".")
        audio=r.listen(source)
        text=r.recognize_google(audio)
       
        try:
            print(text)
            
            if text in dataDis:
                engine.say(dataDis[text])
                print(dataDis[text])
               
            else:
                 engine.say("ye kayaa bole rahae ho")
            
            engine.runAndWait() 
            if(text=='ok bye'):
                
                break;
            elif text=='open YouTube':
               driver = webdriver.Edge(EdgeChromiumDriverManager().install())
               driver.get('https://youtube.com/')
               break;
            elif text=='play a song':
                playsound('D:/mob/apkaIntzar.mp3')
                break;
           
              
              
        except:
            print("something went worng")
     
print('program end')
'''