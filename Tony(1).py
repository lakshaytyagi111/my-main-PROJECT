# import pyAudio
import datetime
import os
import time
import webbrowser as web
from getpass import getpass
import pyautogui as pg
import pyttsx3
import pywhatkit
import speech_recognition as sr
from selenium import webdriver
import phone
from phone import phone_numbers

# This code is just made for purose of fun and will not work on your computer in a way it is supposed to do
# if you still wanna try then--> password : HelloWorld
# when it say's "how can i help you?" just type "what can you do" to see all the functions in short
# OR type "show commands" to get a list of all commands

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" #type: ignore
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

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


#speech recognition function

def inut1():
    r= sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.3
        prYellow('recognising...')
        
        audio= r.record(source, duration= 5)

        try:
            how_to_help = r.recognize_google(audio_data=audio)
            how_to_help = str(how_to_help)
            prCyan(f'\n-> {how_to_help}')
            return how_to_help

        except:
            how_to_help = input('How can i help you? \n->') 
            how_to_help = str(how_to_help)
            prCyan(f'\n-> {how_to_help}')
            return how_to_help


# send whatsapp message intantly

def sent_whatsapp_msg(name, message):
    pywhatkit.sendwhatmsg_instantly(name, message)
    speak('message sent')
    starting_question()


def wrong_whatsname(contact, message):

    speak('no contact named ' + contact)
    speak('do you want to add new contact :')
    print('do you want to add new contact :[yes]/[no]')

    ppp = inut1()

    if ppp == 'y':
        add_contact()

    else:
        starting_question()

    speak('please say the name correctly : ')
    print("reciever's name : ")
    contactA = inut1()

    if contactA == "exit":
        speak("terminal skipped")
        starting_question()

    elif phone_numbers.__contains__(contactA):
        sent_whatsapp_msg(contactA, message)

    else:
        wrong_whatsname(wrong_whatsname(contactA, message), message)


# add contact function
def add_contact():

    speak('what is the name')
    name_contact = str(inut1())
    name_contact= name_contact.capitalize()

    speak('plaese enter phone number...\n')
    phone_contact = input("contact number :")
    file = open("phone.py", "a", encoding='utf-8')
    phone_no = f"+91{phone_contact}"

    phone_numbers.update({name_contact: phone_contact}) # type: ignore #phone_no was initially phone_contact if error occur replace to phone_contact
    phone_numbrs = str(phone_numbers)
    print(phone_numbrs)
    file.truncate(0)
    file.write('phone_numbers = ' + phone_numbrs)
    print(file)

    starting_question()

# shut down device
def shut_down(a=3):
    a = int(a)
    os.system(f"shutdown /s /t {a}")
    pg.press('enter')
    starting_question()
    
def abort():
    os.system("shutdown /a")

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
    speak('please provide username and password.')

    username = input('username:')
    password = getpass()

    web.open('https://instagram.com')
    pg.sleep(15)

    pg.press('tab')
    pg.press('tab')
    pg.typewrite(username)
    pg.press('tab')
    pg.typewrite(password)
    pg.press('enter')
    starting_question()


# text to handwritting function
def text_handwritting():

    speak('please type the text!')
    text = input('please type the text : ')
    pywhatkit.text_to_handwriting(text)

    speak('completed!')
    starting_question()


# screenshot function
def screenshot():

    pywhatkit.take_screenshot()

    speak("done")
    starting_question()

# search function
def search_query(question):
    pywhatkit.info(question, 2)

# this is the main question to be asked repeatedly


def starting_question():

    speak('how can i help you?')
    prLightGray('==============================================')
    prLightPurple('how can i help you :')

    how_to_help = inut1()

    if how_to_help == 'send message':

        speak('to whome should i send a message to? : ')
        contact = inut1()

        speak('what is the message?')
        message = inut1()

        if phone_numbers.__contains__(contact):
            contact = phone_numbers.get(contact)

        else:
            wrong_whatsname(contact, message)

        sent_whatsapp_msg(contact, message)

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

    elif how_to_help == 'open Instagram':
        open_instagram()

    elif how_to_help == "what can you do":

        speak("i can currently do only certain predefined tasks, like")
        speak("sending whatsapp message")
        speak("taking screenshot")
        speak("converting text to handwritting")
        speak("schearching on google")
        speak("here is a list of all commands ")
        prGreen(
            "\n                Here is a list of all functions: \n 1. send whatsapp message : send message \n 2. opening instagram      : open Instagram \n 3. taking screen-shot    : screenshot \n 4. adding a new contact  : add contact \n 5. text to handwritting  : text to handwritting \n \n                  Some other commands \n 1. shutdown 2. exit 3. wait 4. show commands 5. display DNS  6. flush DNS   7. abort\n"
        )
        pg.sleep(4)

        starting_question()

    elif how_to_help == "show commands":
        speak('here you go')
        prGreen(
            "\n                Here is a list of all functions: \n 1.send whatsapp message : send message \n 2.opening instagram      : open Instagram \n 3.taking screen-shot    : screenshot \n 4.adding a new contact  : add contact \n 5.text to handwritting  : text to handwritting \n \n                  Some other commands \n 1. shutdown 2. exit 3. wait 4. show commands 5. display DNS  6. flush DNS   7. abort\n"
        )
        starting_question()

    elif how_to_help == 'abort':
        abort()
        
        speak('system shutdown aborted!')
        starting_question()

    elif how_to_help == "screenshot":
        screenshot()

    elif how_to_help == "shutdown":
        shut_down(20)
    
    elif how_to_help == "display DNS":
        speak('here you go!')
        displaydns()
    
    elif how_to_help == "flush DNS":
        flushdns()
    
    else:
        speak('do you want me to search it on web? ')
        inut = inut1()
        if inut == 'yes':
            speak("here are some results from the web")
            search_query = how_to_help
            answer_to_query = web.open("https://www.google.com/search?q="+ str(search_query) )
            starting_question()
        else:
            starting_question()


def verificate():
    password = getpass()
    if password == "HelloWorld":
        starting_question()
    else:
        prPurple("password don't match")
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
        prYellow('sorry, could not verify you')
        exit()
    else:
        print("password don't match")
        print('you have ' + str(3-int(i)) + ' tries left')
    while i < 4:
        i += 1
        _ask_Verification(i)
    
        
_ask_Verification(1)