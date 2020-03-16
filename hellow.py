
# print(10)#int
# print("i am a student")
# print('i\'am a student')
# #comment
# '''
# this is a comment
# '''
# name = 10
# print(name)
# var1 = 10
# var2 = 20
# print(var1+var2)
# result = var1+var2
# print("sum of 20 and 30 /n "+ str(result))
#
# name = 'rahim'
# age = 18
# selary = 25000
# print(name + "is 18 yeas old")
# print(name + "get selary")
# #Boolean
# is_active = True
# print("this accout has been activet")
# is_passive = False
# print("this accout has not activet")
# print(is_active)
#
# #math_matical_operator
# number_of_studenr =5
# print(number_of_studenr)
# number_of_studenr +2
# print(number_of_studenr)
#
# #type_custing
# #type
# #int
# number1 =int(input("Enter a unumber: "))
# number2 =int( input("Enter a unumber: "))
# result = number1+number2
# print(result)
#
# from math import*
# print(floor(3.7))
# #print(cell(3.7))
# print(divmod(10,3))
#
# #Area Calculator
# base = int (input("Enter the base  of the Trangle: "))
# hight = int (input("Enter the hight of the Trangle: "))
# result = .5 *hight*base #1/2* base*high
# print("area ractungaler is",result)

#QUIZ -if/elif
# print("what is your age?")
# age = int(input())
# if age<18:
#     print("you can not drive")
# elif age == 18:
#     print("we will decide")
# else:
#     print("you will be drive ")
#
# int(input("Enter your age"))
#
# if age<18:
#     print("you can't use this site")
#
# elif age==18:
#     print("please try to next time")
#
# else:
#     print("you use this site")
#
#
# items = [int,float, "apu", 3,5,7,38,89,436]
# for item in items:
#     if str (item).isnumeric()and item>6:
#         print(item)

#guess the number!
# a = 18
# for i in  range(1,10):
#     n = int(input("Guess the number:"))
#     if i < 9 or n == 10:
#         if n < a:
#             print("you guessed the wrong numbr")
#             print("please number of remaning guesses:")
#         if n > a:
#             print("you guessed the wrong numbr")
#             print("please number of remaning guesses:")
#
#
#         else:
#             print("Congratulation You Win.!")
#             print("number of gusses took finish:",i)
#             break
# n = 20
# guess=1
# print("Number guesses is limited only 5 times:")
# while(guess <=5):
#    guess = int(input("Guess the number: \n"))
#    if guess <=20:
#        print("you enter please grater number: \n")
#    elif guess >=20:
#        print("you enter please small number: \n")
#    else:
#        print("you win.! \n")
#        print(guess,"no of guess took finished")
#        break
#        print(5-guess, "no of guess took finished")
#        guess = guess + 1
#        if(guess>5):
#            print("game Over")

# n =int(input())
# rose = True
# t_rose= False

# n=int(input("Enter your number:"))
# a=int(input("Enter your boolean number number:"))
# if(bool(a)):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print('*', end="")
#
# else:
#     for i in range(1,n+1):
#         for j in range(1,n+2-i):
#             print('*',end="")
#


# f = open("apu.text","a")
# f.write("Aftab Apu is a good boy \n")
# f.seek(5)
# f.close()

#gloval varibel

# l=10 #Gloval
# def aftab(name):
#     l=5
#     m=8
#     # global l
#     m=l+45
#     print(l,m)
#     print("i have printed")
#     print(f'this is "{name}')
#
# aftab('aftab apu')


# l= 12
# def aftab():
#     x = 20
#     def apu ():
#         global l
#         x = 20
#         print("inside before calling a apu()}",l+4)
#
#     apu()
#
#     print("outside before calling a apu()",x)
# aftab()
#
# def dj(er):
#     print("this is " + er)
#
# dj("aftab")
#
# def fectorial(n):
#
#     """
#
#     :param n: integer
#     :return: n * n-1 * n-2 * n-3......1
#     """
#     fac=1
#     for i in range(n):
#         fac =fac *(i+1)
#         return fac
#     pass
# number = int(input("enter a number :"))
# print(fectorial(number))
#
#
#Area of  Circle:
#
# Pi = 3.14
# radius = float(input(' Please Enter the radius of a circle: '))
# area = Pi * radius * radius
#
# print(" Area Of a Circle",area)

# name= "This is Python Class"

# title[1]='x'

# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name.title().lower().upper())

# first_name = 'Abdul'
# last_name = 'Zabbar'

