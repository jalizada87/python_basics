'''
1) Напишите программу, которая просит у пользователя ввода десяти чисел по отдельности, добавляет их в список, 
а после этого сортирует данный список, и печатает его, умножив каждое число на 10
'''

user_input = input("Insert 10 numbers. divide by space: ")

user_input = user_input.split()

for i in range(len(user_input)):
    user_input[i] = int(user_input[i])

user_input.sort()

for j in user_input:
    print(j * 10)