print("Lets play the fizbuzz game")
print(" for multiple of 3 =fizz \n for multiple of 5=buzz \n for multiple of 3 and 5=fizzbuzz")

print("number of times u want to play")
p=int(input())
while(p>0):
    n=int(input("enter number"))
    if(n%3==0 and n%5==0):
        print("fizzbuzz")
    elif(n%5==0):
        print("buzz")
    elif(n%3==0):
        print("fizz")
    else:
        print("your number is :",n)
    p=p-1

