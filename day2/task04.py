'''
4) Напишите программу, которая читает файл внутри которого есть несколько строк, 
а в них - фразы разделенные символом "|", далее записывает эти фразы в новый файл, каждую с отдельной строки, 
с пояснениями в начале, что именно выводим.

В качестве примера во входном файле:

Иван Иванов|ivanov@mail.ru|Password123
Дима Нагиев|superman1993@mail.ru|1993superman
Вася Пупкин|pupok@mail.ru|qwerty12345

а на выходе должен появиться такой файл:

Имя: Иван Иванов
E-mail: ivanov@mail.ru
Пароль: Password123
'''
with open("user_list.txt", "r") as file:
    content = file.read()

with open("new_file.txt", "w") as file:
    new_content = content.split("|")
    for i in new_content:
        if " " in i:
            write_content = file.write(f"Имя: {i}\n")
        if "@" in i:
            write_content = file.write(f"E-mail: {i}\n")
        else:
            write_content = file.write(f"Пароль: {i}\n")