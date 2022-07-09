import random

print("                 Welcome to the Guessing Game ")
print("Playing is easy, try to correctly guess the number from 1-50.") 


def start_game():
  answer = random.randint(1,51)
  attempts = 0

  while True:
    
    try:
        player_guess = int(input("        Your Guess: "))
        
        if player_guess < 1:
          print("   TRY AGIAN! 1-50")
        
        elif player_guess > 50:
          print("   TRY AGAIN! 1-50")
        
        elif answer < player_guess:
          print("   It's lower")
          attempts += 1
          
        elif answer > player_guess:
          print("   It's higher")
          attempts += 1
          
        else:
          print("       Congrats, you got it")
          print("       The correct answer is {}".format(answer))
          print("       It took {} attempts".format(attempts))
          print("--------------------------------------------------")
          play_again = input("      Do you want to play again? (yes/no) ")
          if play_again == "yes":
            print("   Good Luck!")
            start_game()
          else:
            print("               END OF GAME")
            print("           Thanks for playing")
          break
                             
    except ValueError:
      print("   try agian, 1-50")

  

start_game()
