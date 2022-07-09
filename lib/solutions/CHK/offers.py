from enum import Enum

class Offer(Enum):
    TakeFree = 'take_free',
    NForX = 'n_for_x',
    NAnyOfListForX = 'n_any_of_list_for_x'

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
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
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
    ],
    'H': [
        {
            'num': 10,
            'price': 80
        },
        {
            'num': 5,
            'price': 45
        }
    ],
    'K': [
        {
            'num': 2,
            'price': 150
        }
    ],
    'P': [
        {
            'num': 5,
            'price': 200
        }
    ],
    'Q': [
        {
            'num': 3,
            'price': 80
        }
    ],
    'U': [
        {
            'num': 4,
            'price': 120
        }
    ],
    'V': [
        {
            'num': 3,
            'price': 130
        },
        {
            'num': 2,
            'price': 90
        }
    ]
}

take_free_offers = {
    'E': [
        {
            'num': 2,
            'free_item_name': 'B'
        }
    ],
    'N': [
        {
            'num': 3,
            'free_item_name': 'M'
        }
    ],
    'R': [
        {
            'num': 3,
            'free_item_name': 'Q'
        }
    ]
}

n_any_of_list_for_x = {
    'items': ['S', 'T', 'X', 'Y', 'Z'],
    'num': 3,
    'price': 45
}



