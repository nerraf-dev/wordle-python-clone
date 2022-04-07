import random
from colorama import init, Fore, Back, Style
init()
play = True
words = ["crown", "build", "logic", "plane", "focus", "money", "plant", "plate", "pound", "other", "input", "horse", "green", "group", "beans", "guide", "layer", "mayor", "lunch", "limit", "model", "point", "scope", "score", "title", "total", "world"]

#Main Loop
while play:
  print(Back.WHITE + Fore.BLACK + "Start a new game? [Y/N]" + Style.RESET_ALL)
  command = input().upper()
  if command == "N":
    play = False
  elif command == "Y":
    turnCount = 0
    print("Enter a word")
    #Game / inner loop
    while turnCount < 6:
      guess = input()
      turnCount = turnCount + 1