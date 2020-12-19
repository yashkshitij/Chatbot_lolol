#Mangaka is the name of our chat bot
import random
import time
import json
responses= ["ohio","konichiwa","sup"]

#goku , naruto , natsu , ash and pikachu

def mangakaspeaks(protaganist,msg) :
    print(protaganist +": " +  msg )

def userspeaks():
    return input("enter message= " ).lower()

#where actaul work with happen
def start_bot(goku=False,naruto=False):
    quit_button = "q"
    print(f"mangaka is starting! quit by replying {quit_button}")
    while True:
          managaka_message= random.choice(responses)
          mangakaspeaks( mangaka + ": "+ managaka_message)
          reply = userspeaks()
          if reply == quit_button :
            quit_mangaka()
            break
def quit_mangaka():
    print("sayonara")
def menu():
    print("_____Menyu_____\n [a]Talk to goku\n [b]Talk to naruto\n[q] Quit Application \n press a or b or q")
    useranswer= userspeaks()
    if useranswer =="a":
        start_bot(True,False)
    elif useranswer =="b":
        start_bot(False,True)
    elif useranswer == "q":
        quit_mangaka()
menu()
