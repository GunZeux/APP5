import requests
from send_mail import send_mail


topic = "tesla"
# credentials
api_key = "pub_54375a8f5e498e039d56c5f54d2e4c5fd652b"
url = "https://newsdata.io/api/1/news?" \
      "apikey=pub_54375a8f5e498e039d56c5f54d2e4c5fd652b" \
      f"&q={topic}&language=en "

# Make a request
request = requests.get(url)

# Get content as Dictionary
content = request.json()

body = f"Subject: New {topic} NEWS from API\n"
for article in content["results"][:20]:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + "\t" \
               + article['description'] + "\n" + article["link"] +2*"\n"

body = body.encode("utf-8")
send_mail(body)

print("Successful")