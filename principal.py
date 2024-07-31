# Modúlos importados ou arquivos python externos:
from arquivo_config import *
from estilo_rich_e_imports import *


# Definição de limpeza; chamada quando aceitar continuar no programa
def limpar_f():
    clean = os.system('cls' if os.name == 'nt' else 'clear')
    return clean


def painel_boas_vindas_f() -> None:
    time.sleep(0.3)

    apresentar: Text = Text('Seu assistente inteligente de renomeação de arquivos no terminal!', justify='center')

    # Painel de boas-vidas do programa
    panel_titulo: Panel = Panel(title='Bem-vindo ao Setter!', title_align='center', subtitle='𝛂', style=caixa_intro,
                                renderable=apresentar, padding=(1, 3), box=box.ASCII2)

    console.print(panel_titulo)
    console.print('—' * largura)
    time.sleep(0.3)


def nome_arquivo_formatado_f(nome_formatado: str) -> None:
    print('' * largura)

    # Tratamento para deixar alinhado dentro do painel
    formatado: Text = Text(f'{' ' * 1}{nome_formatado}', style=painel_arquivo_final)

    panel_final: Panel = Panel(title='Nome Gerado', title_align='left', style=painel_arquivo_final, box=box.ASCII2,
                               renderable=formatado, padding=True, highlight=False)

    console.print(panel_final)

    pyperclip.copy(nome_formatado)
    console.print(f'\nO nome gerado foi copiado!', style=esmaecido)

    time.sleep(0.5)
    return


def tabela_escolha_f() -> int:
    opcoes: dict[int, str] = {1: 'Documento', 2: 'Imagem', 3: 'Vídeo', 4: 'Software', 5: 'Furry'}

    dados: dict[int, str] = opcoes

    titulo_tab: str = 'Tipo de Arquivo'
    coluna_1: str = 'Opções'
    coluna_2: str = 'Tipo'

    sub_infor: str = ''

    tabela_padrao_f(dados, titulo_tab, coluna_1, coluna_2, sub_infor)

    while True:
        try:
            # Solicita ao usuário o número correspondente ao tipo de arquivo
            numero: int = int(input('Digite a opção desejada:'))

            escolha: list[int] = [1, 2, 3, 4]

            if numero in escolha:
                return numero

            elif numero == 5:
                return numero

            else:
                console.print('Opção não consta. Tente novamente.', style=aviso, highlight=False)
                console.print('-' * largura, style=aviso)
                time.sleep(0.3)

        except ValueError:
            console.print('Entrada invalída. Tente novamente', style=alertas)
            console.print('-' * largura, style=alertas)
            time.sleep(0.3)


# Definição principal
def main() -> None:
    painel_boas_vindas_f()

    tipo_numero = tabela_escolha_f()

    if tipo_numero == 5:
        nome_formatado = escolha_furry_f(tipo_numero)

    elif tipo_numero:
        arquivo = Arquivo(tipo_numero)
        nome_formatado = arquivo.nome_formatado

    else:
        return

    nome_arquivo_formatado_f(nome_formatado)


if __name__ == '__main__':
    while True:
        main()
        console.print('Deseja renomear outro arquivo? S/N', end='', style=escolha_s_n)
        sair: str = input(':').strip().lower()

        sim: list[str] = ['s', 'sim', 'si']
        nao: list[str] = ['n', 'não', 'nao']

        if sair in sim:
            limpar_f()

        if sair in nao:
            console.print('—' * largura, style=esmaecido)
            console.print('Obrigado por usar o Setter :D', style=escolha_s_n)
            time.sleep(0.3)
            break
