#for number in range(1,100,5):
#    print(number)

#result=0
#basket_items={'apples' : 4, 'oranges' : 19, 'kites' : 3, 'sandwiches' : 8}
#fruits=['apples', 'oranges', 'pears', 'peaches', 'grapes' , 'bananas']

#for fruit,count in basket_items.items():
#    if fruit in fruits:
#       result+=count

#print("There are {} fruits in the basket.".format(result))


"""fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit, count in basket_items.items():
    if fruit in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} items that are not fruits.".format(fruit_count, not_fruit_count))

"""
"""
number = 5
product = 1

for num in range(2,number+1):
    product *= num

print(product)
"""
"""
limit=40
num=1
while num**2 < limit:
    num += 1

print((num-1)**2)
"""
"""
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
"""
"""
cities=['istanbul','ankara','bursa','rzeszow']

capitilized_cities=[city.title() for city in cities]

print(capitilized_cities)
"""
"""
def cylinder_volume(height,radius):
    pi=3.14
    return height*pi*radius**2

#print(cylinder_volume(10,6))"""
"""
def date(days):
    day=days//7
    remains=days%7
    return "{} weeks {} days".format(day,remains)

print(date(10))"""


#name = input('Enter a name : ')
#print('Hello',name.title())
"""
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
"""
"""
class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        classiness = 0
        if len(self.items) > 0:
            for item in self.items:
                if item == "tophat":
                    classiness += 2
                elif item == "bowtie":
                    classiness += 4
                elif item == "monocle":
                    classiness += 5
        return classiness

me=Classy()
me.addItem("bowtie")
deneme=me.getClassiness()
print(deneme)

"""

"""
def year2Century(year):

    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):  # 100 ,200 300, 400 ... 900
            return int(str_year[0])
        else:                       # 190, 250, 450
            return int(str_year[0])+1
    else:                           # 1750, 1700, 1805
        if(str_year[2:4]=="00"):    # 1700, 1900, 1100
            return int(str_year[:2])
        else:                       # 1705, 1645, 1258
            return int(str_year[:2])+1

print(year2Century(int(input("Bir yıl giriniz: "))))
    
"""

"""
liste = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

temp=9999

for item in liste:
    if(item<temp):
        temp=item
    else:
        continue

print(temp)
"""
"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


e1=Element(1)
e2=Element(2)
e3=Element(3)

l1=LinkedList(e1)
l1.append(e2)
l1.append(e3)

a=l1.get_position(2)
print(l1.head.next.next.value)
"""
"""
def binarySearch(listData,value):
    low=0
    high=len(listData)-1
    while(low<=high):
        mid=int((low+high)/2)
        if(listData[mid]==value):
            return mid
        elif(listData[mid]<value):
            low=mid+1
        else:
            high = mid-1
    return -1

list=[1,4,6,7,11,15,20]
value=int(input("Bir değer giriniz: "))
print(binarySearch(list,value))"""


import numpy as np
import pandas as pd 
import requests
import json

#url="https://wind-bow.glitch.me/twitch-api/channels/freecodecamp"
#JSONContent=requests.get(url).json()
#content=json.dumps(JSONContent,indent=4,sort_keys=True)
#print(content)


# List of channels we want to access
channels = ["ESL_SC2", "OgamingSC2", "cretetion", "freecodecamp", "storbeck", "habathcx", "RobotCaleb", "noobs2ninjas",
            "ninja", "shroud", "Dakotaz", "esltv_cs", "pokimane", "tsm_bjergsen", "boxbox", "wtcn", "a_seagull",
           "kinggothalion", "amazhs", "jahrein", "thenadeshot", "sivhd", "kingrichard"]

channels_list = []
# For each channel, we access its information through its API
for channel in channels:
    JSONContent = requests.get("https://wind-bow.glitch.me/twitch-api/channels/" + channel).json()
    channels_list.append([JSONContent['_id'], JSONContent['display_name'], JSONContent['status'],
                         JSONContent['followers'], JSONContent['views']])



dataset = pd.DataFrame(channels_list)
dataset.columns = ['Id', 'Name', 'Status', 'Followers', 'Views']
dataset.dropna(axis = 0, how = 'any', inplace = True)
dataset.index = pd.RangeIndex(len(dataset.index))
a= dataset.sample(5)
dataset.to_csv('deneme.cvs', sep='\t', encoding='utf-8')
print(a)
