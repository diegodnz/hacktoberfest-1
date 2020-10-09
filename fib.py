def fib(n):    
    if n == 0:
        return 0   
    elif n == 1:
        return 1          
    else:
        print("0\n1")
        x = 0
        y = 1
        z = 1
        print(z)
        for num in range(n-2):
            x = y
            y = z
            z = x + y
            print(z)
        return ""

print(fib(5000))
