# Import the libraries to be used by the google text to speech
from gtts import gTTS 
import os
  
# The text that you want to convert to audio
audio_text = 'Welcome to python repository, sit back,relax and enjoy!'
  
# Language in which you want to convert
language = 'en'
  
#Passing the text,language and the speed of the audio you can remove the speed 
audio_object = gTTS(text=audio_text, lang=language, slow=False)
  
#Saving the audio file (but you can only use it once,you have to change the name when you run it couple of times)
audio_object.save("welcome.mp3")
  
#Playing the converted file
os.system("start welcome.mp3")