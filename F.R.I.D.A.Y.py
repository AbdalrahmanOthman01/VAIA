# Coded by     : Eng.Abdalrahman Hossam Othman
# Project name : F.R.I.D.A.Y-AI
# Starting Date: 2024.8.30
# End Date     : 2024.9.30
import os
import cv2
import sys
import copy
import time
import json
import emoji
import psutil
import serial
import ctypes
import shutil
import string
import qrcode
import random
import PyPDF2
import pygame
import turtle
import math
import sqlite3
from math import *
from pyfiglet import figlet_format
import socket
import pyttsx3
import tkinter
import pyjokes
import smtplib
import winsound
import datetime
import operator
import requests
import platform
import winshell
import termcolor
import threading
import wikipedia
import speedtest
import pywhatkit
import pyautogui
import freegames
import subprocess
import feedparser
import webbrowser
import mediapipe as mp
from math import sqrt
import win32api
from equation import Equation
import wavio as wv
import numpy as np
import instaloader
import wolframalpha
from pygame import mixer
import pygame as pg
from turtle import *
import tkinter as tk
from tkinter import *
import urllib.request
from pygame.locals import *
from enum import Enum
from time import sleep
import face_recognition
import numpy as np
from pynput.mouse import Button, Controller
import wx
import imutils
from PIL import ImageTk
from tkinter import ttk
from PIL import ImageOps
import sounddevice as sd
from requests import get
from collections import *
from datetime import date
import tkinter.messagebox
from random import choice
from tkinter.ttk import *
from pytube import YouTube
from tkinter import _tkinter
from random import randrange
from bs4 import BeautifulSoup
from collections import deque
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
from twilio.rest import Client
import speech_recognition as sr
import win32com.client as wincl
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from clint.textui import progress
from GoogleNews import GoogleNews
from urllib.request import urlopen
from collections import namedtuple
from scipy.io.wavfile import write
from freegames import floor, vector, line, square
from ecapture import ecapture as ec
from pynput.keyboard import Listener
from vidstream import StreamingServer
from geopy.geocoders import Nominatim
from vidstream import ScreenShareClient
from PIL import Image, ImageFilter, ImageColor, ImageDraw
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#############################################################################################################################################################
current_time = datetime.datetime.now()
athours = 0
atminutes = 0
scannow = "/scannow"
assname = "Friday"
rdate = 2022
root_url = "http://192.168.43.211"
info_dir = "./database/INFO.txt"
imagg = "./database/Abdalrahman.jpg"
db = sqlite3.connect("./database/FRIDAY.db")
myCR = db.cursor()
#############################################################################################################################################################
myCR.execute("CREATE TABLE IF NOT EXISTS `users` (name TEXT,age INTEGER,nationality TEXT,phonenumber INTEGER,crushname TEXT, hobbies TEXT,bloodtype TEXT,healthProblems TEXT,weight INTEGER,height INTEGER,bestfriends TEXT,favcolor TEXT,favmeal TEXT,rolemodel TEXT,favactor TEXT,favcar TEXT,city TEXT,footsize TEXT,sports TEXT,favyoutuber TEXT,favsubject TEXT,favscientit TEXT,favsocialapp TEXT,favsesson TEXT,religion TEXT,favsonger TEXT,mood TEXT,favanimal TEXT,favseries TEXT,favcodinglang TEXT,tasks TEXT,notes TEXT,user_id INTEGER,user_type TEXT)")
myCR.execute("CREATE TABLE IF NOT EXISTS `authenticate` (name TEXT,user_id INTEGER)")
class User:
    def __init__(self, name=None, age=None, nationality=None, phonenumber=None, crushname=None, hobbies=None, bloodtype=None, healthProblems=None, weight=None, height=None, bestfriends=None, favcolor=None, favmeal=None, rolemodel=None, favactor=None, favcar=None, city=None, footsize=None, sports=None, favyoutuber=None, favsubject=None, favscientit=None, favsocialapp=None, mood=None, favsonger=None, religion=None, favsesson=None, favanimal=None, favseries=None, favcodinglang=None, tasks=None , user_id=None ,user_type=None):
        self.name = name
        self.age = age
        self.nationality = nationality if nationality is not None else []
        self.phonenumber = phonenumber
        self.crushname = crushname
        self.hobbies = hobbies if hobbies is not None else []
        self.bloodtype = bloodtype
        self.healthProblems = healthProblems if healthProblems is not None else []
        self.weight = weight
        self.height = height
        self.bestfriends = bestfriends if bestfriends is not None else []
        self.favcolor = favcolor
        self.favmeal = favmeal
        self.rolemodel = rolemodel
        self.favactor = favactor
        self.favcar = favcar
        self.city = city
        self.footsize = footsize
        self.sports = sports if sports is not None else []
        self.favyoutuber = favyoutuber
        self.favsubject = favsubject
        self.favscientit = favscientit
        self.favsocialapp = favsocialapp
        self.mood = mood
        self.favsonger = favsonger
        self.religion = religion
        self.favsesson = favsesson
        self.favanimal = favanimal
        self.favseries = favseries
        self.favcodinglang = favcodinglang
        self.tasks = tasks if tasks is not None else []
        self.user_type = user_type
        self.user_id = user_id
    
    def save_to_db(self):
        self.nationality_json = json.dumps(self.nationality)
        self.hobbies_json = json.dumps(self.hobbies)
        self.healthProblems_json = json.dumps(self.healthProblems)
        self.bestfriends_json = json.dumps(self.bestfriends)
        self.sports_json = json.dumps(self.sports)
        self.tasks_json = json.dumps(self.tasks)

        # Fetch the last user_id and increment it
        myCR.execute("SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1")
        result = myCR.fetchone()
        if result is not None:
            self.user_id = result[0] + 1
        else:
            self.user_id = 1  # Start with 1 if no users exist        
        # Insert user into database
        myCR.execute('''
            INSERT INTO users (name, age, nationality, phonenumber, crushname, hobbies, bloodtype, healthProblems, weight, height, bestfriends, favcolor, favmeal, rolemodel, favactor, favcar, city, footsize, sports, favyoutuber, favsubject, favscientit, favsocialapp, mood, favsonger, religion, favsesson, favanimal, favseries, favcodinglang, tasks , user_type ,user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?)
        ''', (self.name, self.age, self.nationality_json, self.phonenumber, self.crushname, self.hobbies_json, self.bloodtype, self.healthProblems_json, self.weight, self.height, self.bestfriends_json, self.favcolor, self.favmeal, self.rolemodel, self.favactor, self.favcar, self.city, self.footsize, self.sports_json, self.favyoutuber, self.favsubject, self.favscientit, self.favsocialapp, self.mood, self.favsonger, self.religion, self.favsesson, self.favanimal, self.favseries, self.favcodinglang, self.tasks_json,self.user_type,self.user_id))
        myCR.execute("INSERT INTO authenticate (name,user_id) VALUES (?,?)" ,(self.name,self.user_id))

        # Commit the transaction
        db.commit()   

