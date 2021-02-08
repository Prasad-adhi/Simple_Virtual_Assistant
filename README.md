# Simple_Virtual_Assistant

This is a simple chatbot where you can talk via microphone and the application listens to your voice and replies according to query put-forth by you.

You need python 3 to run this application in your system

## Required modules you need to run the program:
1) Random:`pip install random`
2) Numpy:`pip install numpy`
3) Joblib:`pip install joblib`
4) Nltk:`pip install nltk`
5) Tensorflow:`pip install tensorflow`
6) SpeechRecognition:`pip install SpeechRecognition`

Since we are downloading `SpeechRcognition` it is advisable to download these modules as well for easy use
1) `pip install pyaudio` (if this doesnt work click [here](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14))
2) `pip install wheel`
3) `pip install google-api-python-client`
4) `pip install monotonic`

Pyttsx3:`pip install pyttsx3`

Disclaimer:Pyttsx3 only works with python 3.7.4 in case you dont have the required version and you are using anaconda prompt 
Then in the anaconda prompt `conda install python==3.7.4` 

Create a new environment with a another version
`conda create --name py33 python=3.7.4`
`source activate py33`

## How to go about the program:
1) I have attached the json file from which the reply is generated accordingly. The first and foremost thing to do is to change the Json file according to your wish. Here change the pattern and the responses to your wish other than that you dont need to change anything.
2) After doing changes to the json file run the chatbot-training.py
3) Now run the SimpleVirtualAssistent.py file to run the application
4) Once you are done working with the application say 'finish' to close the application
