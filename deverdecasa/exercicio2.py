nomes = ["Ana", "Beatriz", "Caio", "Daniela", "Edu"]
nome3 = lambda nome: len(nome) <= 3

print(list(filter(nome3, nomes)))