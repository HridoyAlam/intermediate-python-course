import random
def main():
  num_player = int(input("\tHow many player wants to Play? "))
  dice_rolls = int(input("\tHow many dice would you like to roll? "))

  print("\n")

  for j in range(0, num_player):
    
    dice_sum = 0
    for i in range(0,dice_rolls):
      roll = random.randint(1, 6)
      dice_sum +=roll
      if roll == 1:
        print(f'\tYou rolled a {roll} ! Crictical Fail')
      elif roll == 6:
        print(f'\tYou rolled {roll} ! Critical Success')
      else:
        print(f'\tYou rolled {roll}')
    print(f'\tPlayer {j+1}\t: have rolled total of {dice_sum}\n\n')

if __name__== "__main__":
  main()