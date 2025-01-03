4.1
# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# if a > b:
#     print("O primeiro valor é maior.")
# if a < b:
#     print("O segundo valor é maior.")
# # Se os valores forem iguais, nada será impresso.
# # Isso acontece porque a > b e b > a são falsas quando a = b.

4.2
# velocidade = float(input("Digite a velocidade do seu carro: "))
# if velocidade > 80:
#     multa = (velocidade - 80) * 5
#     print(f"Você foi multado em R$ {multa:1.2f}!")
# if velocidade <= 80:
#     print("Sua velocidade está ok, boa viagem!")

4.3
# a = int(input("Digite o primeiro valor:"))
# b = int(input("Digite o segundo valor:"))
# c = int(input("Digite o terceiro valor:"))
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c >= b:
#     maior = c
# menor = a
# if b < c and b < a:
#     menor = b
# if c <= b and c < a:
#     menor = c
# print(f"O maior número digitado foi {maior}")
# print(f"O menor número digitado foi {menor}")

4.4
# salário = float(input("Digite seu salário: "))
# pc_aumento = 0.15
# if salário > 1250:
#     pc_aumento = 0.10
# aumento = salário * pc_aumento
# print(f"Seu aumento será de: R$ {aumento:1.2f}")

4.5
# Sim, os resultados são os mesmos.

4.6
# distância = float(input("Digite a distância a percorrer: "))
# if distância <= 200:
#     passagem = 0.5 * distância
# else:
#     passagem = 0.45 * distância
# print(f"Preço da passagem: R$ {passagem:1.2f}")

4.7
# O exercício consiste em rastrear o programa da listagem 4.7.
# O resultado deve ser o mesmo do apresentado na tabela 4.2.
# A técnica de rastreamento é apresentada na página 62,
# seção 3.6 Rastreamento.

4.8
# a = float(input("Primeiro número:"))
# b = float(input("Segundo número:"))
# operação = input("Digite a operação a realizar (+,-,* ou /):")
# if operação == "+":
#     resultado = a + b
# elif operação == "-":
#     resultado = a - b
# elif operação == "*":
#     resultado = a * b
# elif operação == "/":
#     resultado = a / b
# else:
#     print("Operação inválida!")
#     resultado = 0
# print(f"Resultado: {resultado}")

4.9
# valor = float(input("Digite o valor da casa: "))
# salário = float(input("Digite o salário: "))
# anos = int(input("Quantos anos para pagar: "))
# meses = anos * 12
# prestacao = valor / meses
# if prestacao > salário * 0.3:
#     print("Infelizmente você não pode obter o empréstimo")
# else:
#     print(f"Valor da prestação: R$ {prestacao:1.2f}. Empréstimo OK")

4.10
# consumo = int(input("Consumo em kWh: "))
# tipo = input("Tipo da instalação (R, C ou I): ")
# if tipo == "R" or "r":
#     if consumo <= 500:
#         preço = 0.40
#     else:
#         preço = 0.65
# elif tipo == "I" or "i":
#     if consumo <= 5000:
#         preço = 0.55
#     else:
#         preço = 0.60
# elif tipo == "C" or "c":
#     if consumo <= 1000:
#         preço = 0.55
#     else:
#         preço = 0.60
# else:
#     preço = 0
#     print("Erro ! Tipo de instalação desconhecido!")
# custo = consumo * preço
# print(f"Valor a pagar: R${custo:1.2f}")

