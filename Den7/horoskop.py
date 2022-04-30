"""https://php.mk/services/horoskop
"""
"""korisnikot da kaze z koj horoskopski znak saka horoskop, kakov da bide"""

import requests
import json

reqHor = requests.get(
    url = "https://php.mk/services/horoskop/v1.0/oven/dneven?", 
    params = {"token":"3a1131a90a3c94eda8a03462c5269af4"}
)

horoskop = json.loads(reqHor.text)
print(horoskop)
