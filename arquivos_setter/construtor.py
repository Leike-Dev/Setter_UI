# Modúlos importados ou arquivos python externos:

from config import *
from rich_estilo_e_imports import *


# Funções para uso da animação
def limpa_anima_f() -> None:

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def anima_f(animar: str) -> None:
    limpa_anima_f()

    console.print(animar, end='\r', highlight=False)
    time.sleep(1.8)

    limpa_anima_f()


def anima_definir_f() -> None:

    for _ in range(1):
        for animar in animar_passos:
            anima_f(animar)


# Lista para renge animar
animar_passos: list[str] = ["Olha que audácia (-_-)", "Tudo bem ^('-')^", "Ô... <('-'<)", "Toma (>'-')>"]


# Funções de construção do nome do arquivo
def painel_f(arquivo, dono):
    # Estilos para os parâmetros 'arquivo' e 'autor' na definição nome_autor
    arquivo_estilo: Text = Text(f'{" " * 1}{arquivo}', style=titulo_painel_arq)
    dono_estilo: Text = Text(dono, style='#419ec6')

    # Separador - Linha entre opções e nome do autor
    console.print('-' * largura, '\n')
    time.sleep(0.3)

    # Construção do painel de exibição do tipo de arquivo selecionado
    console.print(Panel(title='Arquivo Selecionado', title_align='left', style=painel_arquivo, box=box.ASCII2,
                        padding=True, renderable=arquivo_estilo))

    return dono_estilo


def loop_decidir_f(decidir, parte, pedido):

    if decidir:
        console.print('Definido como:', decidir, style=esmaecido, highlight=False)
        time.sleep(0.3)

        return decidir

    while not decidir:
        try:
            console.print(parte, style=aviso, highlight=False)
            console.print('-' * largura, style=aviso)
            time.sleep(0.3)

            print(' ' * largura)

            console.print('Escolha uma opção:', style=escolha_s_n)
            console.print('1. Deixar o campo vazio.')
            console.print('2. Definir como Undefined.')
            console.print('3. Colocar um valor novamente.')

            print(' ' * largura)

            campo_vazio: int = int(input('Escolha:'))

            if campo_vazio == 1:
                console.print('Definido como: Vazio', style=esmaecido, highlight=False)
                time.sleep(0.3)
                return

            elif campo_vazio == 2:
                campo_valor: str = 'Undefined'
                console.print('Definido como:', campo_valor, style=esmaecido, highlight=False)
                time.sleep(0.3)
                return campo_valor

            elif campo_vazio == 3:
                console.print('-' * largura, style=esmaecido)
                campo_valor: str = input(pedido).strip().title()

                if not campo_valor:

                    console.print('Ops...', style=esmaecido, highlight=False)
                    time.sleep(0.3)

                    while True:
                        try:
                            console.print('-' * largura, style=esmaecido)
                            campo_valor: str = input(pedido).strip().title()

                            if not campo_valor:
                                console.print('O campo ainda está vazio, tente novamente.', style=esmaecido)

                            else:
                                console.print('Definido como:', campo_valor, style=esmaecido, highlight=False)
                                time.sleep(0.3)
                                return campo_valor

                        finally:
                            continue

                else:
                    console.print('Definido como:', campo_valor, style=esmaecido, highlight=False)
                    time.sleep(0.3)
                    return campo_valor

            else:
                console.print('Por favor, responda apenas com o que é pedido.', style=aviso)
                console.print('-' * largura, style=aviso)
                time.sleep(0.3)

        except ValueError:
            console.print('Entrada invalida. Tente novamente.', style=alertas)
            console.print('-' * largura, style=alertas)
            time.sleep(0.3)


def nome_autor_f(autor: str) -> str | None:
    # Divisoria entre painel e a entrada para o nome do autor
    console.print(' ' * largura)
    time.sleep(0.3)

    # Pedindo de inserção do nome dono do tipo arquivo exibido pelo painel
    console.print(Text('Por favor, insira o nome do(a)'), autor, end='')
    autor_nome: str = input(':').strip().capitalize()

    decidir = autor_nome
    parte = f'O nome do(a) [{autor}] foi deixado vazio.'
    pedido = 'Digite o nome do autor do arquivo novamente:'

    autor_nome = loop_decidir_f(decidir, parte, pedido)

    return autor_nome