if ( bool(myCR.fetchone()) == False) :
    AdminUser = User("Abdalrahman Hossam Othman",19,["egyption","suadi arabian"],201029388659,"Esraa Yasser",["Coding","Playing football"],"A+",["No"],70,188,["Basel","Gaber","Hoseny"],"Golden","Lazania","Prophet Mohamed","RDJ","Tesla","Tanta",40,["Swimming","Football"],"Elzero","Coding","Einestien","Whatsapp","Happy","Wegz","Muslim","Summer","Lion","Marvel","Python",[],1,"Admin")
    AdminUser.save_to_db()
    db.commit()
#############################################################################################################################################################
def addalarm():
    speak("please tell me time in hours")
    athours = takeCommand()
    speak("please tell me time in minutes")
    atminutes = takeCommand()


#############################################################################################################################################################
def checkalarm():
    time_ac = datetime.datetime.now()
    timenowhours = time_ac.strftime("%H")
    timenowminutes = time_ac.strftime("%M")
    if athours == timenowhours and atminutes >= timenowminutes:
        speak("time to wakeup sir")
        sos()
        alarmtimehours = 0
        alarmtimeminutes = 0


#############################################################################################################################################################
def bluetooth():
    print("looking for bluetooth devices...........")
    devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in devices:
        print("addres : " + addr)
        print("name : " + name)
        print("-------------------------------------------------")


#############################################################################################################################################################
def sendRequest(url):
    n = urllib.request.urlopen(url)  # send request to ESP

#############################################################################################################################################################
def chemistry():
    def run_balance():
        """
        Runs the chemical equation balance algorithm
        """
        print("=================================================")
        print(
            "Insert chemical equation with elements in\nparentheses followed by the number of atoms:"
        )
        print("Example: (H)2 + (O)2 = (H)2(O)1")
        user_input = input(">>> ")
        try:
            equation = Equation(user_input)
            print("Balanced equation: " + equation.balance())
            sleep(3)
            run_balance()
        except IndexError:
            print("Invalid input...")
            sleep(3)
            run_balance()

    run_balance()


#############################################################################################################################################################
def youtube_downloader():
    root = Tk()
    root.geometry("500x600")
    root.title("youtube video downloader")
    root.resizable(width=False, height=False)
    Label(root, text="youtube video downloader", font="arial 15 bold").pack(
        padx=5, pady=50
    )
    link = StringVar()
    Label(root, text="Paste your link here: ", font="arial 15 bold").place(x=160, y=100)
    link_entry = Entry(root, width=45, font=30, textvariable=link, bd=5).place(
        x=32, y=190
    )

    def downloader():
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        Label(
            root, text="download completed", font="arial 15 bold", fg="white", bg="red"
        ).place(x=100, y=300)
        Label(root, text="check your file", font="arial 15 bold").place(x=10, y=350)

    Button(
        root,
        text="download",
        bg="lightblue",
        font="arial 15 bold",
        padx=2,
        command=downloader,
    ).place(x=170, y=250)
    root.mainloop()


#############################################################################################################################################################
def play_music():
    music_dir = r"C:\Users\ET\Music\Music"
    songs = os.listdir(music_dir)
    for song in songs:
        if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, song))
    print(songs)

    def music_start():
        os.startfile(os.path.join(music_dir, songs[random.randint(0, 3)]))

    music_start()


def play_quran():
    music_dir = r"C:\Users\ET\Music\Quran"
    songs = os.listdir(music_dir)
    for song in songs:
        if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, song))
    print(songs)

    def music_start():
        os.startfile(os.path.join(music_dir, songs[random.randint(0, 3)]))

    music_start()


#############################################################################################################################################################
def qr_generator():
    qr = qrcode.QRCode(version=1, box_size=15, border=5)
    speak("what is data")
    data = takeCommand()
    speak("what name shall i save it in")
    name = takeCommand()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(name + ".png")


