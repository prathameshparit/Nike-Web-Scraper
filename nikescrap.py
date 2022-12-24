import pandas as pd
from IPython.core.display import HTML
import requests  # pip install requests
import json


def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'


# Make GET request to site
count = 60
anchor = 0
country = 'gb'
country_language = 'en-GB'
query = 'jordan'


def nike_scrap(count, anchor, country, country_language, query):
    # https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=7AD99480CC8C172189A71396AD43F300&country=in&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(IN)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(e9266a2a-2ed2-4e6b-a602-5a3bae7475bb%2C16633190-45e5-4830-a068-232ac7aea82c)%26anchor%3D24%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D
    url = f'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=241B0FAA1AC3D3CB734EA4B24C8C910D&country={country}&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace({country})%26filter%3Dlanguage({country_language})%26filter%3DemployeePrice(true)%26searchTerms%3D{query}%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D{count}&language={country_language}&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D'

    html = requests.get(url=url)
    output = json.loads(html.text)

    all_titles = []
    all_subtitle = []
    all_price = []
    all_colors = []
    all_image = []
    all_customizable = []

    for item in output['data']['products']['products']:
        title = item['title']
        subtitle = item['subtitle']
        price = item['price']['currentPrice']
        colors = item['colorDescription']
        image = item['images']['portraitURL']
        customizable = item['customizable']
        all_titles.append(title)
        all_subtitle.append(subtitle)
        all_price.append(f"${price}")
        all_colors.append(colors)
        all_image.append(image)
        all_customizable.append(customizable)

    df = pd.DataFrame(
        {'Product Name': all_titles, 'Price': all_price, 'Description': all_subtitle, 'Colors': all_colors,
         'ImageURL': all_image, 'Customizable': all_customizable})

    df.to_csv("output.csv")

    return df


# print(nike_scrap(count, anchor, country, country_language, query))
