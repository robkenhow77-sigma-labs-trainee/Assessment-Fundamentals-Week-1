
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    """ Takes a shopping item as a dictionary and adds it to the basket list"""
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    """ Generates a receipt based on a basket of goods. The basket is a list
    of dictionaries which contain the product name and price.
    """
    if len(basket) == 0:
        return "Basket is empty"
    receipt = ""
    for good in basket:
        if good["price"] == 0:
            receipt += f'{good["name"]} - Free\n'
        else:
            receipt += f'{good["name"]} - £{format_float(good["price"])}\n'
    return  receipt + f"Total: £{format_float(get_total(basket))}"


def format_float(number:float) -> str:
    """ Converts a float value to a string to accurately resemble currency """
    number = round(number, 2)
    number_and_remainder = str(number).split('.')
    if len(number_and_remainder) == 1:
        return f"{number_and_remainder[0]}.00"
    if len(number_and_remainder[1]) == 0:
        return f"{number_and_remainder[0]}.00"
    if len(number_and_remainder[1]) == 1:
        return f"{number_and_remainder[0]}.{number_and_remainder[1]}0"
    return  f"{number_and_remainder[0]}.{number_and_remainder[1]}"


def get_total(basket: list) -> float:
    """ Returns the total cost"""
    total = 0
    for good in basket:
         total += good["price"]
    return total


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