def nome_arquivo_f() -> str:
    # Separador - Linha e pedido de inserção do valor solicitado
    console.print('-' * largura, style=linha_separador)
    arquivo: str = input('Digite o nome do arquivo:').strip()

    nome_arquivo = string.capwords(arquivo)     # TODO: Aplicar as entradas depois

    # Primeiro laço: Impede que o nome do arquivo fique vago
    while not nome_arquivo:
        console.print('O campo referente ao nome do arquivo não pode ser deixado em branco.', style=aviso)
        console.print('-' * largura, style=aviso)
        time.sleep(0.3)
        nome_arquivo: str = input('Digite o nome do arquivo:').strip().title()

    # Uma pré-visualização do que foi enviado para o nome do arquivo sendo construído
    console.print('Definido como:', nome_arquivo, style=esmaecido, highlight=False)
    time.sleep(0.3)

    return nome_arquivo


def fonte_normal_f(tipo_arquivo: str) -> str:
    # Separador - Linha e pedido de inserção do valor solicitado
    console.print('-' * largura, style=linha_separador)

    fonte: str = input('Digite a fonte do arquivo:').strip().title()

    decidir = fonte
    parte = f'A fonte do aquivo [{tipo_arquivo}] está vazia.'
    pedido = 'Digite a fonte do arquivo novamente:'

    fonte = loop_decidir_f(decidir, parte, pedido)

    return fonte


def plataforma_normal_f() -> str | None:
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    # Pedindo de inserção da plataforma
    plataforma: str = input('Digite a plataforma:').strip().title()

    decidir = plataforma
    parte = f'O campo refente a plataforma está vazio.'
    pedido = 'Digite a plataforma do arquivo novamente:'

    plataforma = loop_decidir_f(decidir, parte, pedido)

    return plataforma


def qualidade_video_f() -> str:
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    qualidade: dict[int, str] = {
        0: 'LR',        # Resoluções Baixas (144p, 240p, 360p, 480p, 576p)
        1: 'SD',        # Definição Padrão (480p)
        2: 'HD',        # Alta Definição (720p)
        3: 'FHD',       # Full High Definition (1080p)
        4: '2K',        # Resolução 2K (1440p)
        5: '4K',        # Resolução 4K (2160p)
        6: '8K',        # Resolução 8K (4320p)
        7: '720p60',    # HD com 60 fps
        8: '1080p60',   # Full HD com 60 fps
        9: 'Blu-ray',   # Qualidade Blu-ray
        10: 'DVD',      # Qualidade DVD
        11: 'HDTV'      # TV de Alta Definição
    }

    dados = qualidade

    titulo_tab = 'Qualidades Disponíveis'
    coluna_1 = 'Opções'
    coluna_2 = 'Qualidades'

    sub_infor = 'Selecione a qualidade:'

    tabela_padrao_f(dados, titulo_tab, coluna_1, coluna_2, sub_infor)

    while True:
        try:
            qualidade_numero: int = int(input('Digite a opção desejada:').strip())

            if qualidade_numero in qualidade:

                q = qualidade[qualidade_numero]

                console.print(f'Qualidade [{q}] selecionada.', style=esmaecido, highlight=False)
                time.sleep(0.3)
                return qualidade[qualidade_numero]

            else:
                console.print('Opção invalida. Tente outra vez.', style=aviso)
                console.print('-' * largura, style=aviso)
                time.sleep(0.3)

        except ValueError:
            console.print('Entrada invalida. Tente novamente.', style=alertas)
            console.print('-' * largura, style=alertas)
            time.sleep(0.3)


