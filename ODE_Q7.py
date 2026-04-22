#Online Order Discount Engine
def order_discount(total_amount:float) -> float:
    rate: float = 0.0
    if total_amount >= 5000:
        rate = 0.20
    elif total_amount >= 3000:
        rate = 0.10
    elif total_amount >= 1000:
        rate = 0.05
    return total_amount * (1 - rate)