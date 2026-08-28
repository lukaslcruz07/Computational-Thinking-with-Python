# def criar_lista_recursos(*recursos):
#     lista = []
#     for recurso in recursos:
#         lista.append(recurso)

#     return lista

# print(criar_lista_recursos('hdr', 'grade'))
# print(criar_lista_recursos('timer', 'foco', 'zoom'))

# def registrar_configuracoes(**dados):
#     print(dados)
#     return 'Confiurações registradas'

# registrar_configuracoes(modo='noturno', flase=False)
# registrar_configuracoes(modo='retratos', foco='rosto', timer=3)

dobro = lambda n: n * 2
primeira_letra = lambda texto: texto[0]
nivel = lambda nota: 'Alto' if nota >= 8 else 'baixo'

print(dobro(20))
print(primeira_letra('Altura'))
print(nivel(4))
print(nivel(8))