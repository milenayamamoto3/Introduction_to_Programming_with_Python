5.21
# while True:
#     valor = int(input("Digite o valor a pagar:"))
#     if valor == 0:
#         break
#     cédulas = 0
#     atual = 50
#     apagar = valor
#     while True:
#         if atual <= apagar:
#             apagar -= atual
#             cédulas += 1
#         else:
#             print(f"{cédulas} cédula(s) de R${atual}")
#             if apagar == 0:
#                 break
#             if atual == 50:
#                 atual = 20
#             elif atual == 20:
#                 atual = 10
#             elif atual == 10:
#                 atual = 5
#             elif atual == 5:
#                 atual = 1
#             cédulas = 0

5.22
# while True:
#     print("""

# Menu
# ----
# 1 - Adição
# 2 - Subtração
# 3 - Divisão
# 4 - Multiplicação
# 5 - Sair

# """)
#     opção = int(input("Escolha uma opção:"))
#     if opção == 5:
#         break
#     elif opção >= 1 and opção < 5:
#         n = int(input("Tabuada de:"))
#         x = 1
#         while x <= 10:
#             if opção == 1:
#                 print(f"{n} + {x} = {n + x}")
#             elif opção == 2:
#                 print(f"{n} - {x} = {n - x}")
#             elif opção == 3:
#                 print(f"{n} / {x} = {n / x:1.2f}")
#             elif opção == 4:
#                 print(f"{n} x {x} = {n * x}")
#             x = x + 1
#     else:
#         print("Opção inválida!")

5.23
# while True:
#     n = int(input("Digite um número para saber se é primo ou '0' para sair, lembrando que 0 não é primo:"))

#     if n == 0:
#         break
#     elif n < 0:
#         print("Número inválido. Digite apenas valores positivos, nº negativo não é primo.")
#     elif n == 1:
#         print(f"{n} e 0 são casos especiais, eles não são primo.")
#     else:
#         if n == 2:
#             print("2 é o único número primo que é par.")
#         elif n % 2 == 0:
#             print(f"{n} não é primo, pois 2 é o único número par primo.")
#         else:
#             x = 3
#             while x < n:
#                 if n % x == 0:
#                     break
#                 x = x + 2
#             if x == n:
#                 print(f"{n} é primo")
#             else:
#                 print(f"{n} esse nº ímpar não é primo, pois é divisível por {x}")
# print("Programa encerrado!")

5.24
# while True:
#     print("Lembrete: Todos os números negativos, 0 e 1 não são primos!")
#     n = int(input("Digite um nº a partir de 2 para saber os primeiros números primos desse nº ou '0' para sair:"))

#     if n == 0:
#         break
#     elif n >= 2:
#         print("Os números primos até", n, "são:")
#         print("2")  # O primeiro número primo é 2, já garantido.
#         num = 3    # Começamos a verificar números primos a partir de 3.

#         while num <= n:
#             # Verificar se 'num' é primo
#             eh_primo = True  # Assumimos que 'num' é primo
#             divisor = 2      # Começamos a verificar divisores a partir de 2

#             while divisor * divisor <= num:
#                 if num % divisor == 0:
#                     eh_primo = False  # Não é primo
#                     break
#                 divisor += 1  # Próximo divisor

#             if eh_primo:
#                 print(num)  # 'num' é primo, então imprimimos

#             num += 1  # Próximo número a verificar

# print("Programa encerrado!")

5.25
# Programa para calcular a raiz quadrada de um número usando o método de Newton

# Entrada do usuário
# n = float(input("Digite o número para calcular a raiz quadrada: "))

# # Inicialização da base b
# b = 2.0

# # Definir a precisão desejada
# precisao = 0.0001

# while True:
#     # Calcular o próximo palpite (p)
#     p = (b + (n / b)) / 2
    
#     # Calcular o quadrado de p
#     quadrado_de_p = p ** 2
    
#     # Verificar se a diferença absoluta é menor que a precisão
#     if abs(n - quadrado_de_p) < precisao:
#         break
    
#     # Atualizar b para o próximo cálculo
#     b = p

# # Exibir o resultado
# print(f"A raiz quadrada aproximada de {n} é {p}")

5.26
# # Entrada dos números
# dividendo = int(input("Digite o dividendo (número a ser dividido): "))
# divisor = int(input("Digite o divisor (número que divide): "))

# # Verificar se o divisor é zero
# if divisor == 0:
#     print("Erro: divisão por zero não é permitida.")
# else:
#     # Inicializar o resto como o próprio dividendo
#     resto = dividendo

#     # Subtrair o divisor repetidamente até que o resto seja menor que o divisor
#     while resto >= divisor:
#         resto -= divisor  # Subtração

#     # Exibir o resultado
#     print(f"O resto da divisão de {dividendo} por {divisor} é {resto}.")

5.27
# Entrada do número que é uma str
numero = input("Digite um número para verificar se é palíndromo: ")

# Verificar se o número é igual à sua inversão
if numero == numero[::-1]:
    print(f"O número {numero} é um palíndromo.")
else:
    print(f"O número {numero} não é um palíndromo.")



