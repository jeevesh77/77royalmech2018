import random

a={1:'r',2:'p',3:'s'}

while True:
    p=input("your choice r/p/s:")

    c=a[random.randint(1,3)]

    print("You chose:",p,"computer chose:",c)
    if(p==r):
    	print("p wins")
    elif(r==s):
    	print("s wins")
    elif(s==p):
        print("s wins")
    
                   	
