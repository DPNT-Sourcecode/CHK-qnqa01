from collections import Counter

from .offers import take_free_offers, n_for_x_offers

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) != str:
        return -1

    available_skus = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    final_sum = 0
    sku_groups = Counter(skus)

    # apply take_free_offers
    for key, val in sku_groups.copy().items():
        if not key in available_skus:
            return -1

        if key in take_free_offers:
            print(f'take free offers are available for the key: {key}')
            for offer in take_free_offers[key]:
                even_num = val // offer['num']
                print(f'even num is {even_num}')

                # reduce items
                item_to_take_for_free = offer['free_item_name']
                print(f'Item to change {sku_groups[item_to_take_for_free]}')
                sku_groups[item_to_take_for_free] -= even_num

                # items cannot be negative
                if sku_groups[item_to_take_for_free] < 0:
                    sku_groups[item_to_take_for_free] = 0

    # apply n_for_x_offers
    for key, val in sku_groups.items():
        # calculate the special offers first
        if key in n_for_x_offers:
            print(f'Rule N for X is working here for key {key}')
            for offer in n_for_x_offers[key]:
                even_num = val // offer['num']

                offers_price = even_num * offer['price']

            # calculate others
            rest_sum = (val - even_num * offer['num']) * available_skus[key]

            final_sum += offers_price + rest_sum
            print(f'Finale sum after {key} key is {final_sum}')
        else:
            final_sum += val * available_skus[key]
            print(f'Finale sum after {key} key is {final_sum}')

    return final_sum

