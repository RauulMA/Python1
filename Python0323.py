def calcular_acrescentacao_min(atual, acrescentar):
    Min_Final = atual + acrescentar%60
    Hora_Final = Min_Final // 60

    Texto_Final = Formatar_horario(Hora_Final, Min_Final)

    return Texto_Final

def Formatar_horario(hora, minuto):
    if hora >= 1:
        Texto = print(f"{hora}h{minuto}min")
    else:
        Texto = print(f"{minuto}min")
    return Texto

def pedir_dados(mensagem):
    while True:
        valor = int(mensagem)
        try:
            if valor <= 0:
                minuto_atual = float(input("Digite o minuto de agora: "))
                minutos_acrescentados = float(input("Digite a quantidade de minutos a acrescentar: "))
            continue
        except AttributeError:
            print("Digite um valor correto.")

def main():
    min_atual = pedir_dados(input("Digite a quantidade de minutos a acrescentar: "))
    min_acresc = pedir_dados(input("Digite a quantidade de minutos a acrescentar: "))

    Min_final = calcular_acrescentacao_min(min_atual, min_acresc)

    calcular_acrescentacao_min()

if __name__ == "__main__":
    main()