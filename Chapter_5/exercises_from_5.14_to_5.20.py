5.14
# soma = 0
# quantidade = 0
# while True:
#     n = int(input("Digite um número inteiroou 0 para sair: "))
#     if n == 0:
#         break
#     soma = soma + n
#     quantidade = quantidade + 1
# print("Quantidade de números digitados:", quantidade)
# print("Soma:", soma)
# print(f"Média: {soma/quantidade}")

5.15
# apagar = 0
# while True:
#     código = int(input("Código da mercadoria (0 para sair): "))
#     preço = 0
#     if código == 0:
#         break
#     elif código == 1:
#         preço = 0.50
#     elif código == 2:
#         preço = 1.00
#     elif código == 3:
#         preço = 4.00
#     elif código == 5:
#         preço = 7.00
#     elif código == 9:
#         preço = 8.00
#     else:
#         print("Código inválido!")
#     if preço != 0:
#         quantidade = int(input("Quantidade: "))
#         apagar = apagar + (preço * quantidade)
# print(f"Total a pagar R${apagar:1.2f}")

5.16
# Após substituir os valores fornecidos pelo exercício,
# o programa deve funcionar normalmente 

5.17
# O programa pára logo após imprimir a quantidade de cédulas, que será 0 de R$50,00

5.18
# valor = int(input("Digite o valor a pagar:"))
# cédulas = 0
# atual = 100
# apagar = valor
# while True:
#     if atual <= apagar:
#         apagar -= atual
#         cédulas += 1
#     else:
#         print(f"{cédulas} cédula(s) de R${atual}")
#         if apagar == 0:
#             break
#         elif atual == 100:
#             atual = 50
#         elif atual == 50:
#             atual = 20
#         elif atual == 20:
#             atual = 10
#         elif atual == 10:
#             atual = 5
#         elif atual == 5:
#             atual = 1
#         cédulas = 0

5.19
# Atenção: alguns valores não serão calculados corretamente
# devido a problemas com arredondamento e da representação de 0.01
# em ponto flutuante. Uma alternativa é multiplicar todos os valores
# por 100 e realizar todos os cálculos com números inteiros.

# valor = float(input("Digite o valor a pagar:"))
# cédulas = 0
# atual = 100
# apagar = valor
# while True:
#     if atual <= apagar:
#         apagar -= atual
#         cédulas += 1
#     else:
#         if atual >= 1:
#             print(f"{cédulas} cédula(s) de R${atual}")
#         else:
#             print(f"{cédulas} moeda(s) de R${atual:1.2f}")
#         if apagar < 0.01:
#             break
#         elif atual == 100:
#             atual = 50
#         elif atual == 50:
#             atual = 20
#         elif atual == 20:
#             atual = 10
#         elif atual == 10:
#             atual = 5
#         elif atual == 5:
#             atual = 1
#         elif atual == 1:
#             atual = 0.50
#         elif atual == 0.50:
#             atual = 0.10
#         elif atual == 0.10:
#             atual = 0.05
#         elif atual == 0.05:
#             atual = 0.02
#         elif atual == 0.02:
#             atual = 0.01
#         cédulas = 0

5.20
# Como preparamos o programa para finalizar com valores menores que 0.01,
# este pára de executar após imprimir 0 cédula(s) de R$100.

