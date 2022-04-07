play = True

#Main Loop
while play:
  print("Start a new game? [Y/N]")
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