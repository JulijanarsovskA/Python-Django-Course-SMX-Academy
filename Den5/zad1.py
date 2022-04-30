"""- Da se ispecati nickname, dali profiilot e verificiran
-da se ispecati linkot vo bio
- da se ispecati kolku go sledat ovoj profiil
-kolku sledni
-kolku 'lajkovi' ima ovoj profiil
"""

userInfo = {
    "user": {
        "id": "127905465618821121",
        "uniqueId": "khaby.lame",
        "nickname": "Khabane lame",
        "signature": "Se vuoi ridere sei nel posto giusto😎 \nIf u wanna laugh u r in the right place😎",
        "verified": True,
        "secUid": "MS4wLjABAAAAwAg0rSzO65WQfz4RzQgGv2Xdv108BgPXhRrrmNVIHQZ9PO8-flwwRtEppYTS0OjA",
        "secret": False,
        "ftc": False,
        "relation": 0,
        "openFavorite": False,
        "bioLink": {
            "link": "https://khabyshop.com",
            "risk": 3
        },
        "commentSetting": 0,
        "duetSetting": 0,
        "stitchSetting": 0,
        "privateAccount": False,
        "isADVirtual": False,
        "isUnderAge18": False
    },
    "stats": {
        "followingCount": 71,
        "followerCount": 135400000,
        "heartCount": 0,
        "videoCount": 1037,
        "diggCount": 0,
        "heart": 2200000000
    }
}

for i in userInfo:
    print(userInfo["user"]["nickname"])
    print(userInfo["user"]["verified"])
