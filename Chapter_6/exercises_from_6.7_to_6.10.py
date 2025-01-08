6.7
# expressão = input("Digite a sequência de parênteses a validar:")
# x = 0
# pilha = []
# while x < len(expressão):
#     if expressão[x] == "(":
#         pilha.append("(")
#     if expressão[x] == ")":
#         if len(pilha) > 0:
#             topo = pilha.pop(-1)
#         else:
#             pilha.append(")")  # Força a mensagem de erro
#             break
#     x = x + 1
# if len(pilha) == 0:
#     print("OK")
# else:
#     print("Erro")

6.8
# L = [15, 7, 27, 39]
# p = int(input("Digite o valor a procurar:"))
# x = 0
# while x < len(L):
#     if L[x] == p:
#         break
#     x += 1
# if x < len(L):
#     print(f"{p} achado na posição {x}")
# else:
#     print(f"{p} não encontrado")

6.9
# L = [15, 7, 27, 39]
# p = int(input("Digite o valor a procurar (p): "))
# v = int(input("Digite o outro valor a procurar (v): "))
# x = 0
# achouP = False
# achouV = False
# primeiro = 0
# while x < len(L):
#     if L[x] == p:
#         achouP = True
#         if not achouV:
#             primeiro = 1
#     if L[x] == v:
#         achouV = True
#         if not achouP:
#             primeiro = 2
#     x += 1
# if achouP:
#     print(f"p: {p} encontrado")
# else:
#     print(f"p: {p} não encontrado")
# if achouV:
#     print(f"v: {v} encontrado")
# else:
#     print(f"v: {v} não encontrado")
# if primeiro == 1:
#     print("p foi achado antes de v")
# elif primeiro == 2:
#     print("v foi achado antes de p")

6.10
# L = [15, 7, 27, 39]
# p = int(input("Digite o valor a procurar (p):"))
# v = int(input("Digite o outro valor a procurar (v):"))
# x = 0
# achouP = -1  # Aqui -1 indica que ainda não encontramos o valor procurado
# achouV = -1

# while x < len(L):
#     if L[x] == p:
#         achouP = x
#     if L[x] == v:
#         achouV = x
#     x += 1
# if achouP != -1:
#     print(f"p: {p} encontrado na posição {achouP}")
# else:
#     print(f"p: {p} não encontrado")
# if achouV != -1:
#     print(f"v: {v} encontrado na posição {achouV}")
# else:
#     print(f"v: {v} não encontrado")
# # Verifica se ambos foram encontrados
# if achouP != -1 and achouV != -1:
#     # Qual foi encontrado primeiro
#     if achouP <= achouV:
#         print("p foi achado antes de v")
#     else:
#         print("v foi achado antes de p")