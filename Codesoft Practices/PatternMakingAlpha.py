
def Matching(name):
    s=len(name)
    # for letter ,i in zip(range(ord('a'), ord('z')+1),range(len(name))):

    for i in range(len(name)):
        for letter in range(ord('a'), ord('z')+1):
            print(chr(letter))
            if chr(letter)==name[i]:
                print(chr(letter))
                
    

# Matching(list(input("Enter name in small alphabets : ")))
Matching("shikher")
# "shikher"