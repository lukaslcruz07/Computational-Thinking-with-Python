import time

opcao = ''
while opcao != '3':
    print('=== INCIDENTES ===1')
    print('''
    1 - Salvar
    2 - Consultar
    3 - Sair
    ''')
    opcao = input('Opção: ')

    match opcao:
        case '1':
            with open('./Aula-arquivos-25_10/incidentes.txt', 'a') as arquivo:
                novoCaso = input('Registre seu caso: ')
                arquivo.write(f'CASO: {novoCaso}\n')
        case '2':
            with open('./Aula-arquivos-25_10/incidentes.txt', 'r') as arquivo:
                print(f'{arquivo.read()}')
                time.sleep(2)

        case '3':
            print('Saindo do sistema...')

        case _:
            print('A opção escolhida não existe! Espere 3 segundos.')
            time.sleep(3)