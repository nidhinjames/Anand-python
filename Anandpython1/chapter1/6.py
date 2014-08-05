numcalls=0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    print numcalls
    print x*x



square(12)
square(10)
