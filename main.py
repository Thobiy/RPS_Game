import random

while True:
 possible_option = ["Rock", "Paper", "Scissor"]

 
 CPU = random.choice(possible_option)
 Player = None
 while Player not in possible_option:
        Player = input("pick an option from R, P, S: ")
        if Player == "R":
            Player = possible_option[0]
        elif Player == "P":
            Player = possible_option[1]
        elif Player == "S":
            Player = possible_option[2]
        else:
                print("Error, Enter correct input again")
        


 if Player == CPU:
    print("CPU", {CPU})
    print("Player", {Player})
    print ("it is a tie")
    continue

 elif Player == "Rock":
    if CPU == "Paper":
            print("CPU",{CPU})
            print("Player", {Player})
            print("You Lose")
    else:
            CPU == "Scissor"
            print("CPU", {CPU})
            print("Player", {Player})
            print("You Win")
 elif Player == "Scissor": 
    if CPU == "Rock":
            print("CPU", {CPU})
            print("Player", {Player})
            print("You Lose")
    else:
            CPU == "Paper"
            print("CPU", {CPU})
            print("Player", {Player})
            print("You Win")
 elif Player == "Paper":
    if CPU == "Scissor":
            print("CPU", {CPU})
            print("Player", {Player})
            print("You Lose")
    else:
            CPU == "Rock"
            print("CPU", {CPU})
            print("Player", {Player})
            print("You Win.")

 new_game = input("Play again (y/n): ")
 if new_game.lower() != "y":
    break
