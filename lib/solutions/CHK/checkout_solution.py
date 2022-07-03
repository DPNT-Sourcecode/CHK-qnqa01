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
        'A': {
            'num': 3,
            'price': 130
        },
        'B': {
            'num': 2,
            'price': 45
        }
    }

    final_sum = 0

    sku_groups = Counter(skus)

    for key, val in sku_groups.items():
        if not key in available_skus:
            return -1
        
        # calculate the special offers first
        if key in special_offers:
            even_num = val // special_offers[key]['num']

            final_sum += even_num * special_offers[key]['price']

        # calculate others
        final_sum += (val - even_num) * available_skus[key]

    return final_sum


    return -1






