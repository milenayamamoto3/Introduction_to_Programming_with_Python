6.1
# notas = [0, 0, 0, 0, 0, 0, 0]  # Ou [0] * 7
# soma = 0
# x = 0
# while x < 7:
#     notas[x] = float(input(f"Nota {x}:"))
#     soma += notas[x]
#     x += 1
# x = 0
# while x < 7:
#     print(f"Nota {x}: {notas[x]:1.2f}")
#     x += 1
# print(f"Média: {soma/x:1.2f}")

6.2
# primeira = []
# segunda = []
# while True:
#     e = int(input("Digite um valor para a primeira lista (0 para terminar): "))
#     if e == 0:
#         break
#     primeira.append(e)
# while True:
#     e = int(input("Digite um valor para a segunda lista (0 para terminar): "))
#     if e == 0:
#         break
#     segunda.append(e)
# terceira = primeira[:]  # Copia os elementos da primeira lista
# terceira.extend(segunda)
# x = 0
# while x < len(terceira):
#     print(f"{x}: {terceira[x]}")
#     x = x + 1

6.3
# # Entrada para a primeira lista
# print("Criação da primeira lista:")
# lista1 = []
# n1 = int(input("Quantos elementos terá a primeira lista? "))
# for _ in range(n1):
#     elemento = input("Digite um elemento: ")
#     lista1.append(elemento)

# # Entrada para a segunda lista
# print("\nCriação da segunda lista:")
# lista2 = []
# n2 = int(input("Quantos elementos terá a segunda lista? "))
# for _ in range(n2):
#     elemento = input("Digite um elemento: ")
#     lista2.append(elemento)

# # Criar a terceira lista sem repetições
# terceira_lista = []

# # Adicionar elementos da lista1 à terceira lista
# for elemento in lista1:
#     if elemento not in terceira_lista:
#         terceira_lista.append(elemento)

# # Adicionar elementos da lista2 à terceira lista (evitando repetições)
# for elemento in lista2:
#     if elemento not in terceira_lista:
#         terceira_lista.append(elemento)

# # Exibir as listas
# print("\nPrimeira lista:", lista1)
# print("Segunda lista:", lista2)
# print("Terceira lista (sem repetições):", terceira_lista)

