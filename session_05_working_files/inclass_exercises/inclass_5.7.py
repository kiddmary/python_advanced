# 5.7:  Call callit(), passing greet as argument, then inside callit(), call the
# function through the argument (do not call greet()).

def callit(func):
    func()

def greet():
    print('hello, world!')

def goodbye():
    print('Goodbye, world!')

callit(greet)
callit(goodbye)