from colorama import init, Fore, Back, Style
init()
play = True


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