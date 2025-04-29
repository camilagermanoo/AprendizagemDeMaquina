# AULA - 29/04 - EXERCÍCIO DE CONVERSÃO DE TEMPERATURA

#### PARADIGMA IMPERATIVO

# A variável "f" representa a escala em "Fahrenheit"
# A variável "c" representa a escala em "Celsius"
# A variável "k" representa a escala em "Kelvin"

while True:
    escala = input("Digite a escala de entrada (C/F/K): ").upper()
    valor = float(input("Digite a temperatura: "))

    if escala == "C":
        f = valor * 1.8 + 32
        k = valor + 273.15
        print(f"{valor}°C = {f:.2f}°F | {valor}°C = {k:.2f}°K")
    elif escala == "F":
        c = (valor - 32) / 1.8
        k = c + 273.15
        print (f"{valor}°F = {c:.2f}°C | {valor}°F = {k:.2f}°K")
    elif escala == "K":
        c = valor - 273.15
        f = c * 1.8 + 32
        print (f"{valor}°K = {c:.2f}°C | {valor}°K = {f:.2f}°F")
    else:
        print("Escala inválida")
    
    sair = input("Deseja sair do aplicativo? S/N: ").upper()
    if sair == "S":
            break
    