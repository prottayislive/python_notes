"""             #descriptive notes
# temp = 99.5     #assignment_statement
#temp is an identifier and 99.5 is the object

# accessors - methods that return state of an object but does not change state
# mutators - same as above but change state

# for a bool() class 
# if bool() is empty it returns false
# if number is 0 it returns false
#if a squence is empty it returns false
"""

"""             #list_intro
cars = ['Porsche', 'BMW', 'Audi', 'Ferrari', 'Mustang', 'Hyundai']
print(cars)
cars.insert(2,'Toyota')
print(cars)
popped_car = cars.pop(1)(saves an item)
print(popped_car)
del cars [2]
print(cars)
print(len(cars))
print(sorted(cars))
cars.remove('Porsche')
print(cars)
cars.sort(reverse=True)
"""  # list_intro
"""
                # working list
pizza = ['Seafood', 'Beef', 'Chicken']
for each_pizza in pizza:
    print(f"I Love {each_pizza} pizzas.")
print("\nI love all these pizzas")
# range stuff
for i in range(1,5):
    print(i)

my_list = list(range(1,6))
print(my_list)
even_numbers = list(range(0,11,2))
print(even_numbers)
digits = [1,2,3,4,5,6]
print(min(digits))
print(max(digits))
print(sum(digits))
print(all(digits))# why true?
square = []
for value in range (4, 11):
    square.append(value**2)
print(square)
# list_comprehension
cubes = [number**3 for number in range(1,11)]
print(cubes)
cars = ['Porsche', 'BMW', 'Audi', 'Ferrari', 'Mustang', 'Hyundai']
print(f"Cars I love {cars[2:4]}")
for car in cars[2:4]:
    print(car)
friend = cars[:]
friend.append('Jaguar')
print(cars)
print(friend)
# tuple: values that cannot change = immutable.
# immutable list = tuple
dimensions = (300,200)
for dimension in dimensions:
    print(dimension)"""  # working with lists
