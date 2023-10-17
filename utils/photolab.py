import requests
# import asyncio


async def effect_picture(img_url):
    url = "https://photolab-me1.p.rapidapi.com/photo"

    querystring = {"id":"25626517","photo":img_url}

    headers = {
        "X-RapidAPI-Key": "1c330a2f08msh848ab9829abc7ecp155179jsn3557bd392074",
        "X-RapidAPI-Host": "photolab-me1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    res = response.json()
    return res['result']['img_url'][0]

# print(effect_picture("https://www.ncsasports.org/wp-content/uploads/2023/06/homepage-hero-5-runner-1440.jpg"))

# url = "https://t3.ftcdn.net/jpg/02/43/12/34/360_F_243123463_zTooub557xEWABDLk0jJklDyLSGl2jrr.jpg"   
# rasm = asyncio.run(effect_picture(img_url=url))
# print(rasm)