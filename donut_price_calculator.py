from typing import Union


def calculate_donut_price(multiplier: float, price: int, exp: int) -> float:
    exp_per_purchase = exp * 5 * ((multiplier + 100) / 100)
    return 1_000_000 / exp_per_purchase * (price * 0.75 / 3) + 16666


def donuts_per_item(multiplier: float, price: Union[int, list[int]], exp: int) -> float:
    exp_per_purchase = exp * 5 * ((multiplier + 100) / 100)
    return exp_per_purchase / 1_000_000 * 3


def main():
    items = {
        'Bloodmobile': {
            'price': 132000,
            'exp': 13200
        },
        'KEM': {
            'price': 14400,
            'exp': 2000
        }
    }

    multiplier = 1617.52

    price_for_bloodmobiles = calculate_donut_price(multiplier=multiplier, **items['Bloodmobile'])
    price_for_kem = calculate_donut_price(multiplier=multiplier, **items['KEM'])

    print(f'Multiplier: {multiplier}')
    print(f'Price-Per-Donut Bloodmobile farming:: {price_for_bloodmobiles}')
    print(f'Donuts per bloodmobile: {donuts_per_item(multiplier=multiplier, **items["Bloodmobile"])}')
    print(f'Price-Per-Donut: KEM farming: {price_for_kem}')
    print(f'Donuts per KEM: {donuts_per_item(multiplier=multiplier, **items["KEM"])}')
    percentage = 100 - int(price_for_kem / price_for_bloodmobiles * 100)
    print(f'KEM is %{int(percentage)} more cost efficient')


if __name__ == '__main__':
    main()
