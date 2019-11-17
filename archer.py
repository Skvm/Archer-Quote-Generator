import random
# string = ['a', 'b', 'c']
with open('quotes.txt', 'r') as quotes:
	quote = quotes.readlines()
print (random.choice(quote))