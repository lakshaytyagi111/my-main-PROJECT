# import pyaudio
import pywhatkit
from selenium import webdriver
import time
import pyautogui as pg
import speech_recognition as sr
import webbrowser as web
import pyttsx3
import datetime
import phone
from phone import phone_numbers

# This code is just made for purose of fun and will not work on your computer in a way it is supposed to do
# if you still wanna try then--> password : HelloWorld
# when it say's "how can i help you?" just type "what can you do" to see all the functions in short
# OR type "show commands" to get a list of all commands

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
web.register('edge', None, web.BackgroundBrowser(edge_path))
web2 = web.get('edge')
# This is not Password protected--> password : HelloWorld
password=input("please enter password :")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


date = datetime.datetime.now().day
month = datetime.datetime.now().month
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

HOU = str(hour)
MON = str(month)
DAT = str(date)
MINUT = str(minute)
# This function will wish you according to current time of your computer
def wish_me():
    if hour >= 0 and hour < 12:
        speak('good morning,sir')
    elif hour >= 12 and hour <= 18:
        speak('good afternoon,sir')
    else:
        speak('good evening,sir')
    speak('i am always there to help you,sir')


# screen recorder function this will alow you to record your meeting

def record(x, link):
    # record(1 or 0)
    # 'x' takes values of{0,1,2}
    # 0 for only recording simply
    # 1 for starting recording after a specified time period
    # 2 for starting a meeting (only in microsoft teams) and then recording it
    
    if x == 1:
        # this is for schedulling the recording
        # It will also inform you via a whatsapp message
        hourr = int(input("whats the time (hour) :"))
        minutt = int(input("whats the time (minute) : "))
        pywhatkit.sendwhatmsg("+919588******", "hello", hourr, minutt)
        pg.sleep(8)
        pg.press("enter")
        pg.hotkey("ctrl", "w")
        pg.sleep(5)
        pg.press("enter")
        pg.sleep(8)
        pg.moveTo(1060, 55)
        pg.click()
        pg.sleep(10)
        pg.moveTo(800, 521)
        pg.click()
        pg.sleep(7)
        pg.moveTo(515, 400)
        pg.click()
        pg.sleep(2)
        pg.moveTo(415, 534)
        pg.click()
        pg.moveTo(845, 534)
        pg.click()
    elif x == 2:
        # join meet with record
        hourr = int(input("whats the time (hour) :"))
        minutt = int(input("whats the time (minute) : "))
        pywhatkit.sendwhatmsg("+919588******", "hello", hourr, minutt)
        pg.sleep(8)
        pg.press("enter")
        pg.hotkey("ctrl", "w")
        pg.sleep(5)
        pg.press("enter")
        pg.sleep(8)
        pg.moveTo(1060, 55)
        pg.click()
        pg.sleep(10)
        pg.moveTo(800, 521)
        pg.click()
        pg.sleep(7)
        pg.moveTo(515, 400)
        pg.click()
        pg.sleep(2)
        pg.moveTo(415, 534)
        pg.click()
        pg.moveTo(845, 534)
        pg.click()
        start_meet(link)

        # the end
        # recording will be ended after 1 hour and 30 minutes
        pg.sleep(5400)
        pg.moveTo(1060, 55)
        pg.click()
    else:
        web2.open("google.com")
        pg.sleep(8)
        pg.moveTo(1060, 55)
        pg.click()
        pg.sleep(10)
        pg.moveTo(800, 521)
        pg.click()
        pg.sleep(7)
        pg.moveTo(515, 400)
        pg.click()
        pg.sleep(2)
        pg.moveTo(415, 534)
        pg.click()
        pg.moveTo(845, 534)
        pg.click()
        starting_question()


# starting meeting in Microsoft teams
# just enter the meeting link
def start_meet(link):
    link= input("enter meeting link : ")
    web2.open(link)
    pg.sleep(10)
    pg.press("enter")
    pg.moveTo(990, 380)
    pg.sleep(2)
    pg.click()
    pg.sleep(60)
    pg.moveTo(639, 519)
    pg.click()
    pg.sleep(3)
    pg.moveTo(642, 484)
    pg.click()
    starting_question()

# send whatsapp message intantly
def sent_whatsapp_msg(name, message):
    pywhatkit.sendwhatmsg_instantly(name, message)
    speak('message sent')
    starting_question()


def wrong_whatsname(contact):
    speak('no contact named ' + contact)
    speak('please see the name correctly : ')
    contactA = input("reciever's name : ")
    if contactA == "exit":
        speak("terminal skipped")
        starting_question()
    name = phone_numbers.get(contactA)
    message = input("what is the messgae :")
    elif phone_numbers.__contains__(contactA):
        sent_whatsapp_msg(name, message)

    else:
        wrong_whatsname(wrong_whatsname(contactA))


# add contact function
def add_contact():
    
    name_contact = input("what is the name :")
    phone_contact = input("contact number")
    file = open("phone.py", "a", encoding='utf-8')
    file.write("'"+name_contact+"'" + ':'+"'+91"+phone_contact+"'"+",")
    file.close()
    starting_question()

