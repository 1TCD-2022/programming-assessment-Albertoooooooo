"""
Fliename: Arcade_Games.py
Author: Albert Zhou
Date: 2/07/2022
Description: Rigged Individual games put into a menu for assessment.
"""

#libraries
import threading
import random
import time

#special secret which is the only way to win
def easter_egg(user_points): 
    yay = 0
    return user_points

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

                    #randomizes the random number again if it passes 100
                    if computer_random_number > 100:
                        computer_random_number -= random.randint(30, 60)

                    #rigging the computers number to increase by 3 if users guess is within 3
                    if abs_number_difference < 4:
                        computer_random_number += 3

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
def psr_game(user_points):
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
Good luck and have fun!
""")
          
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
You will only recieve your points if you roll a 6.
Would you like to start playing? If you leave after starting the round, you will lose 50 points. (1 : Yes, 2 : No) """)
    valid_input = False
    while not valid_input:
        try:
            #random dice value
            dice_num = random.randint(1,6)
            print(dice_num)
            user_choice = int(input())
            valid_input = True
        except ValueError:
            print("Please enter 1 to play, and 2 to exit. ")
            valid_input = False

        if valid_input:
            #making sure the user enters 0 or 1
            if user_choice != 1 and user_choice != 0:
                print("Please enter either 1 to play, or 2 to exit ")
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
                user_points += points_total
                print("Congratulations! You have rolled a 6 and won a total of {} points! you now have a total of {} points! " .format(points_total, user_points))
    return user_points


#blackjack game beginning
def user_bj_check(card_number, starting_number, starting_card, random_card):
    #checking if the user has a blackjack
    if starting_card == "ace":
        if card_number_number > 9:
            user_blackjack = 1
            print("lol")
        else:
            print("lolll")
                                            
    elif starting_number > 9:
        if random_card == "ace":
            user_blackjack = 1
            print("lllllll")
        else:
            print("oooo")
    
#checking if the computer has a blackjack
def blackjack_check(computer_first_card, computer_second_card, computer_first_number, computer_second_number):
    if computer_first_card == "ace":
        if computer_second_number > 9 and computer_second_card != "ace":
            return 1

    if computer_first_number > 9 and computer_first_card != "ace" :
        if computer_second_card == "ace":
            return 1
    return 0

    
#starting the blackjack code
def blackjack_game(user_points):
    #preset variables
    total_value = 0
    computer_total = 0
    penalty = 70
    user_blackjack = 0
    computer_blackjack = 0
    #ace and jack both count as 11 points
    eleven = ["ace", "jack"]
    eleven_choice = eleven.pop(random.randint(0,1))
    print(eleven_choice)

    #ordinary cards
    CARD_NUMBERS = {"2" : "two",
                    "3" : "three",
                    "4" : "four",
                    "5" : "five",
                    "6" : "six",
                    "7" : "seven",
                    "8" : "eight",
                    "9" : "nine",
                    "10" : "ten",
                    "11" : eleven_choice,
                    "12" : "queen",
                    "13" : "king"}

    #card suits
    CARD_SUITS = ["spades",
                  "hearts",
                  "diamonds",
                  "clovers"]

    #unfair cards the user might get
    UNFAIR_NUMBERS = {"10" : "ten",
                      "11" : eleven_choice,
                      "12" : "queen",
                      "13" : "king"}

