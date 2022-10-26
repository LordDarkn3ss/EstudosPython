import datetime  # Biblioteca de tempo


def captar_data():  # Função para retornar como String a data atual
    data = datetime.datetime.now()
    return data.strftime("%d/%m/%Y %H:%M")


def atualizar_lib(conta):
    num = []
    saldo = []
    nome = []
    tipo = []
    status = []
    for x in range(len(conta)):
        num.append(conta[x].num)
        saldo.append(conta[x].saldo)
        nome.append(conta[x].nome)
        tipo.append(conta[x].tipo)
        status.append(conta[x].status)

    return {
        "Nº": num,
        "Nome": nome,
        "Tipo": tipo,
        "Saldo": saldo,
        "Ativa": status
    }
