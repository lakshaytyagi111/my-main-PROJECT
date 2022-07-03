# import pyAudio
from getpass import getpass
import pywhatkit
from selenium import webdriver
import time
import os
import pyautogui as pg
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

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

date = datetime.datetime.now().day
month = datetime.datetime.now().month
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

HOUR = str(hour)
MONTH = str(month)
DATE = str(date)
MINUTE = str(minute)

# This function will wish you according to current time of your computer

def wish_me():
    if hour >= 0 and hour < 12:
        speak('good morning,sir')
    elif hour >= 12 and hour <= 18:
        speak('good afternoon,sir')
    else:
        speak('good evening,sir')
    speak('i am always there to help you,sir')
    starting_question()

# send whatsapp message intantly
def sent_whatsapp_msg(name, message):
    pywhatkit.sendwhatmsg_instantly(name, message)
    speak('message sent')
    starting_question()


def wrong_whatsname(contact, message):

    speak('no contact named ' + contact)
    speak('do you want to add new contact :')
    ppp = input('do you want to add new contact :[y]/[n]')
    if ppp == 'y':
        add_contact()
    else:
        starting_question()

    speak('please type the name correctly : ')
    print('or type "exit"')
    contactA = input("reciever's name : ")
    if contactA == "exit":
        speak("terminal skipped")
        starting_question()

    elif phone_numbers.__contains__(contactA):
        sent_whatsapp_msg(contactA, message)

    else:
        wrong_whatsname(wrong_whatsname(contactA))


# add contact function
def add_contact():

    name_contact = input("what is the name :")
    phone_contact = input("contact number :")
    file = open("phone.py", "a", encoding='utf-8')
    phone_no = f"+91{phone_contact}"
    phone_numbers.update({name_contact: phone_contact})
    phone_numbrs = str(phone_numbers)
    print(phone_numbrs)
    file.truncate(0)
    file.write('phone_numbers = ' + phone_numbrs)
    print(file)
    starting_question()

# shut down device
def shut_down(a):
    a = int(a)
    time.sleep(a)
    os.system("shutdown /s /t 1")


def displaydns():
    try:
        os.makedirs('c:/xampp/htdocs')
        open('c:/xampp/htdocs/log.txt')
    except:
        pass
    pg.hotkey('win', 'r')
    pg.typewrite("cmd")
    pg.sleep(1)
    pg.press('enter')
    pg.sleep(1)
    pg.typewrite('ipconfig /displaydns >c:/xampp/htdocs/log.txt')
    pg.press('enter')
    pg.typewrite('exit')
    pg.press('enter')
    starting_question()
    
def flushdns():
    try:
        os.makedirs('c:/xampp/htdocs')
        open('c:/xampp/htdocs/log.txt')    
    except:
        pass
    pg.hotkey('win', 'r')
    pg.typewrite("cmd")
    pg.sleep(1)
    pg.press('enter')
    pg.sleep(1)
    pg.typewrite('ipconfig /flushdns')
    pg.press('enter')
    pg.typewrite('exit')
    pg.press('enter')
    starting_question()

def open_instagram():
    username = input('username:')
    password = getpass()
    web.open('https://instagram.com')
    pg.sleep(30)
    pg.press('tab')
    pg.press('tab')
    pg.typewrite(username)
    pg.press('tab')
    pg.typewrite(password)
    pg.press('enter')
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
    pywhatkit.take_screenshot()
    speak("done")
    starting_question()

# search function
def search_query(question):
    pywhatkit.info(question, 2)

# this is the main question to be asked repeatedly


def starting_question():
    speak('how can i help you?')
    how_to_help = input('how can i help you? : ')
    print()
    if how_to_help == 'send message':
        speak('to whome should i send a message to? : ')
        contact = input('to whome should i send a message to? : ')
        speak('what is the message?')
        message = input('what is the message? : ')
        if phone_numbers.__contains__(contact):
            name = phone_numbers.get(contact)
        else:
            wrong_whatsname(contact, message)

        sent_whatsapp_msg(name, message)

    elif how_to_help == 'text to handwritting':
        text_handwritting()
        
    elif how_to_help == 'open instagram':
        open_instagram()

    elif how_to_help == 'exit':
        speak('allright, terminal exitted')
        exit()

    elif how_to_help == "wait":
        speak('okay')
        hello_again = input(": ")
        verificate()

    elif how_to_help == 'add contact':
        add_contact()

    elif how_to_help == "what is your name":

        speak("i am lakshay's personel assistant, tony")
    elif how_to_help == 'open instagram':
        open_instagram()

    elif how_to_help == "what can you do":

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
            "\n                Here is a list of all functions: \n 1.send whatsapp message : send message \n 2.opening instagram       : open instagram \n 3.taking screen-shot    : screen shot \n 4.adding a new contact  : add contact \n 5.text to handwritting  : text to handwritting \n \n                  Some other commands \n 1.shut down 2.exit 3.wait 4.show commands 5.display dns  6.flush dns\n"
        )
        pg.sleep(4)

        starting_question()

    elif how_to_help == "show commands":
        speak('here you go')
        print(
            "\n                Here is a list of all functions: \n 1.send whatsapp message : send message \n 2.opening instagram      : open instagram \n 3.taking screen-shot    : screen shot \n 4.adding a new contact  : add contact \n 5.text to handwritting  : text to handwritting \n \n                  Some other commands \n 1.shut down 2.exit 3.wait 4.show commands 5.display dns  6.flush dns\n"
        )
        starting_question()

    elif how_to_help == "screen shot":
        screenshot()

    elif how_to_help == "shut down":
        shut_down(20)
    
    elif how_to_help == "display dns":
        speak('here you go!')
        displaydns()
    
    elif how_to_help == "flush dns":
        flushdns()

    else:
        speak('do you want pe to search it on web? ')
        inut = input('do you want pe to search it on web? [yes]/[no] :')
        if inut == 'yes':
            speak("here are some results from the web")
            search_query = how_to_help
            answer_to_query = web.open("https://www.google.com/search?q="+search_query)
            starting_question()
        else:
            starting_question()


def verificate():
    password = getpass()
    if password == "HelloWorld":
        starting_question()
    else:
        print("password don't match")
        exit()

def _ask_Verification(i , test=0):
    if type(i)== int:
        pass
    else:
        if test==1 and i=='a':
            password = getpass()
            if password == "HelloWorld":
                starting_question()
            else:
                exit()

    password = getpass()
    if password == "HelloWorld":
        wish_me()
        starting_question()
    elif i == 3:
        speak('sorry, could not verify you')
        print('sorry, could not verify you')
        exit()
    else:
        print("password don't match")
        print('you have ' + str(3-int(i)) + ' tries left')
    while i < 4:
        i += 1
        _ask_Verification(i)
    
        
_ask_Verification(1)