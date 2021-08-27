"""Relational Operators!"""

__author__ = str(730466264)

left_hand_side: float = float(input("Enter value for left hand side: "))
right_hand_side: float = float(input("Enter value for right hand side: "))
statement_1 = (bool(int(left_hand_side) < int(right_hand_side)))
statement_2 = (bool(int(left_hand_side) >= int(right_hand_side)))
statement_3 = (bool(int(left_hand_side) == int(right_hand_side)))
statement_4 = (bool(int(left_hand_side) != int(right_hand_side)))

print(str(int(left_hand_side)) + " < " + str(int(right_hand_side)) + " is " + str(statement_1))
print(str(int(left_hand_side)) + " >= " + str(int(right_hand_side)) + " is " + str(statement_2))
print(str(int(left_hand_side)) + " == " + str(int(right_hand_side)) + " is " + str(statement_3))
print(str(int(left_hand_side)) + " != " + str(int(right_hand_side)) + " is " + str(statement_4))