#conda activate py33
#conda deactivate
import random
import json
import pickle
import numpy as np

import speech_recognition as sr
import pyttsx3

from ChatbotWorking import get_response,clean_up_sentence,bag_of_words,predict_class,audio_text
from AutomatedGoogleSearch import google_search

from selenium import webdriver 

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer=WordNetLemmatizer()
intents=json.loads(open('intents.json').read())

words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))
model=load_model('chatbotmodel.h5')


r=sr.Recognizer()
choice=int(input("If you want to interact with the chatbot press (1) else if you want to search something press (2)"))
print("say anything : ")
#print(sr.Microphone.list_microphone_names())
while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        audio= r.listen(source)
        try:
            #text = r.recognize_google(audio)
            #text = r.recognize_google(audio,language = 'en-IN', show_all=True)
            text = r.recognize_google(audio,language = 'en-IN')
            if(text=="finish"):
                break
            if(choice==1):
                s_text=text
                print("\t\t You:",format(s_text))
                reply=audio_text(s_text)
                print("Bot:",format(reply))
            else:
                google_search(text)
                reply="This is what I found"
            engine = pyttsx3.init()
            engine.setProperty('rate', 125) 
            engine.say(reply)
            engine.runAndWait()
        except:
            print("could you speak a little bit slower")