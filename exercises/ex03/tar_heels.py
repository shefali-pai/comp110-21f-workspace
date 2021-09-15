"""An exercise in remainders and boolean logic."""

__author__ = "730466264"


# Begin your solution here...
integer: int = int(input("Enter an int: "))
statement_1 = integer % 2 == 0
statement_2 = integer % 7 == 0
statement_3 = integer % 14 == 0

if statement_3:
    print(str("TAR HEELS"))
else: 
    if statement_1:
        print(str("TAR"))
    else:
        if statement_2:
            print(str("HEELS"))
        else:
            print(str("CAROLINA"))