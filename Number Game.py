import random
playing = True
num = str(random.randint(10,20))
print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 Point!")
while playing:
  guess = input("Give me your best guess! \n")
  if num == guess:
    print("You win the game!")
    print("The number was", num)
    break
  else:
    print("Wrong, I'm coming for u. Try again or else. \n")