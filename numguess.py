import random
def guessnum(a):
    a=0
    b=random.randint(1,20)
    while(a!=b):
        if a>b:
            print("guess lower")
        elif a<b:
            print("guess higher")
        a=int(input("guess again"))
    print(":good job")
        
guess=int(input("guess a num"))
guessnum(guess)
