#DiceRoll.py
#Name: Aurora Gunubu
#Date: 3/1/25 
#Assignment:
import random
import math
def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceTotal = dice1 + dice2
    rolls[diceTotal - 1] = rolls[diceTotal - 1] + 1 

  #find the sum total of the two dice
  
  
  #print statictics for dice rolls
  dice = 1
  for count in rolls:
    percentage = round(count/10000 * 100)
    print(dice, ":", count)
    print("Percentage:", percentage,"%")
    dice = dice + 1

if __name__ == '__main__':
  main()
