def inverter_string(s):
    string_invertida = ''
    for i in s:
        string_invertida = i + string_invertida
    return string_invertida

entrada = input("Informe uma string para inverter: ")

resultado = inverter_string(entrada)

print(f"String invertida: {resultado}")
