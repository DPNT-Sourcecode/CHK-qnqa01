from collections import Counter

from .offers import take_free_offers, n_for_x_offers, sku_prices

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) != str:
        return -1

    final_sum = 0
    sku_groups = Counter(skus)

    # apply take_free_offers
    for key, val in sku_groups.copy().items():
        if not key in sku_prices:
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
        product_count = val
        # calculate the special offers first
        if key in n_for_x_offers:
            total_offer_price = 0
            print(f'Rule N for X is working here for key {key}')
            for offer in n_for_x_offers[key]:
                offer_applied_times = product_count // offer['num']

                total_offer_price += offer_applied_times * offer['price']

                product_count -= offer_applied_times * offer['num']

            # calculate others
            print(f'No offer applied left {product_count} out of {val}')
            rest_sku_price = product_count * sku_prices[key]

            final_sum += total_offer_price + rest_sku_price
            print(f'Finale sum of {key} key is {final_sum}')
        else:
            final_sum += val * sku_prices[key]
            print(f'Finale sum after {key} key is {final_sum}')

    return final_sum
