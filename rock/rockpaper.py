import random

user_wins=0
comp_wins=0
options=["rock","paper","scissor"]

while True:
    user_input=input("Type Rock/Paper/Scissor or type q to quit  :").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    comp_pick=options[random_number]
    print("computer picks",comp_pick)

    if user_input=="rock"and comp_pick=="scissor":
        print("you won")
        user_wins+=1
    elif user_input=="scissor"and comp_pick=="paper":
        print("you won")
        user_wins+=1
    elif user_input=="paper"and comp_pick=="rock":
        print("you won")
        user_wins+=1
    elif user_input==comp_pick:
        print("its a draw")
        user_wins+=0
        comp_wins+=0
    else:
        print("computer wins")
        comp_wins+=1
print("you won",user_wins,"times")
print("computer",comp_wins,"times")
print("Good Bye Brow!!! :)")

s=input()