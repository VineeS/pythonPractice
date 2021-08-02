# condition = False --> False Value
# condition = None --> False Value
# condition = 0 --> False Value
# condition = -1  # --> any number other than 0 true Value
# condition = '' --> False Value
# condition = () --> False Value
# condition = [] --> False Value

condition = {}  # --> False Value

if condition:
    print('True')
else:
    print('False')
