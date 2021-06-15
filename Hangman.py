"""
This is a hangman game made for beginners .
This is a two player game
"""







import time
import random
def gamedisplay(x):   
    sc=[["      _____",
        "      |   |",
        "      O   |",
        "     /|\  |",
        "     / \  |",
        "          |",
        "__________|"],
["      _____",
 "      |   |",
 "      O   |",
 "     /|\  |",
 "     /    |",
 "          |",
 "__________|"],
 ["      _____",
 "      |   |",
 "      O   |",
 "     /|\  |",
 "          |",
 "          |",
 "__________|"],
 ["      _____",
 "      |   |",
 "      O   |",
 "     /|   |",
 "          |",
 "          |",
 "__________|"],
 ["      _____",
 "      |   |",
 "      O   |",
 "      |   |",
 "          |",
 "          |",
 "__________|"],
 ["      _____",
 "      |   |",
 "      O   |",
 "          |",
 "          |",
 "          |",
 "__________|"],
 ["     _____",
 "      |   |",
 "          |",
 "          |",
 "          |",
 "          |",
 "__________|"]]
    for i in sc[x]:
        print(i)


def setplword(plword,word,guess):
    for i in range(len(word)):
        if word[i]==guess:
            break
    plword[i]=word[i]
    return plword,word

words=open("D:\Microsoft VS Code\Pirple\Projects\words.txt","r")
def play(x):
    word=""
    if x==1:
        word=random.choice(words)
    else:
        word=input("Enter the word : ")
    print(chr(27) + "[2J") 
    wordlist=list(word)
    plwordlist=[0]*len(word)
    tries=6
    a=[]
    while(tries>0):
        guess=input("Enter Your Guess : ")
        post=0
        for i in wordlist:
            if i==guess:
                post=2
                gamedisplay(tries)
                plwordlist,a=setplword(plwordlist,wordlist,guess)
                stre=""
                for i in plwordlist:
                    stre+=str(i)
                if stre!=word:
                    print("Your guess is present in the word.\n")
                else:
                    post=1
                    print("You have guessed the word : ",word)
                    break
                for i in plwordlist:
                    if i==0 or i=="0":
                        print("_",end=" ")
                    else:
                        print(i,end=" ")
                print(" ")
                break
        wordlist=a
        if post==1:
            break
        elif post==0:
            print("Your guess is not present in the word.\n")
            tries-=1
            gamedisplay(tries)
        else:
            continue
    else:
        print("Your chances are over.")
        print("The word was ",word)
                            

print("Welcome ....")
print("  |    |     /\     |\  |   /-----   |\    /|     /\    |\  |")
print("  |----|    /--\    | \ |   |  ___   | \  / |    /--\   | \ |")
print("  |    |   /    \   |  \|   \----|   |  \/  |   /    \  |  \|")


print("For single player enter 1.")
print("For dual player enter 2.")

while(True):
    ch=input("Enter your choice : ")
    play(ch)
    c=input("Do you want to play again?(Y/N)")
    if c=="Y" or c=="y":
        continue
    else:
        break
print("exiting...")
time.sleep(3)
print("Goodbye")
