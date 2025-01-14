#!/usr/bin/env python
# coding: utf-8

# In[6]:


import speech_recognition as sr

def main():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please say something")
        
        audio = r.listen(source)
        
        try:
            print("You have said: \n" + r.recognize_google(audio))
            
        except Exception as e:
            print("Error : " + str(e))

if __name__ == "__main__":
    main()


# In[ ]:


#if they want to listen to live talks, might need to have a mode that allows 3 second interval subtitle updates

