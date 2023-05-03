# This is the second commit to the repository. This commit fixes the errors in the code.
# Author: Daniel Johnson
# Creation Date: 05/03/2023


import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print ('Gobbles you down in one bite!')


displayIntro()
caveNumber = chooseCave()
checkCave(caveNumber)
    
print("Thanks for playing")
