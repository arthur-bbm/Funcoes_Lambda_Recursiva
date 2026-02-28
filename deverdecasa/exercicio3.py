produtos = [("Teclado", 150), ("Mouse", 80), ("Monitor", 900)]

ordenar = sorted(produtos, key=lambda x: x[1])

print(ordenar)