def minor_number(nums: list):
    return min(nums)


print(minor_number([58, 64, 96, 36, 28, 5]))


def squad_asterix(n: int):
    for i in range(n + 1):
        print(i * "*")


print(squad_asterix(5))


def sum_numbers(n: int):
    sum = 0
    for i in range(n):
        sum += n - i
    return sum


print(sum_numbers(10))


def summation(limit):
    return sum(range(1, limit + 1))


print(summation(10))


def cost_gas(tot: int, type: str):
    value_total = 0
    if type == "A":
        if tot <= 20:
            value_total = (1.90 - 0.03 * 1.90) * tot
        else:
            value_total = (1.90 - 0.05 * 1.90) * tot

    if type == "G":
        if tot <= 20:
            value_total = (2.50 - 0.04 * 2.50) * tot
        else:
            value_total = (2.50 - 0.06 * 2.50) * tot

    return value_total


print(cost_gas(100, "A"))
print(cost_gas(100, "G"))


def fuel_price(type, liters):
    if (type == "A"):
        price = 1.90
        discount = 0.03
        if liters > 20:
            discount = 0.05
    elif (type == "G"):
        price = 2.50
        discount = 0.04
        if liters > 20:
            discount = 0.06

    total = price * liters
    total -= total * discount
    return total


print(fuel_price("A", 100))
print(fuel_price("G", 100))