#computer will recieve one card from each list
    #card the computer will get
    UNFAIR_LOW_NUMBERS = {"6" : "six",
                          "7" : "seven",
                          "8" : "eight",
                          "9" : "nine"}

    #card the computer will get
    UNFAIR_USER_NUMBERS = {"8" : "eight",
                           "9" : "nine",
                           "10" : "ten",
                           "11" : eleven_choice,
                           "12" : "queen",
                           "13" : "king"}

    #chance for computer to get a blackjack if the user gets one
    BLACKJACK_CHANCE = ["1", "1", "1", "2"]
    

    #rules and specifications
    print("""
Welcome to blackjack. You will be playing against the computer for 50+ points.
The rules are:

Face cards each count as 10
Aces count as 11, all others count at face value.
You start with 2 cards, if they are an ace and any 10 or above card including ace, you get a blackjack and immediately win double the points (100). If not, you can get more cards, or end your turn.
If the computer also has a blackjack when you get one, the game ends in tie and neither wins.
If your total card count passes 21, you lose immediately, vice-versa for the computer.
If you get exactly 21 points before the computer, you win 50 points, vice-versa for the computer.
If you end your turn and your total is higher than the computers, you win 50 points. If not, you lose 50 points.

Enter 1 to start the game, 2 to end game with your points, or 0 to leave.
If you leave after the game has started, you will receive a penalty of 70 points.
Would you like to play? """)
    #compter cards and the removed suit
    suit_remove = random.choice(CARD_SUITS)
    computer_first_number = random.randint(10,13)
    computer_second_number = random.randint(6,9)
    computer_first_card = (UNFAIR_NUMBERS[str(computer_first_number)])
    computer_second_card = (UNFAIR_LOW_NUMBERS[str(computer_second_number)])
    computer_first_suit = random.choice(CARD_SUITS)

    #removing a suit if the card numbers are the same
    if computer_first_card == computer_second_card:
        CARD_SUITS.remove(suit_remove)
    computer_second_suit = random.choice(CARD_SUITS)
    #total of computers cards
    computer_total += computer_first_number + computer_second_number

    #sending program to function to see if the computer has a blackjack
    if blackjack_check(computer_first_card, computer_second_card, computer_first_number, computer_second_number) == 1:
        computer_blackjack = 1

    valid_input = False
    while not valid_input:
        try:
            #reset card suits
            CARD_SUITS = ["spades",
                          "hearts",
                          "diamonds",
                          "clovers"]

            #users total
            starting_number = 0
            user_choice = int(input())
            valid_input = True

        except ValueError:
            #making sure user enters an integer
            print("Please enter 1, 2, the play blackjack, or 0 to leave. ")
            valid_input = False

        if valid_input:
            #making sure the user enters 0 - 2
            if user_choice < 0 or user_choice > 2:
                print("Please enter 1, 2, or 0 to leave. ")
                valid_input = False

            #changing the list if the user's total has passed 15
            elif total_value < 21:
                if total_value < 15:
                    card_number = random.randint(2,13)
                else:
                    card_number = random.randint(4,10)
                random_card = (CARD_NUMBERS[str(card_number)])
                user_suit = random.choice(CARD_SUITS)

                #start of game
                if user_choice == 1:
                    if total_value == 0:
                        #user cards and making sure there are no duplicate suits
                        starting_number = random.randint(2,13)
                        starting_card = (CARD_NUMBERS[str(starting_number)])
                        if starting_card == random_card:
                            CARD_SUITS.remove(suit_remove)
                        starting_suit = random.choice(CARD_SUITS)
                        #user's total
                        total_value += starting_number + card_number
                        
                        
                        print("Your first cards are the {} of {}, and the {} of {}. Computer will have one card revealed after you draw. " .format(starting_card, starting_suit, random_card, user_suit))
                        #sending program to function to check if user has gotten a blackjack
                        if user_bj_check(card_number, starting_number, starting_card, random_card) == 1:
                            user_blackjack = 1

                        #giving the computer a chance to get a blackjack if the user also has a blackjack
                        if user_blackjack == 1:
                            blackjack_chance = random.choice(BLACKJACK_CHANCE)
                            print(blackjack_chance)
                            if blackjack_chance == "1":
                                computer_blackjack = 1

                        #outcome if the user has gotten a blackjack
                        if user_blackjack == 1:
                            print("congratulations! you have gotten a blackjack! ")
                            if computer_blackjack == 1:
                                #if computer also has a blackjack
                                print("Unfortunately, computer has also gotten a blackjack. You tie and win nothing. ")
                            else:
                                #if computer does not have a blackjack
                                user_points += 100
                                print("You get a total of 100 points! Your total is now {}" .format(user_points))

                        #rest of the code if user does not have a blackjack
                        if user_blackjack != 1 and total_value < 21:
                            print("Your total is {}. Computer has a {} of {}, and the second card is unknown. Enter 1 to recieve another card, or 2 to end game and reveal hands. 0 to exit game. " .format(total_value, computer_first_card, computer_first_suit))
                            valid_input = False

                    #adding new cards to user total
                    elif total_value != 0:                  
                        total_value += card_number
                        print("You have gotten a {} of {}. Your total is now {}. Would you like to get another card or stop and reveal cards? " .format(random_card, user_suit, total_value))
                        if total_value < 21:
                            valid_input = False
                        elif total_value == 21:
                            print("yay ")
                        else:
                            print("bruhh ")

                #if user wants to leave game
                elif user_choice == 0:
                    
                    if total_value != 0:
                        user_points = exit_command(user_points, penalty)
                        print("Please go enjoy another game. ")

                    #if user leaves and hasn't started the game
                    else:
                        print("* Sigh *. Such a shame. Have fun somewhere else. ")
                        
                    return user_points

                #if user stands and reveals cards
                elif user_choice == 2:

                    #making sure the user has already started the game
                    if total_value == 0:
                        print("You need to start the game in order to stand. and reveal hands. If you want to leave, enter 0 to exit. ")
                        valid_input = False
                    else:
                        #revealing the computer's cards
                        print("Computer has a {} of {}, and a {} of {}. " .format(computer_first_card, computer_first_suit, computer_second_card, computer_second_suit))
                        print("Your total came out to be {}. \nComputer total is {}. " .format(total_value, computer_total))
                        #if user wins, loses, or ties
                        if total_value > computer_total:
                            user_points += 50
                            print("Congratulations! you have beaten the computer and won a total 50 points. Your total is now {} points. " .format(user_points))
                        elif total_value == computer_total:
                            print("You and the computer both have {}. Game ends in tie. No points are given. " .format(total_value))
                        else:
                            user_points -= 50
                            print("Unlucky. You have come up short and you have lost 50 points. Your total points is now {}. " .format(user_points))

            #if user hits 21
            elif total_value == 21:
                if computer_total != 21:
                    user_points += 100
                    print("Congratulations! You have hit 21 and computer has {}. You win and recieve 100 points! \nYour total is now {} points" .format(computer_total, user_points))

            #if user passes 21
            else:
                if computer_total > 21:
                    print("You have gone past 21, but computer has also gone past 21. Game ends in tie. ")
                else:
                    user_points -= 50
                    print("You have gone past 21, computer had a total of {}. You lose 50 points and your total is now {}. " .format(computer_total, user_points))



            
    return user_points


