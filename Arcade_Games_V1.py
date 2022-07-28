"""
Fliename: Arcade_Games.py
Author: Albert Zhou
Date: 2/07/2022
Description: Rigged Individual games put into a menu for assessment.
"""

#libraries
import random
import time

#function for the user penalties during certain games
def exit_command(user_points, penalty):
    user_points -= penalty
    print("such a shame. A penalty of {} points has been taken from your total, leaving you with {} points. " .format(penalty, user_points))
    #sends the users points back to the previous function
    return user_points

#start of number guessing game
def number_guesser(user_points):
    #rules and specifications
    print("""Welcome to the number guessing game.
The prize is 90 points
Guess a number between 1 - 100
You have to get within a range of 3 to win.
Each try will take 10 points from you.
You cannot leave the game.
Good luck! """)
    valid_entry = False
    while not valid_entry:

        #counts the amount of tries the user takes
        count = 0
        #randomly generated number from 1 - 100
        computer_random_number = random.randint(1, 100)
        valid_input = False
        while not valid_input:
            try:
                user_number_guess = int(input())
                valid_input = True
            except ValueError:
                #if user enters a string or anything either than an integer
                print("please enter a interger between 1 - 100 ")
                valid_input = False

            if valid_input:
                #ensuring user enters an integer between 1 and 100
                if user_number_guess <= 0 or user_number_guess > 100:
                    print("please enter a interger between 1 - 100 ")
                    valid_input = False

            if valid_input:
                if user_number_guess != computer_random_number:
                    count += 1
                    number_difference = computer_random_number - user_number_guess
                    #absolute value of the difference between the computers number and the users guess
                    abs_number_difference = abs(number_difference)

                    #rigging the computers number to increase by 3 if users guess is within 3
                    if abs_number_difference < 4:
                        computer_random_number += 3

                    #randomizing the computers number again if it passes 100
                    if computer_random_number > 100:
                        computer_random_number -= random.randint(30, 60)

                    if user_number_guess > computer_random_number:
                        print("My number is lower. ")
                               
                    elif user_number_guess < computer_random_number:
                        print("My number is higher. ")

                    elif user_number_guess == computer_random_number:
                        print("My number is lower. ")
                           
                    valid_input = False

                else:
                    #multiplies the users guess count by 10
                    penalty = count*10
                    user_points -= penalty - 90
                    print("Good job pal! My number was {}, and you got it in {} tries. " .format(computer_random_number, count))
                    print("You have recieved 90 points, and have lost {} points. Your total is now {}. " .format(penalty, user_points))

        #if the user wants to play again
        valid_entry = True      
        play_again = input("Would you like to play again? Yes/No ")


        while play_again.lower() != "yes" and play_again.lower() != "no":
            play_again = input("Please enter Yes or No to play again. ")

        if play_again == "yes":
            print("Great. You know the rules, Enter a number from 1 - 100. ")
            valid_entry = False

    print("Alright, go play something else. ")


