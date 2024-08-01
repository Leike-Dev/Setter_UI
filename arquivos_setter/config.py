# Modúlos importados ou arquivos python externos:
from construtor import *
from rich_estilo_e_imports import *


class Renomear:
    def __init__(self, autor=None, arquivo=None, categoria_software=None, qualidade=None, qualidade_imagem=None,
                 release=None, explicito=None, fonte_normal=None, plataforma_normal=None, fonte_software=None,
                 plataforma_software=None, outras_infor=None):

        self.autor: str | None = autor
        self.arquivo: str = arquivo
        self.categoria_software: str = categoria_software
        self.qualidade: str = qualidade
        self.qualidade_imagem: str = qualidade_imagem
        self.release: str = release
        self.explicito: str = explicito
        self.fonte_normal: str = fonte_normal
        self.plataforma_normal: str | None = plataforma_normal
        self.fonte_software: str = fonte_software
        self.plataforma_software: str = plataforma_software
        self.outras_infor: str | None = outras_infor

        self.nome_formatado = None

    def formatar_nome_c_renomear(self) -> str:
        partes: list[str] = []

        if self.autor:
            partes.append(f'{self.autor} — ')

        if self.arquivo:
            partes.append(f'{self.arquivo} ')

        if self.release:
            partes.append(f'- v.{self.release}')

        if self.categoria_software:
            partes.append(f' ({self.categoria_software})')

        if self.qualidade:
            partes.append(f'- ({self.qualidade}) ')

        if self.qualidade_imagem:
            partes.append(f'({self.qualidade_imagem})')

        if self.explicito:
            partes.append(f'({self.explicito})')

        if self.outras_infor:
            partes.append(f'[{self.outras_infor}]')

        detalhe: list[str] = []

        if self.fonte_normal:
            detalhe.append(f'{self.fonte_normal}')

        if self.plataforma_normal:
            detalhe.append(f'{self.plataforma_normal}')

        if self.fonte_software:
            detalhe.append(f'{self.fonte_software}')

        if self.plataforma_software:
            detalhe.append(f'{self.plataforma_software}')

        if detalhe:
            detalhe_str = ' - '.join(detalhe)
            partes.append(f'[{detalhe_str}]')

        self.nome_formatado: str = ''.join(partes).strip()
        return self.nome_formatado


