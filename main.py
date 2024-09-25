import requests

# credentials
api_key = "pub_54375a8f5e498e039d56c5f54d2e4c5fd652b"
url = "https://newsdata.io/api/1/news?apikey=pub_" \
      "54375a8f5e498e039d56c5f54d2e4c5fd652b&q=tesla "

# Make a request
request = requests.get(url)

# Get content as Dictonary
content = request.json()

for article in content["results"]:
      print(article)