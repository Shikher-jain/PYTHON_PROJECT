# ROCK PAPER SCISSOR
import random
def RPS():
    scoreC=0  #computer score 
    scoreU=0  #user score 
    scoreD=0  #draw score 
    print("WELCOME")
    temp=n=int(input("How many times you want to play:"))
    while(n):
        print(f"\n It's {n} times")
        user=input("\nEnter : \nR for ROCK \nP for PAPER \nS for SCISSORRS \n=>")
        if (user=="R" or user=="r"):
            user= -1
        elif (user=="P" or user=="p"):
            user= 0
        elif (user=="S" or user=="s"):
            user= 1
        else:
            print("Invalid Alphabhets!! ")
            n+=1

        comp = random.randint(-1,1)
        if(comp==user):
            print("DRAW")
            scoreD=scoreD+1

        elif( (user==-1 and comp==0) or (user==0 and comp==1) or (user==1 and comp==-1) ):
            print("YOU LOSE")
            scoreC=scoreC+1

        else:#( (user==-1 and comp==1) or (user==0 and comp==-1) or (user==1 and comp==0) ):
            print("YOU WIN")
            scoreU=scoreU+1
        n=n-1
    print(f"Score will be:\nUSER\tBOT\tDRAW\n{scoreU}\t{scoreC}\t{scoreD}")
    if(scoreC==scoreU):
        print("DRAW")
    elif(scoreU<scoreC):
        print("YOU LOSE")
    else:
        print("YOU WIN")

    if(n!=temp):
        ch=input("\nE for Exit\nA for Play Again\n")
        if (ch=="e" or ch=="E"):
            print("Thanks For Playing\nExiting...")
            exit()
        elif (ch=="A" or ch=="a"):
            RPS()
        else:
            print("Invalid Alphabhets!! ")

RPS()