# name = '    Mr.Rahim    '
#
# print('_' + name.strip() + '_')

# title = 'This is Python Class, and Python is an OOP Language'
# print(title.startswith('This'))
# print(title.endswith('Class'))

# print(title.replace('Python', 'Java'))

# x= 'Bangladesh'
# y= 'India'
# z= 'Nepal'
# print(x + ' | '+ y+ ' | '+ z)
# print(x,y,z, sep = ' | ')

# num1 = 20
# num2 = 30

# print(f"{num1} + {num2} = {num1+num2}")

# title = "Mr. Rahim's age is 60"
# print(title)
#
# person = ("{name}'s age is {age}")
# print(person.format(name='Mr. Karim', age=80))
#
#
# text = "He is a Student"

# print(text[1:6])
# print(text[:6])
# print(text[7:])
# print(text[7:-1])
#
# person ='%s\'s age is %d'
# print(person%('Bill', 50))
#
# a = 20
# b=50
#
# print(a>=b)
# print(a<=b)
# print(a==b)
# print(a!=b)
#
# #MODULE
# import random
# random_number = random.randint(0,1)
# # print(random_number)
# rand = random.random() * 10
# print(rand)

# ss =["google","youtube","facebook","aftab apu"]
# ss=random.choice(ss)
# print(ss)

#Class - Template(later ta likha_ace/liklam add kora)
# Object-(letter er tarikh/element likha made kora)
# class Student:
#     age_of =20
#
#def printdetails(self):#(self hocca oi obj jer kotha bola hocca)
# return f"name is{self.name}.age is {self.age}"
# aftab=Student()
# rohan = Student()
# aftab.name ="aftab"
# aftab.age =21
# rohan.age =22
# print(aftab.printdetails())

# person ='aftab'
# age =44
#
#class Employ:
#     company_name ="TMSS"
#
#     def __init__(self, name,age,selary):
#         self.name=name
#         self.age=age
#         self.selary=selary
#
#     def gretting(self):
#         return f'hey {self.name}\n {self.age} \n {self.selary}'
#
# Rony=Employ('aftab apu',44,2000)
# print(Rony.name)
# print(f'{person},{age}')

# number = 30
# if number <25:
#     print("it is a hot day")
# else:
#     print("it is a cold day")
#
#
# class Data:
#     def __init__(self):
#         self.store=[]
#
#     def append(self,arg):
#         self.store.append(arg)
#
#     def insert(self,index,value):
#         self.store.insert(index,value)
#
# number =Data()
# number.store=[10]
# number.append(1,)
# number.append(5)
# number.insert(0,9)
# print(number.store)

# class Data:
#     age =21
#     _age =90
#     __thim = 88
#public(all over the public)
#protected(protected\public#_protect)
#privet(privet/privecy#_class name__privet)
#
#     def __init__(self ,name,position,selary):
#         self.name=name
#         self.position=position
#         self.selary=selary
#
#     def details(self):
#         return f"hey {self.name} {self.position} {self.selary} {self._age} {self.__thim}"

# user=Data("APU","none", 78)
# print(user.details())
#
# # class Dad:
#     busketball=1
#
# class Son:
#     dance =5
#     def incedent(self):
#         return f'yes im dancer {self.dance} yet no time'
#
# class Grandson:
#     dance = 1
#     def incedent(self):
#         return f'i just dance {self.dance} time'
#
# daddy=Dad()a
# aftab = Son()
# titu =Grandson()
# print(titu.incedent())
#
#
# class Electronic_device:
#     have = 5
#
# class Poket_gadget(Electronic_device):
#     have = 10
#     def indent(self):
#         return f'yes we have a {self.have} Gadget'
#
# class Phone(Poket_gadget):
#     have = 6
#     def indent(self):
#         return  f"we have {self.have} phone "
#
# computer =Electronic_device()
# phone = Poket_gadget()
# tab =Phone()
# print(phone.indent())

# num1 = 50
# num2 =100
#
# max=num1 if num1>num2 else num2
# print(max)


# num1 = 20
# num2 = 30
# num3 = 50
#
# if num1>num2:
#     print(num1)
# else:
#     print(num3)
#     if num1>num2:
#         print(num2)

# marks=49
#
# if marks>=80 and marks<=100:
#     print("A+")
# elif marks >= 70 and marks <= 79:
#           print("A")
# elif marks >= 60 and marks <= 69:
#           print("A-")
# elif marks>=50 and marks<=59:
#           print("B")
# else:
#       print("Fail")
#
# num1 = 20
# num2 = 30
# result_of= 20+30
# print(f"{num1}+{num2} = {num1+num2}")
#
# name ="i am programmer.i like to do code in java.\n " \
#       "java is an oop language.java is also a case sensitive language.\n" \
#       "Replace the java in to"
# int(input(name.replace('java','python')))

