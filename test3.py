import json

def calcular_faturamento(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    
    faturamentos = [item['valor'] for item in data['faturamento'] if item['valor'] > 0]

    if not faturamentos:
        return "Não há dias com faturamento."

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_faturamento)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

resultado = calcular_faturamento('faturamento.json')
print(f"Menor faturamento: {resultado['menor_faturamento']}")
print(f"Maior faturamento: {resultado['maior_faturamento']}")
print(f"Dias acima da média: {resultado['dias_acima_da_media']}")


