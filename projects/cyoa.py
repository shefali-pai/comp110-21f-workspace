"""My first COMP 110 project. Where you can learn which princess or animal you are."""

points: int = int(0)


def greet() -> None:
    """Greeting the player of the quiz."""
    print(str("Welcome to the quiz! You will be asked a series of questions that will allow you to determine what kind of Disney princess or which animal you are. Enjoy the quiz and have fun! "))
    global player
    player = input(str("What is your name? "))
    print(player)
    
    
def main() -> None:
    """Entry point of program."""
    greet()
    print(str("What would you like to do next? a. Take the quiz to determine which Disney princess you are, b. Take the quiz to determine which animal you are, or C. End the quiz."))
    choice: str = str(input("Which one would you like to do? Pick a, b or c. "))
    if choice == str("c"):
        print(str(f"You have quit the game. Thank you for playing and have a great day! You have {points} points. "))
        print(player)
    else:
        if choice == str("a"):
            quiz_1()
        else:
            choice == str("b")
            quiz_2()

    # play_again = str("Do you want to play again?")
    # while (play_again == "yes"):
        # print("play again")
         
        # play_again = str("Do you want to play again?") 
            

def quiz_1() -> None:
    print(1)


def quiz_2() -> None:
    print(2)


if __name__ == "__main__":
    main()