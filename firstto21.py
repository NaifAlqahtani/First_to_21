import random

number = 0
addition = 1
turn = random.choice(['cpu','user'])

if turn == 'cpu':
    print("\n\n0\nComputer Starts!")
elif turn == 'user':
    print("\n\n0\nYou Start!")



while number < 21:
    
    def nextCheckpoint(value):
        if number <= 5:
            return 5
        elif value > 5 and number <= 9:
            return 9
        elif value > 9 and number <= 13:
            return 13
        elif value > 13 and number <= 17:
            return 17
        elif value > 17:
            return 21


    if turn == 'user':
        addition = int(input("Choose 1,2 or 3 to add to the sequence: "))
        if addition > 0 and addition < 4:
            number = number + addition
            print(number)
            print()
            if number < 21:
                turn = 'cpu'
        else: 
            print("please enter a number from 1 to 3\n")

    distance = 21 - number
    cpuChoice = 0

    cpuNumber = (nextCheckpoint(number)-number)

    if turn == 'cpu':
        if cpuNumber > 3 or cpuNumber < 1:
            cpuChoice = random.randint(1,3)
        elif distance > 3:           
            cpuChoice += cpuNumber
        elif distance == 3:
            cpuChoice = 3
        elif distance == 2:
            cpuChoice = 2
        elif distance == 1:
            cpuChoice = 1
        print("The computer chose to add", cpuChoice)
        number = number + cpuChoice
        print(number)
        print()
        if number < 21:
            turn = 'user'

    if number >= 21 and turn == 'user':
        print("You won!")
    elif number >= 21 and turn == 'cpu':
        print("CPU won!")