import requests
from walmart_api.playright import get_cookies


def get_all_saller_offer(url: str, cookies: dict | None):

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US',
        'baggage': 'trafficType=customer,deviceType=desktop,renderScope=SSR,webRequestSource=Browser,pageName=itemPage,isomorphicSessionId=2yLJrkhq0Ta6bctwhf5Wl,renderViewId=0f6ecf43-91dc-4fec-b747-dc5e88d8b407',
        'content-type': 'application/json',
        'downlink': '1.55',
        'dpr': '1',
        'priority': 'u=1, i',
        'referer': url.split("?")[0],
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'tenant-id': 'elh9ie',
        'traceparent': '00-1852e84612d8855b700abeba611bc822-65e19d2eeb527641-00',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'wm_mp': 'true',
        'wm_page_url': url.split("?")[0],
        'wm_qos.correlation_id': '8Bc17sXQRhoJMsjmoGcKlz53nLPKH0leDAgL',
        'x-apollo-operation-name': 'GetAllSellerOffers',
        'x-enable-server-timing': '1',
        'x-latency-trace': '1',
        'x-o-bu': 'WALMART-US',
        'x-o-ccm': 'server',
        'x-o-correlation-id': '8Bc17sXQRhoJMsjmoGcKlz53nLPKH0leDAgL',
        'x-o-gql-query': 'query GetAllSellerOffers',
        'x-o-mart': 'B2C',
        'x-o-platform': 'rweb',
        'x-o-platform-version': 'usweb-1.213.0-5dcbd334871e94b6de9971b2179b3823e5fa497d-7141904r',
        'x-o-segment': 'oaoh',
    }

    item_id = url.split("?")[0].split("/")[-1]
        
    params = {
        'variables': '{"itemId":"' + item_id + '","isSubscriptionEligible":true,"conditionCodes":[1],"allOffersSource":"MORE_SELLER_OPTIONS"}',
    }

    response = requests.get(
        'https://www.walmart.com/orchestra/home/graphql/GetAllSellerOffers/e8826cf06648c06ca0d4324054d869afc1448c465d7304fa9da0262d7687e083',
        params=params,
        cookies=cookies or get_cookies(url=url),
        headers=headers,
    )

    return response.json()

if __name__ == "__main__":
    offers_data = get_all_saller_offer(url="https://www.walmart.com/ip/LEGO-Technic-tbd-42200/6924164794")
    print(offers_data)
