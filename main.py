import requests
from twilio.rest import Client

api_key = ['Your api key']

#twillio
account_sid = ['your account_sid']
auth_token = ['Your auth token']
client = Client(account_sid, auth_token)

parameters = {
    "lat": [YOUR LATITUDE],
    "lon": [YOUR LONGITUDE],
    "appid": api_key,
    "cnt": 4

}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)

index = 0
id_list = []
while index <= 3:
    id_list.append(data['list'][index]['weather'][0]['id'])
    index += 1

for x in id_list:
    if x < 700:
        message = client.messages.create(
            from_=['Your generated number'],
            body='Its going to rain today. Make sure to bring an umbrella! ☔️',
            to=['receiver']
        )
        print(message.status)
        break
