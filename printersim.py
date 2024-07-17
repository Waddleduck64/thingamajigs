er = "Oh shit oh fuck. Now the printer is gonna break down completely."

print("""Please use the printer as you wish.
Warning: do not insert more than 5 papers to print at once, or the printer will jam and stop working.
Warning 2: just use the number buttons 1 to 5, TIM. The other options will just cause errors as well.
""")

while True:
  papers = input("How many papers would you like to print?\n")
  if papers == "1" or papers == "2" or papers == "3" or papers == "4" or papers == "5":
    if papers == "1":
      print("You insert the paper...")
    else:
      print("You insert the papers...")
    for i in range(int(papers)):
      print("The printer ejects a piece of paper with what you wanted printed nicely on it.")
  else:
    print(er)
    break

for i in range(20):
  print("ERROR")