import os
import random

class GameStorage:

    def __init__(self, start_number, end_number):
        self.start_number = start_number
        self.end_number = end_number
        self.choosen_number = 0
        self._num_guessed = 0
    
    def pick_a_number(self):
        self.choosen_number = random.randint(self.start_number, self.end_number)


class Hint:

    def __init__(self, Game: GameStorage):
        self.Game = Game
        
    def give_a_hint(self, last_guessed_number):
        if last_guessed_number > self.Game.choosen_number:
            print("- The choosen number is `lower` than what you just guessed.")
        else:
            print("- The choosen number is `higher` than what you just guessed.")


class User:

    def __init__(self, Game: GameStorage):
        self.Game = Game
        self.Hint = Hint(Game= Game)
        self.number_of_guess = 1
    
    def guess(self, guessed_number):
        self.number_of_guess += 1
        if guessed_number == self.Game.choosen_number:
            os.system("clear")
            print("*"*100)
            print("\n- Well Done, You managed to guess the correct number!\n")
            print("*"*100)
            print("\n\n\n\n\n")
            initialize_game()
            return True
        else:
            print("\n- Oh, no! The number you guessed is wrong. Let me help you.")
            self.Hint.give_a_hint(int(guessed_number))
            return False


def greetings():
    print("*"*100)
    print(" Hello, It's such a great pleasure to meet with you.\n We're gonna have much fun time together.\n This is a game which I'll pick a number and give you some hints about it and you will guess it.\n By each mistake you're gonna give a new hint and of course lower points.\n")
    startup()

def startup():
    ready = input("> So are you ready ? (Yes/No) ")
    if ready.lower() in ["","y", "yes", "yeah"]:
        print("- Great!")
        initialize_game()
    else:
        print("- Oh, snap!. Maybe some other time.")

def play(user_object):
    
    guessed_num = int(input(f"\n> Guess #{user_object.number_of_guess} - Let's have a guess: "))
    r = user_object.guess(guessed_num)
    if r == False:
        play(user_object)
        
def initialize_game():
    # os.system("clear")
    start_number = int(input("\n> From what number you want to start? "))
    end_number = int(input("> What is the end number? "))
    if start_number > end_number:
        print("\n- The number you entered are not valid. The end number can't be lower than the start number. Please choose again.")
        initialize_game()
    elif (end_number - start_number) < 20:
        print("\n- The range should be greater than 20. So I have more options to choose. :) ")
        initialize_game()
    else:
        print(f"\n- Okay, I'm going to pick a number from {start_number} to {end_number}... Well, Lets go.")
        new_game = GameStorage(start_number, end_number)
        new_game.pick_a_number()
        new_user = User(Game= new_game)
        play(new_user)


if __name__ == "__main__":
    greetings()