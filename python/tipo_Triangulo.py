'''Crie um algoritmo que:Receba 3 medidas para formar uma forma geométrica e dependendo da medida
diga se ele é um:
triângulo EQUILÁTERO (3 lados iguais)
ISÓCELES/RETÂNGULO (2 lados iguais)
ESCALENO (nenhum lado igual)'''

print("Digite 3 medidas para formar uma forma geométrica")
medida1 = (input("1° medida:  \n"))
medida2 = (input("2° medida:  \n"))
medida3 = (input("3° medida:  \n"))

if medida1 == medida2 and medida1 != medida3:
    print("Triángulo RETÂNGULO (2 lados iguais e 1 diferente)")

elif medida1 == medida3 and medida1 != medida2:
    print("Triángulo RETÂNGULO (2 lados iguais e 1 diferente)")

elif medida2 == medida1 and medida2 != medida3:
    print("Triángulo RETÂNGULO (2 lados iguais e 1 diferente)")

elif medida2 == medida3 and medida2 != medida1:
    print("Triángulo RETÂNGULO (2 lados iguais e 1 diferente)")

elif medida1 == medida2 and medida1 == medida3:
    print("triângulo EQUILÁTERO (3 lados iguais)")

else:
    print("Triángulo ESCALENO (nenhum lado igual)")







