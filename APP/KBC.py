# KBC
question=[
    ["question 01","option 01","option 02","option 03","option 04","answer(1-4)->",1],
    ["question 02","option 01","option 02","option 03","option 04","answer(1-4)->",2],
    ["question 03","option 01","option 02","option 03","option 04","answer(1-4)->",3],
    ["question 04","option 01","option 02","option 03","option 04","answer(1-4)->",4],
    ["question 05","option 01","option 02","option 03","option 04","answer(1-4)->",1]
]

levels=[100,2000.3000,5000,10000,20000,40000,80000,160000,320000,700000]
money=0
for i in range(len(question)):
    ques=question[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"{ques[0]}\n")
    print(f"a.{ques[1]}\tb.{ques[2]}\nc.{ques[3]}\td.{ques[4]}")

    reply=int(input("Enter your answer (1-4) or 0 for quit:\n"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==ques[-1]):
        print(f"Correct answer you won Rs. {levels[i]}")
        if(i==3):
            money=10000
        elif(i==8):
            money=32000
        elif(i==13):
            money=10000000
    else:
        print("Incorrect Answer")
        break
print(f"Your money is {money}")
print("Thanks For Playing")