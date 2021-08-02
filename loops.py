nums = [1, 2, 2, 3, 4]

for i in nums:
    if i == 3:
        print('Found The value')
        break
    else:
        print(i)

# 1
# 2
# 2
# Found The value

# if we want to just ingnore a value but not break out of the loop

for i in nums:
    if i == 3:
        continue
    else:
        print(i)

# 1
# 2
# 2
# 4

for i in nums:
    for letter in 'abc':
        print(i, letter)
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c

for i in range(1, 10, 2):
    print(i)
