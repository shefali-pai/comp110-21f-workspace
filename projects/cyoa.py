"""My first COMP 110 project. Where you can learn which princess or animal you are."""

from random import randint 
NAME_CONSTANT = "\U0001F600" 


def greet() -> None:
    """Greeting the player of the quiz."""
    print(str("Welcome to the quiz! You will be asked a series of questions that will allow you to determine what kind of Disney princess or which animal you are. Enjoy the quiz and have fun! "))
    global player
    player = input(str("What is your name? "))
    
    
def main() -> None:
    """Entry point of program."""
    global points
    points = int(0)
    play_again: str = str("yes")
    # play_again: str = str("Do you want to play again? Print yes or no. ")
    greet()
    while play_again == str("yes"):
        print(str("What would you like to do next? a. Take the quiz to determine which Disney princess you are, b. Get a fortune, or C. End the quiz."))
        choice: str = str(input("Which one would you like to do? Pick a, b or c. "))
        if choice == str("c"):
            print(str(f"You have quit the game. Thank you for playing and have a great day! You have {points} points. "))
            print(player)
        else:
            if choice == str("a"):
                quiz_1()
            else:
                choice == str("b")
                quiz_2(points)
        print(str(f"Your number of points: {points}"))
        play_again = (input(str("Do you want to play again? Print yes or no. ")))
            

def quiz_1() -> None:
    global points
    points = int(0)
    print(str("This quiz will allow you to determine which Disney princess you are. You will answer 3 multiple choice questions and find out at the end. Have fun!"))
    color = input(str("What is your favorite color? a. red, b. yellow, c. green, d. blue. Print a, b, c, or d. "))
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
    print(points)
    hobby = input(str("What is your favorite hobby? a. spending time in nature, b. reading, c. swimming, d. singing. Print a, b, c or d. "))
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
    print(points)
    global random_int
    random_int = randint(1, 5)
    random_task = input(str(f"Would you rather have {random_int} a. Days of no sleep, b. books to read, c. number of feet, or d. glass slipper(s). Print a, b, c, or d. "))
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
    print(points)
    global randint_1
    randint_1 = randint(1, 12)
    print(str(f"Thank you for taking the quiz! You will get a number printed based on your results. Look on the list to see where your number is to determine which princess you are! 1-3 is Aurora, 4-6 is Belle, 7-9 is Ariel, and 10-12 is Cinderella. Your number is {randint_1}."))
    

def quiz_2(x: int) -> int:
    global points
    points = 0
    pick_1 = input(str("Pick a number 1- 4. "))
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
    return x
    

# print(str(f"Your number of points: {points}"))
# play_again = input(str("Do you want to play again? "))
# while (play_again == "yes"):
    # print(play_again)
    # play_again = str("Do you want to play again? ") 
    # main()
    
    
if __name__ == "__main__":
    print(NAME_CONSTANT)
    print(f"hi {NAME_CONSTANT}")
    main()