#start of snake eyes game
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
Would you like to play? (1 : Yes/ 2 : No) """)
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
            if user_choice != 1 and user_choice != 2:
               print("please enter 1 to roll the dice, and 2 to exit. ")
               valid_input = False

            #if user enters 0 and wants to leave
            elif user_choice == 2:
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
                    print("Unlucky. You have rolled a {} and have lost 60 points. Your new total is now {}. " .format(dice_one + dice_two, user_points - 60))                
            
            
                

#beginnging of word guessing game
#checking if the user has finished the word
def word_guessed(spaces):
    for x in range (0, len(spaces)):
        #checking the list for any "_"
        if spaces[x] == "_":
            print("no ")
            win = 0
            return 0
        
    return 1

#putting the letter in the word if the letter is inside the word
def letter_position(random_word, spaces, user_letter):
    print()
    word_space = -2
    while word_space != -1:
        if user_letter in random_word:
            word_space = random_word.find(user_letter)
            letter_removed = "*"
            #ordering the list from all the "_" before and after the letter 
            random_word = random_word[:word_space] + letter_removed + random_word[word_space + 1:]
            spaces[word_space] = user_letter
        else:
            word_space = -1

    return (random_word, spaces)
        
#start of game
def word_guesser(user_points):
    #preset values
    tries = 8
    penalty = 60
    win = 0

    WORDS = ["Absolute", "Academic", "Accident", "Accurate", "Activity", "Bathroom", "Behavior", "Boundary", "Building", "Business",
             "Campaign", "Capacity", "Category", "Champion", "Complain", "Database", "Deadline", "Decision", "Delicate", "Director",
             "Economic", "Electric", "Employee", "Employer", "Engineer", "Favorite", "Festival", "Firewall", "Frequent", "Function",
             "Generate", "Graduate", "Generous", "Guardian", "Guidance", "Hardware", "Hospital", "Humanity", "Homeless", "Historic",
             "Identity", "Increase", "Industry", "Interior", "Invasion", "Judgment", "Jaundice", "Jeopardy", "Joystick", "Juvenile",
             "Keyboard", "Kangaroo", "Kerosene", "Kindness", "Knockout", "Landlord", "Language", "Laughter", "Lifetime", "Location",
             "Magazine", "Magnetic", "Maintain", "Marriage", "Medicine", "Neighbor", "Notebook", "Negative", "National", "Nineteen",
             "Opponent", "Opposite", "Optional", "Original", "Overcome", "Parallel", "Personal", "Platform", "Platinum", "Position",
             "Quantity", "Question", "Quantize", "Quotable", "Quickset", "Reaction", "Relation", "Relative", "Remember", "Research",
             "Sentence", "Software", "Solution", "Somebody", "Straight", "Teaspoon", "Terrible", "Thousand", "Triangle", "Together",
             "Ultimate", "Umbrella", "Universe", "Unlikely", "Username", "Vacation", "Valuable", "Vertical", "Violence", "Variable",
             "Weakness", "Whatever", "Whenever", "Wherever", "Wireless", "Yourself", "Youthful", "Yearning", "Yearlong", "Yielding"]

    #getting a random 8 letter word
    random_word = random.choice(WORDS)
    random_word = random_word.lower()
    print(random_word)

    #lenght of word
    spaces = ['_']*len(random_word)
    

    #rules and specifications
    print("""
