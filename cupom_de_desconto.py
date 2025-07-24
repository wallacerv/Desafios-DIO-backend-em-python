# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom == "DESCONTO10":
  novopreco = preco - preco*descontos["DESCONTO10"]
  print(f"{novopreco:.2f}")
elif cupom == "DESCONTO20":
  novopreco = preco - preco*descontos["DESCONTO20"]
  print(f"{novopreco:.2f}")
elif cupom == "SEM_DESCONTO":
  novopreco = preco - preco*descontos["SEM_DESCONTO"]
  print(f"{novopreco:.2f}")