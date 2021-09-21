"""My first COMP 110 project. Where you can learn which princess you are or get a fortune."""

__author__ = "730466264"

from random import randint 
CURIOUS_FACE = "\U0001F914" 
HALO_FACE = "\U0001F607"
BLUSHING_FACE = "\U0001F60A"
player: str
points: int = 0


def greet() -> None:
    """Greeting the player of the quiz."""
    print(str("Welcome to the quiz! You will be asked a series of questions that will allow you to determine what kind of Disney princess you are or you can get a fortune. Enjoy the quiz and have fun! "))
    global player
    player = input(str("What is your name? "))
    
    
def main() -> None:
    """Entry point of program."""
    play_again: str = str("yes")
    global points
    points = 0
    greet()
    while play_again == str("yes"):
        print(str("What would you like to do next? a. Take the quiz to determine which Disney princess you are, b. Get a fortune, or C. End the quiz."))
        choice: str = str(input("Which one would you like to do? Pick a, b or c. "))
        if choice == str("c"):
            print(str(f"You have quit the game. Thank you for playing and have a great day! You have {points} points. "))
        else:
            if choice == str("a"):
                quiz_1()
            else:
                choice == str("b")
                quiz_2(points)
        play_again = (input(str(F"Do you want to play again? Print yes or no. {BLUSHING_FACE} ")))
            

def quiz_1() -> None:
    """Disney princess quiz."""
    global points
    print(str(f"Hey {player}! This quiz will allow you to determine which Disney princess you are. You will answer 3 multiple choice questions and find out at the end. Have fun!{HALO_FACE}"))
    color = input(str(f"{player}, what is your favorite color? a. red, b. yellow, c. green, d. blue. Print a, b, c, or d. "))
    if color == str("a"):
        points = points + 1
    else:
        if color == str("b"):
            points = points + 2
        else:
            if color == str("c"):
                points = points + 3
            else: 
                color == str("d")
                points == points + 4
    print(f"Current point value: {points}")
    hobby = input(str(f"{player}, what is your favorite hobby? a. spending time in nature, b. reading, c. swimming, d. singing. Print a, b, c or d. "))
    if hobby == str("a"):
        points = points + 1
    else:
        if hobby == str("b"):
            points = points + 2
        else: 
            if hobby == str("c"):
                points = points + 3
            else:
                hobby == str("d")
                points == points + 4
    print(f"Current point value: {points}")
    random_int: int = randint(1, 5)
    random_task = input(str(f"{player}, would you rather have {random_int} a. Days of no sleep, b. books to read, c. number of feet, or d. glass slipper(s). Print a, b, c, or d. "))
    if random_task == str("a"):
        points = points + 1
    else:
        if random_task == str("a"):
            points = points + 2
        else:
            if random_task == str("c"):
                points = points + 3
            else: 
                random_task == str("d")
                points == points + 4
    print(f"Current point value: {points}")
    randint_1: int = randint(1, 12)
    print(str(f"{player}! Thank you for taking the quiz! You will get a number printed based on your results. Look on the list to see where your number is to determine which princess you are! 1-3 is Aurora, 4-6 is Belle, 7-9 is Ariel, and 10-12 is Cinderella. Your number is {randint_1}."))
    

def quiz_2(x: int) -> int:
    """Fortune quiz."""
    global points
    global player
    points = 0
    pick_1 = input(str(f"Hey {player}! Get a fortune by picking a number 1- 4 {CURIOUS_FACE} "))
    if pick_1 == "1":
        points = points + 1
    else:
        if pick_1 == "2":
            points = points + 2
        else: 
            if pick_1 == "3":
                points = points + 3
            else:
                pick_1 == "4"
                points = points + 4
    print(str("Based on the number of points you have, you will receive a fortune. If you have 1 point, you will have a great day tomorrow. If you have 2 points, you are going to get a lot of money tomorrow. If you have 3 points, you are going to meet your best friend tomorrow. If you have four points, you are going to go on a nice vacation next summer."))
    print(str(f"Your number of points: {points}"))
    return x

    
if __name__ == "__main__":
    main()
