from decimal import Decimal, ROUND_HALF_EVEN


def round_to_paise(price, buffer_percent=0.5, ops='add'):
    price_decimal = Decimal(str(price))
    buffer_amount_decimal = price_decimal * \
        (Decimal(str(buffer_percent)) / 100)

    pending_order_price = (
        price_decimal + buffer_amount_decimal) if ops == 'add' else (price_decimal - buffer_amount_decimal)
    pending_order_price_rounded = (
        pending_order_price * 20).quantize(1, rounding=ROUND_HALF_EVEN) / 20
    return float(pending_order_price_rounded)


if __name__ == "__main__":
    print(round_to_paise(100, 0.5, "sub"))
