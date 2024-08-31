""" fruits = ["apple", "orange", "pear"]
fruits.append("banana")

print(fruits)

answer = "apple" in fruits
answer1 = "carrot" not in fruits

print(answer1)
"""

import random
import word_list

## word =  words[random.randint(0,len(words) - 1)]
word = random.choice(word_list.words)
name =  input("Введите ваше игровое имя: ")
attempts = int(input("Введите количество попыток за которое вы хотите отгадать слово: "))
print("Я загадал слово, отгадай его.")
for char in word:
    print("*", end="")
print()

letters = []

while attempts > 0:
    victory = True
    letter = input("Введите букву: ")
    letters.append(letter)

    for char in word:
        if char in letters:
            print(char, end="")
        else:
            print("*", end="")
            victory = False
    print()

    if letter not in word:
        attempts = attempts - 1
        print("Ты ошибся! У тебя осталось попыток: " + str(attempts))
    if victory == True:
        print(name + " ты победил!")
        break
if attempts == 0:
    print(name + " ты проиграл!")
    print("Секретное слово было " + word)
