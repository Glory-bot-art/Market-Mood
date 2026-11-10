from datetime import datetime, timedelta
import requests


url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
response = requests.get(url, timeout=10)
events: list[dict] = response.json()

today = datetime.today().date()
tomorrow = today + timedelta(days=1)

for event in events:
    date_str = event.get("date")
    if not date_str:
        continue

    dt = datetime.fromisoformat(date_str)
    local_dt = dt.astimezone()

    if event.get("impact") == "High" and local_dt.date() in (today, tomorrow):
        clean_time = local_dt.strftime("%a, %d %b | %I:%M %p")
        print(f"{event.get('country')} | {event.get('title')} | {clean_time}")