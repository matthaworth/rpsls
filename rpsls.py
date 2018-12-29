import random
import os
options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
loop=True
playerwon=0
playerscore = 0

def print_menu():
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Rock"
    print "2. Paper"
    print "3. Scissors"
    print "4. Lizard"
    print "5. Spock"
    print "6. Exit"
    print 67 * "-"

def format_input(choice):
    choice -= 1
    playerchoice=options[choice]
    print ("Player chose ") + playerchoice
    print ("Computer chose ") + cmpchoice
    compare(playerchoice, cmpchoice)

def replay():
    reply = str(raw_input('Would you like to play again (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    else:
        return False

def compare(playerchoice, cmpchoice, ):
    global playerscore
    global playerwon
    playerwon = 0
    if playerchoice == "Lizard" and (cmpchoice == "Paper" or cmpchoice == "Spock"):
      playerwon = 1
    elif playerchoice == "Paper" and (cmpchoice == "Rock" or cmpchoice == "Spock"):
      playerwon = 1
    elif playerchoice == "Rock" and (cmpchoice == "Lizard" or cmpchoice == "Scissors"):
      playerwon = 1
    elif playerchoice == "Scissors" and (cmpchoice == "Lizard" or cmpchoice == "Paper"):
      playerwon = 1
    elif playerchoice == "Spock" and (cmpchoice == "Rock" or cmpchoice == "Scissors"):
      playerwon = 1
    elif playerchoice == cmpchoice:
        playerwon = 3
    else:
        playerwon = 2
    if playerwon == 1:
        playerscore += 1
        print("You Win! You're current score is: " + str(playerscore))
    elif playerwon == 2:
        print("You Lose! You're current score is: " + str(playerscore))
    elif playerwon == 3:
        print("Its a tie You're current score is: " + str(playerscore))

while loop:
    cmpchoice = options[random.randint(0,4)]
    os.system('clear')
    print_menu()
    choice = input("Enter your choice [1-5]: ")
    if choice==1:
        format_input(choice)
        loop=replay()
    elif choice==2:
        format_input(choice)
        loop=replay()
    elif choice==3:
        format_input(choice)
        loop=replay()
    elif choice==4:
        format_input(choice)
        loop=replay()
    elif choice==5:
        format_input(choice)
        loop=replay()
    elif choice==6:
        print "Exiting"
        loop=False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")