# numbers =[3,4,5,7,8,8]
# numbers2=numbers.copy()
# numbers.append(10)
# print(numbers)

# numbers =[4,5,6,9]
# unique =[]
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
#         print(unique)

# secret_number=9
# guess_limit =3
# guess_count=0
#
# while guess_count<=guess_limit:
#     guess =int(input('guess:'))
#     guess_count +=1
#     if guess == secret_number:
#         print('you win')
#         break
#     else:
#         print('you will fail')

# is_hot =False
# is_cold=True
#
# if is_hot:
#     print('it is a hot day')
#     print('Drink some water')
# elif is_cold:
#     print('it is a cold day')
#     print('put on warm cloth')
# else:
#     print('its a lovely day')
#     print('enjoy your day')

# weight=int(input('weight:'))
# unit= input('(L) or (K):')
# if unit.upper()=='L':
#     convert =weight * 0.45
#     print(convert)
# else:
#     convert =weight / 0.45
#     print(convert)

# weight =int(input('Weight:'))
# unit =input('(L)ls or (K)g:')
# if unit.upper()=='L':
#     convert= weight * 0.45
#     print(f'your lbs={convert} killos')
#
# else:
#     convert=weight / 0.45
#     print(f'your K={convert} pounds')
#

# khana =['ruti','porota','alu-puri']
#
# for item in khana:
#     if item =="Tea":
#         break
# else:
#     print("this for loop end properly")

# try:
#     f =open('dose.text')
#
# except Exception as e:
#     print(e)
#     print('it is a suffer')
# else:
#     print("it is true")
#
# Coroutines
# def searcher():
#     import time
#     book="This is my new favourite book"
#     time.sleep(4)
#
#
#     while True:
#         text =(yield)
#         if  text in book:
#             print("your text in the book")
#         else:
#             print('Text is not in the book')
# search = searcher()
# next(search)
# search.close()

# import os
# print(os.getcwd())


# import random
# for item in range(3):
#     print(random.random())

# import random
# name =['apu','anik','asru','none']
# leader=random.choice(name)
# print(leader)
#
#
# import random
# class Student:
#     def Roll(self):
#         frist=random.randint(1,8)
#         secound=random.randint(1,8)
#         return frist,secound
# stu=Student()
# print(stu.Roll())
#
#
# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def talk(self):
#         print(f'Hi im {self.name}')
# Apu=Person("Aftab Apu")
# Apu.talk()
#
# import json
# data='{"var1":"apu" , "var2": 66}'
# parsed=json.loads(data)
# print(parsed['var2'])

# i=0
# num = int(input('Enter number:'))
# while i<=num:
#     i = i+2
#     print(i)


# i=1
# j=1
# while i<=5:
#     print('i am a', end= '')
#     j=1
#
#     while j<=4:
#         print('developer', end= '')
#
#         j =j+1
#     i = i+1
#     print()
#
# sum =1
# num = int(input('number:'))
# for i in range(1,num+1,1):
#     sum=num*5
#     print(sum)

#
# i =2
# sum =0
# num =int(input("Enter number:"))
# while i<=num:
#     sum=sum+i
#     i=i+2
# print("Even number",sum)


# i =2
# sum =0
# num =int(input("Enter number:"))
# while i<num:
#     if (i%2)==0:
#      sum=sum+i
#     i=i+2
# print(sum)


# nun =int(input('number:'))
# if nun>0:
#     print("This is a posative value",nun)
# elif nun<0:
#     print("This is a Negative value",nun)
# else:
#     print("Output is zero")



# 7,11,13,19,23
# num = 7
# for i in range (2,num):
#     if num%i==0:
#         print("not prim")
#
# else:print('prime')

# n=4
# for i in range(n):
#     print("#" , end= "")
#     for j in range(n-i):
#         print("#" , end="")
#         print()



# fruits =['banana', ' ampple']
# print('banana' in fruits)
# print(fruits +['mango'])
# fruits.append(34)
# fruits.insert(1,'tttt')
# fruits.extend(['malta','orange'])
# fruits [0] 'ooop'
# print(fruits)


# fruits =['banana', ' apple']
# fruits [0]='ttt'
# print(fruits)


