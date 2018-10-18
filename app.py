import miniflux
import requests
import os

notify_url = os.environ['REACT_NOTIFY_URL_WITH_CODE']
miniflux_site = os.environ['MINIFLUX']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
client = miniflux.Client(miniflux_site, username, password)

# Unread entries notification
entries = client.get_entries(status="unread", limit=1000, direction="desc")

message = ''
if 'total' in entries:
    unread_count = entries['total']
    if unread_count > 0 and unread_count < 1000:
        message = f'You have {unread_count} unread entries at {miniflux_site}'
    elif unread_count is 1000:
        message = f'You have 1000+ unread entries at {miniflux_site}'

print(message)

if message:
    body = {
        "msg": message,
        "recipientId": "240963940"
    }
    requests.post(notify_url, json = body)

