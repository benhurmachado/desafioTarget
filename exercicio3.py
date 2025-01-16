import json

with open("dados.json") as dadosjson:
    dados = json.load(dadosjson)

faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]

menorValor = min(faturamentos)
maiorValor = max(faturamentos)

mediaMensal = sum(faturamentos) / len(faturamentos)

numeroDias = len([valor for valor in faturamentos if valor > mediaMensal])

print(f"O menor valor de faturamento ocorrido em um dia do mês: {menorValor}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: {maiorValor}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {numeroDias}")