#2.Crie um programa que verifique se um número inserido pelo usuário é par ou ímpar.

num = int(input("digite um numero: "))

if num % 2 == 0:
    print(f"o numero {num} e par!")
else:
    print(f"o numero {num} e impar!")