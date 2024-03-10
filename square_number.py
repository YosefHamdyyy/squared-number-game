
print("welcome to the square game")
coins_number=int(input("enter coins number"))
X=coins_number
while coins_number> 0 :
    p1=int(input("p1 choose a number")) 
    while True : 
        if int(p1**0.5)**2== p1 and p1<=coins_number and p1<X:
            break
        else : p1 =int(input("please enter a valid number"))
    coins_number=coins_number-p1
    print("number of coins = " ,coins_number)
    if coins_number==0 :
     print("p1 wins")
     break
    p2=int(input("p2 choose a number")) 
    while True : 
        if int(p2**0.5)**2== p2 and p2<=coins_number: 
            break
        else : p2 =int(input("please enter a valid number"))
    coins_number=coins_number-p2
    print("number of coins = " ,coins_number)
    if coins_number==0 :
     print("p2 wins")
     break