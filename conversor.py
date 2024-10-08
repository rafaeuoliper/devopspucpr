from datetime import datetime

data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Data e hora atual: {data_atual}")

def conversao_valor(valor_pacote_dolar, cotacao_dolar):
    return valor_pacote_dolar * cotacao_dolar

def calcular_comissao(valor_pacote_real, percentual_comissao):
    return valor_pacote_real * (percentual_comissao / 100)

# Perguntar ao Usuario o Valor do Pacote, a Cotacao do Dolar e o Percentual da Comissao 
valor_pacote_dolar = float(input("Informe o valor do pacote de viagem em dólares: "))
cotacao_dolar = float(input("Informe a cotação atual do dólar: "))
percentual_comissao = float(input("Informe o percentual de comissão do vendedor: "))

# Validação para garantir que os valores inseridos sejam maiores que zero
if valor_pacote_dolar <= 0 or cotacao_dolar <= 0 or percentual_comissao <= 0:
    print("Erro: Todos os valores devem ser maiores que zero.")
    exit(1)

# Calculos
valor_pacote_real = conversao_valor(valor_pacote_dolar, cotacao_dolar)
comissao_vendedor = calcular_comissao(valor_pacote_real, percentual_comissao)

# Respostas
print(f"\nResumo:")
print(f"Valor do pacote em dólares: $ {valor_pacote_dolar:.2f}")
print(f"Cotação do dólar: R$ {cotacao_dolar:.2f}")
print(f"Valor do pacote em reais: R$ {valor_pacote_real:.2f}")
print(f"Percentual de comissão do vendedor: {percentual_comissao}%")
print(f"Comissão do vendedor: R$ {comissao_vendedor:.2f}")