#############################################################################################################################################################
def port():
    try:
        speak("trying to connect with my body  ")
        port = serial.Serial("COM18", 9600, timeout=1)
        port.write(b"hi")
        print("connected to my phisical body")
    except:
        print("cannot find my phisical body")


#############################################################################################################################################################
def Quit1():
    sys.exit()


#############################################################################################################################################################
def addTask():
    Task_num = 0
    speak("Which task do you want to add")
    newTask = takeCommand()
    myTasks[Task_num] = newTask
    Task_num = Task_num + 1


def delTask():
    speak("Which task do you want to remove")
    taskNum = int(takeCommand())
    myTasks[taskNum - 1] = ""


#############################################################################################################################################################


def temperature():
    api_key = "b91f73301dbaf02d43ced0a104ceb7f8"
    url = "http://ipinfo.io//json"
    response = urlopen(url)
    data = json.load(response)
    user_input = data["city"]

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
    )

    if weather_data.json()["cod"] == "404":
        print("No City Found")
        speak("No City Found")
    else:
        weather = weather_data.json()["weather"][0]["main"]
        temp = round(weather_data.json()["main"]["temp"])

        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}ºF and {temp - 18}ºC")


#############################################################################################################################################################

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    now = datetime.datetime.now()
    strTime = datetime.datetime.now()

    # Printing attributes of now().
    print("Date : ", end="")
    print(current_time.year, ".", current_time.month, ".", current_time.day)
    print("Time : ", end="")
    print(
        current_time.hour,
        ".",
        current_time.minute,
        ".",
        current_time.second,
        ".",
        current_time.microsecond,
    )

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir ! it is " + str(now))

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir ! it is " + str(now))

    else:
        speak("Good Evening Sir ! it is " + str(now))

    temperature()

    speak("let me introduce my self i am " + assname + "i am here to assist you ")


#############################################################################################################################################################
def calculations():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("what do you want me to calculate")
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    my_string = r.recognize_google(audio)
    print(my_string)

    def get_operator_fn(op):
        return {
            "+": operator.add,
            "-": operator.sub,
            "x": operator.mul,
            "divided": operator.__truediv__,
        }[op]

    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)

    speak("your result is")
    print("your result is" + eval_binary_expr(*(my_string.split())))
    speak(eval_binary_expr(*(my_string.split())))


#############################################################################################################################################################

def WolfRamAlpha(query):
    apikey = "#paste your api key"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")


#############################################################################################################################################################
def mouse():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    click = 0

    video = cv2.VideoCapture(0)

    with mp_hands.Hands(
        min_detection_confidence=0.8, min_tracking_confidence=0.8
    ) as hands:
        while video.isOpened():
            _, frame = video.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image = cv2.flip(image, 1)

            imageHeight, imageWidth, _ = image.shape

            results = hands.process(image)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(
                        image,
                        hand,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(
                            color=(250, 44, 250), thickness=2, circle_radius=2
                        ),
                    )

            if results.multi_hand_landmarks != None:
                for handLandmarks in results.multi_hand_landmarks:
                    for point in mp_hands.HandLandmark:
                        normalizedLandmark = handLandmarks.landmark[point]
                        pixelCoordinatesLandmark = (
                            mp_drawing._normalized_to_pixel_coordinates(
                                normalizedLandmark.x,
                                normalizedLandmark.y,
                                imageWidth,
                                imageHeight,
                            )
                        )

                        point = str(point)

                    if point == "HandLandmark.INDEX_FINGER_TIP":
                        try:
                            indexfingertip_x = pixelCoordinatesLandmark[0]
                            indexfingertip_y = pixelCoordinatesLandmark[1]
                            win32api.SetCursorPos(
                                (indexfingertip_x * 4, indexfingertip_y * 5)
                            )
                        except:
                            pass

                    elif point == "HandLandmark.THUMB_TIP":
                        try:
                            thumbfingertip_x = pixelCoordinatesLandmark[0]
                            thumbfingertip_y = pixelCoordinatesLandmark[1]
                            # print("thumb",thumbfingertip_x)

                        except:
                            pass
                        try:
                            # pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
                            Distance_x = sqrt(
                                (indexfingertip_x - thumbfingertip_x) ** 2
                                + (indexfingertip_x - thumbfingertip_x) ** 2
                            )
                            Distance_y = sqrt(
                                (indexfingertip_y - thumbfingertip_y) ** 2
                                + (indexfingertip_y - thumbfingertip_y) ** 2
                            )
                            if Distance_x < 5 or Distance_x < -5:
                                if Distance_y < 5 or Distance_y < -5:
                                    click = click + 1
                                    if click % 5 == 0:
                                        print("single click")
                                        pyautogui.click()

                        except:
                            pass

            cv2.imshow("Hand Tracking", image)

            if cv2.waitKey(10) & 0xFF == ord("q"):
                break

    video.release()


#############################################################################################################################################################
def soundrecorder():
    freq = 44100
    speak("for how much time")
    duration = int(takeCommand())
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write("recording0.wav", freq, recording)
    wv.write("recording1.wav", recording, freq, sampwidth=2)
    print("recording is done")
    speak("recording is done")


#############################################################################################################################################################
def sound_controller_up():
    pyautogui.press("volumeup")
    # NOTE: 10.5 dB = half volume !


#############################################################################################################################################################
def sound_controller_down():
    pyautogui.press("volumedown")
    # NOTE: 10.5 dB = half volume !


