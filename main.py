elementos = {
    "Te": "TERRA",
    "Fa": "FANTASMA",
    "Ag": "AGUA",
    "El": "ELETRICO",
    "Ps": "PSICO",
    "Fo": "FOGO",
    "Vo": "VOADOR",
    "Gr": "GRAMA",
    "Dr": "DRAGAO"
}

def transicao_valida(atual, proximo):
    if atual == "Ag" and proximo == "El":
        return False
    if atual == "Vo" and proximo != "Dr":
        return False
    if atual == "Fo" and proximo not in ["Dr", "Vo"]:
        return False
    if atual == "Fa" and proximo == "Ps":
        return False
    return True

entrada = input("Digite 2 ou mais elementos separados por espaço: ").split()

if len(entrada) < 2:
    print("Erro: você deve digitar no mínimo 2 elementos.")
else:
    valido = True

    for e in entrada:
        if e not in elementos:
            print(f"Elemento inválido: {e}")
            valido = False
            break

    if valido:
        for i in range(len(entrada) - 1):
            atual = entrada[i]
            proximo = entrada[i + 1]
            if not transicao_valida(atual, proximo):
                print(f"Transição inválida: {atual} -> {proximo}")
                valido = False
                break

    if valido:
        print("Sequência válida de evolução!")

 # Gabriel Gomes Fernandes - 172317728 \ Diogo Rafael Varela Butzke - 172316253 \ João Brasil - 172311360 \ Gabriel Klein - 172312555 \ João Vitor Demenech - 1726111321
