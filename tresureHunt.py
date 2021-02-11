print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Yo ho Matey!!!!!')
choice = input('If ye be brave or fool enough to face a pirates curse, proceed.type "ahoy" to get started on your quest and "quit" to exit treasure hunt \n')
if choice == "ahoy":
  choice1 = input('You are at a crossroad in a mystical city...which way do you want to go? left or right\n').lower()
  if choice1 == "left":
    choice2 = input('You\'ve come to a lake.A group of fighters are searching for you at the lake. There is an island in the middle of the lake.Type "wait" to wait for a boat in disguise. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
      choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n').lower()
      if choice3 == "yellow":
        print()
        print('YOU WON Matey!!!!!!!!!!!')
        print('Not All Treasure Is Silver And Gold, Mate,This Is The Day You Will Always Remember As The Day You Almost Caught Captain Jack Sparrow.\n')
        print('''
|__
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                                                                     BB-61/
 \_________________________________________________________________________|

''')
      elif choice3 == "red":
        print('You entered a room of fire!!!!!!!!')
        print('GAME OVER')
      elif choice3 == "blue":
        print('You are lost in the infinite ocean!!!!!!!!\n')
        print('GAME OVER')
    else:
        print('You are caught by the sea monster!!!!')
        print('GAME OVER')
  else:
      print('If you were waiting for the opportune moment, that was it.')
      print('GAME OVER')
else:
  print("Bye mate!!!!!")
