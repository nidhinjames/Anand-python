def fxy(f, x, y):
    return f(x) + f(y)

def square(x):
    return x*x

a=fxy(square, 10, 10)
print a