class Arquivo:
    def __init__(self, tipo_numero, tipo_numero_furry=None):
        self.tipo_numero: int = tipo_numero
        self.tipo_numero_furry: str | None = tipo_numero_furry

        self.tipo_arquivo: str | None = None
        self.tipo_nome: str | None = None

        self.estilo_autor: str | None = None

        self.autor: str | None = None
        self.arquivo: str | None = None
        self.categoria_software: str | None = None
        self.qualidade: str | None = None
        self.qualidade_imagem: str | None = None
        self.release: str | None = None
        self.explicito: str | None = None
        self.fonte_normal: str | None = None
        self.fonte_software: str | None = None
        self.plataforma_normal: str | None = None
        self.plataforma_software: str | None = None
        self.outras_infor: str | None = None

        self.nome_formatado: str | None = None

        if self.tipo_numero == 1:
            self.nome_formatado = self.documento()

        elif self.tipo_numero == 2:
            self.nome_formatado: str | None = self.imagem()

        elif self.tipo_numero == 3:
            self.nome_formatado: str | None = self.video()

        elif self.tipo_numero == 4:
            self.nome_formatado: str | None = self.software()

        if self.tipo_numero_furry in [1, 2, 3, 4]:
            self.tipo_numero = 5

        if self.tipo_numero_furry == 1:
            self.nome_formatado: str | None = self.documento_furry()

        if self.tipo_numero_furry == 2:
            self.nome_formatado: str | None = self.imagem_furry()

        if self.tipo_numero_furry == 3:
            self.nome_formatado: str | None = self.video_furry()

        if self.tipo_numero_furry == 4:
            self.nome_formatado: str | None = self.software_furry()

    def tipo_arquivo_c_arquivo(self) -> str:
        definir_titulo: dict[int, str] = {1: 'Documento', 2: 'Imagem', 3: 'Vídeo', 4: 'Software', 5: 'Furry'}

        if self.tipo_numero in definir_titulo:

            self.tipo_arquivo: str = definir_titulo[self.tipo_numero]

            return self.tipo_arquivo

    def tipo_nome_c_arquivo(self):
        definir_categoria: dict[int, str] = {1: 'Autor(a)', 2: 'Autor(a)', 3: 'Artista', 4: 'Desenvolvedor(a)',
                                             5: 'Artista Furry'}

        if self.tipo_numero in definir_categoria:

            self.tipo_nome: str = definir_categoria[self.tipo_numero]

            return self.tipo_nome

    def painel_infor_c_arquivo(self):
        self.estilo_autor = painel_tipo_arquivo_f(self.tipo_arquivo, self.tipo_nome)

    def autor_c_arquivo(self):
        self.autor: str | None = definir_autor_f(self.estilo_autor)

    def arquivo_c_arquivo(self):
        self.arquivo: str | None = definir_nome_arquivo_f()

    def categoria_soft_c_arquivo(self):
        self.categoria_software: str | None = definir_categoria_software_f()

    def qualidade_c_arquivo(self):
        self.qualidade: str | None = definir_qualidade_video_f()

    def qualidade_img_c_arquivo(self):
        self.qualidade_imagem: str | None = definir_qualidade_imagem_f()

    def release_c_arquivo(self):
        self.release: str | None = definir_versao_software_f()

    def explicito_c_arquivo(self):
        self.explicito: str | None = definir_explicito_f()

    def fonte_normal_c_arquivo(self):
        self.fonte_normal: str | None = definir_fonte_normal_f(self.tipo_arquivo)

    def plataforma_normal_c_arquivo(self):
        self.plataforma_normal: str | None = definir_plataforma_normal_f()

    def fonte_soft_c_arquivo(self):
        self.fonte_software: str | None = definir_fonte_software_f()

    def plataforma_soft_c_arquivo(self):
        self.plataforma_software: str | None = definir_plataforma_software_f()

    def outras_infor_c_arquivo(self):
        self.outras_infor: str | None = definir_dados_adicionais_f()

    def documento(self) -> str:
        self.tipo_nome_c_arquivo()
        self.tipo_arquivo_c_arquivo()

        self.painel_infor_c_arquivo()

        self.autor_c_arquivo()
        self.arquivo_c_arquivo()
        self.fonte_normal_c_arquivo()
        self.plataforma_normal_c_arquivo()
        self.outras_infor_c_arquivo()

        renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, fonte_normal=self.fonte_normal,
                                      plataforma_normal=self.plataforma_normal, outras_infor=self.outras_infor)

        nome_formatado: str = renomear.formatar_nome_c_renomear()

        return nome_formatado

    def imagem(self) -> str:
        self.tipo_nome_c_arquivo()
        self.tipo_arquivo_c_arquivo()

        self.painel_infor_c_arquivo()

        self.autor_c_arquivo()
        self.arquivo_c_arquivo()
        self.qualidade_img_c_arquivo()
        self.fonte_normal_c_arquivo()
        self.plataforma_normal_c_arquivo()
        self.outras_infor_c_arquivo()

        renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, qualidade_imagem=self.qualidade_imagem,
                                      fonte_normal=self.fonte_normal, plataforma_normal=self.plataforma_normal,
                                      outras_infor=self.outras_infor)

        nome_formatado: str = renomear.formatar_nome_c_renomear()

        return nome_formatado

    def video(self) -> str:
        console.print('—' * largura)
        time.sleep(0.3)

        sim = ['s', 'sim', 'si']
        nao = ['n', 'não', 'nao']

        while True:
            try:
                console.print('Antes de prosseguir, responda:', style=aviso)
                serie: str = input('O arquivo de vídeo é uma série? (S/N):').strip().lower()

                if serie in sim:

                    self.autor = 'Ep.00'
                    self.arquivo_c_arquivo()
                    self.qualidade_c_arquivo()
                    self.fonte_normal_c_arquivo()
                    self.plataforma_normal_c_arquivo()
                    self.outras_infor_c_arquivo()

                    renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, qualidade=self.qualidade,
                                                  fonte_normal=self.fonte_normal,
                                                  plataforma_normal=self.plataforma_normal,
                                                  outras_infor=self.outras_infor)

                    nome_formatado: str = renomear.formatar_nome_c_renomear()

                    return nome_formatado

                elif serie in nao:
                    break

                else:
                    console.print('Por favor, responda apenas com o que foi pedido.', style=alertas)
                    console.print('-' * largura, style=alertas)
                    time.sleep(0.3)

            finally:
                pass

        console.print('-' * largura, style=aviso)
        time.sleep(0.3)

        while True:
            try:
                console.print('Antes de prosseguir, responda:', style=aviso)
                serie: str = input('O arquivo de vídeo é um filme ou documentario? (S/N):').strip().lower()

                if serie in sim:

                    self.arquivo_c_arquivo()
                    self.qualidade_c_arquivo()
                    self.fonte_normal_c_arquivo()
                    self.plataforma_normal_c_arquivo()
                    self.outras_infor_c_arquivo()

                    renomear: Renomear = Renomear(arquivo=self.arquivo, qualidade=self.qualidade,
                                                  fonte_normal=self.fonte_normal,
                                                  plataforma_normal=self.plataforma_normal,
                                                  outras_infor=self.outras_infor)

                    nome_formatado: str = renomear.formatar_nome_c_renomear()

                    return nome_formatado

                elif serie in nao:
                    break

                else:
                    console.print('Por favor, responda apenas com o que foi pedido.', style=alertas)
                    console.print('-' * largura, style=alertas)
                    time.sleep(0.3)

            finally:
                pass

        self.tipo_nome_c_arquivo()
        self.tipo_arquivo_c_arquivo()

        self.painel_infor_c_arquivo()

        self.autor_c_arquivo()
        self.arquivo_c_arquivo()
        self.qualidade_c_arquivo()
        self.fonte_normal_c_arquivo()
        self.plataforma_normal_c_arquivo()
        self.outras_infor_c_arquivo()

        renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, qualidade=self.qualidade,
                                      fonte_normal=self.fonte_normal, plataforma_normal=self.plataforma_normal,
                                      outras_infor=self.outras_infor)

        nome_formatado: str = renomear.formatar_nome_c_renomear()

        return nome_formatado

    def software(self) -> str:
        self.tipo_nome_c_arquivo()
        self.tipo_arquivo_c_arquivo()

        self.painel_infor_c_arquivo()

        self.autor_c_arquivo()
        self.arquivo_c_arquivo()
        self.release_c_arquivo()
        self.categoria_soft_c_arquivo()
        self.fonte_soft_c_arquivo()
        self.plataforma_soft_c_arquivo()
        self.outras_infor_c_arquivo()

        renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, release=self.release,
                                      categoria_software=self.categoria_software, fonte_software=self.fonte_software,
                                      plataforma_software=self.plataforma_software, outras_infor=self.outras_infor)

        nome_formatado: str = renomear.formatar_nome_c_renomear()

        return nome_formatado

    def documento_furry(self) -> str:
        # Definição tanto para imagem quanto para arquivo
        self.tipo_nome_c_arquivo()
        self.tipo_arquivo_c_arquivo()

        self.painel_infor_c_arquivo()

        self.autor_c_arquivo()
        self.arquivo_c_arquivo()
        self.explicito_c_arquivo()
        self.fonte_normal_c_arquivo()
        self.plataforma_normal_c_arquivo()
        self.outras_infor_c_arquivo()

        renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, explicito=self.explicito,
                                      fonte_normal=self.fonte_normal, plataforma_normal=self.plataforma_normal,
                                      outras_infor=self.outras_infor)

        nome_formatado: str = renomear.formatar_nome_c_renomear()

        return nome_formatado

    def imagem_furry(self) -> str:
        # Definição arq. Vídeo Furry
        self.tipo_nome_c_arquivo()
        self.tipo_arquivo_c_arquivo()

        self.painel_infor_c_arquivo()

        self.autor_c_arquivo()
        self.arquivo_c_arquivo()
        self.qualidade_img_c_arquivo()
        self.explicito_c_arquivo()
        self.fonte_normal_c_arquivo()
        self.plataforma_normal_c_arquivo()
        self.outras_infor_c_arquivo()

        renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, qualidade_imagem=self.qualidade_imagem,
                                      explicito=self.explicito, fonte_normal=self.fonte_normal,
                                      plataforma_normal=self.plataforma_normal, outras_infor=self.outras_infor)

        nome_formatado: str = renomear.formatar_nome_c_renomear()

        return nome_formatado

    def video_furry(self) -> str:
        # Definição arq. Vídeo Furry
        self.tipo_nome_c_arquivo()
        self.tipo_arquivo_c_arquivo()

        self.painel_infor_c_arquivo()

        self.autor_c_arquivo()
        self.arquivo_c_arquivo()
        self.qualidade_c_arquivo()
        self.explicito_c_arquivo()
        self.fonte_normal_c_arquivo()
        self.plataforma_normal_c_arquivo()
        self.outras_infor_c_arquivo()

        renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, qualidade=self.qualidade,
                                      explicito=self.explicito, fonte_normal=self.fonte_normal,
                                      plataforma_normal=self.plataforma_normal, outras_infor=self.outras_infor)

        nome_formatado: str = renomear.formatar_nome_c_renomear()

        return nome_formatado

    def software_furry(self) -> str:
        # Definição tanto para imagem quanto para arquivo
        self.tipo_nome_c_arquivo()
        self.tipo_arquivo_c_arquivo()

        self.painel_infor_c_arquivo()

        self.autor_c_arquivo()
        self.arquivo_c_arquivo()
        self.release_c_arquivo()
        self.categoria_soft_c_arquivo()
        self.explicito_c_arquivo()
        self.fonte_soft_c_arquivo()
        self.plataforma_soft_c_arquivo()
        self.outras_infor_c_arquivo()

        renomear: Renomear = Renomear(autor=self.autor, arquivo=self.arquivo, release=self.release,
                                      categoria_software=self.categoria_software, explicito=self.explicito,
                                      fonte_software=self.fonte_software, plataforma_software=self.plataforma_software,
                                      outras_infor=self.outras_infor)

        nome_formatado: str = renomear.formatar_nome_c_renomear()

        return nome_formatado


