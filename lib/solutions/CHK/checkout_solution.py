from collections import Counter

from sandbox.interview_tasks.accelerate_runner.lib.solutions.CHK.offers import take_free_offers, n_for_x_offers

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


    final_sum = 0
    sku_groups = Counter(skus)

    # apply take_free_offers
    for key, val in sku_groups.items():
        if not key in available_skus:
            return -1

        if key in n_for_x_offers:
            for offer in take_free_offers[key]:
                even_num = val // offer['num']

                # reduce items
                item_to_take_for_free = offer['free_item_name']
                sku_groups[item_to_take_for_free] -= even_num

                if sku_groups[item_to_take_for_free] < 0:
                    sku_groups[item_to_take_for_free] = 0

    # apply n_for_x_offers
    for key, val in sku_groups.items():
        # calculate the special offers first
        if key in n_for_x_offers:
            even_num = val // n_for_x_offers[key]['num']
            print(f'even_num: {even_num}')

            offers_price = even_num * n_for_x_offers[key]['price']

            print(f'offers price: {offers_price}')

            # calculate others
            rest_sum = (val - even_num * n_for_x_offers[key]['num']) * available_skus[key]

            final_sum += offers_price + rest_sum

            print(f'and the final sum is {final_sum}')
        else:
            final_sum += val * available_skus[key]

    return final_sum






