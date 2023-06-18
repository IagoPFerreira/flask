# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b);


# permission = {"member", "group"}
# print(permission)

# permission.add("root")
# print(permission)

# permission.add("member")
# print(permission)


# print(permission.union({"user"}))


# print(permission.intersection({"user", "member"}))


# print(permission.difference({"user"}))

# info = {
#   "personagem": "Margarida",
#   "origem": "Pato Donald",
#   "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
# }

# info["recorrente"] = "Sim"

# print(info)

# restaurants = [
#     {"name": "Restaurante A", "nota": 4.5},
#     {"name": "Restaurante B", "nota": 3.0},
#     {"name": "Restaurante C", "nota": 4.2},
#     {"name": "Restaurante D", "nota": 2.3},
# ]

# min_rating = 3.0

# filtred_restaurants = [
#   restaurant
#   for restaurant in restaurants
#   if restaurant["nota"] > min_rating
# ]

# print(filtred_restaurants)

# n = 10
# last, next = 0, 2

# while last < next:
#     print(last)
#     last, next = next, last + next

# def string(a, b):
#     return a + b


# print(string('oi', ' idiota'))
class Classe:
    _atributo_da_classe = 1

    @classmethod
    def seta_atributo_da_classe(cls, valor):
        cls._atributo_da_classe = valor

    @classmethod
    def retorna_atributo_da_classe(cls):
        return cls._atributo_da_classe


objeto_1 = Classe()
objeto_2 = Classe()

print(Classe.retorna_atributo_da_classe())  # Saída: 1
print(objeto_1.retorna_atributo_da_classe())  # Saída: 1
print(objeto_2.retorna_atributo_da_classe())  # Saída: 1

Classe.seta_atributo_da_classe(2)
print(Classe.retorna_atributo_da_classe())  # Saída: 2
print(objeto_1.retorna_atributo_da_classe())  # Saída: 2
print(objeto_2.retorna_atributo_da_classe())  # Saída: 2

objeto_1.seta_atributo_da_classe(3)
print(Classe.retorna_atributo_da_classe())  # Saída: 3
print(objeto_1.retorna_atributo_da_classe())  # Saída: 3
print(objeto_2.retorna_atributo_da_classe())  # Saída: 3