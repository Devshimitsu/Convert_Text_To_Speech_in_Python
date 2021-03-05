from gtts import gTTS 
  
mytext = input("\nText That You Want To convert To Audio: ")
  
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save(input("\nFile Name: ") +".mp3") 

#By_Devshimitsu
