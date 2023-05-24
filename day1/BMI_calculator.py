#!/usr/bin/env python3
print("Welcome BMI calculator please insert in below field you gender,age,weight and height")
user_gender = input("Please insert gender: ")
user_age = int(input("Please insert age: "))
user_weight = int(input("Please insert your weight in kq: "))
user_height = int(input("Please insert your height in sm: "))

user_height_to_m = user_height / 100
BMI = user_weight / ( user_height_to_m * user_height_to_m )

#Junior Class
if 18 < user_age <= 24 and BMI < 20:
    print("Underweight")
elif 18 < user_age <= 24 and 20 <= BMI <= 25:
    print('Normal weight')
elif 18 < user_age <= 24 and 25 < BMI <= 30:
    print('Overweight')
elif 18 < user_age <= 24 and 30 < BMI <= 40:
    print('Obesity')
#Middle Class
if 25 <= user_age <=34 and BMI < 21:
    print("Underweight")
elif 25 < user_age <= 34 and 21 <= BMI <= 26:
    print('Normal weight')
elif 25 < user_age <= 34 and 26 < BMI <= 31:
    print('Overweight')
elif 25 < user_age <= 34 and 31 < BMI <= 41:
    print('Obesity')
#Senior Class
if 35 < user_age <= 44 and BMI < 22:
    print("Underweight")
elif 35 < user_age <= 44 and 22 <= BMI <= 27:
    print('Normal weight')
elif 35 < user_age <= 44 and 27 < BMI <= 32:
    print('Overweight')
elif 35 < user_age <= 44 and 32 < BMI <= 42:
    print('Obesity')
#Old Class
if 45 <= user_age <=54 and BMI < 23:
    print("Underweight")
elif 45 < user_age <= 54 and 23 <= BMI <= 28:
    print('Normal weight')
elif 45 < user_age <= 54 and 28 < BMI <= 33:
    print('Overweight')
elif 45 < user_age <= 54 and 33 < BMI <= 43:
    print('Obesity')
#Oldest Class
if 55 <= user_age <= 64 and BMI < 24:
    print("Underweight")
elif 55 < user_age <= 64 and 24 <= BMI <= 29:
    print('Normal weight')
elif 55 < user_age <= 64 and 29 < BMI <= 34:
    print('Overweight')
elif 55 < user_age <= 64 and 34 < BMI <= 44:
    print('Obesity')
#Omenoo
if 64 < user_age and BMI < 25:
    print("Underweight")
elif 64 < user_age and 25 <= BMI <= 30:
    print('Normal weight')
elif 64 < user_age and 30 < BMI <= 35:
    print('Overweight')
elif 64 < user_age and 35 < BMI <= 45:
    print('Obesity')