from bs4 import BeautifulSoup
import requests
import pandas as pd

#QB List

compiledlist = []
URLlist = ["http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=1&filter=quarterback","http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=quarterback"]

for URL in URLlist:
  QB_List = requests.get(URL)

  soup = BeautifulSoup(QB_List.content, "html.parser")

  table = soup.find("table", id = "result")

  links = table.find_all("a")

  player = []
  hyper = []

  for link in links[::2]:
    player.append(link.get_text())
    #print(link.get("href"))
    hyper.append(link.get("href"))

  hypertrim = []

  for item in hyper:
    hypertrim.append(item[:-7])

  team = []

  for link in links[1::2]:
    team.append(link.get_text())
    #print(link.get("href"))

  dfstarter = {"Player": player, "Team": team, "Link": hypertrim}

  linktable = pd.DataFrame(dfstarter).set_index("Player")

  compiledlist.append(linktable)

QBoutput = pd.concat(compiledlist)

print(QBoutput)

QBoutput.to_csv("out.csv")