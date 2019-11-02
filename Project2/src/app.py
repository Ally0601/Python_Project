import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.ea.com/games/apex-legends")
soup = BeautifulSoup(request.content, "html.parser")
element = soup.find("h2", {"class": "d4 d4-dark"})
check = element.text
print(check)
if check == "Play For Free*":
    print("Go ahead")
else:
    print("Get to work")


#<h2 class="d4 d4-dark">Play For Free*</h2>