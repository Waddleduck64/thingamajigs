import math


maingirls = ["Cassie", "Mio", "Quill", "Elle", "Nutaku", "Iro", "Bonnibel", "Ayeka", "Fumi", "Bearverly", "Nina", "Alpha", "Pamu", "Luna", "Eva", "Karma", "Sutra", "Dark One", "Qpernikiss"]

lastgirl = input("Type the name of the last girl you've unlocked in the main game.\n").capitalize()

while lastgirl not in maingirls:
  if lastgirl == "Dark one" or lastgirl == "The dark one":
    lastgirl = "Dark One"
    break
  if lastgirl == "Ayano":
    lastgirl = "Ayeka"
    print("Since Ayano was renamed, this program will refer to her as Ayeka.")
    break
  if lastgirl == "Qpiddy" or lastgirl == "Q-piddy":
    lastgirl = "Qpernikiss"
    break
  lastgirl = input("That's not a valid name. Remember, this counts main game/story girls only, so no phone flings or event reward girls. Try again.\n").capitalize()

maingirls = maingirls[:maingirls.index(lastgirl) + 1]

tierlist = [maingirls[0]]
answer = ""

for i in range(1, len(maingirls)):
  low = 0
  up = len(tierlist)
  while low != up:
    now = math.floor((up-low)/2)+low
    answer = input("Which of these girls do you like better?\n1. " + tierlist[now] + "\n2. " + maingirls[i] + "\n").capitalize()
    if answer == "Dark one":
      answer = "Dark One"
    while answer != "1" and answer != "2" and answer != tierlist[now] and answer != maingirls[i]:
      answer = input("Currently, these are the only two options. Please pick one of them.\n").capitalize()
      if answer == "Dark one":
        answer = "Dark One"
    if answer == "1" or answer == tierlist[now]:
      low = now+1
    else:
      up = now
  tierlist.insert(low, maingirls[i])


print("Here are your favourite girls in order:")
for k in range(len(tierlist)):
  print(str(k + 1) + ". " + tierlist[k])