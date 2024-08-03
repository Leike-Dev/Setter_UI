from pathlib import Path
import exiftool
from arquivos_setter.rich_estilo_e_imports import *

extensoes_imagens = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}


def caminho_f() -> Path:

    while True:
        try:
            entrada: str = input('Cole o caminho para a pasta:')

            caminho: Path = Path(entrada).absolute()

            if caminho.exists() and caminho.is_dir():
                console.print(f'O caminho é valido (Pasta).', style=esmaecido)
                print('\n')
                time.sleep(0.3)
                return caminho

            elif caminho.exists() and caminho.is_file():
                console.print('O caminho invalido (Arquivo). Tente inserir um caminho para uma pasta.', style=aviso)
                console.print('-' * largura, style=aviso)
                time.sleep(0.3)

            else:
                console.print('Caminho não existe. Tente novamente.', style=aviso)
                console.print('-' * largura, style=aviso)
                time.sleep(0.3)

        except ValueError:
            console.print('Erro ao passar o caminho. Entrada invalida.', style=alertas)
            console.print('-' * largura, style=alertas)
            time.sleep(0.3)


def listar_arquivos_img(caminho) -> list:

    arquivos_imagens: list = []

    for arquivo in caminho.iterdir():

        if arquivo.is_file() and arquivo.suffix.lower() in extensoes_imagens:
            arquivos_imagens.append(arquivo)

    return arquivos_imagens


def obter_metadados(arquivo_imagens) -> tuple[dict[str, str], list[str]]:

    lista_nome_valor_img: dict[str, str] = {}
    qualidade_pixel: list[str] = []

    with exiftool.ExifToolHelper() as et:
        for caminho_arquivo in arquivo_imagens:
            metadata = et.get_metadata(str(caminho_arquivo))

            if metadata:

                for entrar in metadata:

                    nome_image: str = ''
                    qualidade_image: str = ''
                    megapixel_valor: float = 0

                    for tag, value in entrar.items():

                        nome = 'File:FileName'
                        tamanho = 'Composite:ImageSize'
                        pixel = 'Composite:Megapixels'

                        if tag == nome:
                            nome_image = value

                        if tag == tamanho:
                            qualidade_image = value

                        if tag == pixel:
                            megapixel_valor = value

                    if nome_image and qualidade_image:
                        lista_nome_valor_img.update({nome_image: qualidade_image})

                    if megapixel_valor:

                        megapixel: float = round(megapixel_valor, 3)

                        if megapixel < 1:
                            q_pixel = 'SD'  # Qualidade SD

                        elif 1 <= megapixel < 2:
                            q_pixel = 'HD'  # Qualidade HD

                        elif 2 <= megapixel < 6:
                            q_pixel = 'FHD'  # Qualidade FHD

                        elif 6 <= megapixel <= 20:
                            q_pixel = 'UHD'  # Qualidade UHD

                        else:
                            q_pixel = 'EXQ'  # Qualidade Extrema EXQ

                        qualidade_pixel.append(q_pixel)

    return lista_nome_valor_img, qualidade_pixel


def tabela_exibir(lista_nome_valor_img, qualidade_pixel) -> None:

    tabela: Table = Table(title='Informações', title_style=assunto_tabela_titulo, title_justify='center',
                          box=box.ASCII2, show_lines=True, border_style=dim, show_footer=True, footer_style=aviso)

    tabela.add_column('L x A', justify='center', style=escolha_tabela_1, no_wrap=True, header_style=tabela_titulo)
    tabela.add_column('Nome', justify='left', style=escolha_tabela_2, header_style=tabela_titulo, overflow='ellipsis',
                      footer_style=linha_final, max_width=50, min_width=30)
    tabela.add_column('Qualidade', justify='center', style=qualidade_img, no_wrap=True, header_style=tabela_titulo)

    with Live(tabela, auto_refresh=True):
        for key, value in lista_nome_valor_img.items():
            q_pixel: int = qualidade_pixel.pop(0) if qualidade_pixel else 0

            time.sleep(0.4)

            tabela.add_row(value, key, str(q_pixel))

        total = str(tabela.row_count)
        t = Text('Arq. Lidos:', justify='center')
        n = Text(total, justify='left')

        tabela.columns[0].footer = t
        tabela.columns[1].footer = n

    console.save_html('imagens_qualidade.html')

    time.sleep(0.4)
    console.print('Concluído', style=esmaecido)


def main() -> None:
    painel = Panel(title='Ferramenta', title_align='center',
                   renderable=Text('Obtenção da Qualidade de Imagens', justify='center'),
                   style=caixa_intro, box=box.ASCII2, padding=(1, 3), width=80)

    # Imprime o painel de boas vindas
    console.print(painel)

    # Chama a função para obter o caminho para os arquivos
    caminho = caminho_f()

    # Passando o caminho para lista_arquivos_img obtém-se uma lista com arquivos de imagem
    arquivos_imagens = listar_arquivos_img(caminho)

    # A função obter_metadados pega todos os dados dos arquivos de imagem e retorna um diciónario e uma lista
    lista_nome_valor_img, qualidade_pixel = obter_metadados(arquivos_imagens)

    # Ao final do processo, tabela_exibir recebe os respectivos valores e os imprime de forma clara ao usuário
    tabela_exibir(lista_nome_valor_img, qualidade_pixel)


if __name__ == '__main__':
    main()
