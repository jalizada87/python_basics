'''
2) Напишите программу которая содержит список матерных слов, 
далее открывает какой-либо файл с текстом, заменяет в нем матерные слова на строку "LOL".
записывает результат во второй файл
'''

abuse_words = ["дурак", "дебил", "даун", "плохой"]
changed_word = []
with open("18+.txt", "r") as file:
    content = file.read()

for i in content.split(","):
    if i in abuse_words:
        changed_word.append("LOL")
    else:
        changed_word.append("it's ok")


changed_word = " ".join(changed_word)

with open("changed_word.txt", "w") as file1:
    file1.write(changed_word)