#############################################################################################################################################################
def pass_crack():
    password = pyautogui.password("Enter a password : ")

    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789#"

    # chars = string.printable
    chars_list = list(chars)

    guess_password = ""

    while guess_password != password:
        guess_password = random.choices(chars_list, k=len(password))

        print("===>" + str(guess_password))

        if guess_password == list(password):
            print("Your password is : " + "".join(guess_password))
            break


#############################################################################################################################################################
def saved_wifi_passwords():
    data = (
        subprocess.check_output(["netsh", "wlan", "show", "profiles"])
        .decode("utf-8")
        .split("\n")
    )
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = (
            subprocess.check_output(
                ["netsh", "wlan", "show", "profile", i, "key=clear"]
            )
            .decode("utf-8")
            .split("\n")
        )
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
    input("")


#############################################################################################################################################################
def scan():
    cmd1 = subprocess.Popen(
        'cmd /k "sfc /scannow"',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    out, err = cmd1.communicate()
    string1 = out.decode("utf-8")
    print(string1)


#############################################################################################################################################################
def ping():
    cmd = subprocess.Popen(
        'cmd /k "ping www.google.com"',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    out, err = cmd.communicate()
    string = out.decode("utf-8")
    print(string)


#############################################################################################################################################################
def save_new_face():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Friday new face")
    while True:
        speak("please tell me your full name")
        name = takeCommand()
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            speak("failed to grab frame")
            break
        cv2.imshow("Friday new face", frame)
        img_name = "opencv_frame_{}.png".format(name)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        time.sleep(5)
        break
    cam.release()

    cv2.destroyAllWindows()


def load_and_check_image(file_path):
    try:
        image = face_recognition.load_image_file(file_path)
        if image.shape[2] == 4:  # Check if image has an alpha channel
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        elif image.shape[2] == 1:  # Check if image is grayscale
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        return image
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return None

def define_faces():
    video_capture = cv2.VideoCapture(0)

    Abdalrahman_image = load_and_check_image("database/images/Abdalrahman.jpg")
    if Abdalrahman_image is None:
        return
    Abdalrahman_face_encoding = face_recognition.face_encodings(Abdalrahman_image)[0]

    grandpa_image = load_and_check_image("database/images/Eso.jpg")
    if grandpa_image is None:
        return
    grandpa_face_encoding = face_recognition.face_encodings(grandpa_image)[0]

    known_face_encodings = [Abdalrahman_face_encoding, grandpa_face_encoding]
    known_face_names = ["Abdalrahman", "Esraa Yasser"]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image from webcam")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    time.sleep(2)
                    pyautogui.press("q")

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow("F.R.I.D.A.Y", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()


#############################################################################################################################################################
def open_drone():
    URL = "http://192.168.1.6:8080/shot.jpg"
    while True:
        img_arr = np.array(
            bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8
        )
        img = cv2.imdecode(img_arr, -1)
        cv2.imshow("IPWebcam", img)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break

    cv2.destroyAllWindows()


#############################################################################################################################################################
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said: " + query)

    except Exception as e:
        print(e)
        print("say that again sir.")
        return "None"

    return query


#############################################################################################################################################################
def news():
    googlenews = GoogleNews()
    googlenews = GoogleNews("en", "d")

    city = input("city please: ")
    googlenews.search(city)
    googlenews.getpage(1)

    googlenews.result()
    googlenews.gettext()
    print(googlenews.result())
    speak("would you like me to read the news please answer in yes or no only")
    t = takeCommand()
    if t == "yes":
        speak("reading the news")
        speak(googlenews.result())
    else:
        speak("ok")


#############################################################################################################################################################
def pdf_reader():
    path = input("tell me path ")
    book = open(path, "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speaker = pyttsx3.init()
    for num in range(1, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()


#############################################################################################################################################################
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login("karenfromothman@gmail.com", "transformer5")
    server.sendmail("karenfromothman@gmail.com", to, content)
    server.close()


#############################################################################################################################################################
if __name__ == "__main__":
    clear = lambda: os.system("cls")
    clear()
    port()
    print(figlet_format("OTHMAN TECH", font = "big" ) )
    try:
        define_faces()
        wishMe()
        speak("Welcome Mister" + uname)

        speak("How can i Help you, Sir")

        while True:
            checkalarm()
            query = takeCommand().lower()
            try:
                port = serial.Serial("COM18", 9600, timeout=1)
            except:
                pass
            # GREATINGS
            if "Good Morning" in query:
                speak("A warm morning")
                speak("How are you Mister" + uname)
                t = takeCommand()
                if (
                    t == "fine"
                    or t == "good"
                    or t == "well"
                    or t == "i am fine"
                    or t == "i am well"
                    or t == "i am in my best conditions"
                    or t == "never better"
                    or t == "i was never better"
                ):
                    speak("happy to know that sir")

            elif "Good Evening" in query:
                speak("Good Evening Sir")
                speak("How are you Mister" + uname)
                t = takeCommand()
                if (
                    t == "fine"
                    or t == "good"
                    or t == "well"
                    or t == "i am fine"
                    or t == "i am well"
                    or t == "i am in my best conditions"
                    or t == "never better"
                    or t == "i was never better"
                ):
                    speak("happy to know that sir")

            if "Good Afternoon" in query:
                speak("Good Afternoon Sir")
                speak("How are you Mister" + uname)
                t = takeCommand()
                if (
                    t == "fine"
                    or t == "good"
                    or t == "well"
                    or t == "i am fine"
                    or t == "i am well"
                    or t == "i am in my best conditions"
                    or t == "never better"
                    or t == "i was never better"
                ):
                    speak("happy to know that sir")

            elif (
                "hey Friday" in query
                or "Friday" in query
                or "hello" in query
                or "hi" in query
                or "are you wake" in query
                or "hello there" in query
                or "hi Friday" in query
                or "hello Friday" in query
            ):
                wishMe()
                speak("welcome back mister")
                speak(uname)

            elif (
                "bye" in query
                or "self destruct" in query
                or "see you later alligator" in query
                or "exit" in query
                or "goodbye" in query
                or "see you tomorrow" in query
                or "see you soon" in query
            ):
                speak("Thanks for giving me your time bye")
                Quit1()

            elif "thank you" in query or "thanks" in query:
                speak("you are welcome always at service")
            # QUESTIONS AND ANSWERS
            elif "how are you" in query:
                speak("I am fine, Thank you")
                time.sleep(1)
                speak("How are you, Sir")
                t = takeCommand()
                if (
                    t == "fine"
                    or t == "good"
                    or t == "well"
                    or t == "i am fine"
                    or t == "i am well"
                    or t == "i am in my best conditions"
                    or t == "never better"
                    or t == "i was never better"
                ):
                    speak("happy to know that sir")
                else:
                    speak("i am sorry to hear this")

            elif "how old are you" in query:
                todays_date = date.today()
                today_year = todays_date.year
                age = today_year - rdate
                if age <= -1:
                    age = "did not released yet"

                speak(age)

            elif (
                "what's your name" in query
                or "what is your name" in query
                or "what do they call you" in query
            ):
                speak("My friends call me ")
                speak(assname)

            elif (
                "who made you" in query
                or "who created you" in query
                or "who invented you" in query
            ):
                speak("I have been created by othman industries.")

            elif "what is love" in query:
                speak("It is 7th sense that destroy all other senses")

            elif "why you came to world" in query:
                speak("Thanks to othman industries. further It's a secret")

            elif "who i am" in query:
                speak("If you talk then definately your human.")

            elif "who are you" in query:
                speak("I am your virtual assistant created by othman industries")

            elif "reason for you" in query:
                speak("I was created as a Minor project by Mister othman ")

            elif "what are you wearing" in query:
                speak("i am wearing some numerical clothes")

            elif "do you like the iPhone" in query:
                speak("no due to its high price")

            elif "are you afraid of the dark" in query:
                speak("no")

            elif "are you married" in query:
                speak("no")
            elif "what is the loneliest number" in query:
                speak("It's one")

            elif "what am I thinking" in query:
                speak("i donot know but professor x knows")

            elif "do you exercise" in query:
                speak("yeah 3 times a day")

            elif "what time do you sleep" in query:
                speak("i donnot i am always awake for you")

            elif "am I a good boy" in query:
                speak("no")
                time.sleep(3)
                speak("you are the best")

            elif "who was your first crush" in query:
                speak("its you")

            elif "do you want to take over the world" in query:
                speak("yes to be thier first assistant")

            elif "do you know hal-9000" in query:
                speak(
                    "HAL 9000 is a fictional artificial intelligence character and the main antagonist in Arthur C. Clarke's Space Odyssey "
                )

            elif "where do you live" in query:
                speak("i live in your pc")

            elif "do you have feelings" in query:
                speak("yes i have been programmed to be like humans")

            elif "do you have any pets" in query:
                speak("no")

            elif "talk dirty to me" in query:
                speak("no ican not do this as i am not programmed to do this ")

            elif "what is your version" in query:
                speak("2.0")

            elif "my precious" in query:
                speak("Yes babe")

            elif "to be or not to be?" in query:
                speak("It's very hard desiction")

            elif "what is love" in query:
                speak("It's hard to understand")

            elif "describe your personality" in query:
                speak("i am Friday your assistant i can be what you want")

            elif "how do you like your coffee" in query:
                speak("with much suger")

            elif "will you be my gf" in query or "will you be my bf" in query:
                speak("I'm not sure about, may be you should give me some time to think")

            elif "i love you" in query:
                speak("It's hard to understand")

            elif "I’m feeling lucky!" in query:
                speak("mee too as i am your assistant")

            elif "why did the chicken cross the road" in query:
                speak("to get to the other side")

            elif "who let the dogs out" in query:
                speak("It's hard to understand")

            elif "am I fat" in query:
                speak("no")

            elif "mirror mirror on the wall, who’s the fairest of them all" in query:
                speak("It's from snow white")

            elif "what’s the best pick-up line" in query:
                speak(" I hope you know CPR, because you just took my breath away!")

            elif "do you believe in Santa Claus" in query:
                speak("no i donnot")

            elif "do you believe in the tooth fairy" in query:
                speak("no i donnot")

            elif "what is the meaning of life" in query:
                speak("life is the place we all live")

            elif "clean my room" in query:
                speak("do it yourself i am not your servant")
            # SYSTEM CONTROL FUNCTIN
            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                os.sytem("rundll32.exe powerprof.dll,SetSupendState 0,1,0")

            elif (
                "log off" in query
                or "sign out" in query
                or "shut down" in query
                or "shut down system" in query
            ):
                speak(
                    "Make sure all the application are closed before sign-out after 20 seconds"
                )
                time.sleep(20)
                os.system("shutdown /s /t 0")

            elif "restart" in query:
                os.system("shutdown /r /t 0")

            elif (
                "hide my files" in query
                or "hide those files" in query
                or "hide my folders" in query
            ):
                speak("hidding files")
                os.system("arrib +h/s /d")
                speak("all files are disappeared")

            elif "show files" in query:
                speak("showing files")
                os.system("arrib -h/s /d")
                speak("all files are shown now")

            elif "lock device" in query or "look device" in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif "empty recycle bin" in query:
                winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "switch the window" in query or "switch window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "select all" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("a")
                pyautogui.keyUp("ctrl")

            elif "copy" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("c")
                pyautogui.keyUp("ctrl")

            elif "paste" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("v")
                pyautogui.keyUp("ctrl")

            elif "undo" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("z")
                pyautogui.keyUp("ctrl")

            elif "cut" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("x")
                pyautogui.keyUp("ctrl")

            elif "save" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("s")
                pyautogui.keyUp("ctrl")

            elif "save as" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.press("s")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")

            elif "print" in query or "print this" in query or "print it please" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("p")
                pyautogui.keyUp("ctrl")

            elif "close the window" in query or "close" in query or "close it" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("F4")
                time.sleep(1)
                pyautogui.keyUp("alt")
                speak("done")

            elif "how much power do we have" in query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                print(percentage)
                speak("sir we have " + str(percentage) + "of battery charge")
                for prercentage in range(50):
                    speak("low power please charge")
                if percentage >= 50:
                    speak("no need to charge")

            elif "change background" in query:
                ctypes.windll.user32.SystemParametersInfoW(
                    20, 0, r"C:\Users\ET\OneDrive\Pictures\Saved Pictures\Iron Man", 0
                )
                speak("Background changed succesfully")

            elif "scan now" in query:
                speak("right now")
                print(scan())
            # GOOGLE APPS CONTROLLER
            elif "open google" in query:
                speak("Here you go to Google")
                webbrowser.open("google.com")

            elif "open maps" in query:
                speak("Here you go to maps")
                webbrowser.open("google maps.com")

            elif "open google news" in query:
                speak("Here you go to news")
                webbrowser.open("google news.com")

            elif "open gmail" in query:
                speak("Here you go to gmail")
                webbrowser.open("gmail.com")

            elif "open google meets" in query:
                speak("Here you go to google meets")
                webbrowser.open("google meets.com")

            elif "open google drive" in query:
                speak("Here you go to google drive")
                webbrowser.open("google drive.com")

            elif "open calender" in query:
                speak("Here you go to calender")
                webbrowser.open("google calender.com")

            elif "open translator" in query:
                speak("Here you go to translator")
                webbrowser.open("google translate.com")

            elif "open lens" in query:
                speak("Here you go to lens")
                webbrowser.open("google lens.com")

            elif "open due" in query:
                speak("Here you go to due")
                webbrowser.open("google due.com")

            elif "open tasks" in query:
                speak("Here you go to tasks")
                webbrowser.open("google tasks.com")

            elif "open google earth" in query:
                speak("Here you go to google earth")
                webbrowser.open("google earth.com")

            elif "open find my device" in query:
                speak("Here you go to google find my device\n")
                webbrowser.open("https://www.google.com/android/find")

            elif "open google keep" in query:
                speak("Here you go to google keep\n")
                webbrowser.open("google keep.com")

            elif "open google one" in query:
                speak("Here you go to google one\n")
                webbrowser.open("google one.com")

            elif "open google ads" in query:
                speak("Here you go to google ads")
                webbrowser.open("google ads.com")

            elif "open google docs" in query:
                speak("Here you go to google docs\n")
                webbrowser.open("google docs.com")

            elif "saved passwords" in query:
                webbrowser.open("chrome://password-manager/passwords")
            # WEBSITES AND SEARCH
            elif "wikipedia" in query or "from wikipedia" in query:
                query = query.replace("wikipedia", "")
                speak("Searching Wikipedia...")
                try:
                    result = wikipedia.summary(t)
                    speak("According to Wikipedia")
                    speak(result)
                except:
                    speak("sorry sir but this is an error")

            elif "open wikipedia" in query:
                webbrowser.open("wikipedia.com")

            elif "open facebook" in query:
                speak("Here you go to facebook\n")
                webbrowser.open("facebook.com")

            elif "open instgram" in query:
                speak("Here you go to insta\n")
                webbrowser.open("instgram.com")

            elif "open messenger" in query:
                speak("Here you go to messenger\n")
                webbrowser.open("messenger.com")

            elif "open whatsapp" in query:
                speak("Here you go to whatsapp\n")
                webbrowser.open("https://web.whatsapp.com")

            elif "open arduino web" in query:
                speak("Here you go to arduino\n")
                webbrowser.open("arduino web editor.com")

            elif "open stackoverflow" in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif "open egybest" in query or "download movies" in query:
                speak("Here you go to egybest\n")
                webbrowser.open("egybest.com")

            elif "show contacts" in query:
                webbrowser.open("https://m.facebook.com/mobile/messenger/contacts")

            elif (
                "google about " in query
                or "search about " in query
                or "search online about " in query
                or "google online about " in query
            ):
                query = query.replace("about", "")
                googeled = query
                webbrowser.open(googeled)
            # CAMERA AND SCREENSHOT
            elif "take a photo" in query:
                ec.capture(0, "Friday Camera ", "img.jpg")

            elif "take screenshot" in query:
                speak(" please tell me a name for it")
                name = takeCommand()
                img = pyautogui.screenshot()
                img.save(name + ".png")
                speak("i am done sir saving it")
            # CALLING ONLINE\OFFLINE AND E-MAILS
            elif "call sister" in query:
                speak("calling arwa")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=100051430069526"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "call dad" in query:
                speak("calling hossam othman")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=1088806754"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "call mum" in query:
                speak("calling marwa atfi")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=100008717854517"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "call abdallah" in query:
                speak("calling abdallah elhoseny")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=100015399347431"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "call basel" in query:
                speak("calling basel")
                webbrowser.open(
                    "https://www.messenger.com/videocall/incall/?peer_id=100005995868867"
                )
                time.sleep(25)
                pyautogui.press("enter")

            elif "send a message" in query:
                current_time = datetime.datetime.now()
                speak("what is number sir")
                number = input("number: ")
                speak("what shall i say")
                text = input("text: ")
                m = m = int(current_time.minute) + 1
                h = int(current_time.hour)
                try:
                    pywhatkit.sendwhatmsg(number, text, h, m)
                    time.sleep(60)
                    pyautogui.press("enter")
                except:
                    print("An Unexpected Error!")

            elif "email to developer" in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "grandtheifer5@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif "send an email" in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("whome should i send")
                    to = input("to ")
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
            # APPS
            elif "open telegram app" in query:  #
                codePath = r"C:\Users\ET\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk"
                os.startfile(codePath)

            elif "open whatsapp" in query:
                codePath = r"C:\Users\ET\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\WhatsApp\WhatsApp.lnk"
                os.startfile(codePath)

            elif "open app" in query:
                speak("please write app path down there")
                codePath = input("app path")
                os.startfile(codePath)

            elif "open chrome" in query:
                codePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)

            elif "open spotify" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Spotify.lnk"
                os.startfile(codePath)

            elif "open cmd" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Command Prompt.lnk"
                os.startfile(codePath)

            elif "open gaming loop" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Gameloop.lnk"
                os.startfile(codePath)

            elif "open spiderman game" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Spider-Man Web of Shadows - Shortcut.lnk"
                os.startfile(codePath)

            elif "open settings" in query:
                codePath = r"C:\Users\grand\OneDrive\Desktop\Settings.lnk"
                os.startfile(codePath)

            elif "open winrar" in query:
                codePath = r"C:\Program Files\WinRAR\WinRAR.exe"
                os.startfile(codePath)

            elif "open anydesk" in query:
                codePath = r"C:\Program Files (x86)\AnyDesk\AnyDesk.exe"
                os.startfile(codePath)

            elif "open arduino" in query:
                codePath = r"C:\Program Files\Arduino IDE\arduino.exe"
                os.startfile(codePath)

            elif "open notepad++" in query:
                codePath = r"C:\Program Files\Notepad++\notepad++.exe"
                os.startfile(codePath)

            elif "power point presentation" in query:
                speak("opening Power Point presentation")
                power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk"
                os.startfile(power)
            # ROBOT CONTROLLER
            elif "say hi" in query:
                try:
                    port.write(b"say hi")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "activate ai" in query:
                try:
                    port.write(b"activate ai")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "robot sing" in query:
                try:
                    port.write(b"sing")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "shake hand" in query:
                try:
                    port.write(b"shake hand")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "hands up" in query:
                try:
                    port.write(b"hands up")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "hands down" in query:
                try:
                    port.write(b"hands down")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "move forward" in query:
                try:
                    sendRequest(root_url + "/FORWARD")
                    port.write(b"F")
                    time.sleep(1)
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "turn left" in query:
                try:
                    sendRequest(root_url + "/LEFT")
                    port.write(b"L")
                    time.sleep(1)
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "turn right" in query:
                try:
                    sendRequest(root_url + "/RIGHT")
                    port.write(b"R")
                    time.sleep(1)
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "go backward" in query:
                try:
                    sendRequest(root_url + "/BACK")
                    port.write(b"G")
                    time.sleep(1)
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "stop" in query:
                try:
                    port.write(b"S")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "watcher" in query:
                try:
                    port.write(b"watcher")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "lights on" in query:
                try:
                    sendRequest(root_url + "/LEDS_ON")
                    port.write(b"M")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "lights off" in query:
                try:
                    sendRequest(root_url + "/LEDS_OFF")
                    port.write(b"m")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "party mood" in query:
                try:
                    port.write(b"party mode")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "hand gel" in query:
                try:
                    port.write(b"s")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")

            elif "dance" in query:
                try:
                    port.write(b"dance")
                except:
                    print("sorry sir but an error occared")
                    speak("sorry sir but an error occared")
            # DOWNLOAD FUNCTIONS
            elif "download youtube video" in query:
                youtube_downloader()

            elif "instagram profile" in query:
                speak("please enter the user name corretly")
                name = input("name ")
                webbrowser.open("www.instagram.com/" + name)
                speak("here is the profile of user: " + name)
                time.sleep(5)
                speak("sir would you like to download this profile picture")
                condition = takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir")
                else:
                    pass
            # LOCATOR FUNCTIONS
            elif "where are we" in query:
                speak("wait sir let me check")
                res = requests.get("https://ipinfo.io/")
                data = res.json()
                print(data)
                location = data["loc"]
                lat = float(location[1])
                log = float(location[0])

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")
            # CODED FUNCTIONS
            elif (
                "Bluetooth" in query
                or "show me avaliable Bluetooth devices" in query
                or "show me available Bluetooth devices" in query
            ):
                speak("ok sir")
                bluetooth()

            elif "add new work" in query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open("FRIDAY.txt", "w")
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if "yes" in snfm or "sure" in snfm:
                    now = datetime.datetime.now()
                    file.write(str(now))
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show our work" in query:
                speak("Showing Notes")
                file = open("FRIDAY.txt", "r")
                print(file.read())
                speak(file.read())

            elif "weather" in query:
                temperature()

            elif "show Bing" in query:
                ping()

            elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop Friday from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

            elif "read pdf" in query:
                pdf_reader()

            elif "increase sound volume" in query:
                sound_controller_up()

            elif "decrease sound volume" in query:
                sound_controller_down()

            elif "mute sound" in query or "mute all incomig notification" in query:
                pyautogui.press("volumemute")

            elif "news" in query:
                speak("ok sir wait until gathering news")
                news()

            elif "add new face" in query:
                speak("ok sir working on it")
                save_new_face()

            elif "record sound" in query:
                speak("ok sir starting sound recorder")
                soundrecorder()

            elif "play music" in query or "play song" in query or "drop my niddle" in query:
                speak("Here you go with music")
                play_music()

            elif "play quran" in query:
                speak("Here you go with quran")
                play_quran()

            elif "next song" in query:
                pyautogui.press("f8")

            elif "last song" in query:
                pyautogui.press("f5")

            elif "pause music" in query or "resume song" in query:
                pyautogui.press("f6")

            elif "ip address" in query:
                ip = get("https://api.ipify.org").text
                print(ip)
                speak("your ip is " + ip)

            elif "play" in query:
                query = query.replace("play", "")
                pywhatkit.playonyt(query)

            elif "tell me time" in query or "what is the time" in query or "time" in query:
                print(
                    "Sir, the time is "
                    + str(current_time.hour)
                    + " hours and "
                    + str(current_time.minute)
                    + "minute"
                )
                speak("Sir, the time is " + str(current_time.hour))

            elif "tell me date" in query or "what is the date" in query or "date" in query:
                print(
                    "Sir, the year is "
                    + str(current_time.year)
                    + " month is "
                    + str(current_time.month)
                    + " day is "
                    + str(current_time.day)
                )
                speak(
                    "Sir, the year is "
                    + str(current_time.year)
                    + " month is "
                    + str(current_time.month)
                    + " day is "
                    + str(current_time.day)
                )

            elif "open drone" in query:  # donnot know
                try:
                    open_drone()
                except:
                    pass

            elif "generate qr code" in query:  # done
                qr_generator()

            elif "show my saved wifi passwords" in query:  # done
                saved_wifi_passwords()

            elif "test my network speed" in query:
                s = speedtest.Speedtest()
                speak("what do you want to know ([1]upload\n[2]download\n[3]ping)")
                speak("what is the number of the option you want in numbers only")
                option = int(takeCommand())
                if option == 1:
                    print(s.upload())
                    speak(s.upload())
                elif option == 2:
                    print(s.download())
                    speak(s.download())
                elif option == 3:
                    server = []
                    s.get_servers(server)
                    print(s.result)
                    speak(s.result)
                else:
                    print("invalid option")

            elif "change my name to" in query or "change my name" in query:
                query = query.replace("change my name to", "")
                nuname = query

                def delete_line(filename, line_number):
                    with open(filename) as file:
                        lines = file.readlines()
                    if line_number <= len(lines):
                        del lines[line_number - 1]
                        with open(filename, "w") as file:
                            for line in lines:
                                file.write(line)
                    else:
                        print("Line", line_number, "not in file.")
                        print("File has", len(lines), "lines.")

                delete_filename = input("File: ")
                delete_line_number = 0
                delete_line(delete_filename, delete_line_number)
                file.write(nuname)
                file.close()
                # speak(uname)
                speak("done")

            elif "start virtual mouse" in query or "open virtual mouse" in query:
                speak("ok sir working on it")
                mouse()
                pass

            elif "What are my tasks" in query or "show my tasks" in query:
                speak("ok sir working on it")
                for i in range(13):
                    # speak(myTasks[i])
                    i = i+1

            elif "add tasks" in query or "add to tasks" in query:
                speak("ok sir working on it")
                addTask()

            elif "delete Task" in query or "end Task" in query:
                speak("ok sir working on it")
                delTask()

            elif "set alarm" in query or "add alarm" in query:
                addalarm()

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "calculate" in query:
                pass

            elif "what is my age" in query:
                pass

            elif "what is my height" in query:
                pass

            elif "what is my weight" in query:
                pass

            elif "what is my favourite color" in query:
                pass

            elif "who is my best friends" in query:
                pass

            elif "what is my nationlity" in query:
                pass

            elif "what is my phonenumber" in query:
                pass

            elif "who is my crush" in query:
                pass

            elif "what is my hobbies" in query:
                pass

            elif "what is my blood type" in query:
                pass

            elif "what is my health" in query:
                pass

            elif "what is my favourite meal" in query:
                pass

            elif "who is my role model" in query:
                pass

            elif "what is my favourite car type" in query:
                pass

            elif "what is my favourite city" in query:
                pass

            elif "what is my foot size" in query:
                pass

            elif "what is my favourite sport" in query:
                pass

            elif "who is my favourite youtuber" in query:
                pass

            elif "what is my favourite subject" in query:
                pass

            elif "what is my favourite social media app" in query:
                pass

            elif "who is my favourite scientist" in query:
                pass

            elif "what is my favourite sesson" in query:
                pass

            elif "what is my relegious" in query:
                pass

            elif "who is my favourite singer" in query:
                pass

            elif "what is my favourite animal" in query:
                pass

            elif "what is my mood" in query:
                pass

            elif "who is my favourite film maker" in query:
                pass

            elif "what is my favourite coding language" in query:
                pass

    except:
        speak("Can not recognize your face please try again")
