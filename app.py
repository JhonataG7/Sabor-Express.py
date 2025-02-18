import os

restaurantes = [{'nome':'Brasão' , 'categoria':'Churrascaria', 'ativo':False}, 
                {'nome':'Pizzaria', 'categoria':'Massas', 'ativo':True}]

def exibir_nome_do_programa():
    '''Nome do programa'''
    print('Sabor Express\n')

def exibir_opcoes():
    '''Mostrar opções'''
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurante')
    print('3 - Ativar Restaurante')
    print('4 - Sair\n')

def finalizar_app():
    '''Função para finalizar o app'''
    exibir_subtitulo('Finalizar app!')

def voltar_ao_menu_principal():
    '''Função responsável para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Função responsável por informar uma  opção invalida'''
    print('Opção ivalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Função responsável pelo subtitulo'''
    os.system('cls')
    print(texto)
    print()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar novos restaurantes'''
    exibir_subtitulo('Cadastrar novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    restaurantes.append(nome_do_restaurante)
    dados_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    '''Função responsável por listar o restaurantes'''
    exibir_subtitulo('Lista de restaurantes')

    print(f'{"Nome do ressturante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo_restaurante}')
        
    voltar_ao_menu_principal()

def alternar_restaurante():
    '''Função responsável ativar/desativar o restaurante'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso :)' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado :(')
    voltar_ao_menu_principal()
    
def escolher_opcoes():
    '''Case responsavel por escolher as opções'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:  
            alternar_restaurante()
        elif opcao_escolhida == 4:    
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Menu'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__== '__main__':
    main()