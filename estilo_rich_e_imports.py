from rich.table import Table
from rich import (box, print)
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.layout import Layout
from rich.style import Style

import time
import os
import pyperclip
import string

console: Console = Console(record=True)
largura: int = console.size.width
layout: Layout = Layout()

# Definições de estilos do rich -------- Para todos -----------------------------------------------------*
painel_arquivo: Style = Style(color='#dac048', bold=True)
titulo_painel_arq: Style = Style(color='#dac048', bold=True)

assunto_tabela_titulo: Style = Style(color='#dac048', bold=True)
tabela_titulo: Style = Style(bold=True)
escolha_tabela_1: Style = Style(color='#23A9CF', bold=True)
escolha_tabela_2: Style = Style(color='#937BE2', bold=True)

indefinido: Style = Style(color='#fa8100', bold=True)

dim: Style = Style(dim=True)

zebra = [Style(dim=True), Style(dim=False)]

linha_final: Style = Style(color='#dac048', bold=True)

qualidade_img: Style = Style(color='#41c300', bold=True)

escolha_s_n: Style = Style(color='#00af87')
destaque: Style = Style(color='#ff8787', bold=True)
esmaecido: Style = Style(dim=True, bold=True)
alertas: Style = Style(color='#dc5774', bold=True)
aviso: Style = Style(color='#dac048', bold=True)

linha_separador: Style = Style(color='#419ec6', bold=True)

# a = Style(color='#808080') Antiga cor do esmaecido

# Definição de estilos do rich - Principal ---------------------------------------------------------------*
caixa_intro: Style = Style(color='#419ec6', bold=True)
painel_arquivo_final: Style = Style(color='#5f75ce', bold=True)


# Definição de estilos para quase todas as tabelas do programa -------------------------------------------*
def tabela_padrao_f(dados, titulo_tab, coluna_1, coluna_2, sub_infor):

    if sub_infor:
        print(sub_infor)
        print(' ' * largura)

    else:
        print(' ' * largura)

    time.sleep(0.3)

    tabela = Table(title=titulo_tab, title_justify='center', title_style=assunto_tabela_titulo, box=box.ASCII2,
                   show_lines=True, min_width=30, style=dim)

    tabela.add_column(coluna_1, justify='center', style=escolha_tabela_1, no_wrap=True, header_style=tabela_titulo)
    tabela.add_column(coluna_2, justify='left', style=escolha_tabela_2, header_style=tabela_titulo)

    for key, value in dados.items():
        tabela.add_row(f'{key}', value)

    console.print(tabela)
    print(' ' * largura)
