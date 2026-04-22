#Smart Electricity Bill
FIRST_SLAB = 100
SECOND_SLAB = 100

RATE_1 = 3
RATE_2 = 5
RATE_3 = 8

SURCHARGE_THRESHOLD = 300
SURCHARGE_RATE = 1.1


def calculate_bill(units: int) -> int:
    original_units = units
    total = 0

    if units > FIRST_SLAB:
        total += FIRST_SLAB * RATE_1
        units -= FIRST_SLAB

    if units > SECOND_SLAB:
        total += SECOND_SLAB * RATE_2
        units -= SECOND_SLAB

    if units > 0:
        total += units * RATE_3

    if original_units > SURCHARGE_THRESHOLD:
        total = int(total * SURCHARGE_RATE)

    return total

units_input = int(input(""))
print(calculate_bill(units_input))