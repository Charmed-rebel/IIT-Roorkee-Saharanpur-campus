def add(a,b):
    return a+b    
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: cannot divide by zero."
def mod(a,b):
    return a%b
def gcd(a,b):
     r = a%b 
     if r==0:
        result = b
        return result
     else :
        rem = r
        return gcd(b,rem)
    