#Paper Scissors Rock Game
def PSR_game(user_points):
    penalty = 10

    #computer win outcome
    WIN_OUTCOME = {"paper": "rock",
                   "scissors": "paper",
                   "rock": "scissors"}

    #computer draw outcome
    DRAW_OUTCOME = {"paper": "paper",
                    "scissors": "scissors",
                    "rock": "rock"}

    #computer lose outcome
    LOSE_OUTCOME = {"paper": "scissors",
                    "scissors": "rock",
                    "rock": "paper"}

    #seeing if the computer will win, draw or lose
    GAME_OUTCOME = ["won", "draw", "lost", "lost", "lost"]
    game_random_choice = random.choice(GAME_OUTCOME)

    COMPUTER_OUTCOME = {"won": WIN_OUTCOME,
                       "draw": DRAW_OUTCOME,
                       "lost": LOSE_OUTCOME}
    
    #users choice between rock, paper, and scissors
    USER_CHOICE = {"1": "paper",
                   "2": "scissors",
                   "3": "rock"}
    
    #rules and specifications
    print("""
Welcome to the paper scissors rock game!
The rules are:
You choose between:
1: Paper
2: Scissors
3: Rock
0: Leave the game
Type 1, 2, or 3 to play the game, or 0 to exit.
The prize is 60 points if you win against the computer.
You will lose 40 points if you lose against the computer.
If you choose to leave, you will be penalized 10 points.
Good luck and have fun! """)
      
    valid_input = False
    while not valid_input:
        try:
            user_choice = int(input("Please enter 1, 2, 3 or 0 to play the game. "))
            valid_input = True
        except ValueError:
            print()
            valid_input = False

        if valid_input:
            #Making sure the user enters something between 0 and 3
            if user_choice < 0 or user_choice > 3:
                valid_input = False
                
            elif user_choice == 0:
                #If the user wants to leave mid game
                user_points = exit_command(user_points, penalty)
                print("Please go and enjoy another game. ")

            else:
                #takes the random outcome and user's choice, and turns it into the computer's choice
                computer_outcome = (COMPUTER_OUTCOME[str(game_random_choice)])
                user_choice = (USER_CHOICE[str(user_choice)])
                computer_choice = (computer_outcome[str(user_choice)])
                print("You have chosen {}, and computer has chosen {}. " .format(user_choice, computer_choice))

                #user wins
                if game_random_choice == "won":
                    user_points += 60
                    print("Nice! you have beat the computer and have won 60 points. Your total is now {}" .format(user_points))

                #user draws    
                elif game_random_choice == "draw":
                    print("You have picked the same as the computer. You have lost no points. ")

                #user loses
                elif game_random_choice == "lost":
                    user_points -= 40
                    print("Unlucky. You have lost and will loose 40 points. your total is now {}. " .format(user_points))
    
    return user_points

#456 game
def four_five_six_game(user_points):
    #preset variables
    dice_points = 0
    points_total = 0
    penalty = 50
    #rules and specifications
    print("""Welcome to the 456 game. The rules are:
You roll a ordinary dice
If the number is above 3, you get that amount of points x 10.
If you get 3 or below, you reset and lose half the amount of the points you could have obtained.
You will only recieve and double your points if you roll a 6.
Would you like to start playing? If you leave after starting the round, you will lose 50 points. (1 : Yes, 2 : No) """)
    valid_input = False
    while not valid_input:
        try:
            #random dice value
            dice_num = random.randint(1,6)
            user_choice = int(input())
            valid_input = True
        except ValueError:
            print("Please enter 1 to play, and 0 to exit. ")
            valid_input = False

        if valid_input:
            #making sure the user enters 0 or 1
            if user_choice != 1 and user_choice != 0:
                print("Please enter either 1 to play, or 0 to exit ")
                valid_input = False 
               
        #if the user enters 0
        if user_choice == 0:
            if dice_points != 0:
                user_points = exit_command(user_points, penalty)
            else:
                print("Alright go gain some points at some other games. Your total is still {} points. " .format(user_points))

        #if the user enters 1 and rolls the dice
        elif user_choice == 1:
            if dice_num == 4 or dice_num == 5:
                dice_points = dice_points + dice_num
                points_total = dice_points*10
                print("you have rolled a {}. you now have a total of {} points. " .format(dice_num, points_total))
                valid_input = False  

            #losing the game
            elif dice_num <= 3:
                #taking off half the points they would have gotten if they rolled a 6
                user_points = user_points - points_total//2
                print("Unlucky. You have rolled a {}. Because you have a total of {} points, you will have half of it subtracted from your starting points. Your new total is now {}. " .format(dice_num, points_total, user_points))

            #winning the game
            elif dice_num == 6:
                user_points += points_total*2
                print("Congratulations! You have rolled a 6 and won a total of {} points! you now have a total of {} points! " .format(points_total, user_points))
    return user_points


