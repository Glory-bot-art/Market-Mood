import requests
from datetime import date

url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
response = requests.get(url)
today_str = str(date.today())  # Gives '2026-11-09'
events = response.json()

for event in events:
    if event.get("impact") == "High" and event.get("date").startswith(today_str):
        print(event.get("country"), event.get("title"), event.get("date"))
    else:
        print("no news")

