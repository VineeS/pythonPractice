def hello_func():
    pass


print(hello_func)
# this will return <function hello_func at 0x1024ccef0>

# To execute the function you need to add ()
print(hello_func())


def hello_functions():
    return "Hello Function"


print(hello_functions().upper())


# This can be any
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# Special Symbols Used for passing arguments:-

# 1.)*args (Non-Keyword Arguments)


# 2.)**kwargs (Keyword Arguments)
student_info('Math', 'Art', 123, name='Vinee')
