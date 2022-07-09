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
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }
'''
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
'''
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



