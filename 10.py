#10.Crie um programa que calcule o Índice de Massa Corporal (IMC) a partir do peso e altura fornecidos pelo usuário.
peso = float(input("digite o seu pesso: "))
altura = float(input("digite sua altura: "))

imc = peso / (altura * altura)

print(f"\no seu indice de massa corporal(IMC) e: {imc:.1f}")