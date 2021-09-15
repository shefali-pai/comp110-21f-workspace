"""Drawing forests in a loop."""

__author__ = "730466264"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth_input: int = int(input("What depth do you want your forest to be? "))
i: int = int(0)

while i <= depth_input:
    print(TREE * i)   
    i = i + 1
