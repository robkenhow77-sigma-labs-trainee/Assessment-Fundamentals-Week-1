"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    """Generates the final VAT invoice"""
    final_receipt = "VAT RECEIPT\n\n"
    original_prices = get_prices(receipt_string)
    vat_prices = get_vat_prices(original_prices)
    total_vat = format_float(get_total_vat(original_prices,vat_prices))
    vat_receipt = create_vat_receipt(receipt_string, vat_prices)
    final_receipt += f"{vat_receipt}\nTotal: £{format_float(sum(vat_prices))}\n"
    final_receipt += f"VAT: £{total_vat}\n"
    total_price_including_vat = get_total_price_including_vat(receipt_string)
    final_receipt += f"Total inc VAT: £{format_float(total_price_including_vat)}"
    if sum(original_prices) == 0:
        return """VAT RECEIPT\n\nTotal: £0.00\nVAT: £0.00\nTotal inc VAT: £0.00"""
    return  final_receipt


def get_prices(receipt_string: str) -> list:
    """Extracts the prices from the receipt string"""
    receipt_list = receipt_string.split("\n")
    new_prices = []
    for row in receipt_list[:-1]:
        new_prices.append(round(float(row.split("£")[1]),2))
    return new_prices


def get_vat_prices(prices:list[float]) -> list:
    """Returns a list of the prices after vat has been applied"""
    return [price * 0.8 for price in prices]


def get_total_vat(original_prices:list[float], vat_prices:list[float]) -> float:
    """ Returns the total vat"""
    return sum(original_prices) - sum(vat_prices)


def create_vat_receipt(receipt_string: str, vat_prices:list[float]) -> str:
    """Creates the items part of the final receipt"""
    receipt_list = receipt_string.split("\n")
    items = [row.split("£")[0] for row in receipt_list]
    vat_receipt = ""
    for i in range(len(vat_prices)):
        vat_receipt += f"{items[i]}£{format_float(vat_prices[i])}\n"
    return vat_receipt


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


def get_total_price_including_vat(receipt_string: str) -> float:
    """Returns the total price"""
    receipt_list = receipt_string.split("\n")
    return float(receipt_list[-1].split("£")[1])



if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""

    print(generate_invoice(receipt_string))
