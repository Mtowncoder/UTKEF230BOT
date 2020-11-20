# Motion sensor turns it on
# Hey Lazy Dog also turns it on
# HEy Lazy dog activates voice recgonition
# or button turns on voice regonition
# Happy, Sad, Mad quotes done
# Next find out how to get weather data
i = "I'm Happy"

if i == "what's the weather":
# import required modules
# install requests and Json packages
    import requests, json 
  
# Enter your API key here 
    api_key = "3a27fe66ad4e02d5fc787979f159dd1f"
  
# base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
    city_name = 'Knoxville' #input("Your city : ")
    # make city name equal to variable stored by voice recognizer make speech ask what's your city or set city to knoxville
  
# complete_url variable to store 
# complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return response object 
    response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
    x = response.json() 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
try:
    if x["cod"] != "404": 
      
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
      
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = round((y["temp"] - 273.15)*(9/5) + 32)
        
        
      
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
      
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
      
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
      
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
      
        # print following values 
        weather = (" The Temperature is currently " +
                        str(current_temperature) +
                   "\n Degrees Fahrenheit." +


              "\n The Weather in Knoxville:,, " +
                        str(weather_description))
      
    else: 
        weather = " City Not Found "
except:
    dontwork =5
    


parking_spots = "there are six parking spots available"

# find date using date import
from datetime import date
today = date.today()
d2 = today.strftime("%B %d, %Y")
date_finder = d2
# find time
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
time_finder = current_time
        # end

        # Create random from 1-10
        # Create dictionary of quotes with keys from 1-10 so each quote will be random
from random import *

x = randint(1, 10)    # Pick a random number between 1 and 10.

s_dictionary = { 1:"Do you want a hug?", 2:"You are not alone in this", 3:"May the strength of the past reflect in your future.", 4: "You have so many extraordinary gifts–how can you expect to live an ordinary life?",
                         5:"I can’t really fully understand what you are feeling, but I can offer my compassion.",
                         6:"What's the difference between Mechanical Engineers and Civil Engineers? Mechanical Engineers build weapons, Civil engineers build targets",
                         7:"Did you hear the one about the constipated engineer? He managed to work it out with a pencil. Turns out it was a natural log",
                         8:"What do you call it when Batman skips church? Christian Bale", 9:"How do you organize a space party? You planet.", 10: "you are loved and you matter"}             
                         

s_quotes = s_dictionary[x]



m_dictionary = { 1:"When you look at the dark side, careful you must be. For the dark side looks back", 2:"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering",
                         3:"speak when you are angry and you will make the best speech you will ever regret", 4: "there are two things a person should never be angry at, what they can help, and what they cannot",
                         5: "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned.", 6:"take a deep breath and relax", 7: "The best fighter is never angry", 8:"Don't be",
                         9: "Calm down", 10: "Good vibes only"}

m_quotes = m_dictionary[x]

h_dictionary = { 1:"I'm Glad to hear that", 2: "Your smile is perfect", 3: "your smile brings people joy keep smiling",  4:"That is Great, thats what i like to hear", 5:"you are shining",
                 6:"Awesome, have a good day", 7:"I wish I could feel emotion", 8:"Do you want a cookie", 9:"Keep smiling", 10:"Nice"}


h_quotes = h_dictionary[x]


EF_class = "Here are some good resources, check your email"
#install pyttsx3 package
   

if i == "what's the weather":

# importing the pyttsx library 
    import pyttsx3 
  
# initialisation 
    engine = pyttsx3.init() 
  
# testing 
    engine.say(weather) 
    engine.runAndWait()

elif i == "I'm Sad":

    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say(s_quotes) 
    engine.runAndWait()


elif i == "I'm Mad":
    
    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say(m_quotes) 
    engine.runAndWait()


elif i == "I'm Happy":
    
    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say(h_quotes) 
    engine.runAndWait()
   

elif i == 'EF Help':
    import smtplib, ssl
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "emailyouwanttousetosend"
    receiver_email = "emailyouwanttogetmessage"
    password = 'yourpassword'
    message = """\
    Subject: EF Help 

    I heard you need EF HELP, Here are some good resources:
    ef.engr.utk.edu/efp/
    www.coop.utk.edu
    youtube.com
    www.coop.utk.edu
    stackexchange.com
    nasa.com
    """


    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("youremail@what.com", password)
        server.sendmail(sender_email, receiver_email, message)
        # TODO: Send email here
   
    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say(EF_class) 
    engine.runAndWait()


elif i == "what is todays date":
    
    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say(time_finder)
    engine.say(date_finder)
    engine.runAndWait()


elif i == "EF Parking":

    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say(parking_spots) 
    engine.runAndWait()

    
else:
    
    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say("Unknown command, please repeat") 
    engine.runAndWait()
