5.6
# n = int(input("Tabuada de:"))
# x = 1
# while x <= 10:
#     print(f"{n} x {x} = {n * x}")
#     x = x + 1

5.7
# n = int(input("Tabuada de: "))
# inicio = int(input("De: "))
# fim = int(input("Até: "))
# x = inicio
# while x <= fim:
#     print(f"{n} x {x} = {n * x}")
#     x = x + 1

5.8
# p = int(input("Primeiro número: "))
# s = int(input("Segundo número: "))
# x = 1 # contador de vezes
# r = 0 # acumulador da soma
# while x <= s:
#     r = r + p
#     x = x + 1
# print(f"{p} x {s} = {r}")

5.9
# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))
# quociente = 0
# x = dividendo
# while x >= divisor:
#     x = x - divisor
#     quociente = quociente + 1
# resto = x
# print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")

5.10
# pontos = 0
# questão = 1
# while questão <= 3:
#     resposta = input(f"Resposta da questão {questão}: ")
#     if questão == 1 and (resposta == "b" or resposta == "B"):
#         pontos = pontos + 1
#     if questão == 2 and (resposta == "a" or resposta == "A"):
#         pontos = pontos + 1
#     if questão == 3 and (resposta == "d" or resposta == "D"):
#         pontos = pontos + 1
#     questão += 1
# print(f"O aluno fez {pontos} ponto(s)")