	#100sol01.py
age = int(input("Dog's age: "))
# Python2:
# age = int(raw_input("Dog's age: "))
#%%
print(age)
#%%
if age <= 0:
    print("This can't be true!")
elif age == 1:
    print("about 14 years")
elif age == 2:
    print("about 22 years")
elif age > 2:
    human = 22 + (age - 2)*5
    print("in human years:", human)

### 
# Python 2:
# raw_input('press Return>')
input('press Return>')
	----------------------------------------
	#100sol02.py
year = int(input("Year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year:
    print(str(year) + 
            ": leap year!")
else:
    print(str(year) + 
            ": not a leap year!")
	----------------------------------------
	#100sol03.py
K = float(input("Starting capital? "))
p = float(input("Interest rate? "))
n = int(input("Number of years? "))
# python2: raw_input instead of input

i = 0
while i < n:
    K +=  K * p / 100.0
    # or K *=  1 +  p / 100.0
    i += 1
    print(i)
print("Capital after " + str(n) + " ys: " + str(K))
	----------------------------------------
	#100sol04.py
A = 4 * 10 **7
pA = 3.3
B = 7 * 10 ** 7
pB = 1.9

i = 0
while A < B:
	A *= 1 + pA/100.
	B *= 1 + pB/100.
	print('\t' + str(i))
	i += 1 
print(i)
	----------------------------------------
	#100sol05.py
import random
n = 20
to_be_guessed = random.randint(1,n)

guess = int(input("Your guess: "))
while guess != to_be_guessed:
    if guess > to_be_guessed:
        print("Number is too large")
    elif guess < to_be_guessed:
        print("Number is too small")
    guess = int(input("Your new guess: "))
print("You got it!")
import random
n = 20
to_be_guessed = random.randint(1,n)

while True:
    guess = int(input("Your guess: "))
    if guess > to_be_guessed:
        print("Number is too large")
    elif guess < to_be_guessed:
        print("Number is too small")
    if guess == to_be_guessed:
        break
print("You got it!")
	----------------------------------------
	#100sol06.py
import random

supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}            
              }


available_articles = list(supermarket.keys()) + ["pears", "cherries"]
print(supermarket)

max_articles_per_customer = 5 # not like a real supermarket :-)
customers = ["Frank", "Mary", "Paul", "Jennifer"]
shopping_lists = {}
for customer in customers:
    no_of_items = random.randint(1, len(available_articles))
    shopping_lists[customer] = []
    for article_name in random.sample(available_articles, no_of_items):
        quantity = random.randint(1, max_articles_per_customer)
        shopping_lists[customer].append((article_name, quantity))

# let's look at the shopping lists
for customer in customers:     
    print(customer + ":  " + str(shopping_lists[customer]))
    
# filling the carts
carts = {}
for customer in customers:
    carts[customer] = []
    for article, quantity in shopping_lists[customer]:
        if article in supermarket:
            if supermarket[article]["quantity"] < quantity:
                quantity = supermarket[article]["quantity"]
            if quantity:
                supermarket[article]["quantity"] -= quantity
                carts[customer].append((article, quantity))
for customer in customers:                            
     print(carts[customer])
            
            
print("checkout")
for customer in customers:
    print("\ncheckout for " + customer + ":")
    total_sum = 0
    for name, quantity in carts[customer]:
        unit_price = supermarket[name]["price"]
        item_sum = quantity * unit_price
        print( "{0:3d} {1:12s} {2:8.2f} {3:8.2f}".format(quantity, name, unit_price, item_sum))
        total_sum += item_sum
    print("{0:22s} {1:11.2f}".format("total_sum:", total_sum))

	----------------------------------------
	#100sol07.py
en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
print(en_de)
print(en_de["red"])
print(en_de["green"])
print(en_de["blue"])
print(en_de["yellow"])
	----------------------------------------
	#100sol08.py
edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
#        break
    print("Great, delicious " + food)
#else:
#    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")
	----------------------------------------
	#100sol09.py