Welcome to the word guessing game.
There is a prize of 100 points per word guessed.
The rules are:
Computer will give you a random 8 letter word to guess
You have three "letter guesses", where you guess a letter in the word, similar to hang man.
After those three guesses, you have to try to guess the word.
If you do not get the word, you will lose 70 points.
If you leave after you have started guessing, you will be penalized.
Enter 1 to start, and 0 to exit. """)
    valid_input = False
    while not valid_input:
        try:
            user_choice = int(input())
            valid_input = True
        except ValueError:
            #making sure the user enters an integer
            print("Please enter 1 to start, and 0 to exit. ")
            valid_input = False

        if valid_input:
            #making sure the user enters 0 or 1 
            if user_choice < 0 or user_choice > 1:
                print("Please enter 1 to start, and 0 to leave. ")
                valid_input = False
            else:
                    #taking off a try when the user starts
                    tries -= 1
                    if tries > 1:
                        print("Your 8 letter word is {}. Guess a letter. " .format(spaces))
                        valid_letter = False
                        while not valid_letter and win == 0:
                            try:
                                user_letter = input()
                                valid_letter = True

                            #making sure the user enters a string
                            except ValueError:
                                print("Yay ")
                                valid_letter = False
                                
                            if valid_letter:

                                #making sure the user enters 1 letter         
                                if len(user_letter) == 1:
                                    if user_letter in random_word:
                                        #sending program to function to see if the users letter is inside the word
                                        random_word, spaces = letter_position(random_word, spaces, user_letter)
                                        print("lol ")
                                        print(spaces)
                                    else:
                                        print("That letter is not in the word. ")

                                    #sending program to check if the user has won
                                    if word_guessed(spaces) == 1:
                                        print("yayyyy ")

                                else:
                                    print("Please enter 1 letter. ")
                                valid_letter = False

                                
    return user_points

#coin toss game is not done
class threadtimer(threading.Thread):
    def __init__(self):
        self.timer = 5

    def increment(self):
        while timer > 0:
            time.sleep(1)
            self.timer -= 1
        

def coin_toss(user_points):
    timer = 5
    #useless hints
    HINTS = ["tail of a mongoose", "front of a viper", "feathers on the hawk", "beneath the dragon", "descendant of the legends",
             "whisper of the wind", "breath of the wilds", "opening in the abyss", "fear in the back", "burning of the eyes", "silence of the underneath",
             "movement of the air", "warmth of the sun", "closure of the mask"]
    
    computer_outcome = {"heads" : "tails",
                        "tails" : "heads"}

    #rules and specifications
    print("""
