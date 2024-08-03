from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.style import Style
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich import box

import time
import os
import string
import pyperclip

live = Live
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

