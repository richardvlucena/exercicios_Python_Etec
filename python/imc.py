'''Desenvolver um algoritmo que receba nome, altura e peso de uma pessoa e calcule o IMC mediante este valor, também será apresentado em tela, se a pessoa está abaixo do peso, tem o peso normal, está acima do peso ou obesa. (Saída de dados deve conter nome, IMC e o status citado).
Formula do IMC: peso/(altura * altura)'''

nome = input("nome: \n")
altura = float(input("altura: \n"))
peso = float(input("peso: \n"))
imc = peso/(altura * altura)

if imc <17: #16
    print("Muito abaixo do peso")

elif imc > 16 and imc <= 18.49: #17 e 18.49:
    print("Abaixo do peso")

elif imc > 18.49 and imc <= 24.99: #18,5 e 24,99
    print("Peso normal")

elif imc > 24.99 and imc <= 29.99: #Entre 25 e 29,99
    print("Acima do peso")

elif imc > 29.99 and imc <= 34.99: #Entre 30 e 34,99
    print("Obesidade I")

elif imc > 34.99 and imc <= 39.99: #Entre 35 e 39,99
    print("Obesidade II (severa)")

else: #Acima de 40
    print("Obesidade III (mórbida)")

