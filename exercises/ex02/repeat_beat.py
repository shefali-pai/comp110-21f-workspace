"""Repeating a beat in a loop."""

__author__ = "730466264"

# Begin your solution here...


beat: str = str(input("What beat do you want to repeat? "))
beat_times = int(input("How many times do you want to repeat it? "))
if beat_times <= 0:
    print("No beat...")
else: 
    beat_output = str(beat)
    i: int = 1
    while i < beat_times:
        beat_output = beat_output + " " + beat
        i = i + 1
    print(beat_output)  