# text=input("enter a digit:")
# numer_of_latter =0
# numer_of_word =0
# numer_of_digit =0
#
# for x in text:
#     if x>='a' and x<='z':
#         numer_of_latter=+1
#     elif:x >= 0 and x <= 9:
#         numer_of_word = +1
#     elif:
#         x >= 'a' and x <= 'z':
#             numer_of_digit = +1
#

# t1 =1,2,3,4
# t2 =1,3,3,4
#
# if t1==t2:
#     print('oky')
# else:
#     print('ont oky')

#list=[mutable]
#tupple=(immutable,fast)



# count = 0
# while count <= 5:
#     print('1' * count)
#     count = count + 1
# print('Done')




# n= 5
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(j, end= ' ')
#     print(" ")

#
# stoke =50
# n =int(input('enter your number:'))
# while n<=stoke:
#     print('Product on Stoke')
#     break
# else:
#     n =n>stoke
#     print('Product have no stoke,thank you')

#Function
# def Function_name():
#     print('welcome to function')
# Function_name()
#
# def student(name,reg_no):
#     print(name)
#     print(reg_no)
#
# student('Aftab',218971)


#varible_length_argument

# def add(a,*b):
#     c=a
#     for i in b:
#         c=c+i
#         return c
# result=add(1,4,5,7,8,8,9)
# print(result)

# tupple we used * and dictionary used **

#
# num = 20
# def add(num):
#     num =num +20
#     return num
# print(add(num))
# print(num)

#lambda
# def squar(num):
#     num=num*num
#     print(num)
# squar(2)
#
# squar=lambda num: \
#     num*num
# print(squar(2))


# def is_even(n):
#     return n%2
# even_list =[1,2,3,4,5,6]
# result = even_list
#
# number_list =[1,2,3,4,5,6]
# even_list=list(filter(lambda n: n%2==0, number_list))
# print(even_list)

# Map
# def get_double(n):
#     return  n * 2
# double_list = list(map(lambda n: n*2,number_list))
# print(double_list)

# Reduce
# from functools import reduce
# def add(a,b):
#     sum =a+b
#     return sum
# result =reduce(lambda a,b: a+b, number_list)
# print(result)

# decorate
# def div(a,b):
#     if a<b:
#         a,b=b,a
#     print(a/b)
# div(2,10)
#
#
# def decorator_fun(fun):
#     def inner(a,b):
#         if a<b:
#             a,b =b,a
#             return fun(a,b)
#         return inner
# div1 = decorator_fun(div)
# div2 = decorator_fun(div)
# div(2,4)
# div(4,16)
#
# number_list =[1,3,4,5,6]
# result =list(map(lambda n: n*2, number_list))
# print(result)
#
# result = [n*2 for n in number_list]
# print(result)
#
# result =list(filter(lambda n: n%2==0, number_list))
# print(result)
#
# even_result = [n for n in number_list if n%2==0]
# print(even_result)

# # dict comprehensive
# key_list= ['mango', 'banana','apple']
# value_list =[10,0,30]
# key_value_list ={}
#
# for i in range(len(key_list)):
#     key_value_list[key_list[i]]=value_list[i]
#     print(key_value_list)

# key_value_list = {key_list[i]: value_list[i] for i in range(len(key_list))}
# print(key_value_list)
#
# Fibonacci_number
# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c= a+b
#         # if c<=100:
#         a=b
#         b=c
#         print(c)
# fib(10)

# def fac(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
#
#     return f
#
# result =fac(5)
# print(result)


# class Animal:
#     name=""
#     colour=""
#
# def set_value(self,name,color):
#     name="CAT"
#     color='white'
#     self.name{name}
#     self.color{color}
#

#
# class Triangle:
#     def __init__(self, base,hight):
#        self.base= base
#        self.hight= hight
#
#     def dislay(self):
#         area = 0.5 * self.base * self.hight
#         print(area)
#
# obj1= Triangle(20,30)
# obj2= Triangle(10,20)
# obj1.dislay()
# obj2.dislay()

# class Animal:
#     age = 8
#     def __init__(self):
#         self.name ="mini"
#         self.color ='white'
#
# c1 = Animal()
# c2 =Animal()
# Animal()
# c2.color ='black'
# print(c1.name, c1.age)
# print(c2.color)


class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3


    def avg(self):
        result =(self.m1 + self.m2 + self.m3)/3
        print(result)

s1= Student(34,45)
s2= Student(67,89)
s3= Student(66,89)
s1.avg()
s2.avg()
s3.avg()

#inner class
















