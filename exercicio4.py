faturamentoEstado = {
    "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "Outros" : 19849.53
}

faturamentoTotal = sum(faturamentoEstado.values())

percentuais = {
    estados: (valor / faturamentoTotal) * 100
    for estados, valor in faturamentoEstado.items()
}

for estado, percentual in percentuais.items():
    print(f"{estado} : {percentual:.2f}")