def qualidade_imagem_f() -> str:
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    resolucao: dict[int, str] = {1: 'SD', 2: 'HD', 3: 'FHD', 4: 'UHD', 5: 'EXQ'}

    dados = resolucao

    titulo_tab = 'Qualidades Disponíveis'
    coluna_1 = 'Opções'
    coluna_2 = 'Qualidades'

    sub_infor = 'Selecione a qualidade da imagem:'

    tabela_padrao_f(dados, titulo_tab, coluna_1, coluna_2, sub_infor)

    while True:
        try:
            qualidade_numero: int = int(input('Digite a opção desejada:').strip())

            if qualidade_numero in resolucao:

                q = resolucao[qualidade_numero]

                console.print(f'Qualidade [{q}] selecionada.', style=esmaecido, highlight=False)
                time.sleep(0.3)
                return resolucao[qualidade_numero]

            else:
                console.print('Opção invalida. Tente novamente.', style=aviso)
                console.print('-' * largura, style=aviso)
                time.sleep(0.3)

        except ValueError:
            console.print('Entrada invalida. Tente novamente.', style=alertas)
            console.print('-' * largura, style=alertas)


def categoria_software_f() -> str:
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    # Dicionário para a categoria software
    cat_soft: dict[int, str] = {1: 'Grátis', 2: 'Open-Source', 3: 'Crackeado', 4: 'SO', 5: 'Driver', 6: 'Plugin',
                                7: 'ROM'}

    dados = cat_soft

    titulo_tab = 'Categorias para Software'
    coluna_1 = 'Opções'
    coluna_2 = 'Categorias'

    sub_infor = 'Selecione a categoria:'

    tabela_padrao_f(dados, titulo_tab, coluna_1, coluna_2, sub_infor)

    while True:
        try:
            categoria: int = int(input('Digite a opção deseja:').strip())

            if categoria in cat_soft:

                c = cat_soft[categoria]

                console.print(f'Categoria [{c}] selecionada.', style=esmaecido, highlight=False)
                time.sleep(0.3)
                return cat_soft[categoria]

            elif categoria not in cat_soft:
                console.print('Opção selecionada não consta. Tente outra vez.', style=alertas)
                console.print('-' * largura, style=alertas)
                time.sleep(0.3)

        except ValueError:
            console.print('Entrada invalida. Tente novamente.', style=alertas)
            console.print('-' * largura, style=alertas)
            time.sleep(0.3)


def fonte_software_f() -> str:
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    fonte_software: str = input('Digite a fonte do arquivo:').strip().title()

    decidir = fonte_software
    parte = f'O campo refente a fonte do software está vazio.'
    pedido = 'Digite a fonte do arquivo novamente:'

    fonte_software = loop_decidir_f(decidir, parte, pedido)

    return fonte_software


