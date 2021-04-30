"""def any():
    print(var+1,end=' ')

var=1
any()
print(var)"""
def fun(x):
    global y
    y=x*x
    return y
fun(2)
print(y)