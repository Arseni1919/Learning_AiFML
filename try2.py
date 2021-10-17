import requests

url = "https://rest.yahoofinanceapi.com/v6/finance/quote"

querystring = {"symbols": "AAPL,BTC-USD,EURUSD=X"}

headers = {
    'x-api-key': "YOUR-PERSONAL-API-KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)