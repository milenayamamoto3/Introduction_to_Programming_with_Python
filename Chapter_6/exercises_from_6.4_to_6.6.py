6.4
# Se não verificarmos que a lista está vazia antes de charmos pop(),
# o programa pára com uma mensagem de erro, informando que tentamos
# retirar um elemento de uma lista vazia.
# A verificação é necessária para controlar este erro e assegurar
# o bom funcionamento do programa.
6.5
# último = 10
# fila = list(range(1, último + 1))
# while True:
#     print(f"\nExistem {len(fila)} clientes na fila")
#     print("Fila atual:", fila)
#     print("Digite F para adicionar um cliente ao fim da fila,")
#     print("ou A para realizar o atendimento. S para sair.")
#     operação = input("Operação (F, A ou S):")
#     x = 0
#     sair = False
#     while x < len(operação):
#         if operação[x] in "Aa":
#             if len(fila) > 0:
#                 atendido = fila.pop(0)
#                 print(f"Cliente {atendido} atendido")
#             else:
#                 print("Fila vazia! Ninguém para atender.")
#         elif operação[x] in "Ff":
#             último += 1  # Incrementa o ticket do novo cliente
#             fila.append(último)
#             print(f"Cliente {último} adicionado")
#         elif operação[x] in "Ss":
#             sair = True
#             break
#         else:
#             print(
#                 f"Operação inválida: {operação[x]} na posição {x} da operação! Digite apenas F, A ou S!"
#             )
#             # lembrando que as mensagens são para o programador e não para o usuário.
#         x = x + 1
#     if sair:
#         break

6.6
# último = 0
# fila1 = []
# fila2 = []
# while True:
#     print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} na fila 2.")
#     print("Fila 1 atual:", fila1)
#     print("Fila 2 autal:", fila2)
#     print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
#     print("ou A para realizar o atendimento a fila 1 (ou B para fila 2")
#     print("S para sair.")
#     operação = input("Operação (F, G, A, B ou S):")
#     x = 0
#     sair = False
#     while x < len(operação):
#         # Aqui vamos usar fila como referência a fila 1
#         # ou a fila 2, dependendo da operação.
#         if operação[x] == "A" or operação[x] == "F":
#             fila = fila1
#         else:
#             fila = fila2
#         if operação[x] == "A" or operação[x] == "B":
#             if len(fila) > 0:
#                 atendido = fila.pop(0)
#                 print(f"Cliente {atendido} atendido")
#             else:
#                 print("Fila vazia! Ninguém para atender.")
#         elif operação[x] == "F" or operação[x] == "G":
#             último += 1  # Incrementa o ticket do novo cliente
#             fila.append(último)
#             print(f"Cliente {último} adicionado")
#         elif operação[x] == "S":
#             sair = True
#             break
#         else:
#             print(
#                 f"Operação inválida: {operação[x]} na posição {x} da operação! Digite apenas F, A ou S!"
#             )
#         x = x + 1
#     if sair:
#         break