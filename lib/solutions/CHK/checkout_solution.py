from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) != str:
        return -1

    available_skus = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    special_offers = {
        'A': [
            {
                'name': 'NForX',
                'num': 5,
                'price': 200
            },
            {
                'name': 'NForX',
                'num': 3,
                'price': 130
            }
        ],
        'B': [
            {
                'name': 'NForX',
                'num': 2,
                'price': 45
            }
        ],
        'E': [
            {
                'name': 'TakeFree',
                'num': 2,
                'freeItemName': 'B'
            }
        ]
    }

    final_sum = 0

    sku_groups = Counter(skus)

    for key, val in sku_groups.items():
        if not key in available_skus:
            return -1
        
        # calculate the special offers first
        if key in special_offers:
            even_num = val // special_offers[key]['num']
            print(f'even_num: {even_num}')

            offers_price = even_num * special_offers[key]['price']

            print(f'offers price: {offers_price}')

            # calculate others
            rest_sum = (val - even_num * special_offers[key]['num']) * available_skus[key]

            final_sum += offers_price + rest_sum

            print(f'and the final sum is {final_sum}')
        else:
            final_sum += val * available_skus[key]

    return final_sum




