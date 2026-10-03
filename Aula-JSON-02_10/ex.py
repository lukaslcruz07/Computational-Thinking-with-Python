import json
import time

nome = "./Aula-JSON-02_10/incidente.json"
incidentes = []

def exibir_menu():
    opcao = " "
    while opcao != '3':
        print("""
        1 Registrar incidente
        2 Consultar histórico
        3 Sair
        """)

        opcao = input('Digite uma opção: ')

        match opcao:
            case "1":
                registrar_ocorrencia()
            case "2":
                consultar_historico()
            case "3":
                print('Saindo do sistema...')
                time.sleep(2)

def registrar_ocorrencia():
    try:
        with open(nome, 'r', encoding="utf-8") as arq:
            dados = json.load(arq)

        print("\n", dados,"\n")
    except FileNotFoundError:
        incidentes =[]
    
    except json.JSONDecodeError:
        print("JSON inválido. Confira o arquivo.")

    servico = input('Serviços: ')
    descricao = input('Descrição: ')
    status = input('Status: ')
    incidente = {"servicos": servico, "descricao": descricao, "status": status}
    incidentes.append(incidente)

def consultar_historico():
    try:
        with open(nome, 'r', encoding="utf-8") as arq:
            dados = json.load(arq)

        print("n", dados,"\n")
    except FileNotFoundError:
        incidentes = []
    
    except json.JSONDecodeError:
        print("JSON inválido. Confira o arquivo.")

exibir_menu()