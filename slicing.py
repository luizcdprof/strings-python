# texto = "BR-SP-2024-0042"
# print(texto[-4:])

valor = 1250.5
print(f"R$ {valor:.2f}".replace(".", ","))
print(f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))



valor = 0.857
print(f"{valor:.2%}".replace(".", ","))