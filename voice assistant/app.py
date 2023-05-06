import datetime
import os
import random
import smtplib
import webbrowser
from tkinter import *
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
from PIL import ImageTk


def get_location(): #in--------------------------------------------------------------------------------------------comp
    """ Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' + my_ip + '.json')
    geo_data = geo_request.json()
    geo = geo_data['city']
    return geo


a = {'voice assistant': 'abisheik619@gmail.com'} #json array from software testing
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendemail(to, content):#in------------------------------------------comp
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abisheik619@gmail.com',
                 'app-password')  # replace app-password
    server.sendmail('abisheik619@gmail.com', to, content)
    server.close()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning ")
        window.update()
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon")
        window.update()
        speak("Good Afternoon")
    else:
        var.set("Good Evening ")
        window.update()
        speak("Good Evening ")
    speak("have a nice day")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='orange')
    wishme()
    speak("Myself your voice assistant! How may I help you ")
    while True:
        btn1.configure(bg='orange')

        query = takeCommand().lower()
        if 'exit' and 'button' in query:
            var.set("voice command required :'exit'")
            window.update()
            speak('if you want to exit then tell the command, exit')

        elif 'exit' in query:
            var.set("Bye Bye")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("see you soon")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(query)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'play' in query:
            var.set('opening youtube for playing')
            window.update()
            song =query.replace('play', '')
            speak('playing' +song)
            pywhatkit.playonyt(song)



        elif 'open browser' in query:
            var.set('opening browser')
            window.update()
            speak('opening browser')
            webbrowser.open("google.com")

        elif 'say hello' in query:
            var.set('Hello Everyone! My self your voice assistant')
            window.update()
            speak('Hello Everyone! My self your voice assistant')

        elif 'hello' in query:
            var.set('Hello ')
            window.update()
            speak("Hello ")

        elif ('play music' in query) or ('change music' in query):#offline music folder #not --------------------------------comp
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'path-to\\songs'
            songs = os.listdir(music_dir)
            n = random.randint(0, 3)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set(" the time is %s" % strtime)
            window.update()
            speak(" the time is %s" % strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)

        elif 'thank you' in query:
            var.set("Welcome")
            window.update()
            speak("dont thank me \n anyways Welcome")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks ')
            window.update()
            speak('I can do multiple tasks for you boss. tell me whatever you want to perform for you')

        elif 'old are you' in query:
            var.set("I dont know my age but iam better than 100year old person")
            window.update()
            speak("I dont know my age but iam better than 100year old person")

        elif 'your name' in query:
            var.set("Myself voice assistant")
            window.update()
            speak('myself voice assistant \n dont try to change my name because i love this')

        elif 'who created you' in query:
            var.set('My Creators are abisheik,arvind,kathirhavan.')
            window.update()
            speak('My Creators are  abi,shake \n ar,vind \n kathirhavan.')

        """elif 'weather' in query:#not----------------------------------------------comp website:Free Weather API - WeatherAPI.com
            owm = pyowm.OWM('api-key')
            # current weather forecast
            loc = owm.weather_at_place(city)
            weather = loc.get_weather()
            # status
            status = weather.get_detailed_status()
            var.set(f'{status} in {city}')
            window.update()
            speak(f'{status} in {city}')
            # temperature
            temp = weather.get_temperature(unit='celsius')
            for key, val in temp.items():
                if key == 'temp':
                    var.set(f'{val} degree celcius')
                    window.update()
                    speak(f"current temperature is {val} degree celcius")
            # humidity, wind, rain, snow
            humidity = weather.get_humidity()
            wind = weather.get_wind()
            var.set(f'{humidity} grams per cubic meter')
            window.update()
            speak(f'humidity is {humidity} grams per cubic meter')
            var.set(f'wind {wind}')
            window.update()
            speak(f'wind {wind}')
            # sun rise and sun set
            sr = weather.get_sunrise_time(timeformat='iso')
            ss = weather.get_sunset_time(timeformat='iso')
            var.set(sr)
            window.update()
            speak(f'SunRise time is {sr}')
            var.set(ss)
            window.update()
            speak(f'SunSet time is {ss}')
            # clouds and rain
            loc = owm.three_hours_forecast(city)
            clouds = str(loc.will_have_clouds())
            rain = str(loc.will_have_rain())
            if clouds == 'True':
                var.set("It may have clouds in next 5 days")
                window.update()
                speak("It may have clouds in next 5 days")
            else:
                var.set("It may not have clouds in next 5 days")
                window.update()
                speak("It may not have clouds in next 5 days")
            if rain == 'True':
                var.set("It may rain in next 5 days")
                window.update()
                speak("It may rain in next 5 days")
            else:
                var.set("It may not rain in next 5 days")
                window.update()
                speak("It may not rain in next 5 days")


           elif 'email to' in query:                 #in------------------------------------------comp
            try:
                query = query.replace("email to", "")
                query = query.replace(" ", "")
                print(query)
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = a[query]
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')#

            except Exception as e:
                print(e)
                var.set("Sorry! I was not able to send this email")
                window.update()
                speak('Sorry! I was not able to send this email')"""



def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [ImageTk.PhotoImage(file='C:/Users/abish/PycharmProjects/collageminiproject/assist.gif', format='gif -index %i' % (i)) for i in range(100)]
window.title('Voice assistant')

label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)
btn0 = Button(text='WISH ME', width=20, command=wishme, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='START', width=20, command=play, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()