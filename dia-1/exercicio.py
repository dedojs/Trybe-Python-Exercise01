import math


def maior(a: int, b: int):
    if a > b:
        return a
    else:
        return b


print(maior(100, 1000))


def media(nums: list):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)


print(media([10, 2, 3]))


def asterix(n: int):
    for i in range(n):
        print(n * "*")


print(asterix(3))


def bigger_name(names: list):
    big = []
    for name in names:
        big.append(len(name))
        if len(name) == max(big):
            return name


def bigger_name_course(names: list):
    big_name = names[0]
    for name in names:
        if len(name) > len(big_name):
            big_name = name
    return big_name


print(bigger_name(["andre", "luisa", "lara", "bob"]))
print(bigger_name_course(["andre", "luisaFlorminda", "lara", "bob"]))


def paint_wall(m: int):
    cobertura_tinta = 3
    tamanho_lata_tinta = 18
    custo_lata_tinta = 80
    # preco_litro_tinta = custo_lata_tinta / tamanho_lata_tinta
    litros_necessarios = m / cobertura_tinta
    latas_necessarias = math.ceil(litros_necessarios / tamanho_lata_tinta)
    custo_total = latas_necessarias * custo_lata_tinta
    return (latas_necessarias, custo_total)


print(paint_wall(1000))


def triangle_type(a: int, b: int, c: int):
    if (a + b) <= c or (b + c) <= a or (a + c) <= b:
        return "Não é um triângulo"

    else:
        if a == b and b == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isóceles"
        else:
            return "Triângulo Escaleno"


print(triangle_type(2, 3, 5))
print(triangle_type(5, 3, 3))
print(triangle_type(5, 2, 5))
