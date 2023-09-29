import json
import requests
import sys
try:
    bitcoin_amount = float(sys.argv[1])
    bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = float(bitcoin["bpi"]["USD"]["rate"].replace(",", ""))
    dollarsValue = bitcoin_amount * rate
    print(f"${dollarsValue:,.4f}")

except (TypeError, ValueError):
    sys.exit("Command-line argument is not a number")

except IndexError:
    sys.exit("Missing command-line argument")
