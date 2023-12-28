#6.Crie um programa que conte quantas vogais existem em uma frase inserida pelo usuário.
frase = input("digite uma frase: ")
vogais = ["a", "e", "i", "o", "u"]

qtd_vogais = 0
for letra in frase:
    if letra in vogais:
        qtd_vogais += 1

print("\nA frase tem {} vogais.".format(qtd_vogais))