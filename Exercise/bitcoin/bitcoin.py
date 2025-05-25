import requests, sys

if len(sys.argv) < 2:
    sys.exit('Missing command-line argument')

try:
    bitcoin = float(sys.argv[1])

except ValueError:
    sys.exit('Command-line argument is not a number')

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
amount = bitcoin * o['bpi']['USD']['rate_float']

print(f"${amount:,.4f}")