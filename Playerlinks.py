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

QBoutput.to_csv("QBout.csv")

#RB List
compiledlist = []
URLlist = ["http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=1&filter=runningback&conferenceAbbr=null", "http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=2&filter=runningback&conferenceAbbr=null", "http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=runningback&conferenceAbbr=null"]

for URL in URLlist:
  RB_List = requests.get(URL)

  soup = BeautifulSoup(RB_List.content, "html.parser")

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

RBoutput = pd.concat(compiledlist)

print(RBoutput)

RBoutput.to_csv("RBout.csv")

#WR List
compiledlist = []
URLlist = ["http://www.nfl.com/players/search?category=position&filter=widereceiver&conferenceAbbr=null&playerType=current&conference=ALL", "http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=widereceiver&conferenceAbbr=null", "http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=widereceiver&conferenceAbbr=null", "http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=4&filter=widereceiver&conferenceAbbr=null", "http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=5&filter=widereceiver&conferenceAbbr=null"]

for URL in URLlist:
  WR_List = requests.get(URL)

  soup = BeautifulSoup(WR_List.content, "html.parser")

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

WRoutput = pd.concat(compiledlist)

print(WRoutput)

WRoutput.to_csv("WRout.csv")

#TE List
compiledlist = []
URLlist = ["http://www.nfl.com/players/search?category=position&filter=tightend&conferenceAbbr=null&playerType=current&conference=ALL", "http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=tightend&conferenceAbbr=null", "http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=tightend&conferenceAbbr=null"]

for URL in URLlist:
  TE_List = requests.get(URL)

  soup = BeautifulSoup(TE_List.content, "html.parser")

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

TEoutput = pd.concat(compiledlist)

print(TEoutput)

TEoutput.to_csv("TEout.csv")