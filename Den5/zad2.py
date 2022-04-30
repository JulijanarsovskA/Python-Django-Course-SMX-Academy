
data = [
    {
        "slug": "bitcoin",
        "metrics": {
                "market_data": {
                    "price_usd": 47203.69062565459
                }
        }
    },
    {
        "slug": "ethereum",
        "metrics": {
                "market_data": {
                    "price_usd": 3392.506503557496
                }
        }
    },
    {
        "slug": "tether",
        "metrics": {
                "market_data": {
                    "price_usd": 1.0001999629387988
                }
        }
    },
    {
        "slug": "binance-coin",
        "metrics": {
                "market_data": {
                    "price_usd": 446.4306552695586
                }
        }
    }]


# prv nacin

bitcoin = data[0]
print(bitcoin['slug'])
print(bitcoin['metrics']['market_data']['price_usd'])

# vtor nacin

bitcoin = data[0]
ime_valuta = bitcoin['slug']
vrednost_valuta = bitcoin['metrics']['market_data']['price_usd']

print(ime_valuta)
print(vrednost_valuta)