# Definição para arquivos furry
def painel_furry_f() -> None:
    # Separador - Linha entre opções e nome do autor
    console.print('-' * largura, '\n')
    time.sleep(0.3)

    arquivo_estilo: Text = Text(f"{' ' * 1}{'Antes de prosseguir, escolha o tipo de arquivo furry.'}", style=aviso)

    # Construção do painel de exibição do tipo de arquivo selecionado
    console.print(Panel(title='Atenção', title_align='left', style=aviso, box=box.ASCII2,
                        padding=True, renderable=arquivo_estilo))

    time.sleep(0.3)


def escolha_furry_f(tipo_numero: int) -> str | None:
    # Definição para arq. Furry
    painel_furry_f()

    tabela_escolha: dict[int, str] = {1: 'Documento', 2: 'Imagem', 3: 'Vídeo', 4: 'Software'}

    dados = tabela_escolha

    titulo_tab = 'Opções Furry'
    coluna_1 = 'Opções'
    coluna_2 = 'Tipo'

    sub_infor = ''

    tabela_padrao_f(dados, titulo_tab, coluna_1, coluna_2, sub_infor)

    while True:
        try:

            tipo_numero_furry: int = int(input('Escolha o tipo de arquivo:').strip())

            if tipo_numero_furry in tabela_escolha:
                arquivo: Arquivo = Arquivo(tipo_numero, tipo_numero_furry)
                return arquivo.nome_formatado

            else:
                console.print('Opção incorreta. Tente novamente.', style=aviso)
                console.print('-' * largura, style=aviso)
                time.sleep(0.3)

        except ValueError:
            console.print('Entrada invalída. Tente novamente', style=alertas)
            console.print('-' * largura, style=alertas)
            time.sleep(0.3)
