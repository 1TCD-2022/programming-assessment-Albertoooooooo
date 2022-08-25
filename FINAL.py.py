"""
Fliename: Arcade_Games.py
Author: Albert Zhou
Date: 2/07/2022
Description: Rigged Individual games put into a menu for assessment.
"""

# libraries
import threading
import random
import time

# special secret which is the only way to win


class points(threading.Thread):
    def __init__(self, value, increment):
        threading.Thread.__init__(self)  # initilize the thread
        self.value = value  # starting value
        self.increment = increment  # amount to add
        self.alive = False  # controls the while loop in the run command

    def run(self):  # main function that will run in a separate thread
        self.alive = True
        while self.alive:
            self.value += self.increment  # do the counting

    def show(self):
        return self.value

    def finish(self):  # stops the thread and returns the final value
        self.alive = False
        return self.value


def easter_egg(user_points):
    # sets the thread values
    winning_points = points(1, 9)
    # starts the thread
    winning_points.start()
    print("ENTER 1 TO SEE YOUR GROWING POINTS, AND 0 TO RECIEVE THEM. ")
    valid_input = False
    while not valid_input:
        try:
            growing_points = int(input())
            valid_input = True

        except ValueError:
            print("PLEASE ENTER 1 TO SEE YOUR PO\
INTS AND 0 TO GET THOSE YAYY. ")

        if valid_input:
            if growing_points > 1 or growing_points < 0:
                print("PLEASE ENTER 1 OR 0 TO DO SUM STUFFFFFF. ")
                valid_input = False

            # shows the user the thread value if 1 is entered
            elif growing_points == 1:
                print("YOUR GROWING POINTS {} AND RISING. \
" .format(winning_points.show()))
                valid_input = False

            # stops thread and returns the thread value
            else:
                print("YOUR POINTS ARE NOW {}. HAVE FUN WITH THOSE. \
" .format(winning_points.finish()))

    # returns to 456 game
    user_points = winning_points.finish()
    return user_points


# function for the user penalties during certain games
def exit_command(user_points, penalty):
    user_points -= penalty
    print("such a shame. A penalty of {} points has been taken from your total, \
leaving you with {} points.\n " .format(penalty, user_points))
    # sends the users points back to the previous function
    return user_points


