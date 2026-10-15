'''
1 for snake
-1 for water
0 for gun

'''
import random

# computer = -1
computer = random.choice([0, -1, 1])

# youstr = input("Enter your choice: ")
you = int(input("Enter your choice (1 for Snake, -1 for Water, 0 for Gun): "))

youDict = {"S" : 1, "W" : -1, "g" : 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
# you = youDict[youstr]
if you not in reverseDict:
    print("Invalid choice!")

else:
    print(f"You choose {reverseDict[you]}\nComputer chooses {reverseDict[computer]}")

# print(f"You choose {youDict[you]}\nComputer Choose {reverseDict[computer]}")
# print(f"You choose {reverseDict[you]}\nComputer Choose {reverseDict[computer]}")

if(computer == you):
    print("Its draw")
else:

     if(computer == -1 and you == 1):
       print("You Win! ")

     elif(computer == -1 and you == 0):
        print("You Lose!")

     elif(computer == 1 and you == -1):
        print("You lose!")

     elif(computer == -1 and you == 0):
       print("You Win!")

     elif(computer == 0 and you == -1 ):
       print("You lose!")

     elif(computer == 0 and you == 1):
      print("You Lose!")

     else:
      print("Something want wrong")