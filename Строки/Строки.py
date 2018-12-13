# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 17:33:12 2018

@author: kiril
"""
#Строки

#Задание 1
Name = str(input("Введите имя:"))
Surname = str(input("Введите фамилию:"))
Middle_name = str(input("Введите отчество:"))
print(Name, Surname[0], Middle_name[0])

#Задание 2
 
#Задание 3
y = str(input("Вводи строку!:"))
a = len(y.split())
print(a)

#Задание 4
a = str(input("Введите сообщение:"))
b=int(len(a))
if b > 10:
    x=b-10
    print('Вы написали на', x , 'символов больше')
    
#Задание 5
x = input("Сколько звёзд на небе?")
y = input("Сколько листьев на дереве?")
z = input("Почему в трамвайных поручнях не живут тараканы?")
print(x.isdigit())
print(y.isdigit())
print(z.isalpha())

#Задание 6
b = input("Вводи сюда свои скобки!:")
x = b.count("(")
y = b.count(")")
if x==y:
    print('Ура,все правильно!')
else:
    print('Кол-во скобок открывающих не равно кол-ву скобок закрывающих')

#Задание 7
