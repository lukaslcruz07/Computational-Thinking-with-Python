# Ex 01
# configuracoes = { 
#     "grade": "ativa linhas de apoio na tela", 
#     "hdr": "reequilibra áreas claras e escuras", 
#     "timer": "atrasa o disparo da foto" 
# }

# def consultar_recurso(dados, recurso):
#     if recurso in dados:
#         return dados[recurso]
#     else:
#         return 'Recurso não encontrado!'

# print(consultar_recurso(configuracoes, "grad"))    

# EX 02

# def gerar_mensagem(estudante=True):
#     if estudante == False:
#         return "Modo avançado ativado"
#     else:
#         return "Modo simples ativado"

# print(gerar_mensagem())
# print(gerar_mensagem(estudante=False))

#Ex 04

# classificacao = ''
# mensagem = ''

# def classificar_avaliacao(nota):
#     if nota >= 9:
#         return "excelente" , "usar como destaque"
#     elif nota >= 7:
#         return "boa", "manter no produto" 
#     else:
#         return "revisar" , "precisa melhorar"

# classificacao, mensagem = classificar_avaliacao(5)

# print(classificacao, mensagem)

# Ex 05

# def configurar_captura(modo, qualidade, flash=True):    
#     return modo, qualidade, flash

# print("CONFIGURAÇÃO DA CÂMERA")

# print(configurar_captura('hrd', 'media', flash=False))

# Ex 06

# def avaliar_configuracao(nome, qualidade, facilidade, utilidade):
#     media = (qualidade + facilidade + utilidade) / 3
#     if media >= 8:
#         situacao = "aprovada"
#     else:
#         situacao =  "revisar"
#     return nome, media, situacao

# nome, media, situacao = avaliar_configuracao('hrd', 6, 8, 10)
# nome, media, situacao = avaliar_configuracao('timer', 4, 6, 10)

# print(nome, int(media), situacao)

# EX 08


recursos = {
    "noturno": "melhora fotos com pouca luz",
    "retrato": "destaca pessoas",
    "documento": "melhora leitura de textos"

}

nota=[]
 
def configuracao(dados, recurso):
    if recurso in dados:
      return dados[recurso]
    return "recurso não cadastrado"
 
def avaliar_recurso(dados,nome):
    if nome in dados:
        clareza = int(input("Digite uma nota de 0 a 10 para a clareza do recurso:"))
        nota.append(clareza)
        utilidade = int(input("Digite uma nota de 0 a 10 para a utilidade do recurso:"))
        nota.append(utilidade)
        facilidade = int(input("Digite uma nota de 0 a 10 para a facilidade do recurso:"))
        nota.append(facilidade)
        media = sum(nota)/ len(nota)
        devolucao = print(f"Esse foi o recurso escolido para fazer a avaliaçao: {nome}, e ele tem essa media: {round(media, 1)}")
        return devolucao
    return "recurso não cadastrado"
 
opc = input("""
    digite a sua opção
    1. Consultar recurso2
    2. Avaliar utilidade
    0. Sair
""")

match opc:
    case "1":
        configuracao(recursos, input("Digite o nome do recurso: "))
        
    case "2":
       avaliar_recurso(recursos, input("Digite o nome do recurso: "))

    case "0":

        print("Saindo do programa.")
    case _:
        print("Opção inválida........")

 


 