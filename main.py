import sys
import json
from FetchFromRestaurantURL import FetchRestaurantData
from FetchFromLocation import getAllRestaurants
# url = "https://www.swiggy.com/restaurants/gupta-dhaba-janakpuri-sagar-pur-delhi-314645"

# develope the speed using asyncio


if __name__ == "__main__":

    if len(sys.argv) > 1:
        location = sys.argv[1]
        URLS = getAllRestaurants(location)
        print(URLS)
        All_restuarantData = []

        for i, restaurant_url in enumerate(URLS):
            print(i)
            restuarantData = FetchRestaurantData(restaurant_url)
            print(restuarantData['restaurant_name'])
            All_restuarantData.append(restuarantData)
        json_object = json.dumps(All_restuarantData, indent=4)
        print(type(json_object))
        # df = json_normalize(json_object)
        # df = pd.read_json(json_object)
        # df.to_csv('csvfile.csv', encoding='utf-8', index=False)

        with open(location +"-Restaurants-Swiggy-Data.json", "w") as outfile:
                outfile.write(json_object)
    else:
        raise ValueError(f"Please add Restaurant URL")




