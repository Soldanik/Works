# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:19:54 2018

@author: kiril
"""

Name = input("Как вас зовут?") 
print("Привет, {}".format(Name)) 

#2 Задание 

print('''Ага! 
Я могу управлять этим компьютером! 
Вот только зачем? :'C 
Пойду поищу смысл жизни "__"''') 

#3 Задание 


print("Задайте последовательно 3 числа: ") 
a = int(input("Первое число: ")) 
b = int(input("Второе число: ")) 
c = int(input("Третье число: ")) 
print("Сумма: {}" .format(a + b + c)) 

#4 Задание 


radius = int(input("Радиус: ")) 
x = 3.14 
pi = x 
area = pi * radius **2 
print(area) 

#5 Задание 
Radius = float(input("Введите радиус: ")) 
print(Radius) 


#6 Задание
x = int(input("Школьников было:"))
y = int(input("Яблок было:"))
m = y // x
l = y % x
print(m,l)

#7 Задание
n = int(input("Сколько минут я спал?"))
hours = n % (60 * 24) // 60
minutes = n % 60
print("Так,я спал {} часов и {} минут" .format(hours, minutes))
#8 задание
a=int(input("Введите первое число:"))
b=int(input("Введите второе число:"))
a=a+b
b=a-b
a=a-b
print("Первое число: {} ; Второе число: {};" .format(a,b))
#9 задание
а=float(input("Введите сторону квадрата:"))
p=(a*4)
s=(a**2)
print("Периметр: {}; Площадь: {};" .format(p,s))
#10 задание
print(int("24"*15)**2)