# shut down laptop
def shut_down():
    pg.moveTo(1100,15000)
    pg.click()
    time.sleep(3)
    pg.hotkey("alt","f4")
    time.sleep(3)
    pg.press("enter")

# open itutor task function
# well this is not for everyone

def i_tutor(wait_time: int = 10):

    web.open("https://digital.aakash.ac.in/login")
    time.sleep(wait_time)
    pg.moveTo(1250, 80)
    pg.click()
    time.sleep(wait_time)
    pg.click()
    time.sleep(wait_time)
    pg.moveTo(1150, 650)
    pg.click()
    time.sleep(wait_time)
    pg.moveTo(800, 500)
    pg.click()
    starting_question()


# text to handwritting function

def text_handwritting():
    # text to handwritting
    speak('please type the text!')
    text = input('please type the text : ')
    pywhatkit.text_to_handwriting(text)
    speak('completed!')
    starting_question()

# screenshot function
def screenshot():
    # screen shot
    pywhatkit.take_screenshot(
        "new capture." + DAT + "/" + MON+"//" + HOU+"/"+MINUT)
    speak("done")
    starting_question()

# search function
def search_query(question):
    pywhatkit.info(question, 5)

# 333333333333333333333333333333333333333333333333333333333
# 333333333333333333333333333333333333333333333333333333333
# 333333333333333333333333333333333333333333333333333333333

# this is the main question to be asked repeatedly


def starting_question():
    speak('how can i help you?')
    how_to_help = input('how can i help you? : ')
    print()
    if how_to_help == 'send message':
        speak('to whome should i send a message to? : ')
        contact = input('to whome should i send a message to? : ')
        if phone_numbers.__contains__(contact):
            name = phone_numbers.get(contact)
        else:
            wrong_whatsname(contact)

        speak('what is the message?')
        message = input('what is the message? : ')
        sent_whatsapp_msg(name, message)

    elif how_to_help == 'text to handwritting':
        text_handwritting()

    elif how_to_help == "join msmeet":           #######################
        link = input("please give link : ")
        start_meet(link)
    elif how_to_help == "record screen":         ######################
        record(0, "abc")
    elif how_to_help == "join meet with record": #######################
        link = input("please give link to meeting: ")
        record(2, link)
    elif how_to_help == 'exit':                  ####################### 
        speak('allright terminal skipped')

    elif how_to_help == "wait":                  #######################
        speak('okay')
        hello_again = input(": ")
        if hello_again ==password:
            starting_question()
        else :
            pass
    elif how_to_help == 'add contact':           #######################
        add_contact()
    elif how_to_help=="what is your name":       #######################
        speak("i am lakshay's personel assistant")
    
    elif how_to_help=="what can you do":         #######################
        speak("i can currently do only certain predefined tasks, like")
        speak("sending whatsapp message")
        speak("starting a meeting on MS teams")
        speak("recording your class")
        speak("recording only")
        speak("opening i-tutor")
        speak("taking screenshot")
        speak("converting text to handwritting")
        speak("schearching on google")
        speak("here is a list of all commands ")
        
        print(
            "\n                Here is a list of all functions: \n 1.send whatsapp message : send message \n 2.opening i-tutor       : tutor \n 3.taking screen-shot    : screen shot \n 4.adding a new contact  : add contact \n 5.text to handwritting  : text to handwritting \n 6.join in ms teams      : join msmeet \n 7.only recording        : record screen \n 8.recording a class     : join meet with record \n \n                  Some other commands \n 1.shut down 2.exit 3.wait \n"
        )
        pg.sleep(4)
        starting_question()
    elif how_to_help=="show commands":
        speak('here you go')
        print(
            "\n                Here is a list of all functions: \n 1.send whatsapp message : send message \n 2.opening i-tutor       : tutor \n 3.taking screen-shot    : screen shot \n 4.adding a new contact  : add contact \n 5.text to handwritting  : text to handwritting \n 6.join in ms teams      : join msmeet \n 7.only recording        : record screen \n 8.recording a class     : join meet with record \n \n                  Some other commands \n 1.shut down 2.exit 3.wait 4.show commands\n"
        )
        starting_question()

    elif how_to_help.__contains__("tutor"):
        i_tutor()
    elif how_to_help == "screen shot":
        screenshot()

    elif how_to_help=="shut down":
        shut_down()

    else:
        speak("here are some results from the web")
        search_query = how_to_help
        answer_to_query = web.open(
            "https://www.google.com/search?q="+search_query)
        # speak(answer_to_query)
        starting_question()

if password=="HelloWorld":
    wish_me()
    starting_question()
else:
    print("password don't match")


# 333333333333333333333333333333333333333333333333333333333
# 333333333333333333333333333333333333333333333333333333333
# 333333333333333333333333333333333333333333333333333333333
# 333333333333333333333333333333333333333333333333333333333
