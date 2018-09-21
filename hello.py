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