# start of number guessing game
def number_guesser(user_points):
    # rules and specifications
    print("""
Welcome to the number guessing game.
The prize is 90 points
Guess a number between 1 - 100
The computer will tell you higher or lower, depending on your guess.
Each try will take 10 points from you.
You cannot leave the game. """)
    new_game = "yes"
    while new_game.upper() == "YES":

        print("Good luck! Guess 1 - 100")
        # counts the amount of tries the user takes
        count = 0
        # randomly generated number from 1 - 100
        computer_random_number = random.randint(1, 100)
        valid_input = False
        while not valid_input:
            try:
                user_number_guess = int(input())
                valid_input = True
            except ValueError:
                # if user enters a string or anything either than an integer
                print("please enter a interger between 1 - 100 ")

            if valid_input:
                # ensuring user enters an integer between 1 and 100
                if user_number_guess <= 0 or user_number_guess > 100:
                    print("please enter a interger between 1 - 100 ")
                    valid_input = False

                elif user_number_guess != computer_random_number:
                    count += 1
                    number_difference = computer_random_number - user_number_guess
                    # absolute value of the number difference
                    abs_number_difference = abs(number_difference)

                    # randomizes the random number again if it passes 100
                    if computer_random_number > 100:
                        computer_random_number -= random.randint(30, 60)

                    # increases number by 3 if in range of 3
                    elif abs_number_difference < 4:
                        computer_random_number += 3

                    if user_number_guess > computer_random_number:
                        print("My number is lower. ")

                    elif user_number_guess < computer_random_number:
                        print("My number is higher. ")

                    elif user_number_guess == computer_random_number:
                        print("My number is lower. ")

                    valid_input = False

                else:
                    # multiplies the users guess count by 10
                    penalty = count*10
                    user_points -= penalty - 90
                    print("Good job pal! My number was {}, \
and you got it in {} tries. \
You have recieved 90 points, and have lost {} points. \
Your total is now {}. \
" .format(computer_random_number, count, penalty, user_points))

        # if the user wants to play again
        new_game = input("Do you want to play again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO":
            new_game = input("Please enter again. ")
        if new_game.upper() == "NO":
            print("Alright, go enjoy another game. ")

    return user_points


# Paper Scissors Rock Game
def psr_game(user_points):
    penalty = 10

    # computer win outcome
    WIN_OUTCOME = {"paper": "rock",
                   "scissors": "paper",
                   "rock": "scissors"}

    # computer draw outcome
    DRAW_OUTCOME = {"paper": "paper",
                    "scissors": "scissors",
                    "rock": "rock"}

    # computer lose outcome
    LOSE_OUTCOME = {"paper": "scissors",
                    "scissors": "rock",
                    "rock": "paper"}

    # seeing if the computer will win, draw or lose
    GAME_OUTCOME = ["won", "draw", "lost", "lost", "lost"]
    game_random_choice = random.choice(GAME_OUTCOME)

    COMPUTER_OUTCOME = {"won": WIN_OUTCOME,
                        "draw": DRAW_OUTCOME,
                        "lost": LOSE_OUTCOME}

    # users choice between rock, paper, and scissors
    USER_CHOICE = {"1": "paper",
                   "2": "scissors",
                   "3": "rock"}

    # rules and specifications
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
    new_game = "yes"
    while new_game.upper() == "YES":
        game_random_choice = random.choice(GAME_OUTCOME)
        print("Paper, Scissors, or Rock? ")
        valid_input = False
        while not valid_input:
            try:
                user_choice = int(input())
                valid_input = True
            except ValueError:
                print("Please enter 1, 2, 3 or 0 to play the game. ")

            # Making sure the user enters something between 0 and 3
            if valid_input:
                if user_choice < 0 or user_choice > 3:
                    valid_input = False

                elif user_choice == 0:
                    # If the user wants to leave mid game
                    user_points = exit_command(user_points, penalty)
                    print("Please go and enjoy another game. ")
                    return user_points

                else:
                    # creates computers choice from user's choice
                    computer_outcome = (COMPUTER_OUTCOME[str(game_random_choice)])
                    user_choice = (USER_CHOICE[str(user_choice)])
                    computer_choice = (computer_outcome[str(user_choice)])
                    print("You have chosen {}, \
and computer has chosen {}. " .format(user_choice, computer_choice))

                    # user wins
                    if game_random_choice == "won":
                        user_points += 60
                        print("Nice! you have beat the computer \
and have won 60 points. Your total is now {}" .format(user_points))

                    # user draws
                    elif game_random_choice == "draw":
                        print("You have picked the same as the computer. \
You have lost no points. ")

                    # user loses
                    elif game_random_choice == "lost":
                        user_points -= 40
                        print("Unlucky. You have lost and will loose 40 points. \
your total is now {}. " .format(user_points))

        new_game = input("Do you want to play again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO":
            new_game = input("I don't know what you entered. \
Please try again. ")
        if new_game.upper() == "NO":
            print("Alright, have a good day. ")

    return user_points


# 456 game
def four_five_six_game(user_points):
    # preset variables
    penalty = 50
    # rules and specifications
    print("""Welcome to the 456 game. The rules are:
You roll a ordinary dice
If the number is above 3, you get that amount of points x 10.
If you get 3 or below, you reset and lose \
half the amount of the points you could have obtained.
You will only recieve your points if you roll a 6.
Would you like to start playing? If you leave after starting the round, \
you will lose 50 points. (1 : Yes, 0 : No) """)
    new_game = "yes"
    while new_game.upper() == "YES":
        new_game = "no"
        print("Enter 1 to roll the dice, and 0 to exit. ")
        points_total = 0
        dice_points = 0

        valid_input = False
        while not valid_input:
            try:
                # random dice value
                dice_num = random.randint(1, 6)
                user_choice = int(input())
                valid_input = True
            except ValueError:
                print("Please enter 1 to play, and 0 to exit. ")

        # making sure the user enters 0 or 1
            if valid_input:
                if user_choice != 1 and user_choice != 0:
                    print("Please enter either 1 to play, or 0 to exit ")
                    valid_input = False

                # if the user enters 0
                elif user_choice == 0:
                    if dice_points != 0:
                        user_points = exit_command(user_points, penalty)
                    else:
                        print("Alright. ")

                # if the user enters 1 and rolls the dice
                elif user_choice == 1:
                    if points_total > 200:
                        dice_num = random.randint(1, 3)
                        user_points -= points_total//2
                        print("Unlucky. You have rolled a {}. \
Because you have a total of {} points, you will have \
half of it subtracted from your starting points. \
Your new total is now {}. " .format(dice_num, points_total, user_points))

                    if dice_num == 4 or dice_num == 5:
                        dice_points += dice_num
                        points_total = dice_points*10
                        print("you have rolled a {}. you now have a total of {} points. \
" .format(dice_num, points_total))
                        valid_input = False

                    # losing the game
                    elif dice_num <= 3:
                        # taking half the total points
                        user_points -= points_total//2
                        print("Unlucky. You have rolled a {}. \
Because you have a total of {} points, you will have \
half of it subtracted from your starting points. Your new total is now {}. \
" .format(dice_num, points_total, user_points))

                    # winning the game
                    elif dice_num == 6:
                        user_points += points_total
                        print("Congratulations! \
You have rolled a 6 and won a total of {} points! \
you now have a total of {} points! " .format(points_total, user_points))

        # if user wants to play again
        new_game = input("Do you want to play again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO" and new_game.upper() != "NOT GONNA LIE":
            new_game = input("I don't know what you entered. \
Please try again. ")
        if new_game.upper() == "NO":
            print("Alright, go enjoy another game. ")

        # sends user to easter egg
        elif new_game.upper() == "NOT GONNA LIE":
            user_points = easter_egg(user_points)

    # returns user to main
    return user_points


def blackjack_game(user_points):
    # preset variables
    penalty = 70
    # ace and jack both count as 11 points
    eleven = ["ace", "jack"]
    eleven_choice = eleven.pop(random.randint(0, 1))
    print(eleven_choice)

    # ordinary cards
    CARD_NUMBERS = {"2": "two",
                    "3": "three",
                    "4": "four",
                    "5": "five",
                    "6": "six",
                    "7": "seven",
                    "8": "eight",
                    "9": "nine",
                    "10": "ten",
                    "11": eleven_choice,
                    "12": "queen",
                    "13": "king"}

    # card suits
    card_suits = ["spades",
                  "hearts",
                  "diamonds",
                  "clovers"]

    # computer will recieve one card from each list
    # unfair cards the cmoputer might get
    UNFAIR_NUMBERS = {"10": "ten",
                      "11": eleven_choice,
                      "12": "queen",
                      "13": "king"}

    # card the computer will get
    UNFAIR_LOW_NUMBERS = {"6": "six",
                          "7": "seven",
                          "8": "eight",
                          "9": "nine",
                          "10": "ten",
                          "11": eleven_choice,
                          "12": "queen",
                          "13": "king"}

    # card the user will get if their total passes 10
    UNFAIR_USER_NUMBERS = {"8": "eight",
                           "9": "nine",
                           "10": "ten",
                           "11": eleven_choice,
                           "12": "queen",
                           "13": "king"}

    # chance for computer to get a blackjack if the user gets one
    BLACKJACK_CHANCE = ["1", "1", "1", "2"]

    # rules and specifications
    print("""
Welcome to blackjack. You will be playing against the computer for 50+ points.
The rules are:

Face cards count as 10 including 10
Aces count as 1 or 11
All other cards count at face value

You start with 2 cards
Each turn you can recieve another card
If your total passes 21, You lose.
If your total ends up lower than the computer's, you Lose.
If you get exactly 21, you win 100 points
If you do not have 21 and have a higer total than the computer, \
you win 50 points.

Enter 1 to start the game, 2 to end game with your points, or 0 to leave.
If you leave after the game has started, \
you will receive a penalty of 70 points.
Would you like to play? """)
    new_game = "yes"
    while new_game.upper() == "YES":
        print("Enter 1 to start, 2 to stand, and 0 to leave. ")
        # compter cards and the removed suit
        suit_remove = random.choice(card_suits)
        computer_first_number = random.randint(10, 13)
        computer_second_number = random.randint(6, 13)
        computer_first_card = (UNFAIR_NUMBERS[str(computer_first_number)])
        computer_second_card = (UNFAIR_LOW_NUMBERS[str(computer_second_number)])
        computer_first_suit = random.choice(card_suits)
        computer_second_suit = random.choice(card_suits)

        # calculating card values
        if computer_first_card == computer_second_card:
            card_suits.remove(suit_remove)
            computer_second_suit = random.choice(card_suits)

        if computer_first_number > 10:
            computer_first_number = 10

        if computer_first_card == "ace":
            computer_first_number += 1

        if computer_second_number > 10:
            computer_second_number = 10

        if computer_second_card == "ace":
            computer_second_number += 1

        # reseting the user_total
        user_total = 0

        valid_input = False
        while not valid_input:
            try:
                # reseting the suits
                card_suits = ["spades",
                              "hearts",
                              "diamonds",
                              "clovers"]
                suit_remove = random.choice(card_suits)
                computer_total = computer_first_number + computer_second_number
                user_choice = int(input())
                valid_input = True

            except ValueError:
                print("Please enter an integer from 0 - 2 ")

            if valid_input:
                if user_choice < 0 or user_choice > 2:
                    print("Please enter only 1, 2 or 0 to leave. ")
                    valid_input = False

                # if user enters 1
                elif user_choice == 1:
                    user_random_number = random.randint(2, 13)
                    user_random_card = (CARD_NUMBERS[str(user_random_number)])

                    # changing the list of cards if total passes 10
                    if user_total != 0 and user_total > 10:
                        user_random_number = random.randint(8, 13)
                        user_random_card = (UNFAIR_USER_NUMBERS[str(user_random_number)])

                    # making all number above 10 equal 10
                    if user_random_number > 10:
                        user_random_number = 10

                    # making ace 11
                    if user_random_card == "ace":
                        user_random_number += 1
                    user_random_suit = random.choice(card_suits)

                    # getting user first card
                    if user_total == 0:
                        user_first_number = random.randint(2, 13)
                        user_first_card = (CARD_NUMBERS[str(user_first_number)])

                        if user_first_number > 10:
                            user_first_number = 10

                        if user_first_card == "ace":
                            user_first_number += 1

                        if user_random_card == user_first_card:
                            card_suits.remove(suit_remove)
                        user_first_suit = random.choice(card_suits)

                        user_total += user_random_number + user_first_number

                        print("Your first cards are the {} of {}, \
and the {} of {}. Your total is {}\nComputer has a {} of {}, \
and their second card is unknown. \
" .format(user_first_card, user_first_suit, user_random_card, user_random_suit, user_total, computer_first_card, computer_first_suit))

                    # if user wants another card
                    else:
                        user_total += user_random_number
                        print("Your extra card is the {} of {}. \
Your total is now {}. \
" .format(user_random_card, user_random_suit, user_total))

                    # giving user blackjack
                    if user_total == 21 or user_total == 31:
                        print("You have gotten a blackjack. ")
                        if computer_total != 21:
                            user_points += 100
                            print("\
Congratulations! You have beaten the computer and won a total of 100 points. \
Your points are now {}. " .format(user_points))
                        else:
                            print("\
Unlucky. Computer has a {} of {} and a {} of {}. \
They have also hit a blackjack. You tie and win nothing. \
" .format(computer_first_card, computer_first_suit, computer_second_card, computer_second_suit))

                    # if user has passed 21
                    elif user_total > 21 and user_total != 31:
                        user_points -= 50
                        print("\
Your total has passed 21, and you have busted. \
You lose 50 points. Your total is now {}. " .format(user_points))

                    else:
                        valid_input = False

                # if user wants to stand
                elif user_choice == 2:
                    if user_total != 0:
                        print("Computer has a {} of {}, and a {} of {}. \
" .format(computer_first_card, computer_first_suit, computer_second_card, computer_second_suit))
                        print("Your total is {}, and computer total is {}. \
" .format(user_total, computer_total))
                        if user_total > computer_total:
                            user_points += 50
                            print("\
Congrats! You have beaten the computer and won a total of 50 points. \
Your total is now {}. " .format(user_points))

                        elif user_total < computer_total:
                            user_points -= 50
                            print("\
Unlucky. Computer has a higher total than you. \
You lose 50 points, and your total is now {}. " .format(user_points))

                        else:
                            print("\
You and computer both have {} total. \
You tie and win nothing. " .format(user_total))

                    else:
                        print("You need to start the game in order to stand. ")
                        valid_input = False

                # if user wants to leave
                else:
                    if user_total != 0:
                        user_points = exit_command(user_points, penalty)
                    else:
                        print("Such a shame. Have fun at another game. ")
                    return user_points

        # if user wants to play again
        new_game = input("Do you want to play again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO":
            new_game = input("Please enter again. ")
        if new_game.upper() == "NO":
            print("Alright, have a good day. ")

    return user_points


# start of snake eyes game
def snake_eyes(user_points):
    # preset variables
    penalty = 30
    # rules and specifications
    print("""
Welcome to the snake eyes game. The rules are:
You roll 2 dice.

If the numbers on the dice add up to be 8, you win 20 points.
If the numbers on the dice add up to 10, your current points double.
If the numbers on the dice add to 12, you recieve your points.
If the numbers on the dice are the same except for 6, you lose the Game.

The game will cost 60 points for an entry,
If you leave after you have gained points, you will get a penalty of 30 points.
Would you like to play? (1 : Yes/ 0 : No) """)
    new_game = "yes"
    while new_game.upper() == "YES":
        points_total = 0
        print("Enter 1 to roll dice and 0 to exit. ")
        valid_input = False
        while not valid_input:
            try:
                # random dice values
                dice_one = random.randint(1, 6)
                dice_two = random.randint(1, 6)
                # both dice added together
                dice_total = dice_one + dice_two
                user_choice = int(input())
                valid_input = True
            except ValueError:
                print("Please enter 1 to play, and 0 to exit. ")

            if valid_input:

                # making sure the user enters 1 or 2
                if user_choice != 1 and user_choice != 0:
                    print("please enter 1 to roll the dice, and 0 to exit. ")
                    valid_input = False

                # if user enters 0 and wants to leave
                elif user_choice == 0:
                    if points_total != 0:
                        user_points = exit_command(user_points, penalty)
                    else:
                        print("\
Welp, it's all good if you chickened out. *sigh* ")

                # if user didn't enter 0
                else:
                    print("\
You rolled a {} and a {}. " .format(dice_one, dice_two))

                    # if user has not won yet
                    if dice_one != dice_two:

                        if dice_total == 8:
                            points_total += 20
                            dice_value = "increased by 20"

                        elif dice_total == 10:
                            points_total *= 2
                            dice_value = "doubled"

                        else:
                            dice_value = "not changed"

                        print("\
You have rolled an {} and your points has {}. \
Your points are {}. \
" .format(dice_total, dice_value, points_total))
                        valid_input = False

                    # user wins
                    elif dice_total == 12:
                        print("\
Congratulations! You have won {} points. \
Your new total is now {}. \
" .format(points_total, points_total + user_points))

                    # user loses
                    else:
                        user_points -= 60
                        print("\
Unlucky. You have rolled a {} and have lost 60 points. \
Your new total is now {}. " .format(dice_one + dice_two, user_points))

        new_game = input("Do you want to play again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO":
            new_game = input("\
I don't know what you entered. Please try again. ")
        if new_game.upper() == "NO":
            print("Alright, have a good day. ")

    return user_points


# beginnging of word guessing game
# checking if the user has finished the word
def word_guessed(spaces):
    for x in range(0, len(spaces)):
        # checking the list for any "_"
        if spaces[x] == "_":
            return 0

    return 1


# putting the letter in the word if the letter is inside the word
def letter_position(random_word, spaces, user_letter):
    word_space = -2
    while word_space != -1:
        if user_letter in random_word:
            word_space = random_word.find(user_letter)
            letter_removed = "*"
            # ordering the list from all the "_" before and after the letter
            random_word = random_word[:word_space] + letter_removed + random_word[word_space + 1:]
            spaces[word_space] = user_letter
        else:
            word_space = -1

    return (random_word, spaces)


# start of game
def word_guesser(user_points):
    # preset values
    penalty = 60
    words = ["Absolute", "Academic", "Accident", "Accurate", "Activity",
             "Bathroom", "Behavior", "Boundary", "Building", "Business",
             "Campaign", "Capacity", "Category", "Champion", "Complain",
             "Database", "Deadline", "Decision", "Delicate", "Director",
             "Economic", "Electric", "Employee", "Employer", "Engineer",
             "Favorite", "Festival", "Firewall", "Frequent", "Function",
             "Generate", "Graduate", "Generous", "Guardian", "Guidance",
             "Hardware", "Hospital", "Humanity", "Homeless", "Historic",
             "Identity", "Increase", "Industry", "Interior", "Invasion",
             "Judgment", "Jaundice", "Jeopardy", "Joystick", "Juvenile",
             "Keyboard", "Kangaroo", "Kerosene", "Kindness", "Knockout",
             "Landlord", "Language", "Laughter", "Lifetime", "Location",
             "Magazine", "Magnetic", "Maintain", "Marriage", "Medicine",
             "Neighbor", "Notebook", "Negative", "National", "Nineteen",
             "Opponent", "Opposite", "Optional", "Original", "Overcome",
             "Parallel", "Personal", "Platform", "Platinum", "Position",
             "Quantity", "Question", "Quantize", "Quotable", "Quickset",
             "Reaction", "Relation", "Relative", "Remember", "Research",
             "Sentence", "Software", "Solution", "Somebody", "Straight",
             "Teaspoon", "Terrible", "Thousand", "Triangle", "Together",
             "Ultimate", "Umbrella", "Universe", "Unlikely", "Username",
             "Vacation", "Valuable", "Vertical", "Violence", "Variable",
             "Weakness", "Whatever", "Whenever", "Wherever", "Wireless",
             "Yourself", "Youthful", "Yearning", "Yearlong", "Yielding"]

    print("""
Welcome to the word guessing game.
You are playing for a prize of 100 points. The rules are:
You are given an 8 letter word, \
and you guess single letters in the word, like hangmaN.
You have 3 wrong guesses, and after your guesses reach 0, you lose 70 points.
If you want to leave during the game, you will recieve a penalty of 60 points.

You can also swap in your own 8 letter words, \
but if you do, you won't gain or lose any points.
Enter 2 if you would like to play your own word guesser. """)

    new_game = "yes"
    while new_game.upper() == "YES":
        tries = 3

        # getting a random 8 letter word
        random_word = random.choice(words)
        random_word = random_word.lower()
        string_word = random_word

        # length of word
        spaces = ['_']*len(random_word)

        print("\
Enter 1 to start, 2 for your own word guesser, and 0 to exit. ")
        valid_input = False
        while not valid_input:
            try:
                user_choice = int(input())
                valid_input = True
            except ValueError:
                # making sure the user enters an integer
                print("Please enter 1, 2, or 0 to exit. ")

            if valid_input:
                # making sure the user enters 0 or 1
                if user_choice < 0 or user_choice > 2:
                    print("Please enter 1, 2, and 0 to leave. ")
                    valid_input = False

                # ordinary word guesser
                elif user_choice == 0:
                    print("bruh")

                # if user wants to put in a word
                elif user_choice == 2:
                    print("\
Please enter a 8 letter word to put into the list of random words. \n\
Note that if you put in anything other than the alphabet, \
you cannot enter anything when guessing. ")
                    extra_word = False
                    while not extra_word:
                        word_swap = random.randint(0, 119)
                        add_word = input()
                        extra_word = True

                        # if user wants to stop putting in words
                        if add_word == "0":
                            print("Time to guess your own words. ")

                        # making sure user enters 8 letters
                        else:
                            if len(add_word) != 8:
                                print("Please make the word 8 letters long. ")
                                extra_word = False

                            # changing a word in the list
                            else:
                                words[word_swap] = add_word
                                print("\
{} has been added to the list. " .format(add_word))
                                extra_word = False

        # if user wants to guess a word
        if user_choice != 0:
            print("\
Your 8 letter word is {}. Guess a letter. " .format(spaces))

            valid_letter = False
            while not valid_letter:
                try:
                    user_letter = input()
                    valid_letter = True

                # making sure the user enters a string
                except ValueError:
                    print("Please enter a letter. ")
                    valid_letter = False

                if valid_letter:
                    # if user wants to leave
                    if user_letter == "0":
                        if tries != 3:
                            user_points = exit_command(user_points, penalty)
                        else:
                            print("\
I guess you aren't the most literate person for this game. ")

                    else:
                        # making sure user enters a letter
                        if user_letter.isalpha() is False:
                            print("Please enter a letter. ")
                            valid_letter = False

                        # making sure the user enters 1 letter
                        elif len(user_letter) == 1:
                            if user_letter in random_word:
                                # program goes to function to check letter
                                random_word, spaces = letter_position(random_word, spaces, user_letter)
                                print(spaces)
                            else:
                                tries -= 1
                                print("\
That letter is not in the word. You have {} more wrong guesses. " .format(tries))
                                valid_letter = False

                        else:
                            print("Please enter 1 letter. ")
                            valid_letter = False

                        # sending program to check if the user has won
                        if word_guessed(spaces) == 1:
                            print("\
Congratulations! You have won a prize of 100 points! ")

                            # not giving any points if user entered 2
                            if user_choice == 2:
                                print("\
unfortunately, you do not gain any points, as you have altered the words. ")

                            else:
                                user_points += 100
                                print("Your total is now {}. " .format(user_points))
                            valid_letter = True

                        elif tries < 1:
                            print("\
You have ran out of tries. the word was {}. " .format(string_word))
                            if user_choice == 2:
                                # not taking any points if user entered 2
                                print("\
You do not lose any points, as you have altered the word bank. ")
                            else:
                                user_points -= 70
                                print("\
You have lost 70 points, now your total is {}." .format(user_points))
                            valid_letter = True

                        else:
                            valid_letter = False

        # if user wants to play again
        new_game = input("Do you want to play again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO":
            new_game = input("Please enter again. ")
        if new_game.upper() == "NO":
            print("Alright, have a good day. ")

    return user_points


class counter(threading.Thread):
    def __init__(self, value, increment):
        threading.Thread.__init__(self)  # initilize thread
        self.value = value  # starting value
        self.increment = increment  # amount to add
        self.alive = False  # controls while loop in run

    def run(self):  # main function that will run thread
        self.alive = True
        while self.alive:
            time.sleep(1)
            self.value += self.increment  # does the counting

    def finish(self):  # stops thread and returns final value
        self.alive = False
        return self.value


# start of coin toss game
def coin_toss(user_points):
    # prest values
    penalty = 50
    # useless hints
    HINTS = ["tail of a mongoose", "front of a viper",
             "feathers on the hawk", "beneath the dragon",
             "descendant of the legends", "whisper of the wind",
             "breath of the wilds", "opening in the abyss",
             "fear in the back", "burning of the eyes",
             "silence of the underneath", "movement of the air",
             "warmth of the sun", "closure of the mask"]

    COMPUTER_OUTCOME = {"heads": "tails",
                        "tails": "heads"}

    USER_CHOICE = {"h": "heads",
                   "t": "tails"}

    # rules and specifications
    print("""
Welcome to the coin toss.
You will be playing against the computer for a total of 200 points.
The rules are:
The computer will give you a riddle to help you find your answer.
A coin will be thrown in the air. \
You have five seconds to shout heads or tails before the timer ends.
If you do not answer within the 5 seconds, you will automatically lose.
If you choose to leave while the coin has been tossed, \
you will get a penalty of 50 points.
If you guess and the coin is the opposite, you lose 10 points.
If you guess right and the coin is the same face as your answer, you win. """)

    new_game = "yes"
    while new_game.upper() == "YES":
        # setting timer values
        coin_counter = counter(1, 1)
        print("\
Enter 1 to start playing, \
h: heads, t: tails, 0 to leave the game. ")

        valid_input = False
        while not valid_input:
            try:
                user_choice = int(input())
                valid_input = True
            # making sure user enters 1 or 0
            except ValueError:
                print("Please enter 1 to play, and 0 to leave. ")

            if valid_input:
                if user_choice < 0 or user_choice > 1:
                    print("Please enter 1 to play, and 0 to leave. ")
                    valid_input = False

                # if user enters 0
                elif user_choice == 0:
                    print("\
I get it, you don't like 'gambling'. \
Go enjoy another game. ")

                else:
                    random_hint = random.choice(HINTS)
                    print("\
coin is flipping. Please enter within 5 seconds. \
Your hint is: \n\n{} " .format(random_hint))
                    # starting coin timer
                    coin_counter.start()
                    coin_face = False
                    while not coin_face:
                        try:
                            face_choice = input().lower()
                            coin_face = True

                        # making sure user enters h, t, or 0
                        except ValueError:
                            print("\
please enter h for heads, and t for tails. ")

                        if coin_face:
                            if face_choice != "h" and face_choice != "t" and face_choice != "0":
                                print("\
please enter h for heads, and t for tails. \
or 0 to exit. ")
                                coin_face = False

                            # checking how long the user took
                            else:
                                if coin_counter.finish() > 5:
                                    user_points -= 10
                                    print("\
Too late, the coin has already hit the ground. \
\nYou have lost 10 points. Your total is now {}. \
" .format(user_points))

                                # letting user leave
                                elif face_choice == "0":
                                    user_points = exit_command(user_points, penalty)

                                # if user entered h, or t
                                else:
                                    user_face = (USER_CHOICE[str(face_choice)])
                                    computer_face = (COMPUTER_OUTCOME[str(user_face)])
                                    user_points -= 10
                                    print("\
You have chosen {}. \nThe coin face is {}. \nUnlucky. \
You have lost 10 points. Your total is now {}. \
" .format(user_face, computer_face, user_points))

        # if user wants to play again
        new_game = input("Do you want to go again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO":
            new_game = input("Please enter again. ")
        if new_game.upper() == "NO":
            print("Alright, have a good day. ")

    return user_points


# beginning of joke teller
def dad_jokes(user_points):

    # "soft" guestions and answers
    soft_questions = {"1": "How does a man on the moon cut his hair?",
                      "2": "\
Why is it a bad idea to iron your four-leaf clover?",
                      "3": "\
When I was a kid, my mother told me I could be anyone I wanted to be.",
                      "4": "\
Why did the invisible man turn down the job offer?",
                      "5": "Want to hear a joke about construction?",
                      "6": "How does Moses make his coffee?",
                      "7": "Why do bees have sticky hair?",
                      "8": "Why do Dads \
take an extra pair of socks when they go golfing?",
                      "9": "What's the best time to go to the dentist?",
                      "10": "Why did the scarecrow win an award?"}

    soft_answers = {"1": "Eclipse it.",
                    "2": "Cause you shouldn't press your luck.",
                    "3": "Turns out, identity theft is a crime.",
                    "4": "He couldn't see himself doing it!",
                    "5": "I'm still working on it!",
                    "6": "Hebrews it.",
                    "7": "Because they use a honeycomb.",
                    "8": "In case they get a hole in one.",
                    "9": "Tooth-hurty.",
                    "10": "Because he was outstanding in his field!"}

    # "hard" questions and answers
    hard_questions = {"1": "I can't take my dog \
to the pond anymore because the ducks keep attacking him.",
                      "2": "What do sprinters eat before a race?",
                      "3": "Why couldn't the bicycle stand up by itself?",
                      "4": "How many apples grow on a tree?",
                      "5": "Why did the old man fall in the well?",
                      "6": "Do you know the last thing \
my grandfather said to me before he kicked the bucket?",
                      "7": "What is the tallest building in the world?",
                      "8": "What do you call a beehive without an exit?",
                      "9": "How does a penguin build its house?",
                      "10": "I like telling Dad jokes."}

    hard_answers = {"1": "That's what I get for buying a pure bread dog.",
                    "2": "Nothing, they fast!",
                    "3": "It was two tired!",
                    "4": "All of them!",
                    "5": "Because he couldn't see that well!",
                    "6": "'Grandson, watch how far I can kick this bucket.'",
                    "7": "The library—it's got the most stories.",
                    "8": "Unbelievable.",
                    "9": "Igloos it together!",
                    "10": "Sometimes he laughs!"}

    # nested dictionary if user wants to add their own jokes
    JOKE_CHANGE = {"1": soft_questions,
                   "2": hard_questions,
                   "3": soft_answers,
                   "4": hard_answers}
    print("""
Welcome to the joke telling room. \
We will tell you jokes for free. Just because we can.
You are also able to put in your own jokes into the code if you want. """)
    new_game = "yes"
    while new_game.upper() == "YES":

        # rules and specifications

        print("""
1 to get the funny jokes
2 for the INTENSE jokes,
3 to put in your own jokes,
and 0 to leave.
Enjoyyyyyyyyyy. """)
        valid_input = False
        while not valid_input:
            try:
                random_number = random.randint(1, 10)
                user_choice = int(input())
                valid_input = True
            except ValueError:
                # making sure the user enters an integer
                print("\
Please enter 1 or 2 for a joke, \
3 to make your own jokes, and 0 to leave. ")

            if valid_input:
                # making sure the user enters 0 - 2
                if user_choice < 0 or user_choice > 3:
                    print("\
please enter 1 or 2 for a joke, \
3 to make your own jokes, and 0 to leave. ")
                    valid_input = False

                # if user wants to leave the game
                elif user_choice == 0:
                    print("\
It was great having you. Don't worry, \
your points are still {}. \nGo and enjoy another game. \
" .format(user_points))
                    return user_points

                # if user wants to add their own jokes
                elif user_choice == 3:
                    extra_joke = "yes"
                    while extra_joke.upper() == "YES":

                        # list use wants to change
                        print("\
Would you like to change a joke from list 1 or 2? ")
                        valid_joke = False
                        while not valid_joke:
                            try:
                                joke_list = int(input())
                                valid_joke = True

                            except ValueError:
                                print("\
Please enter 1 or 2 to choose the list. ")
                                valid_joke = False

                            if valid_joke:
                                if joke_list != 1 and joke_list != 2:
                                    print("\
Please enter 1 or 2 for a list you want to change. ")
                                    valid_joke = False

                                else:
                                    print("\
Enter 1 - 10 to pick which slot you want to put in. ")
                        # which slot user wants to fill
                        valid_number = False
                        while not valid_number:
                            try:
                                joke_choice = int(input())
                                valid_number = True

                            except ValueError:
                                print("\
Please enter 1 - 10 for the slot you want to fill. ")
                                valid_number = False

                            if valid_number:
                                if joke_choice < 1 or joke_choice > 10:
                                    print("\
Please enter 1 - 10 for the slot you want to fill. ")
                                    valid_number = False

                                else:
                                    print("\
Please type in the question part of your joke. ")
                        # question part of joke
                        valid_question = False
                        while not valid_question:
                            joke_question = input()
                            valid_question = True

                            if len(joke_question) == 0:
                                print("Please don't submit an empty space. ")
                                valid_question = False

                        # answer part of joke
                        print("Please type in your answer to the question. ")
                        valid_answer = False
                        while not valid_answer:
                            joke_answer = input()
                            valid_answer = True

                            if len(joke_answer) == 0:
                                print("Please don't submit an empty space. ")
                                valid_answer = False

                        # putting question and answer into list
                        JOKE_CHANGE[str(joke_list)][str(joke_choice)] = joke_question
                        joke_list += 2
                        JOKE_CHANGE[str(joke_list)][str(joke_choice)] = joke_answer
                        print("In list {}, number {}, \
you have put in the joke: \nQuestion: {} \nAnswer: {} \
" .format(joke_list - 2, joke_choice, joke_question, joke_answer))

                        # if user wants to add more jokes
                        extra_joke = input("Do you want \
to add another joke? yes/no ")
                        while extra_joke.upper() != "YES" and extra_joke.upper() != "NO":
                            extra_joke = input("\
I don't know what you entered. Please try again. ")
                        if extra_joke.upper() == "NO":
                            print("Time to user your custom jokes. \
\nEnter 1 for funny jokes, and 2 for INTENSE jokes. ")
                            valid_input = False

                # user enters 1
                elif user_choice == 1:
                    random_question = (soft_questions[str(random_number)])
                    random_answer = (soft_answers[str(random_number)])
                    print(random_question)
                    print("The answer will appear in 5 seconds\n ")
                    time.sleep(5)
                    print(random_answer)

                # user enters 2
                else:
                    random_question = (hard_questions[str(random_number)])
                    random_answer = (hard_answers[str(random_number)])
                    print(random_question)
                    print("The answer will appear in 5 seconds\n ")
                    time.sleep(5)
                    print(random_answer)

        new_game = input("Do you want to go again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO":
            new_game = input("Please enter again. ")
        if new_game.upper() == "NO":
            print("Alright, have a good day. ")

    return user_points


# beginning of 21 game
def twenty_one_game(user_points):
    # preset values
    penalty = 40
    # computer's choices
    COMPUTER_CHOICES = {"1": 3,
                        "2": 2,
                        "3": 1}

    # rules and specifications
    print("""
Welcome to the 21 game. The rules are:
You and the computer are counting up to 21 from 0.
You can up count any values from 1 - 3, \
you and the computer will take turns counting up.
Whoever is forced to count 21 loses the game.
The game will cost 10 points for an entry, for a prize of 100 points per win.
If you leave after the round has started, you will get a penalty of 40. """)
    new_game = "yes"
    while new_game.upper() == "YES":
        print("Please enter 1, 2, or 3, and 0 to leave. ")
        current_total = 0
        valid_input = False
        while not valid_input:
            try:
                user_choice = int(input())
                valid_input = True
            except ValueError:
                # making sure user enters an integer
                print("Please enter 1, 2, 3 or 0 to leave")
                valid_input = False

            if valid_input:
                if user_choice < 0 or user_choice > 3:
                    # making sure user enters 0 - 3
                    print("Please enter something between 0 - 3. ")
                    valid_input = False

            # if user wants to leave game
                elif user_choice == 0 and current_total != 0:
                    user_points = exit_command(user_points, penalty)

            # if game has not ended yet
                elif user_choice != 0:
                    if current_total < 20:
                        computer_choice = (COMPUTER_CHOICES[str(user_choice)])
                        print(computer_choice)

                        current_total += user_choice + computer_choice
                        print(current_total)
                        print("You have chosen {}, \
computer has decided on {}. The total is now {}. \
" .format(user_choice, computer_choice, current_total))
                        valid_input = False

                    # game has ended
                    elif valid_input and current_total >= 20:
                        user_points -= 50
                        print("Unlucky. You have landed on 21, \
meaning you have lost. the fee was 10 points, \
meaning your total is now {} " .format(user_points))

        new_game = input("Do you want to go again? yes/no ")
        while new_game.upper() != "YES" and new_game.upper() != "NO":
            new_game = input("Please enter again. ")
        if new_game.upper() == "NO":
            print("Alright, have a good day. ")

    return user_points


# main block
def main():
    # users starting points
    user_points = 200
    print("""Hello there user.
Welcome to the arcade, where you can play for points \
and feel good about yourself \
when your points multiply tenfold.
Please choose a game on this list to play, \
depending on the difficulty and risk level.
The games include: """)

    valid_entry = False
    while not valid_entry:
        # games
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

            # making sure user enters an integer
            except ValueError:
                print("Please enter an integer. ")
                valid_input = False

            if valid_input:
                # making sure user enters 0 - 9
                if game_choice > 9 or game_choice < 0:
                    print("Please enter 0 through 9. ")
                    valid_input = False

                # if user wants to exit program
                elif game_choice == 0:
                    print("Thank you for playing the Arcade_Games Program. ")
                    valid_entry = True

                else:
                    # each input will send user to the corresponding function
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
