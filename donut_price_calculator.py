from typing import Union


def calculate_donut_price(multiplier: float, price: int, exp: int, **kwargs) -> float:
    exp_per_purchase = exp * 5 * ((multiplier + 100) / 100)
    return 1_000_000 / exp_per_purchase * (price * 0.75 / 3) + 16666


def donuts_per_item(multiplier: float, exp: int, **kwargs) -> float:
    exp_per_purchase = exp * 5 * ((multiplier + 100) / 100)
    return exp_per_purchase / 1_000_000 * 3


def main():
    items = {
        'Bloodmobile': {
            'price': 132000,
            'exp': 13200
        },
        'Kwik-E-Mart': {
            'price': 14400,
            'exp': 2000
        }
    }

    multiplier = 2060.52

    print(f'===== Multiplier: {multiplier} =====')
    for key, value in items.items():
        items[key] = {
            **items[key],
            'PPD': calculate_donut_price(multiplier=multiplier, **items[key]),
            'DPI': donuts_per_item(multiplier=multiplier, **items[key])
        }
        print(f'{key.ljust(11)} - price-per-donut: {items[key]["PPD"]:2.2f}')
        print(f'{key.ljust(11)} - donuts-per-item: {items[key]["DPI"]:2.2f}')

    percentage = 100 - int(items['Kwik-E-Mart']['PPD'] / items['Bloodmobile']['PPD'] * 100)
    print(f'KEM is %{int(percentage)} more cost efficient (Using MAX price only)')


if __name__ == '__main__':
    main()