import sys
print(len(sys.argv))
for i, arg in enumerate(sys.argv):
    print(i, arg)
if len(sys.argv)==1:
    print('arguments expected')
elif sys.argv[1]=='-h':
    print('option -h found')
else:
    print('unknown option')
	----------------------------------------
	#100sol10.py
char_morse = {'A':'.-', 'B':'-...', 
'C':'-.-.', 'D':'-..', 
'E':'.', 'F':'..-.', 
'G':'--.','H':'....', 
'I':'..', 'J':'.---', 
'K':'-.-', 'L':'.-..',
'M':'--', 'N':'-.', 
'O':'---', 'P':'.--.', 
'Q':'--.-', 'R':'.-.', 
'S':'...', 'T':'-', 'U':'..-', 
'V':'...-', 'W':'.--', 'X':'-..-',
'Y':'-.--', 'Z':'--..', 
'1':'.----', '2':'...--', 
'3':'...--', '4':'....-', 
'5':'.....', '6':'-....', 
'7':'--...', '8':'---..', 
'9':'----.', '0':'-----', 
',':'--..--', '.':'.-.-.-', 
'?':'..--..', ';':'-.-.-', ':':'---...', 
'/':'-..-.', '-':'-....-', '\'':'.----.',
'(':'-.--.-', ')':'-.--.-', '[':'-.--.-', 
']':'-.--.-', '{':'-.--.-', '}':'-.--.-', '_':'..--.-'}

morse_char = {}
for char in char_morse:
    morse_char[char_morse[char]] = char
    
def txt2morse(txt, alphabet):
    morse_code = ""
    for char in txt.upper():
        if char == " ":
            morse_code += "   "
        else:
            morse_code += alphabet[char] + " "
    return morse_code

def morse2txt(txt, alphabet):
    res = ""
    mwords = txt.split("   ")
    for mword in mwords:
        for mchar in mword.split():
            res += alphabet[mchar]
        res += " "
    return res

mstring = txt2morse("So what?", char_morse)
print(mstring)
print(morse2txt(mstring, morse_char))
	----------------------------------------
	#100sol11.py
def number_of_neighbours(board, row, col):
    """ counts the numbers of an array_element with
    the position row and column. It is assumed,
    that i,j > 0 and i,< < len(board)-1"""
    counter = 0
    for i in [row-1,row,row+1]:
        for j in [col-1,col,col+1]:
             counter += board[i][j]
    counter -= board[row][col]
    return counter

board = [ [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,1,0,1,0,0,0,0,1,0,1,0],
          [0,1,0,1,0,1,0,1,0,0,0,0],
          [0,1,1,0,0,0,0,0,1,1,1,0],
          [0,0,0,1,1,0,0,0,0,0,0,0],
          [0,1,0,1,0,0,0,0,1,0,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0]]
while True:
    r = int(input("row: "))  # Python2: raw_input
    if r == 0:
        break
    c = int(input("col: "))  # Python2: raw_input
    print("neighbours: ", number_of_neighbours(board, r,c))
	----------------------------------------
	#100sol12.py
def findnth(s, sub, n):
    num = 0
    start = -1
    while num < n:
        start = s.find(sub, start+1)
        if start == -1: 
            break
        num += 1
    
    return start

s = "abcxyzabcjkjkjkabclkjkjlkjabcjlj"
print(findnth(s,"abc", 4))
	----------------------------------------
	#100sol13.py
def replacenth(source, search, replacement, n):
    pos = findnth(source, search, n)
    if pos == -1: 
        return source
    return source[:pos] + replacement + source[pos+len(search):]

s = "abcxyzabcjkjkjkabclkjkjlkjabcjlj"
print(findnth(s,"abc", 4))
print(replacenth(s,"abc","---", 4))
	----------------------------------------
	#100sol14.py
def mymean(*args):
    accumulator = 0
    counter = 0
    for a in args:
       accumulator += a
       counter += 1
    print('sum(args): ', sum(args))
    print('len(args): ', len(args))
    print('type(args): ', type(args))
    return accumulator/counter  # in Py3 division defaults to float div
                                # for Py2 cast to float
