3.7
# x = int(input("Digite um número inteiro: "))
# y = int(input("Digite outro número inteiro: "))
# print(x+y)

3.8
# metros = float(input('Digite a medida em metros: '))
# milimetros = metros*1000
# print("%4.2f metros equivalem a %4.2f milímetros." % (metros, milimetros))

3.9
# dias = int(input("Quantos dias: "))
# horas = int(input("Quantas horas: "))
# minutos = int(input("Quantos minutos: "))
# segundos = int(input("Quantos segundos: "))
# segundos_total = segundos + (minutos*60) + (horas*60*60) + (dias*24*60*60)
# print(f'Seus segundos totais são {segundos_total}.')

3.10
# salario = float(input("Qual seu salário: "))
# porcentagem_aumento = float(input("Porcentagem de aumento: "))
# aumento = salario*(porcentagem_aumento/100)
# salario_com_aumento = salario + aumento
# print(f"Seu aumento foi de R${aumento:4.2f} e seu salário ficou R${salario_com_aumento:4.2f}")

3.11
# preco = float(input("Qual o valor do produto: "))
# porcentual_desconto = float(input('Qual a porcentagem do desconto: '))
# desconto =  preco*porcentual_desconto/100
# preco_a_pagar = preco - desconto
# print(f"Seu desconto é de R${desconto:4.2f} e o preço a ser pago é R${preco_a_pagar:4.2f}.")

3.12
# distancia = float(input("Distância em km: "))
# velocidade = float(input("Velocidade em km/h: "))
# tempo = distancia/velocidade
# tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
# horas = int(tempo_s / 3600)  # parte inteira da divisão para hrs
# resto = int(tempo_s % 3600)  # o resto das hrs em seg; todo resto é int
# minutos = int(resto / 60) # parte inteira da divisão para minutos
# segundos = int(resto % 60) # pegando o resto dos min em seg; todo resto é int
# # As horas pode ultrapassar 2 dígitos mas não os min e segs
# # se tiver só 1 dígito ou nada, o 0 será preenchido nos lugares vazios
# print(f"Seu tempo para chegar é de {horas:02}:{minutos:02}:{segundos:02}")