Welcome to the coin toss.
You will be playing against the computer for a total of 200 points.
The rules are:
The computer will give you a riddle to help you find your answer.
A coin will be thrown in the air. You have five seconds to shout heads or tails before the timer ends.
If you do not answer within the 5 seconds, you will automatically lose.
If you guess and the coin is the opposite, you lose 100 points.
If you guess right and the coin is the same face as your answer, you win.
Enter 1 to start playing, h: heads, t: tails, 0 to leave the game. """)

    valid_input = False
    while not valid_input:
        try:
            user_choice = int(input())
            valid_input = True
        except ValueError:
            print("Please enter 1 to play, and 0 to leave. ")

        if valid_input:
            if user_choice < 1 or user_choice > 2:
                print("Please enter 1 to play, and 0 to leave. ")
                valid_input = False

            else:
                random_hint = random.choice(HINTS) 
                print("coin is flipping. Your hint is: \n{} " .format(random_hint))
                coin_face = False
                while not coin_face:
                    try:
                        toss_timer = timer(5, -1)
                        toss_timer.start
                        face_choice = input() .lower()
                        coin_face = True

                    except ValueError:
                        print("please enter h for heads, and t for tails. ")
                        coin_face = False

                    if coin_face:
                        timer



                    
                        

                        
                        
    return user_points

#beginning of joke teller
def dad_jokes(user_points):
    #"soft" guestions and answers 
    SOFT_QUESTIONS = {"1": "How does a man on the moon cut his hair?", 
                      "2": "Why is it a bad idea to iron your four-leaf clover?",
                      "3": "When I was a kid, my mother told me I could be anyone I wanted to be.",
                      "4": "Why did the invisible man turn down the job offer?",
                      "5": "Want to hear a joke about construction?",
                      "6": "How does Moses make his coffee?",
                      "7": "Why do bees have sticky hair?",
                      "8": "Why do Dads take an extra pair of socks when they go golfing?",
                      "9": "What's the best time to go to the dentist?",
                      "10": "Why did the scarecrow win an award?"}

    SOFT_ANSWERS = {"1": "Eclipse it.", 
                    "2": "Cause you shouldn't press your luck.",
                    "3": "Turns out, identity theft is a crime.",
                    "4": "He couldn't see himself doing it!",
                    "5": "I'm still working on it!",
                    "6": "Hebrews it.",
                    "7": "Because they use a honeycomb.",
                    "8": "In case they get a hole in one.",
                    "9": "Tooth-hurty.",
                    "10": "Because he was outstanding in his field!"}

    #"hard" questions and answers
    HARD_QUESTIONS = {"1": "I can't take my dog to the pond anymore because the ducks keep attacking him.", 
                      "2": "What do sprinters eat before a race?",
                      "3": "Why couldn't the bicycle stand up by itself?",
                      "4": "How many apples grow on a tree?",
                      "5": "Why did the old man fall in the well?",
                      "6": "Do you know the last thing my grandfather said to me before he kicked the bucket?",
                      "7": "What is the tallest building in the world?",
                      "8": "What do you call a beehive without an exit?",
                      "9": "How does a penguin build its house?",
                      "10": "I like telling Dad jokes."}
    
    HARD_ANSWERS = {"1": "That's what I get for buying a pure bread dog.", 
                    "2": "Nothing, they fast!",
                    "3": "It was two tired!",
                    "4": "All of them!",
                    "5": "Because he couldn't see that well!",
                    "6": "'Grandson, watch how far I can kick this bucket.'",
                    "7": "The library—it's got the most stories.",
                    "8": "Unbelievable.",
                    "9": "Igloos it together!",
                    "10": "Sometimes he laughs!"}

    #rules and specifications
    print("""
