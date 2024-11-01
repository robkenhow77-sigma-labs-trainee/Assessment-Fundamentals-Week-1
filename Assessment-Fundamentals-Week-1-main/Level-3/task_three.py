"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    final_receipt = "VAT RECEIPT\n\n"
    original_prices = get_prices(receipt_string)
    VAT_prices = get_VAT_prices(original_prices)
    total_VAT = format_float(get_total_VAT(original_prices,VAT_prices))
    VAT_receipt = create_VAT_receipt(receipt_string, VAT_prices)
    final_receipt += f"{VAT_receipt}\nTotal: £{format_float(sum(VAT_prices))}\n"
    final_receipt += f"VAT: £{total_VAT}\n"
    total_price_including_VAT = get_total_price_including_VAT(receipt_string)
    final_receipt += f"Total inc VAT: £{format_float(total_price_including_VAT)}"
    return  final_receipt


def get_prices(receipt_string: str) -> list:
    receipt_list = receipt_string.split("\n")
    new_prices = []
    for row in receipt_list[:-1]:
       new_prices.append(round(float(row.split("£")[1]),2))
    return new_prices


def get_VAT_prices(prices:list[float]) -> list:
    return [price * 0.8 for price in prices]
 

def get_total_VAT(original_prices:list[float], VAT_prices:list[float]) -> float:
    return sum(original_prices) - sum(VAT_prices)


def create_VAT_receipt(receipt_string: str, VAT_prices:list[float]) -> str:
    receipt_list = receipt_string.split("\n")
    items = [row.split("£")[0] for row in receipt_list]
    VAT_receipt = ""
    for i in range(len(VAT_prices)):
        VAT_receipt += f"{items[i]}£{format_float(VAT_prices[i])}\n "
    return VAT_receipt
    

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


def get_total_price_including_VAT(receipt_string: str) -> float:
    receipt_list = receipt_string.split("\n")
    return float(receipt_list[-1].split("£")[1])
    


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
