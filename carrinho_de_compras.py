# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input("digite um valor").strip())
# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input("digite um produto seguindo do preço").strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco


# TODO: Exiba os itens e o total da compra
for _ in range(n):
    print(f"{carrinho[_][0]}: R${carrinho[_][1]:.2f}")
print(f'Total: R${total:.2f}')