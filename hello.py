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
