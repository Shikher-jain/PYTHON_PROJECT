import array
import random

l=5
p=''
spe_symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']  

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
spe_sym=['`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[','{',']','}','\\','|',';',':','"',"'",'/','?','.','>',',','>']
print("len",len(spe_sym))
print("len",len(spe_symbols))
for i in range(l):
    RAND_DIGITS=random.choice(DIGITS)
    print(RAND_DIGITS)
    p+=RAND_DIGITS
# print(p)
tr=array.array('u',p)
random.shuffle(tr)
# print(tr)
passwoord=''
for i in tr:
    passwoord+=i
print(passwoord)