def plataforma_software_f() -> str:
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    plataformas: dict[int, str] = {1: 'PC', 2: 'Console', 3: 'Mobile', 4: 'WebApp', 5: 'Emulador', 6: 'Vr', 7: 'OP'}

    plat_pc: dict[int, str] = {1: 'Windows', 2: 'MacOS', 3: 'Linux'}

    dados_tab_1 = plataformas

    titulo_tab_1 = 'Plataformas Disponíveis'
    coluna_1_tab_1 = 'Opções'
    coluna_2_tab_1 = 'Plataformas'

    sub_infor_tab_1 = 'Selecione a plataforma do software:'

    dados_tab_2 = plat_pc
    titulo_tab_2 = 'Sistemas Operacionais'
    coluna_1_tab_2 = 'Opções'
    coluna_2_tab_2 = 'Sistemas'

    sub_infor_tab_2 = 'Selecione o sistema operacional:'

    tabela_padrao_f(dados_tab_1, titulo_tab_1, coluna_1_tab_1, coluna_2_tab_1, sub_infor_tab_1)

    # Laço para tratar o valor da escolha feita pelo usuário
    while True:
        try:
            plat_escolha: int = int(input('Digite a opção desejada:').strip())

            if plat_escolha in plataformas:

                if plat_escolha == 1:

                    console.print('-' * largura, style=esmaecido)
                    time.sleep(0.3)

                    tabela_padrao_f(dados_tab_2, titulo_tab_2, coluna_1_tab_2, coluna_2_tab_2, sub_infor_tab_2)

                    plat_escolha_pc: int = int(input('Digite a opção:').strip())

                    if plat_escolha_pc in plat_pc:
                        console.print(f'Definido como {plat_pc[plat_escolha_pc]}', style=esmaecido, highlight=False)
                        time.sleep(0.3)
                        return plat_pc[plat_escolha_pc]

                    elif plat_escolha_pc not in plat_pc:
                        console.print(f'Opção selecionada não consta.', style=aviso)
                        console.print('-' * largura, style=aviso)
                        time.sleep(0.3)

                console.print(f'Definido como {plataformas[plat_escolha]}', style=esmaecido, highlight=False)

                time.sleep(0.3)
                return plataformas[plat_escolha]

            elif plat_escolha not in plataformas:
                console.print('Opção selecionada não consta. Tente novamente', style=aviso)
                console.print('-' * largura, style=aviso)
                time.sleep(0.3)

        # Mesmo ficando vazio, except receber e trata esse 'probleminha'; essa opção não pode ficar vazia
        except ValueError:
            console.print('Entrada invalida. Tente novamente.', style=alertas)
            console.print('-' * largura, style=alertas)
            time.sleep(0.3)


def versao_software_f() -> str:
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    versao: str = input('Digite a versão do software:').strip()

    # Laço que impede que a versão do software fique vazia
    while not versao:
        console.print('O campo refente não pode ficar em branco.', style=alertas)
        console.print('-' * largura, style=alertas)
        time.sleep(0.3)
        versao: str = input('Digite a versão do software:').strip()

    # Uma pré-visualização do que foi enviado para o nome do arquivo sendo construído
    console.print(f'Definido como: {versao}', style=esmaecido, highlight=False)
    time.sleep(0.3)

    return versao