def snake_eyes(user_points):
    #preset variables
    penalty = 30
    points_total = 0
    #rules and specifications
    print("""
Welcome to the snake eyes game. The rules are:
You roll 2 dice.

If the numbers on the dice add up to be 8, you win 20 points.
If the numbers on the dice add up to 10, your current points double.
If the numbers on the dice add to 12, you recieve your points.
If the numbers on the dice are the same except for 6, you lose the game.

The game will cost 60 points for an entry,
If you leave after you have gained points, you will get a penalty of 30 points.
Would you like to play? (1 : Yes/ 0 : No) """)
    valid_input = False
    while not valid_input:
        try:
            #random dice values
            dice_one = random.randint(1,6)
            dice_two = random.randint(1,6)
            #both dice added together
            dice_total = dice_one + dice_two
            user_choice = int(input())
            valid_input = True
        except ValueError:
            print("Please enter 1 to play, and 2 to exit. ")
            valid_input = False

        if valid_input:

            #making sure the user enters 1 or 2
            if user_choice != 1 and user_choice != 0:
               print("please enter 1 to roll the dice, and 2 to exit. ")
               valid_input = False

            #if user enters 0 and wants to leave
            elif user_choice == 0:
                if points_total != 0:
                    user_points = exit_command(user_points, penalty)
                else:
                    print("Welp, it's all good if you chickened out. *sigh* ")
                print("Please go enjoy another game. ")
                return user_points

            #if user didn't enter 0
            else:
                print("You rolled a {} and a {}. " .format(dice_one, dice_two))
                
                #if user has not won yet
                if dice_total != 12 and dice_one != dice_two:
                    
                    if dice_total == 8:
                        points_total += 20
                        dice_value = "increased by 20"
                        
                    elif dice_total == 10:
                        points_total *= 2
                        dice_value = "doubled"

                    else:
                        dice_value = "not changed"
                        
                    print("You have rolled an {} and your points has {}. Your points are {}. " .format(dice_total, dice_value, points_total))
                    valid_input = False

                #user wins
                elif dice_total == 12:
                    print("Congratulations! You have won {} points. Your new total is now {}. " .format(points_total, points_total + user_points))    

                #user loses
                else:
                    user_points -= 60
                    print("Unlucky. You have rolled a {} and have lost 60 points. Your new total is now {}. " .format(dice_one + dice_two, user_points))                
            
            
                

#snake_eyes()


def twenty_one_game(user_points):
    current_total = 0
    penalty = 40
    exit_command
    COMPUTER_CHOICES = {"1": 3,
                        "2": 2,
                        "3": 1}
                       
    print("""
Welcome to the 21 game. The rules are:
You and the computer are counting up to 21 from 0.
You can up count any values from 1 - 3, you and the computer will take turns counting up.
Whoever is forced to count 21 loses the game.
The game will cost 10 points for an entry, for a prize of 100 points per win.
If you leave after the round has started, you will get a penalty of 40.
Please enter 1, 2, or 3, and 0 to leave. """)
    valid_input = False
    while not valid_input:
        try:
            user_choice = int(input())
            valid_input = True
        except ValueError:
            print("Please enter 1, 2, 3 or 0 to leave")
            valid_input = False

        if valid_input:
            if user_choice < 0 or user_choice > 3:
                print("Please enter something between 0 - 3. ")
                valid_input = False

        if valid_input and user_choice == 0:
            if current_total != 0:
                user_points = exit_command(user_points, penalty)
                print("hello ")
                print(user_points)

            print("What would you like to play next? ")
            return user_points

        if valid_input and current_total < 20:
            computer_choice = (COMPUTER_CHOICES[str(user_choice)])
            print(computer_choice)
               
            current_total += user_choice + computer_choice
            print(current_total)
            print("You have chosen {}, computer has decided on {}. The total is now {}. " .format(user_choice, computer_choice, current_total))
            valid_input = False

        elif valid_input and current_total >= 20:
            user_points -= 50
            print("Unlucky. You have landed on 21, meaning you have lost. the fee was 10 points, meaning your total is now {} " .format(user_points))
       


def main():
    user_points = 200
    print("""Hello there user.
Welcome to the arcade, where you can play for points and feel good about yourself when your points multiply tenfold.
Please choose a game on this list to play, depending on the difficulty and risk level.
The games include: """)

    valid_input = False
    while not valid_input:
        print("""High Risk Games:
1. |Number Guessing Game
2. |Paper Scissors Rock Game
3. |6 5 4 Dice Game

Low Risk Games:
4. |Blackjack Game
5. |Snake Eyes Game
6. |Word Guessing Game

No Risk Games:
7. |Complement/Insult Generator
8. |Dad Joke Teller
9. |21 Counting Game """)
        valid_input = True
    game_choice = int(input("you are over here "))

    print(user_points)
    #number_guesser(user_points)
    print("hello")
    user_points = number_guesser(user_points)
    print(user_points)
    valid_input = False
    print("helooooooooo")
    print(user_points)


main()

