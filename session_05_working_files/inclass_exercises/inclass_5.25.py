# 5.25:  greet has been assigned to callit.  Call greet inside the function.
def callit(arg):
    arg()
def greet():
    print('hello, world')

callit(greet)