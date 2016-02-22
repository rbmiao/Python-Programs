import math

'''
You have started a restaurant and are trying to make it easier to take can calculate orders.
Since your restaurant only sells 6 different items, you assign each one to a number, as below:
1, Chicken, $3.5
2, French Fried, $2.5
3, Hamburger, $4.0
To quickly take orders, you program should allow the user to type a string of numbers and then
it should calculate the cost of the order. For example, 322, mean the order includes:  one
hamburger(3), one French Fries(2), and one french fries(2). The total cost will be $9
'''

__author__ = 'RongbingMiao'

# Put items into a list of tuples
items = [(1, 'Chicken', 3.5), (2, 'French Fries', 2.5), (3, 'Hamburger', 4.0),
         (4, 'Hotdog', 3.5), (5, 'Large Drink', 1.75), (6, 'Medium Drink', 1.50)]

order = []

s = 322456
tot = 0.0


for c in str(s):
#    print(c)
    order.append([items[int(c)-1][0],items[int(c)-1][1], items[int(c)-1][2]])
#    order.append(items[int(c)-1][1])
#    order.append(items[int(c)-1][2])

    if   int(c) == 3:
        tot += 4.0
    elif int(c) == 2:
        tot += 2.5
    elif int(c) == 1:
        tot += 3.5
    elif int(c) == 4:
        tot += 3.5
    elif int(c) == 5:
        tot += 1.75
    elif int(c) == 6:
        tot += 1.5
    else:
        pass

print("\nYour order is:\n")
for i in range(len(order)):
##    print(order[i])
    print(order[i][0], order[i][1], order[i][2])


print("\nTotal is: ", tot)
