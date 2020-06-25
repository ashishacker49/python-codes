print("Api Calculator")
print("---------built by Ashish Kumar-----------")
n=int(input("Enter Number of refereed Journals You published"))
n=n*15
p=int(input("Enter Number of Non-refereed Journals but having ISBN/ISSN numbers You published"))
p=p*10
q=int(input("Enter Number of Conferrence Procedings "))
q=q*7
total=n+p+q
r="yes"
f="no"
p=input("Are you publishing this first time?\n Type yes or no")
if p==r:
            v=0.6*total
            b=float(total+v)
            print("your Score is"+str(b))
else:
    n=0.4*total
    m=n+total
    print("your score is"+str(m))
print("-------program ends------------")
print("Thankyou ")
#built by Ashish Kumar
    
    
    
