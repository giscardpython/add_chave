# ADICIONANDO NOVA CHAVE
pessoa = {
'Nome':'Giscard Stephanou',
'Idade':49,
'Profissao':'programador',
'Empresa':'SENAI'
}

# adicionando uma nova chave ao dicionário
pessoa['cidade'] = input('Cidade onde moras: ')

nova_chave = input('Digite a nova chave: ')
novo_valor = input('Digite um valor para a nova chave: ')
                   
pessoa[nova_chave] = novo_valor

# exibindo os dados do dicionário
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
