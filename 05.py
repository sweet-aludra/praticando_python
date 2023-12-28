#5.Escreva um programa que solicite um número inteiro positivo ao usuário e calcule o fatorial desse número.
print("Calculando o Fatorial!")
num = int(input("\ndigite um numero positivo: "))

def fatorial(num):
    if num == 0:
        return 1
    elif num < 0:
        print("digite um numero positivo!")
    else:
        return num * fatorial(num - 1)
    
print(f"{num}! = ", fatorial(num))
