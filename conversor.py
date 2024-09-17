def conversao_valor(valor_pacote_dolar, cotacao_dolar):
    return valor_pacote_dolar * cotacao_dolar

def calcular_comissao(valor_pacote_real, percentual_comissao):
    return valor_pacote_real * (percentual_comissao / 100)

# Perguntar ao Usuario o Valor do Pacote, a Cotacao do Dolar e o Percentual da Comissao 
valor_pacote_dolar = float(input("Informe o valor do pacote de viagem em dólares: "))
cotacao_dolar = float(input("Informe a cotação atual do dólar: "))
percentual_comissao = float(input("Informe o percentual de comissão do vendedor: "))

# Calculos
valor_pacote_real = conversao_valor(valor_pacote_dolar, cotacao_dolar)
comissao_vendedor = calcular_comissao(valor_pacote_real, percentual_comissao)

# Respostas
print(f"Valor do pacote em reais: R$ {valor_pacote_real:.2f}")
print(f"Comissão do vendedor: R$ {comissao_vendedor:.2f}")