#%%
print(mymean(1,5.5))
print(mymean(1,5, -3))
	----------------------------------------
	#100sol15.py
my_list = [('a', 232), ('b', 343), ('c', 543), ('d', 23)]
list(zip(*my_list))
	----------------------------------------
	#100sol16.py
	----------------------------------------
	#100sol17.py
board = [j+str(i) for i in range(1,9) for j in 'abcdefgh']
board
	----------------------------------------
	#100sol18.py
di = {'DE':'Deutschland','FR':'Frankreich'}
inv = dict((di[i],i) for i in di)
inv
	----------------------------------------
	#100sol19.py
def letter_frequency(s):
    frequency_dict = {}
    for char in s.lower():
        if char.isalpha():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    #f =  frequency_dict.items()      # Python2
    f =  list(frequency_dict.items()) # Python3
    f.sort(key = lambda x: (-x[1], x[0]))
    return f
s = "Monty Python"
x = letter_frequency(s)
print(x)
	----------------------------------------
	#100sol20.py
def fak(n):
    if n == 1:
        return 1
    if n>1:
        return n*fak(n-1)
    
print(fak(4))
	----------------------------------------
	#100sol21.py
from math import factorial

days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def n_in_factorial_k(n):
    n = str(n)
    k = 0
    while True:
        if n in str(factorial(k)):
            return k
        k += 1

factorial_birthdays = []
for month in range(0, 12):
    for day in range(1, days_in_month[month]+1):
        birthday = "{:02d}{:02d}".format(day, month+1)
        factorial_birthdays.append((birthday, 		
											n_in_factorial_k(birthday)))      
print(sorted(factorial_birthdays, key=lambda x: (x[1], x[0])))
print('-'*30)
print(sorted(factorial_birthdays))
	----------------------------------------
	#100sol22.py
def nfind(haystack, needle, n, pos=0):
    pos = haystack.find(needle, pos)
    if n == 1 or pos == -1:
        return pos
    else:
        return nfind(haystack, needle, n-1, pos+1)


for i in range(7):
    print(i,nfind("abcjjjabcooiabckkabc", "c", i))
	----------------------------------------
	#100sol23.py
def flatten(x):
  """flatten(sequence) -> list"""

  result = []
  for el in x:
    # alternatively:
    # if isinstance(el, (list, tuple)):
    if type(el)==list or type(el)==tuple:
      result.extend(flatten(el))
    else:
      result.append(el)
  return result
  
print(flatten([(1, 2), "Python", ["a", [1,7]], 1, 1.3]))
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)

s = 0
for i in range(10):
    s += succ(i)
    
print(succ.calls)
	----------------------------------------
	#100sol24.py
with open("data/bundeslaender.txt", encoding="ISO-8859-1") as fh:
    #first line contains no data:
    fh.readline()
    max_size = 10000
    small_lands = []
    for line in fh:
        land, size_of_land, *rem = line.split()
        size_of_land = float(size_of_land)
        if size_of_land < max_size:
            small_lands.append(land)
    print(small_lands)
	----------------------------------------
	#100sol25.py
import urllib.request
url = "https://www.python-course.eu/material/texts/bundeslaender.txt"
with urllib.request.urlopen(url) as fh:
    with open("bundeslaender.txt", "w") as fhw:
        fh.readline()
        for line in fh:
            line = line.decode("iso8859-1")   #  "utf-8" 
            land, area, male, female = line.split()
            population = int(male) + int(female)
            area_sq_km = population / float(area) * 1000
            output = land + " " + str(area)
            output += " " + str(population) + " " + str(area_sq_km)
            fhw.write( output + "\n" )
	----------------------------------------
	#100sol26.py
data = []
fh = open("data/hacker_poll.txt")
for line in fh:
    language, votes = line.strip().rsplit(None, 1)
    data.append((language, int(votes)))

