from random import randint, choice
army = []


def add_soldier():
    name = input("qual o nome do soldado ? ")
    army.append(name)


while True:
    add = input("tem soldado(S/N) ? ").upper()
    if add == "S":
        add_soldier()
        print("Soldado adicionado")
    elif add == "N":
        break
    else:
        print("Opção invalida. Digite 'S' ou 'N'. ")

print(army)

chosen_soldier = choice(army)
start_index = army.index(chosen_soldier)

number = randint(1, len(army))

print(f"Soldado sorteado para começar foi {chosen_soldier}")
print(f"Numero sorteado para a contagem: {number}")


while True:
    start_index = (start_index + number - 1) % len(army)
    print(f"o soldado {army[start_index]} foi removido")
    army.pop(start_index)

    if len(army) == 1:
        break

print(f"o soldado {army[0]} foi buscar ajuda")