"""
cars = ['porsche', 'bmw', 'audi', 'ferrari', 'mustang', 'hyundai']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
for car in cars:
    if car != 'bmw':
        print(car.title())
    else:
        print(car.upper())
age = 19
print(age == 12)

age = 12
if age < 5:
    sign = 0
elif age < 18:
    sign = 9
else:
    sign = 10
print('your age is', sign)
# checking special items
orders = ['mushroom', 'pepperoni', 'sausage', 'olives']
for order in orders:
    if order == 'sausage':
        print("don't have sausages")
    else:
        print(f"{order} added")
for car in cars:
    if car == 'bmw':
        print("I don't have a bmw")
    else:
        print(f'I have a {car.title()}')
# checking list is not empty
boxes = cars
if boxes:
    for box in boxes:
        print(f"Adding {box}")
    print("Finished making box\n")
else:
    print("Are you sure you want a plain pizza")
# using multiple lists
requests = ['sauce', 'gravy', 'beef', 'prawn']
available = ['sauce', 'chicken', 'beef', 'fish']
for request in requests:
    if request in available:
        print(f"adding {request}")
    else:
        print(f"sorry, we dont have {request}")

print("Order complete!\n")
# exercise
current_users = ['sheldon','penny', 'raj', 'howard', 'leonard']
new_users = ['bernadette', 'sheldon', 'amy', 'raj']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} Name already exists")
    else:
        print(f"{new_user} name is available")

my_list = list(range(1,10))
print(my_list)
for i in my_list:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")"""  # if - else
"""
# dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
monster = {}
monster['color'] = 'red'
monster['power'] = 10
print(monster)
monster['color'] = 'green'
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
del alien_0['color']
print(alien_0)
favourite_lang = {
    'amy': 'python',
    'penny': 'c++',
    'howard': 'java',
    'bernadette': 'python',
    'sheldon': 'sql',
    'stewart': 'java',
    'rajesh': 'python'
}
language = favourite_lang['amy']
print(language)
point = favourite_lang.get('raj', 'bash')
print(point)
add = favourite_lang.get('leonard')
print(add)
admin = {
    'username': 'admin',
    'f_name': 'prottay',
    'l_name': 'karim',
    'password': 'admin123'
}
for key, value in admin.items():
    print(f"Key:{key}")
    print(f"Value:{value}\n")
for name, lang in favourite_lang.items():
    print(name, "'s favourite programming language is: ", lang)
for name in favourite_lang.keys():
    print(name.title())
print("")
other_langs = {'samuel', 'jack', 'penny'}
for name in favourite_lang.keys():
    print(f"Hi {name}")
    if name in other_langs:
        lang = favourite_lang[name].title()
        print(f"\tI see you like {lang}")
if 'jack' not in favourite_lang.keys():
    print(f"{other_langs} not in poll")
for name in sorted(favourite_lang.keys()):
    print(name)
for langu in set(favourite_lang.values()):
    print(langu.upper())
for langu in favourite_lang.values():
    print(langu)
boss_0 = {'color': 'red', 'eyes': 'blue', 'points': 5, 'level': 1}
boss_1 = {'color': 'green', 'eyes': 'purple', 'points': 10, 'level': 2}
boss_2 = {'color': 'black', 'eyes': 'red', 'points': 15, 'level': 3}

bosses = [boss_0, boss_1, boss_2]
for boss in bosses:
    print(boss)
print("")
zombies = []
for zombie in range(30):
    new_zombie = {'color': 'green', 'points': 5}
    zombies.append(new_zombie)
for zombie in zombies[2:4]:
    if zombie['color'] == 'green':
        zombie['color'] = 'red'
        zombie['points'] = 10
for zombie in zombies[:5]:
    print(zombie)
print('...')
print('total number of zombies is', len(zombies))
print("")
pizza = {
    'crust': 'thin',
    'sauce': 'spicy',
    'toppings': ['mushroom', 'beef', 'chicken', 'prawn'],
    'type': 'baked'
}
print("Selected toppings are:")
for topping in pizza['toppings']:
    print("\t\t\t", topping)
favourite_programming_language = {
    'amy': ['python', 'typescript'],
    'penny': ['c++', 'c#'],
    'howard': ['java', 'pyhton', 'r'],
    'bernadette': ['python'],
    'sheldon': ['sql', 'nosql', 'html'],
    'stewart': ['java'],
    'rajesh': ['python', 'django']
}
for username, programming_languages in favourite_programming_language.items():
    print(f"{username} knows:")
    for programming_language in programming_languages:
        print(f"\t\t{(programming_language).title()}")
for fav in set(favourite_lang.values()):
    print(fav)
scientists = {
    'sheldonc': {
        'fname': 'sheldon',
        'lname': 'copper',
        'occupation': 'physicist',
    },
    'amyf': {
        'fname': 'amy',
        'lname': 'fowler',
        'occupation': 'biologist',
    }
}
for scientist, info in scientists.items():
    print(f"\nUsername: {scientist}")
    fullname = f"{info['fname']} {info['lname']}"
    print("Name:", fullname.title())
"""  # dictionaries
"""
# input and while lopps
# age = int(input("What's your age?"))

age = 33
if age <= 18:
    print("You can't vote")
else:
    print("Welcome to vote")
current = 1
while current <= 5:
    print(current)
    current += 1

active = True
while active:
    message = input("Keep looping till you say 'quit'!")
    if message == 'quit':
        active = False
    else:
        print(message)
while True:
    city = input("Where have you been?")
    if city == 'quit':
        break
    else:
        print("I would love to visit", city)
number = 0
while number < 10:
    number = number + 1
    if number % 2 == 0:
        continue
    else:
        print(number)
unconfirmed_users = ['sheldon', 'howard', 'penny']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("New users", current_user.title())
    confirmed_users.append(current_user)
print(confirmed_users)
pets = ['dog', 'cat', 'bird', 'cat', 'dog', 'horse', 'chuwawa', 'cat']
print(pets)
while pets:
    if pets == 'cat':
        pets.remove('cat')
print(pets)
"""  # input and while loops
"""
# functions
def is_leap(year):
    leap = False

    # Write your logic here

    if year % 100 == 0:
        leap = False
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap


year = int(input("Year: "))
print(is_leap(year))


def greet_user(username):
    print("Hello", username.title())


greet_user('jessi')


def describe_pet(animal_type, pet_name):
    print("This is my pet", pet_name, "he is a", animal_type)


describe_pet("dog", "bobby")


# another way
def my_room(room_color, room_type):
    print("My", room_type, "is", room_color, "in color")


my_room(room_color="red", room_type="bedroom")


def name(fname, lname, mname=""):
    if mname:
        full_name = f"{fname} {mname} {lname}"
    else:
        full_name = f"{fname} {lname}"
    return full_name.title()


my_name = name("prottay", "karim", "lee")
print(my_name)


def user(firstname, lastname):
    dict = {
        "first": firstname,
        "last": lastname
    }

    return dict


full = user("prottay", "karim")

print(full)


def creds(username, password):
    login = f"{username} has a password: {password}"
    return login


while True:
    i1 = input("Enter User name")
    if i1 == '':
        break
    i2 = input("Enter Password")
    if i2 == '':
        break
    id = creds(i1.title(), i2)
    print(id)

players = ['amy', 'sheldon', 'raj']


def gamers(devs):
    for dev in devs:
        print("hello", dev, "! welcome!!")


gamers(players)


def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(sent_messages):
    while messages:
        complete = messages.pop()
        sent_messages.append(complete)


messages = ["Hi! I am", "Prottay", "Nice to meet You"]
sent_messages = []
show_messages(messages)
send_messages(sent_messages)
print(messages)
print(sent_messages)



def make_pizza(*toppings):  # * means empty tuple if ** empty dictionary
    print(toppings)


make_pizza('pepperoni')
make_pizza('olives', 'jamba juice')


def sandwich(*insides):
    for inside in insides:
        print(inside)


sandwich('beef')
sandwich('beef', 'chicken', 'sauce')
sandwich('chicken', 'sauce', 'vegetables')


def user_profile(fname,lname,**user_info):
    user_info['first_name'] = fname
    user_info['last_name']  = lname
    return user_info


build = user_profile('prottay','karim',
                     location='dhaka',
                     occu='student')
print(build)

"""  # functions
"""

# Class
# restaurant code
class Restaurant:
    def __init__(self, name, cusine_type):
        self.name = name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} restaurant servers {self.cusine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open")

    def restaurant(self):
        print('number of people served:', self.number_served)

    def set_number_served(self, new_served):
        self.number_served = new_served

    def increment_number_served(self, new_guests):
        self.number_served += new_guests


class IceCreamStand(Restaurant):
    def __init__(self, name, cusine_type):
        super().__init__(name, cusine_type)

    def flavor(self):
        flavors = ['hazel', 'choco', 'vanilla']
        print(f'{flavors} are available here')


best_restaurant = Restaurant("BFC", "Fast Food")
ice_cream = IceCreamStand("BnH", 'Ice Cream')
best_restaurant.describe_restaurant()
best_restaurant.open_restaurant()
best_restaurant.set_number_served(5)
best_restaurant.increment_number_served(10)
best_restaurant.restaurant()
ice_cream.flavor()


# information code
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def personal_info(self, location):
        print(f"{self.first_name} lives in {location}")

    def occupation(self, occupation):
        print(f"Mr.{self.last_name} works as a {occupation}")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        
        print(f"total login:{self.login_attempts}")

    def reset_login_attempt(self):
        if self.login_attempts == 3:
            self.login_attempts = 0
            print("reset:", self.login_attempts)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def allowance(self):
        prevs = ['can delete post', 'can ban user', 'can add post']
        for each_prev in prevs:
            print(each_prev)


user_ad = Admin("jane", "doe")
user1 = User('Prottay', 'Karim')
user1.personal_info("dhaka")
user1.increment_login_attempts()
user1.reset_login_attempt()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempt()
user_ad.allowance()

from random import randint

choice = randint(1, 6)
print(choice)


class Die:

    def __init__(self):
        self.sides = 6

    def roll_dice(self):
        die_side = randint(1, self.sides)
        return die_side


x = 0
while x < 9:
    ludo = Die()
    x = x + 1
    print(f"x is {x}")
"""  # Class
"""
#files
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    for content in contents:
        content = content.rstrip()
        content = int(content)
        print(content)
        if 23 in content:
            print(content)
"""

