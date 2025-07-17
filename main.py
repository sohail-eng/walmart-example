from walmart_api.playright import get_cookies
from walmart_api.walmart import get_all_saller_offer
import json
import hjson


if __name__ == "__main__":

    urls_to_scrape = [
        "https://www.walmart.com/ip/Truck-Toys-Kids-Toys-Car-for-Boys-4-in-1-Carrier-Vehicle-Transport-Toys-Birthday-Party-Boy-Gifts-for-Kids/2380327018?adsRedirect=true",
        "https://www.walmart.com/ip/LEGO-Technic-tbd-42200/6924164794",
        "https://www.walmart.com/ip/Lucky-Doug-Small-5-1-Police-Truck-Toys-2-3-4-5-Years-Old-Boys-Gifts-Toddlers-Toys-Mini-Car-Light-Sound-Car-Toys-3-4-5-Years-Old-Boy/5488927594?adsRedirect=true"
    ]

    cookies = get_cookies(url=urls_to_scrape[0])
    records = []
    for url in urls_to_scrape:
        records.append(get_all_saller_offer(url=url, cookies=cookies))
    
    with open('records.hjson', 'w') as f:
        hjson.dump(records, f)
    
    with open('records.json', 'w') as f:
        json.dump(records, f)
