# *args     : allows you to pass multiple non key arguments => packs(store) on tuple
# **kwargs  : allows you to pass multiple keyword arguments => packs(store) on dictionary
# * is unpacking operator

#  *args converts all arguments in tuple format
#  args name can vary

# *args (Arbitrary Positional Arguments) , The * unpacks the arguments into a tuple.

def addition(*args):
    print(type(args))
    total = 0;
    for arg in args:
        total += arg
    return total

print(addition(1,2,3,4)) # you can pass multiple args withput different parameters

#  kwargs name can vary

def name(**kwargs):
    print(type(kwargs))

    for key,value in (kwargs.items()) :
        print(f"{key} : {value}")

print(name(fn="John" , ln="Doe"))