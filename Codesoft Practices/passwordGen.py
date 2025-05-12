import array
import random

#Minimum lenght of password is 5 which means l>4
l=int(input("Enter The Lenght Of Password (Lenght>4): "))  
password=''

if(l>4):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    lower_chr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 

    upper_chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 

    spe_symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']  

    combination = digits + upper_chr + lower_chr + spe_symbols 

    rand_digit = random.choice(digits) 
    rand_upper = random.choice(upper_chr) 
    rand_lower = random.choice(lower_chr) 
    rand_symbol = random.choice(spe_symbols) 
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 

    # print(temp_pass)

    for for_iterate in range(l-4):
        temp_pass+=random.choice(combination)

        print(temp_pass)
        tr=array.array("u",temp_pass)
        random.shuffle(tr) #shuffling makes password more strong
        # random.shuffle(tr) #if you want more than apply more shuffles
        
    for i in tr:
        password+=i
    print(password)  #Final PassWord
else:
    print("Invalid Lenght\nKindly Enter Valid Length\n(i.e. : > 4)")