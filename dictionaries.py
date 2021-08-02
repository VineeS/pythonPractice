student = {'name': 'john', 'age': 23, 'courses': ['Math', 'Science']}

print(student.keys())
print(student.values())
print(student.items())

# if the key does not exist the dict will trough an error
# hence we use get
print(student.get('name'))

print(student.get('number', 'Not Found'))

student['Phone'] = 9312690090
student['Phone'] = 7126539090

print(student)

# update multiple values in dict

student.update({'name': 'Vinee', 'age': 29})
print(student)

# delete an key

del student['name']
print(student)

age = student.pop('age')
print(student)

# is operator
a = 1
b = 1

print(id(a))
print(id(b))

print(a is b)  # True

a = [1, 2]
b = [1, 2]

print(id(a))  # 4545633248
print(id(b))  # 4547187648

print(a is b)  # False
print(a == b)  # True

a = 1
b = a

print(id(a))
print(id(b))

print(a is b)
