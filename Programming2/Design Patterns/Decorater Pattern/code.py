# class Decorator(object):
#     def __init__(self,original_function):
#         self.original_function = original_function
#     def __call__(self,*args,**kwargs):
#         print("This is executed")
#         return self.original_function(*args,**kwargs)

# @Decorator    
# def example():
#     print("Ths is is example")

# example()

#decorater
def sytemhello(func):
    def wrapper():
        print("This is system hello")
        func()
    return wrapper

def hello(func):
    def wrapper():
        print("Hello")
        func()
    return wrapper

# @sytemhello
# @hello
# def func():
#     print("I am anique")

# func()

# def robot():
#     print("I am robot")








def convert_str(func):
    def wrapper(x):
        return str(func(x))
    return wrapper

def roundof(func):
    def wrapper(x):
        return round(func(x),2)
    return wrapper
@convert_str
@roundof
def convert_celcius(x):
    return (x-32)*(5/9)


print(type(convert_celcius(102)))

