import requests

response = requests.get("https://status.playstation.com/data/statuses/region/SCEA.json")
data = response.json()

networks = ["Account Management:\t", "Gaming & Social:\t", "PS Video:\t\t", "PS Store:\t\t"]
for i,n in enumerate(networks):
    print(n + ("Down" if data['status'][i]['statusType'] == 'Degraded' else "Up"))