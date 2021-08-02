from collections import Counter
courses = ['History', 'Math', 'Physics']

courses.append('CompScience')
print(courses)
print(len(courses))  # 4
# ['History', 'Math', 'Physics', 'CompScience']
print(courses[1:3])

for i in enumerate(courses):
    print(i)


list_of_number = [1, 2, 4, 1, 3, 4]
list_to_counter = Counter(list_of_number)
for key, value in list_to_counter.items():
    print(key, value)


num = [1, 2, 4, 5, 10, 1]
arr = []
for i in range(len(num)):
    if num[i] in arr:
        print("index - ", i, 'value - ', num[i])
        break
    else:
        arr.append(num[i])

courses = ['History', 'Math', 'Physics']
course2 = ['English', 'Hindi']
# adds the list to the courses insted of individual values
# courses.insert(0, course2)  # if we append(course2) this will also add the list
print(courses)
courses.insert(0, 'Art')
courses.extend(course2)
print(courses)

popped = courses.pop()
print(courses)
print(popped)

print("remove english")
courses.remove('English')
print(courses)

# by using the sort the orignal list is been sorted
value = [1, 3, 4, 2, 0]
value.sort()
print(value)

value.sort(reverse=True)
print(value)

# what if we want to sort without altering the main list we use sorted
value = [1, 3, 4, 2, 0]

sorted_courses = sorted(value)  # sorted version
print(sorted_courses)
print(value)

# min max and sum

print(min(value))
print(max(value))
print(sum(value))

# find the index of certain value
print("Index of Math : ", courses.index('Math'))

# gives an erro ValueError: 'English' is not in list
#print("Index of Math : ", courses.index('English'))

# Boolean to check if that element in list or not
print('Art' in courses)
print('English' in courses)

for index, value in enumerate(courses, start=1):
    print(index, value)


list_of_words = ["Welcome", "Aman", "to", "our",
                 "billionaire's", "club", "you are a billionaire now"]

sentence = ' '.join(list_of_words)
print(sentence)

string_to_list = sentence.split(' ')
print(string_to_list)

# Tupils (Immutable)

tuples_1 = (1, 2, 4, 5)
tuples_2 = tuples_1

print(tuples_1)
print(tuples_2)

# tuples_1[0] = 9
# # we cannot change the value or add
# tuples_1.pop() cannot pop or remove

# Set
# sets are used to test whether a value is part of a set membership test
# null set
set_1 = set()
print(type(set_1))

# the sets are not in order format
set_1 = {'History', 'Math', 'Physics', 'Math'}
print(set_1)  # when you print the set everytime the order

set_1.pop()
print(set_1)
set_1.add('English')
print(set_1)

# see for the comman things between two set is easier

set_1 = {'History', 'Math', 'Physics'}
set_2 = {'History', 'English', 'Chemestry'}

print(set_1.intersection(set_2))

# see all the courses in both sets this wont print the duplicate
print(set_1.union(set_2))

# see all the uncomman courses
print(set_1.difference(set_2))  # for set1

print(set_2.difference(set_1))  # for set2


# Empty list tuples and sets

set_empty = set()  # empty set
# set_empty1 = {}
# # this will create empty dictionary

tuple_empty = ()
tuple_empty1 = tuple()

list_empty1 = []
list_empty2 = list()


print(type(set_empty))


print(type(tuple_empty))
print(type(tuple_empty1))

print(type(list_empty1))
print(type(list_empty2))

# <class 'set'>
# <class 'tuple'>
# <class 'tuple'>
# <class 'list'>
# <class 'list'>
