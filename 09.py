#9.Escreva um programa que verifique se uma frase inserida pelo usuário é um palíndromo (frase que é lida da mesma forma de trás para frente).
frase = input("Digite uma frase: ")

frase_invertida = frase[::-1]

if frase == frase_invertida:
    print("A frase é um palindromo.")
else:
    print("A frase não é um palindromo.")