data.sort(key=lambda x: (x[1], x[0]), reverse = True)

top10 = data[:10]
print(top10)
	----------------------------------------
	#100sol27.py
import re
from collections import Counter

def word_freq(txt):
    word_dict = {}
    list_of_words = re.findall(r"\b\w+\b", txt)
    for word in list_of_words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1           
    items = list(word_dict.items())
    items.sort(key = lambda x: x[1], reverse=True)
    return items

def word_freq2(txt):
    word_dict = Counter()
    list_of_words = re.findall(r"\b\w+\b", txt)
    for word in list_of_words:
        word_dict[word] += 1
    return word_dict.most_common()

def word_freq3(txt):
    return Counter(re.findall(r"\b\w+\b", txt)).most_common()


fobj = open("data/1984.txt")
text = fobj.read()
fobj.close()
x = word_freq2(text)
print(x[:40])
x = word_freq3(text)
print(x[:40])
y = word_freq(text)
print(y)
	----------------------------------------
	#100sol28.py
def fibonacci():
    """Ein Fibonacci-Zahlen-Generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()
counter = 0
for x in f:
    print(x)
    counter += 1
    if (counter > 10):
        break 
	----------------------------------------
	#100sol29.py
import random

def random_ones_and_zeros():
    p = random.random()
    while True:
        x = random.random()
        message = yield 1 if x < p else 0
        if message != None:
            p = message
        
x = random_ones_and_zeros()
next(x)  # not interested in the return value
for p in [0.2, 0.8]:
    x.send(p)
    print("\nprobabiliy: " + str(p))    
    for i in range(15):
        print(next(x), end=" ")
	----------------------------------------
	#100sol30.py
def trange(start, stop, step):
    """ 
    trange(stop) -> time as a 3-tuple (hours, minutes, seconds)
    trange(start, stop[, step]) -> time tuple

    start: time tuple (hours, minutes, seconds)
    stop: time tuple
    step: time tuple

    returns a sequence of time tuples from start to stop
    incremented by step
    
    The generator can be rest by sending a new "start" value.
    """        

    current = list(start)
    while current < list(stop):
        new_start = yield tuple(current)
        if new_start != None:
            current = list(new_start)
            continue
        seconds = step[2] + current[2]
        min_borrow = 0
        hours_borrow = 0
        if seconds < 60:
            current[2] = seconds
        else:
            current[2] = seconds - 60
            min_borrow = 1
        minutes = step[1] + current[1] + min_borrow
        if minutes < 60:
            current[1] = minutes 
        else:
            current[1] = minutes - 60
            hours_borrow = 1
        hours = step[0] + current[0] + hours_borrow
        if hours < 24:
            current[0] = hours 
        else:
            current[0] = hours -24
            
for time in trange((10, 10, 10), (13, 50, 15), (0, 15, 12) ):
        print(time)           
	----------------------------------------
	#100sol31.py
from random import randint, seed

def random_ascending_lists(length, value_range=(1,100), secret_key = 0):
    seed(secret_key)
    counter = 0
    while True:
        seq = [randint(*value_range) for _ in range(length)]
        counter += 1
        if seq == sorted(seq):   
            new_secret_key = (yield (counter, secret_key, seq))
            if new_secret_key:
                secret_key = new_secret_key
                seed(secret_key)

numbers = 7
range_of_values = (1, 100)
alists = random_ascending_lists(numbers, range_of_values, 42) 
for i in range(10):
    print(next(alists))
	----------------------------------------
	#100sol32.py
from random import randint, seed
def random_ascending_lists(length, value_range=(1,100), secret_key = 0):
    seed(secret_key)
    counter = 0
    while True:
        seq = [randint(*value_range) for _ in range(length)]
        counter += 1
        if seq == sorted(seq):   
            new_secret_key = (yield (counter, secret_key, seq))
            if new_secret_key:
                secret_key = new_secret_key
                seed(secret_key)
                
def random_ascending_lists2(length, value_range=(1,100), secret_key = 0):
    while True:
        seed(secret_key)
        seq = [randint(*value_range) for _ in range(length)]
        secret_key += 1
        if seq == sorted(seq):   
            new_secret_key = (yield (secret_key, seq))
            if new_secret_key:
                secret_key = new_secret_key
                seed(secret_key)


range_of_values = (1, 100)
#alists = random_ascending_lists(7, range_of_values, 42) 
alists = random_ascending_lists2(7, range_of_values) 
for i in range(10):
    print(next(alists))
	----------------------------------------
	#100sol33.py
def chain(*iterables):
    """ This generator is equivalent 
        to the chain
        method of iterables  """
    for iterable in iterables:
        for element in iterable:
            yield element

names1 = ["Pete", "Tom"]
names2 = ["Tom", "Oscar"]        
c = chain(names1, names2)
for el in c:
    print(el)
	----------------------------------------
	#100sol34.py
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element
        
numbers = cycle("abcde")
for _ in range(12):
    print(next(numbers), end=", ")
	----------------------------------------
	#100sol35.py
import sys
file_list=[
    'data/unbekannt.txt',
    'data/unbenannt.txt',
    'data/ignored.txt',
]
for fn in file_list:
    fh=None
    try:
        fh=open(fn)
    except :
        (type, value, traceback) = sys.exc_info()
        print("Type: ", type)
        print("Value: ", value)
        print("traceback: ", traceback)
        print('Failed to open '+fn+' for reading')
        print('-'*30)
        continue
    contents=fh.read()
    print(contents)
    fh.close()
        
	----------------------------------------
	#100sol36.py
from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("My string!")
	----------------------------------------
	#100sol37.py
import doctest

def palindromic_squares(n = 100000000):
    """ 
    creates a list of all the palindromical 
    square numbers less than n

    >>> {1, 4, 9, 121, 484, 676, 10201} <= set(palindromic_squares(1000000000000))
    True
    """

    counter = 1
    squared = 1
    palindrome_list = []
    while squared < n:
        s = str(squared)
        if s == s[::-1]:
            palindrome_list.append(squared)
        counter += 1
        squared = counter * counter

    return palindrome_list

def find_even_len_palindromes(plist):
    """
    returns a list of all the pallindromes of
    plist, which have an even number of digits

    >>> find_even_len_palindromes(palindromic_squares(1000000000)) == [698896]
    True
    >>> 
   
    """
    even_len_list = []
    for i in plist:
        if not len(str(i)) % 2:
             even_len_list	.append(i)
    return even_len_list  


if __name__ == "__main__": 
    doctest.testmod()

	----------------------------------------
	#100sol38.py
class Robot:
 
    def __init__(self, name=None, build_year=None):
        self.name = name 
        self.build_year=build_year
        
    def say_hi(self):
        Pass  # code as in previous example
            
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name    
    def set_build_year(self, by):
        self.build_year = by
        
    def get_build_year(self):
        return self.build_year    
    

x = Robot("Henry", 2008)
y = Robot()
y.set_name(x.get_name())
print(x.get_name(), x.get_build_year())
	----------------------------------------
	#100sol39.py
class Robot:
 
    def __init__(self, name="None", build_year=2000):
        self.__name = name
        self.__build_year = build_year 
        
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Sorry, I am nameless")
                 
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set_build_year(self, build_year):
        self.__build_year = build_year
    def get_build_year(self):
        return self.__build_year
	----------------------------------------
	#100sol40.py
class Robot:
 
    def __init__(self, name="None", build_year=2000):
        self.name = name
        self.build_year = build_year 
      
    @property   
    def name(self):
        return self.__name              
    @name.setter
    def name(self, name):
        self.__name = "Marvin" if name == "Henry" else name

    @property
    def build_year(self):
        return self.__build_year
    @build_year.setter
    def build_year(self, by):
        self.__build_year = 2000 if by < 2000 else by
	----------------------------------------
	#100sol41.py
class Clock(object):

    def __init__(self,hours=0, minutes=0, seconds=0):
        self._hours = hours     # protected, needed in ClockCalendar
        self.__minutes = minutes
        self.__seconds = seconds

    def tick(self):
        """ Time will be advanced by one second """
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                self._hours = 0 if self._hours==23  \
                                else self._hours + 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1
    def set(self,hours, minutes, seconds=0):
        self._hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return "%02d:%02d:%02d" % (self._hours, 
                                   self.__minutes, 
                                   self.__seconds)

if __name__ == "__main__":
    x = Clock(23, 59, 30)
    print(x)
    for i in range(31):
        x.tick()
    print(x)            
	----------------------------------------
	#100sol42.py
class Fraction(object):
    def __init__(self,z,n):
        self.__num = z
        self.__den = n
        self.reduce()

    def __str__(self):
        return str(self.__num)+'/'+str(self.__den)

    @staticmethod
    def gcd(a,b):
        while b != 0:
            a,b = b,a%b
        return a

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num = self.__num // g
        self.__den = self.__den // g

    def __mul__(self,other):
        p = Fraction(self.__num * other.__num,
                     self.__den * other.__den)
        p.reduce()
        return p
    # in Python 2: __div__
    def __truediv__(self,other):
        p = Fraction(self.__num * other.__den,
                  self.__den * other.__num)
        p.reduce()
        return p

    def __add__(self,other):
        s = Fraction(self.__num*other.__den + other.__num * self.__den,
                     self.__den*other.__den)
        s.reduce()
        return s

    def __sub__(self,other):
        s = Fraction(self.__num*other.__den - other.__num * self.__den,
                     self.__den * other.__den)
        s.reduce()
        return s

    def __eq__(self, other):
        return self.__num * other.__den == other.__num * self.__den
    def __ne__(self, other):
        return not self.__eq__(other)  
    def __gt__(self, other):
        return self.__num * other.__den > other.__num * self.__den
    def __ge__(self, other):
        return self.__num * other.__den >= other.__num * self.__den
    def __lt__(self, other):
        return self.__num * other.__den < other.__num * self.__den
    def __le__(self, other):
        return self.__num * other.__den <= other.__num * self.__den

if __name__ == "__main__":
    x = Fraction(2, 6)
    y = Fraction(3, 14)
    print(x * y)
    print(x / y)
    print(x + y)
    print(x - y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")
    print(x)    
	----------------------------------------
	#100sol43.py
import numpy as np
a = np.array([3,8,12,18,7,11,30])
a[1::2]
a[::-1]
m = np.array([ [11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
m
m[::,::-1]
m[::-1]
m[::-1,::-1]
m[1:-1,1:-1]
	----------------------------------------
	#100sol44.py
np.arange(1,16).reshape(5,3)           # 2d array
	----------------------------------------
	#100sol45.py
num_labels = 4
labels = np.random.randint(4, size=6)[:,None]
labels
labels_one_hot = (np.arange(num_labels) == labels).astype(np.float64)
labels_one_hot
	----------------------------------------
	#100sol46.py
import numpy as np
A = np.array([3,4,6,10,24,89,45,43,46,99,100])
A[A%3!=0]
A
A[A%5==0]
A[(A%3==0) & (A%5==0)]
A[A%3==0] = 42
A
	----------------------------------------
	#100sol47.py
b = np.arange(12).reshape(3,4)
print(b)
b1=b.sum(axis=0)
print(b1)
b2 = np.vstack((b,b1))
print(b2)
b3=b2.sum(axis=1)
print(b3)
b3=b3[:,np.newaxis]               # this allows to have a 2D columns vector
print(b3)
b4 = np.hstack((b2,b3))
print(b4)
	----------------------------------------
	#100sol48.py
np.zeros(7)

checkerboard = np.zeros((8,8),dtype=int)
checkerboard[::2,1::2] = 1
checkerboard[1::2,::2] = 1
print(checkerboard)
#alternativ:
np.tile([[1,0],[0,1]],(4,4))
	----------------------------------------
	#100sol49.py
v = np.random.randint(-8, 8, 10)
v
vp = v<=0
vp
v[vp]
	----------------------------------------
	#100sol50.py
PersAnz = np.array([[100,175,210],[90,160,150],[200,50,100],[120,0,310]])
Preis_per_100_g = np.array([2.98,3.90,1.99])
Preis_in_Cent = np.dot(PersAnz,Preis_per_100_g)
Preis_in_Euro = Preis_in_Cent / np.array([100,100,100,100])
Preis_in_Euro
	----------------------------------------
	#100sol51.py
import numpy as np
xdata = np.arange(-5, 5, 0.5)
ydata = np.array([20.773, 15.04, 12.9, 9.5, 7.5, 4.3, 2.4, 1, 0.2, 0, 0, 0.6, 2.1, 3.9, 6, 8, 12, 14, 19, 23])
coefficients = np.polyfit(xdata, ydata, 2)
print(coefficients)
f = np.poly1d(np.polyfit(xdata, ydata, 2))
print(f(6.201765102680708))
	----------------------------------------
	#100sol52.py
import numpy as np
A = np.genfromtxt("data/shop_sales_figures_extended.txt", usecols=(1,3,4), dtype=None)
A
A1 = A[1:,:].astype(np.float)
A1.sum(axis=0)
	----------------------------------------
	#100sol53.py
%matplotlib inline
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

data = []
fh = open("data/hacker_poll.txt")
for line in fh:
    language, votes = line.strip().rsplit(None, 1)
    data.append((language, int(votes)))
data.sort(key=lambda x: (x[1], x[0]), reverse = True)

languages, votes = zip(*data[:10])
languages = np.asarray(languages)
votes = np.asarray(votes)

index = np.arange(len(votes))
bar_width = 1.0
plt.bar(index, votes, bar_width,  color="blue")
plt.xticks(index +bar_width / 2, languages,rotation='vertical') 
plt.show()
	----------------------------------------
	#100sol54.py
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

data = []
fh = open("data/hacker_poll.txt")
for line in fh:
    language, votes = line.strip().rsplit(None, 1)
    data.append((language, int(votes)))
data.sort(key=lambda x: (x[1], x[0]), reverse = True)
languages, votes = zip(*data[:10])
languages = np.asarray(languages)
votes = np.asarray(votes)
languages
total_votes = votes.sum()
total_votes
votes_percentage = votes/total_votes*100
votes_percentage
index = np.arange(len(votes))
sizes = votes_percentage
labels = languages
explode1 =[ [0]*len(votes)]  # only "explode" the 2nd slice (i.e. 'Hogs')
explode1
explode = explode1[0]
explode[0]=0.1
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
	----------------------------------------
	#100sol55.py
import pandas as pd
fruits = ['peaches', 'oranges', 'cherries', 'pears']
S = pd.Series([25, 33, 52, 29], index=fruits)
S.apply(lambda x: int(x/10)*10)
	----------------------------------------
	#100sol56.py
%matplotlib inline
import pandas as pd
data = pd.read_csv('data/visitors_python_de.txt',
                   index_col=False,
                  quotechar='"',
                   thousands=",",
                   delimiter=r"\s+")
data.head()
data.columns
month_year =  data[["Month", "Year"]]
month_year.dtypes
month_year = month_year.apply(lambda x: x[0] + " " + str(x[1]), 
                              axis=1)
data["Month"] = month_year
del data["Year"]

data.set_index("Month", inplace=True)
def unit_convert(x):
    value, unit = x
    if unit == "MB":
        value *= 1024
    elif unit == "GB":
        value *= 1048576 # i.e. 1024 **2
    return value
b_and_u= data[["Bandwidth", "Unit"]]
bandwidth = b_and_u.apply(unit_convert, axis=1)
del data["Unit"]
data["Bandwidth"] = bandwidth
data.tail()
data[:-1][["Unique visitors", "Number of visits"]].plot()
	----------------------------------------
	#100sol57.py
%matplotlib inline
import pandas as pd
data = pd.read_csv('data/smartphone_os.txt',
#                   header=1, # first data line lost
                   skiprows=1,
                   names=["Operating System","1Q16 Units","1Q16 Market Share (%)","1Q15 Units",
                          "1Q15 Market Share (%)",
                         ],
                   index_col="Operating System",
                  quotechar='"',
                   thousands=",",
                   delimiter=r"\s+",
                   engine = 'python',
                   skipfooter=2,
                  )
data.head()
data.dtypes
# plot bar
data[['1Q16 Units','1Q15 Units']].head()
data[['1Q15 Units','1Q16 Units']].plot(kind='bar')
	----------------------------------------
	#100sol58.py
import os
os.environ['PYTHONPATH']=''
print('PYTHONPATH set to empty')
print('PYTHONPATH ',os.environ['PYTHONPATH'] )
#del os.environ['PYTHONPATH']
if 'PYTHONPATH' in os.environ:
    print('in if')
    print(os.environ['PYTHONPATH'] )
else:
    print('in else')
    os.environ['PYTHONPATH']=os.environ['PYTHONPATH']+os.path.pathsep+r'C:\temp\my_pthon_lib'
    print(os.environ['PYTHONPATH'] )
	----------------------------------------
	#100sol59.py
import os, subprocess
fn= input('File path: ')
print('your input: ', fn)
!type data\bundeslaender.txt
#x = subprocess.Popen(['type ' + fn]) # not under W10
x = subprocess.Popen('type ' + fn, shell=True)
print(x.returncode)
cmd = 'type %s'%fn
theOutput=subprocess.getstatusoutput(cmd)
print( theOutput)


	----------------------------------------
	#100sol60.py
%%file my_script_args.py
#run this in a terminal, 
import sys
def usage():
    print('''usage: python my_script_args.py --version|-n ##
            where ## is a positive integer
    ''')
if len(sys.argv) == 1:
    usage()
    exit(1)
if len(sys.argv) == 2:
    if sys.argv[1] == '--version':
        print('0.1')
        exit(0)
    else:
        usage()
        exit(1)
if len(sys.argv) == 3: 
    if sys.argv[1] == '-n':
        n=0
        try:
            n=int(sys.argv[2])
        except:
            usage()
            exit(1)
        for i in range(1,n+1):
            print(i)
        exit(0)
    else:
        usage()
        exit(1)
if len(sys.argv) > 3:
    print('3 arguments detected')
    usage()
    exit(1)

#print( sys.argv)
	----------------------------------------
	#100sol61.py
# %%file multithreading_sync.py
# run as: python multithreading_sync.py
import threading 
import random
import time
import datetime
lck = threading.Lock()

random.seed(42)
def incrementer(fname, id):
    time.sleep(random.random())
    global lck
    lck.acquire()
    with open(fname, 'r') as f:
        for ln in f:
            tokens = ln.split()
            n = int(tokens[0])
    n += 1
    with open(fname, 'a') as f:
        f.write(str(n)+" by " + str(id) + " at "+ datetime.datetime.now().strftime("%H:%M:%S") +'\n')

    lck.release()        
# filename to use
fname = 'counter.txt'

# re-initialize file
with open(fname, 'w') as f:
    f.write('0\n')

threads = []
for i in range(0, 20):
    t = threading.Thread(target = incrementer, args = (fname, i ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()        
	----------------------------------------
	#100sol62.py
%%file largest_files.py
#run fron terminal
import os, sys

dname = sys.argv[1] if len(sys.argv)>1 else '.'

files = os.listdir(dname)
f_list=[]
total =0
for x in files:
  fpath = dname + '/' + x
#  print(fpath,type(fpath))
  if os.path.isfile(fpath):
     hrfilesize = round(os.path.getsize(fpath) / 1024, 2)
     total += hrfilesize
     f_list.append([ x,hrfilesize])
#     print( x,hrfilesize)
f_list.sort(key=lambda x: -x[1])
print(f_list[:10])
	----------------------------------------

