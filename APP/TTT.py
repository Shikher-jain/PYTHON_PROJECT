'''
 1 | 2 | 3 
 4 | 5 | 6 
 7 | 8 | 9 
'''

#  00000000001111111111222222222     
#  01234567890123456789012345678
#  |||||||||||||||||||||||||||||
s="1 | 2 | 3 4 | 5 | 6 7 | 8 | 9"

l=list(s)
print(l)

print(l)

def display():
    for i in range(29):
        print(l[i] ,end="")
        if i==9 or i ==19:
            print()    
used =[]
win=-1
turn=1
r=9 #round
display()
while r:
    if turn == 1:
        print("\nX turn")
        turn = 0
    else:
        print("\nO turn")
        turn = 1
    X_O=(input(" \nEnter b/w 1-10 \n"))
    x_o=int(X_O)
    if X_O in used:
        raise Exception(f"Invaild !!\n\n {X_O} is already used")
    else:
        if (x_o < 10 and int(X_O) > 0 and turn==0):
            l=list(map(lambda x: x.replace(X_O,"X"),l))
            display()
        if (int(X_O) < 10 and int(X_O) > 0 and turn==1):
            l=list(map(lambda x: x.replace(X_O,"O"),l))
            display()
        used.append(X_O)
        if r>=4:
            if (((l[0]=="X" and l[4]=="X") and l[8]=="X") or (l[10]=="X" and (l[14]=="X" and l[18]=="X")) or ((l[20]=="X" and l[24]=="X") and l[28]=="X") or ((l[0]=="X" and l[10]=="X") and l[20]=="X") or ((l[4]=="X" and l[14]=="X") and l[24]=="X") or ((l[8]=="X" and l[18]=="X" )and l[28]=="X") or ((l[0]=="X" and l[14]=="X") and l[28]=="X") or ((l[8]=="X" and l[14]=="X") and l[20]=="X")  ):
                win = 1
                break
            
            elif ((l[0]=="O" and l[4]=="O" and l[8]=="O") or (l[10]=="O" and l[14]=="O" and l[18]=="O") or (l[20]=="O" and l[24]=="O" and l[28]=="O") or (l[0]=="O" and l[10]=="O" and l[20]=="O") or (l[4]=="O" and l[14]=="O" and l[24]=="O") or (l[8]=="O" and l[18]=="O" and l[28]=="O") or (l[0]=="O" and l[14]=="O" and l[28]=="O") or (l[8]=="O" and l[14]=="O" and l[20]=="O")  ):
                win = 0
                break
            else:
                win =-1
                
        r-=1
if win == 1 :
    print("\nX is winner ")     
elif win==0:
    print("\nO is Winner")
else :
    print("\nDRAW")



# 00 , 04 , 08 ,
# 10 , 14 , 18 ,
# 20 , 24 , 28