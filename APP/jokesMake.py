import pyjokes
for i in range(int(input("Enter NO. Of jokes : "))):
    joke =pyjokes.get_joke()
    print("\n",joke)