Preco = float(input("Preço unitário:"))
Quant = int(input("Quantidade:"))
Frete = float(input("Frete:"))

print(f"Subtotal: {Preco * Quant}")
print(f"Total: {(Preco * Quant) + Frete}")