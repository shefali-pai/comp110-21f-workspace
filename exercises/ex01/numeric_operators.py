"""Numeric Operaters Machine!"""

__author__ = str(730466264)

left_hand_side: float = float(input("Enter value for left hand side: "))
right_hand_side: float = float(input("Enter value for right hand side: "))

first_equation = int(left_hand_side) ** int(right_hand_side)
second_equation = int(left_hand_side) // int(right_hand_side)
third_equation = float(left_hand_side) / float(right_hand_side)
fourth_equation = int(left_hand_side) % int(right_hand_side)
print(str(int(left_hand_side)) + " " + "** " + str(int(right_hand_side)) + " is " + str(first_equation))
print(str(int(left_hand_side)) + " " + "// " + str(int(right_hand_side)) + " is " + str(second_equation))
print(str(int(left_hand_side)) + " " + "/ " + str(int(right_hand_side)) + " is " + str(third_equation))
print(str(int(left_hand_side)) + " " + "% " + str(int(right_hand_side)) + " is " + str(fourth_equation))