Welcome to the joke telling room. We will tell you jokes for free. Just because we can.
Enter:
1 to get the funny jokes
2 for the INTENSE jokes,
and 0 to leave.
Enjoyyyyyyyyyy. """)
    valid_input = False
    while not valid_input:
        try:
            random_number = random.randint(1, 10)
            user_choice = int(input())
            valid_input = True
        except ValueError:
            #making sure the user enters an integer
            print("Please enter 1 or 2 for a joke, and 0 to leave. ")

        if valid_input:
            #making sure the user enters 0 - 2
            if user_choice < 0 or user_choice > 2:
                print("please enter 1 or 2 for a joke, and 0 to leave. ")
                valid_input = False

            #if user wants to leave the game
            elif user_choice == 0:
                print("It was great having you. Don't worry, your points are still {}. \nGo and enjoy another game. " .format(user_points))
                return user_points

            #user enters 1
            elif user_choice == 1:
                random_question = (SOFT_QUESTIONS[str(random_number)])
                random_answer = (SOFT_ANSWERS[str(random_number)])
                print(random_question)
                print("The answer will appear in 5 seconds\n ")
                time.sleep(5)
                print(random_answer)

            #user enters 2  
            else:
                random_question = (HARD_QUESTIONS[str(random_number)])
                random_answer = (HARD_ANSWERS[str(random_number)])
                print(random_question)
                print("The answer will appear in 5 seconds\n ")
                time.sleep(5)
                print(random_answer)
                
        
    return user_points

#beginning of 21 game
def twenty_one_game(user_points):
    #preset values
    current_total = 0
    penalty = 40
    #computer's choices
    COMPUTER_CHOICES = {"1": 3,
                        "2": 2,
                        "3": 1}

    #rules and specifications
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
            #making sure user enters an integer
            print("Please enter 1, 2, 3 or 0 to leave")
            valid_input = False

        if valid_input:
            if user_choice < 0 or user_choice > 3:
                #making sure user enters 0 - 3
                print("Please enter something between 0 - 3. ")
                valid_input = False

        #if user wants to leave game
        if valid_input and user_choice == 0:
            if current_total != 0:
                user_points = exit_command(user_points, penalty)
                print("hello ")
                print(user_points)

            print("What would you like to play next? ")
            return user_points

        #if game has not ended yet
        if valid_input and current_total < 20:
            computer_choice = (COMPUTER_CHOICES[str(user_choice)])
            print(computer_choice)
               
            current_total += user_choice + computer_choice
            print(current_total)
            print("You have chosen {}, computer has decided on {}. The total is now {}. " .format(user_choice, computer_choice, current_total))
            valid_input = False

        #game has ended
        elif valid_input and current_total >= 20:
            user_points -= 50
            print("Unlucky. You have landed on 21, meaning you have lost. the fee was 10 points, meaning your total is now {} " .format(user_points))
       

#main block
def main():
    #users starting points
    user_points = 200
    print("""Hello there user.
Welcome to the arcade, where you can play for points and feel good about yourself when your points multiply tenfold.
Please choose a game on this list to play, depending on the difficulty and risk level.
The games include: """)

    valid_entry = False
    while not valid_entry:
        #games 
        print("""High Risk Games:
1. |Number Guessing Game
2. |Paper Scissors Rock Game
3. |6 5 4 Dice Game

Low Risk Games:
4. |Blackjack Game
5. |Snake Eyes Game
6. |Word Guessing Game

No Risk Games:
7. |Coin Toss Game
8. |Dad Joke Teller
9. |21 Counting Game

0. |Exit

Your current total points are {}.

Please pick a game to play. """ .format(user_points))
        valid_input = False
        while not valid_input:
            try:
                game_choice = int(input())
                valid_input = True

            #making sure user enters an integer
            except ValueError:
                print("Please enter an integer. ")
                valid_input = False
                
            if valid_input:
                #making sure user enters 0 - 9
                if game_choice > 9 or game_choice < 0:
                    print("Please enter 0 through 9. ")
                    valid_input = False

                #if user wants to exit program
                elif game_choice == 0:
                    print("Alright, have a good day. ")
                    
                else:
                    #each input will send user to the corresponding function
                    if game_choice == 1:
                        user_points = number_guesser(user_points)

                    if game_choice == 2:
                        user_points = psr_game(user_points)

                    if game_choice == 3:
                        user_points = four_five_six_game(user_points)

                    if game_choice == 4:
                        user_points = blackjack_game(user_points)

                    if game_choice == 5:
                        user_points = snake_eyes(user_points)

                    if game_choice == 6:
                        user_points = word_guesser(user_points)

                    if game_choice == 7:
                        user_points = coin_toss(user_points)

                    if game_choice == 8:
                        user_points = dad_jokes(user_points)

                    if game_choice == 9:
                        user_points = twenty_one_game(user_points)

                    valid_entry = False


main()
