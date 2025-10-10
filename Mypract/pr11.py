#class person:
from fileinput import filename

#def __init__(self, name, age):
        #self.name = name
        #self.age = age

#per1 = person("Adil", 18)
#per2 = person("Rasul", 16)

#print("per1.Adil, per1.18 лет")
#print("per2.Rasul, per2.16 лет")

#import os
#from fileinput import filename


#def get_words(filename):
    #with open(filename, encoding="utf8") as file:
        #text = file.read()
    #text = text.replace("\n", "")
    #text = text.replace(",","").replace(".", "").replase("?", "").replase("!","")
    #text = text.lower()
    #words = text.split()
    #return words

#def get_words_dict(words):
    #words_dict = dict()

    #for word in words:
        #if word in words_dict:
            #words_dict[word] = words_dict[word] + 1
    #else:
        #words_dict[word] = 1
    #return words_dict


#def main():
    #filename = input("Введите путь к файлу: ")
    #if not os.path.exists(filename):
        #print("Указанный файл не существует")
    #else:
       # words = get_words(filename)
        #words_dict = get_words_dict(words)
        #print(f"Кол-во слов: {len(words)}")
        #print(f"Кол-во уникальных слов: {len(words_dict)}")
       # print("Все использованные слова:")
        #for word in words_dict:
            #print(word.ljust(20), words_dict[word])


#if __name__ == "__main__":


#import random

#filename = input("Введите имя файла или путь к нему: ")

#with open("hello.txt", "w") as file:
    #for _ in range(100):
        #number = random.randint(0, 4)
        #file.write(str(number) + "\n")
    #print("100 случайных чисел добавлены в файл")

filename = input("Введите имя файла: ")

