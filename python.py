print("hellow world")
print("0-----------------")
print("||||||")
print('*' * 10)
price = 10
print (price)


birth_year = input ('Birth year: ')
print (type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

weight_lbs =input('weight (lbs):' )
weight_lbs =int(weight_lbs) * 0.45
print (weight_lbs)


course = 'python for "beginner" '
print (course [:5])
name ='Aftab apu'
print (name[1:-1])

first = 'aftab'
last = 'apu'
message = 'first +  ['+ last +'] is a coder'
msg = f'{first} [{last}] is a codder '
print (msg)

course = 'python for beginners'
print (len(course))
course = 'python for  beginner'
print (course.upper())
print (course.lower())
course = 'python for  beginner'
print(course.replace('beginner','aftab apu Absolute beginner'))

print (10**3)
x = 10
x -= 3
print(x)
x=(2+3) * 10 * 5 - 2
print(x)
import math
print (math.floor(2.9))
#Boolean
is_hot = False
is_cold = True

if is_hot:
    print("it is a hot day")
    print("drink plenty water")
elif is_cold:
    print("it is a cold day")
    print("were warm cloth")
else:
    print("it is a lovely day")
print("Enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
    print(f"down payment: ${down_payment}")

temperature = 35
if temperature > 30:
    print('it is a hot day')
else:
    print('it is not hot day')

name = "aftab apu"
if len(name) < 3:
    print("Name must be at last 3 character")
elif len(name) > 50:
    print("Name must be of 50 character")
else:
    print("Name looks good")

weight =int(input('weight:'))
unit = input('(L) bs or (K)g:')
if unit.upper() =='L':
   converted = weight * 0.45
   print(f'you are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'you are {converted} pounds')

guess_count = 1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count = guess_count + 1
print('Done')

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int ( input('guess'))
    guess_count += 1
    if guess == secret_number:
        print('you won.!')
        break
else:
    print('sorry, you failed.!')

    command =""
    while command != "quit":
          command = input("> ").lower()
    if command == "start":
        print('car started...')
    elif command == "stop":
            print('car stoped...')
    elif command == "help":
            print("""
            start - to start the car
            stop - to stop the car
            quit - to quit""")
    else:
         print("sorry, i do not understand that. ")

for item in range (5,10,2):
    print(item)

for x in range (4):
    for y in range (3):
        print(f'({x},{y})')

number = [5, 2, 5, 3, 2]
for x_count in number:
    print('x'* x_count)

names = ['apu', 'anik', 'kakon', 'asru', 'tamjil']
names [4] = 'tanjil'
print(names)

matrix = [
    [ 3,4,5],
    [6,7,8],
]
for row in matrix:
    for item in row:
        print(item)

numbers = [3,5,7,9]
numbers2= numbers.copy()
numbers.append(10)
print(numbers2)

numbers = [2,2,3,4,6,1,6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        print(uniques)

Coordinates = [1,2,3]
x, y, z = Coordinates
print(x)

customer = {
    "name" : "Aftab apu",
    "age" : 19,
    "is_verified" : True
}
customer["name"] = "Amith anik"
print(customer["name"])

phone = input("phone:")
digits_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output = ""
for ch in phone :
    output += digits_mapping.get(ch, "!") + " "
print(output)

massage = input(">")
words = massage.split(' ')
emojis = {
    ":)": "😃",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

def greet_user (first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('welcome guys')

print("start")
greet_user("Aftab","Saima")
print("Finish")

def square (number):
    return number *number
print(square(3))

try:
    age = int (input('Age:'))
    print(age)
except ValueError:
    print('Invalid value')

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

class Point:
    def __init__(self, x, y): #(init er maddom e amera argument nita perbo)
        self.x = x #(self hocca oi obj jer kotha bola hocca)
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")
point = Point(10,20)
point.y = 77
print(point.y)


class person :
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi im {self.name}")

Aftab = person("Aftab Apu")
Aftab.talk()
#inheritance
class Mammal:
    def walk(self):
        print("walk")

class Dog (Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be_anoying(self):
        print('anoying')

cat1 = Cat()
cat1.be_anoying()

#modules/package
# from ecommarce.shipping import calc_shipping
# calc_shipping()

#Generatic_Random_values
import random
for i in range(3):
    print(random.random())

import random
members =['apu','saima','merry']
leader = random.choice(members)
print(leader)

import random
class Dice:
    def roll(self):
       frist = random.randint(1,6)
       secound = random.randint(1,6)
       return first,secound

dice = Dice()
print(dice.roll())

#Filed and Directories
# pypi and pip
