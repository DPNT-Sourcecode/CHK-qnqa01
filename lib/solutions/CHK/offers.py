from enum import Enum

class Offer(Enum):
    TakeFree = 'take_free',
    NForX = 'n_for_x'

special_offers = {
    'A': [
        {
            'name': Offer.NForX,
            'num': 5,
            'price': 200
        },
        {
            'name': Offer.NForX,
            'num': 3,
            'price': 130
        }
    ],
    'B': [
        {
            'name': Offer.NForX,
            'num': 2,
            'price': 45
        }
    ],
    'E': [
        {
            'name': Offer.TakeFree,
            'num': 2,
            'freeItemName': 'B'
        }
    ]
}

take_free_offers = {}

# for sku, offers in special_offers.items():
#     for offer in offers:
#         if offer['name'] == Offer.TakeFree:
#             if sku in take_free_offers:
#                 take_free_offers[sku].append(offer)
#             else:
#                 take_free_offers[sku] = [offer]





