import requests
from bs4 import BeautifulSoup
import json


def FetchRestaurantData(url):
    payload = {}
    headers = {
        'Cookie': '__SW=KwXK_WBkzaXgoe42RJ2IoFqTHNYgbfeh; _device_id=42892482-e1b7-55dc-05fe-13b99c52e95b; _guest_tid=3b481432-f04d-4851-ae39-100ed040f40e; _is_logged_in=; _sid=2zs88fbd-e814-44e1-b15e-6bb8bd0a7f2f; order_campaign=google_search_sok_food_na_narm_order_web_m_web_clubbedcities_neev_brand_newuser_v1_v2_brand_em; order_medium=CPC; order_source=Google-Sok'
    }
    restuarantData = {"error" : "Failed to load the page..."}
    response = requests.request("GET", url, headers=headers, data=payload)

    html_text = response.text
    with open("swiggy.html", "w", encoding="utf-8") as f:
        f.write(html_text)
    # print(html_text)
    soup = BeautifulSoup(html_text, "html.parser")
    child_soup = soup.find_all('script')
    for i in child_soup:
        scriptData = str(i.string)
        if ("window.___INITIAL_STATE__" in scriptData):
            # print(scriptData)

            # print(type(scriptData))
            scriptData = scriptData.split('window.___INITIAL_STATE__ =')[1]
            scriptData = scriptData.split(';   window.webpackManifest')[0]
            x = json.loads(scriptData)

            menu_obj = x['menu']

            restuarantData = {
                "restaurant_id": menu_obj['restaurant'].get('id', None),
                "restaurant_name": menu_obj['restaurant'].get('name', None),
                "latLong": menu_obj['restaurant'].get('latLong', None),
                "city": menu_obj['restaurant'].get('city', None),
                "area": menu_obj['restaurant'].get('area', None),
                "areaPostalCode": menu_obj['restaurant'].get('areaPostalCode', None),
                "areaSlug": menu_obj['restaurant'].get('areaSlug', None),
                "type": menu_obj['restaurant'].get('type', None),
                "locality": menu_obj['restaurant'].get('locality', None),
                "avgRating": menu_obj['restaurant'].get('avgRating', None),
                "totalRatings": menu_obj['restaurant'].get('totalRatings', None),
                "avgRatingString": menu_obj['restaurant'].get('avgRatingString', None),
                "totalRatingsString": menu_obj['restaurant'].get('totalRatingsString', None),
                "costForTwo": menu_obj['restaurant'].get('totalRatingsString', None),
                "costForTwoMsg": menu_obj['restaurant'].get('costForTwoMsg', None),
                "cuisines": menu_obj['restaurant'].get('cuisines', None),
                "isNew": menu_obj['restaurant'].get('isNew', None),
                "isVeg": menu_obj['restaurant'].get('isVeg', None),
                "multiOutlet": menu_obj['restaurant'].get('multiOutlet', None),
                "availability": menu_obj['restaurant'].get('availability', None),
                "aggregatedDiscountInfo": menu_obj['restaurant'].get('aggregatedDiscountInfo', None),
                "restaurantLicenses": menu_obj['restaurant'].get('restaurantLicenses', None),
                "cafe": menu_obj['restaurant'].get('cafe', None),
                "preorderable": menu_obj['restaurant'].get('preorderable', None),
                "timeStamp": menu_obj['restaurant'].get('timeStamp', None),
                "items": menu_obj.get('items', None)

            }
    return restuarantData