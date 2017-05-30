import sys

c = 1

if (len(sys.argv) > 1):
    n = sys.argv[1]
else:
    n = input("Type a number: ")
    

    try:    
        n = int(n)
        
    except ValueError:
        print("NAN: Input invalid")
        n = input("Type a number: ")

    

print("Fizz buzz counting up to {0}".format(n))

for c in range (n + 1):
    if c == 0:
       print     
    elif (c % 3 == 0) and (c % 5 == 0) :
        print("Fizz Buzz")
    elif (c % 3) == 0:
        print("Fizz")
    elif (c % 5) == 0:
        print("Buzz")
    else:
        print(c)