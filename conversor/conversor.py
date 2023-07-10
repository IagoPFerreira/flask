variantes = {
    'mili': 0.001,
    'centi': 0.01,
    'deci': 0.1,
    'base': 1,
    'deca': 10,
    'hecto': 100,
    'kilo': 1000
}

referenciais = {
    'libra': 0.45359237,
}

print(
    'Use as medidas abaixo como referência: \n',
    'mili - para miligrama\n',
    'centi - para centigrama\n',
    'deci - para decigrama\n',
    'base - para grama\n',
    'deca - para decagrama\n',
    'hecto - para hectograma\n',
    'kilo - para quilograma\n',
)

valor = input('Insira o valor a ser convertido: ')
de = str(input('Insira a medida de base: '))
para = str(input('Insira a medida para onde ir: '))
conversor = variantes[de] / variantes[para]


print(round(float(valor) * conversor, 2), conversor, de, para)