def dados_adicionais_f() -> str:
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    # Dicionário de dados adicíonais
    dados: dict[int, str] = {
        1: '!',         # Falta o autor
        2: 'P',         # Arq pessoal
        3: 'F',         # Arq favorito
        4: 'Old',       # Arq antigo
        5: 'Alt',       # Arq alterado
        6: 'Proj',      # Arq de projeto
        7: 'Rascunho',  # Arq de rascunho
        8: 'Final',     # Arq final
        9: 'Bkp',       # Arq de backup
        10: 'Edu',      # Arq de educação
        11: 'Cr',       # Arq criptografado
        12: 'Demo',     # Arq de Demonstração
        13: 'AI',       # Arq de inteligencia artificial
        14: 'Dev',      # Arq de desenvolvimento
    }

    # Dicíonario para impressão na tabela
    infor_tab: dict[int, str] = {1: 'Falta autor', 2: 'Arq. pessoal', 3: 'Arq. favorito', 4: 'Arq. antigo',
                                 5: 'Arq. alterado', 6: 'Arq. projeto', 7: 'Arq. rascunho', 8: 'Arq. final',
                                 9: 'Arq. de backup', 10: 'Arq. educacional', 11: 'Arq. criptografado',
                                 12: 'Arq. de demonstração', 13: 'Arq. de inteligencia artificial',
                                 14: 'Arq. de desenvolvimento', 0: 'Não desejo adicionar nem uma opção'}

    dados = infor_tab

    titulo_tab = 'Dados Adicionais'
    coluna_1 = 'Opções'
    coluna_2 = 'Informação'

    sub_infor = 'Informações adicionais:'

    tabela_padrao_f(dados, titulo_tab, coluna_1, coluna_2, sub_infor)

    # Lista na qual os valores são armazenados
    opcional_lista: list[str] = []

    # Primeira função e laço perguntando se deseja adicionar algum valor
    def pedido_1(mensagem):
        while True:
            try:
                opcional = int(input(mensagem).strip())

                if opcional in [0, 00]:
                    console.print('Nem um valor foi adicionado.', style=aviso)
                    console.print('—' * largura, style=aviso)
                    time.sleep(0.3)
                    return

                if opcional in dados:
                    opcional_lista.append(dados[opcional])
                    console.print(f'Valor [{dados[opcional]}] foi adicionado ao nome do arquivo.', style=esmaecido)
                    time.sleep(0.3)
                    break

                else:
                    console.print('Opção não encontrada. Tente novamente.', style=aviso)
                    console.print('-' * largura, style=aviso)
                    time.sleep(0.3)

            except ValueError:
                console.print('Entrada invalida. Tente outra vez.', style=alertas)
                console.print('—' * largura, style=alertas)
                time.sleep(0.3)

    # Segunda função e laço perguntando se deseja adicionar mais um ou vários valores
    def pedido_2(mensagem):
        while True:
            try:
                console.print(mensagem, end="", style=escolha_s_n)
                novo_valor = str(input()).strip().lower()

                sim = ['s', 'sim', 'si']
                nao = ['n', 'não', 'nao']

                if novo_valor in sim:

                    opcional_a = int(input('Certo, escolha mais um valor:'))

                    if opcional_a in [0, 00]:
                        anima_definir_f()
                        print(f'Apenas o valor {opcional_lista} foi adicionado.')
                        console.print('—' * largura, style=esmaecido)
                        time.sleep(0.3)
                        break

                    if opcional_a in dados:
                        if dados[opcional_a] in opcional_lista:

                            d = dados[opcional_a]

                            console.print(f'O Valor [{d}] já foi adicionado. Tente novamente.', style=aviso)
                            console.print('-' * largura, style=aviso)
                            time.sleep(0.3)

                        else:
                            opcional_lista.append(dados[opcional_a])
                            console.print(f'O Valor [{dados[opcional_a]}] foi adicionado ao nome do arquivo.')
                            console.print('-' * largura, style=esmaecido)
                            time.sleep(0.3)

                    else:
                        console.print('Opção não encontrada. Tente novamente.', '\n', '-' * largura, style=aviso)
                        time.sleep(0.3)

                elif novo_valor in nao:
                    console.print(f'Apenas o(s) valor(es) {opcional_lista} foi(foram) adicionado(s)',
                                  style=esmaecido, highlight=False)
                    console.print('—' * largura)
                    time.sleep(0.3)
                    break

                else:
                    console.print('Por favor, responda apenas com o que é pedido.', style=aviso)
                    console.print('-' * largura, style=aviso)
                    time.sleep(0.3)

            except ValueError:
                console.print('Entrada invalida. Tente outra vez.', style=alertas)
                console.print('—' * largura, style=alertas)
                time.sleep(0.3)

    pedido_1(mensagem='Escolha o que deseja adicionar:')
    pedido_2(mensagem='Deseja adicionar mais um valor? (S/N):')

    # Formatação dos valores armazenados na lista
    if (len(opcional_lista)) <= 1:
        return ''.join(opcional_lista)
    else:
        return '. '.join(opcional_lista)


def explicito_f():
    # Separador - Linha
    console.print('-' * largura, style=linha_separador)

    while True:
        try:
            saber_explicito: str = input('O conteúdo do arquivo é explícito? (S/N):').lower().strip()

            sim = ['s', 'sim', 'si']
            nao = ['n', 'não', 'nao']

            if saber_explicito in sim:
                console.print('Conteúdo definido como Explicíto', style=esmaecido)
                time.sleep(0.3)
                return 'NSFW'

            elif saber_explicito in nao:
                console.print('Conteúdo definido como não Explicíto', style=esmaecido)
                time.sleep(0.3)
                return 'SFW'

            else:
                console.print('Entrada invalida. Tente novamente.', style=alertas)
                console.print('-' * largura, style=alertas)
                time.sleep(0.3)

        except ValueError:
            console.print('Entrada invalída. Tente novamente', style=alertas)
            console.print('-' * largura, style=alertas)
            time.sleep(0.3)
