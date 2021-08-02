# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2
a = 'Welcome\'s to'
# or
a = "Welcome's to"
b = 'The world of Science'

print(a+b)
message = f'{a} {b}'
print(message)
print(len(message))
print(message.upper())
print(message.lower())
print(dir(message))
# this removes this particular char defined inside split # and then split it
print(message.split('l'))

print(message.rsplit())
print(message.lstrip('l'))

str = "---geeksforgeeks---"
print(str.strip('-'))
print(str.lstrip('-'))
print(str.rstrip('-'))


num = -34.6
print(ascii(num))
print(abs(round(num)))

num1 = 20
num2 = '20'
print(num1 == num2)
# print(num1 + num2) gives an error message

num_2 = int(num2)
print(num1 == num_2)
