#!/usr/bin/env python3
import subprocess
# Install googletrans library
subprocess.check_call(['pip3', 'install', 'googletrans==4.0.0-rc1'])

#
import googletrans

from googletrans import Translator

translator = Translator()

user_input = input("Welcome to our translator. Please select language: EN,RU : \nДобро пожаловать в наш переводчик. Выберите язык: EN,RU: ")

if user_input == "EN":
    user_word = input("Please insert word that you want translate to Russian: ")
    translated = translator.translate(user_word, dest='ru')
    print(translated.text)
elif user_input == "RU":
    user_word = input("Пожалуйста укажите слово которое хотите перевести на Английский: ")
    translated = translator.translate(user_word, dest='en')
    print(translated.text)