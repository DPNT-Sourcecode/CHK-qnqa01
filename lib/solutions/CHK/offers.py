from enum import Enum

class Offer(Enum):
    TakeFree = 'take_free',
    NForX = 'n_for_x'

sku_prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10
    }

n_for_x_offers = {
    'A': [
        {
            'num': 5,
            'price': 200
        }, # order is important
        {
            'num': 3,
            'price': 130
        }
    ],
    'B': [
        {
            'num': 2,
            'price': 45
        }
    ],
    'F': [
        {
            'num': 3,
            'price': 20
        }
    ]
}

take_free_offers = {
    'E': [
        {
            'num': 2,
            'free_item_name': 'B'
        }
    ]
}

# for sku, offers in special_offers.items():
#     for offer in offers:
#         if offer['name'] == Offer.TakeFree:
#             if sku in take_free_offers:
#                 take_free_offers[sku].append(offer)
#             else:
#                 take_free_offers[sku] = [offer]




