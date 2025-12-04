ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(f"Digite F para adicionar um cliente ao final da fila,")
    print(f"ou A para realizar o atendimento. S para sair.")
    operacao = input("Operacao (F, A ou S):")
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operacao inválida! Digite apendas F, A ou S!")
