#4.Faça um programa que converta uma temperatura de Celsius para Fahrenheit ou vice-versa, dependendo da escolha do usuário.

print("Escolha a operação:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("\nDigite 1 ou 2 para escolher: "))

if opcao == 1:
   tCelsius = int(input("digite a temperatura: "))
   tFahrenheit = (tCelsius * 9/5) + 32

   print(f"temperatura em Fahrenheit: {tFahrenheit:.1f} ºF")

elif opcao == 2:
   tFahrenheit = int(input("digite a temperatura: "))
   tCelsius = (tFahrenheit - 32) * 5/9

   print(f"temperatura em Celsius: {tCelsius:.1f} ºC")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2 para selecionar a operação desejada.")
