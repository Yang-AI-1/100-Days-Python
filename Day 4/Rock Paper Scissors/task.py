rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
rand_numb = random.randint(0,2)
choices = [rock,paper,scissors]
select = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 For Scissors."))

if select >= 3 or select <0:
    print("That's not even valid.You loose!")

elif select == 0 or 1 or 2:
    print(choices[select])
    print("The computer chose:")
    print(choices[rand_numb])


if select == 0 and rand_numb == 0:
    print("That's a draw.")
elif select == 0 and rand_numb == 1:
    print("you loose.")
elif select == 0 and rand_numb == 2:
    print("You win")
elif select == 1 and rand_numb == 0:
    print("You win.")
elif select == 1 and rand_numb == 1:
    print("That's a draw.")
elif select == 1 and rand_numb == 2:
    print("You lose!")
elif select == 2 and rand_numb == 0:
    print("You loose!")
elif select == 2 and rand_numb == 1:
    print("You win!")
elif select == 2 and rand_numb == 2:
    print("That's a draw!")

