import random

def user():
    user_choice=str(input('enter rock or paper or scissor'))
    while user_choice not in ('rock','paper','scissor'):
       print('invalid choice, try again')
       user_choice=str(input('enter rock , paper ,scissor')).lower()
    return user_choice

def comptr():
    computer_choice =random.choice (['rock','paper','scissor'])
    return computer_choice


def win(user,computer):
 if user==computer :
     return "its a tie"
 elif (user=="rock" and computer=="paper") or (user=="paper" and computer=="scissor") or (user=="scissor" and computer=="rock"):
    return "computer win"
 else:
    return "user win"
def game() :
   print('lets play rock,paper,scissor')
   user_choice=user()
   computer_choice=comptr()
   print(f"you choose:{user_choice}")
   print(f"computer choose:{computer_choice}")
   result=win(user_choice,computer_choice)
   print(result)
game()   
 



      