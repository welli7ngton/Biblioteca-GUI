import os
import json
import sys
# from typing import Optional
import qdarktheme
from variaveis import CAMINHO_DB_FILES
from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow,
                               QCalendarWidget,
                               QVBoxLayout,
                               QGridLayout,
                               QFormLayout,
                               QWidget,
                               QFrame,
                               QApplication,
                               QPushButton,
                               QLabel,
                               QDialog,
                               QLineEdit,
                               QSpinBox,
                               QDateEdit,
                               QDialogButtonBox,
                               QMessageBox
                               )

IDS_ALUNOS = os.path.join(CAMINHO_DB_FILES, "id_alunos.json")
INFO_ALUNOS = os.path.join(CAMINHO_DB_FILES, "info_alunos.json")
IDS_LIVROS = os.path.join(CAMINHO_DB_FILES, "id_livros.json")
INFO_LIVROS = os.path.join(CAMINHO_DB_FILES, "info_livros.json")
EMPRESTIMOS = os.path.join(CAMINHO_DB_FILES, "emprestimos.json")
ID_EMPRESTIMO = os.path.join(CAMINHO_DB_FILES, "id_emprestimo.json")
ANO_ATUAL = datetime.now().year
MES_ATUAL = datetime.now().month
DIA_ATUAL = datetime.now().day


class Biblioteca:

    def __init__(self) -> None:

        # Importando dados
        self.id_alunos = self.importacao(IDS_ALUNOS)
        self.info_alunos = self.importacao(INFO_ALUNOS)
        self.id_livros = self.importacao(IDS_LIVROS)
        self.info_livros = self.importacao(INFO_LIVROS)
        self.emprestimos = self.importacao(EMPRESTIMOS)
        self.id_emprestimo = self.importacao(ID_EMPRESTIMO)

    def importacao(self, caminho):
        with open(caminho, "r") as arq:
            dados = json.load(arq)
        return dados

    def exportacao(self, caminho, dados):
        with open(caminho, "w") as arq:
            json.dump(dados, arq, ensure_ascii=False, indent=2)

    def cadastra_aluno(
            self,
            nome: str,
            idade: str,
            serie: str,
            turno: str,
            contato: str,
            endereco: str
            ):
        _id = str(len(self.id_alunos))
        if _id in self.id_alunos:
            return False
        self.id_alunos.append(_id)
        # print("ID =", _id)

        # ########### change ########### #
        # nome = input("Nome do Aluno: ")
        # idade = int(input("Idade: "))
        # serie = input("Série: ")
        # turno = input("Turno: ")
        # contato = input("Contato (00 0 0000-0000): ")
        # print("Endereço: Rua, Bairro, Número.:")
        # endereco = input()
        # ########### change ########### #

        self.info_alunos[_id] = (
            f"ID: {_id}, Nome: {nome.title()}, Série: {serie}, "
            f"Turno: {turno.title()}, Idade: {idade}, Contato: {contato}, "
            f"Endereço: {endereco.title()}"
        )
        self.exportacao(IDS_ALUNOS, self.id_alunos)
        self.exportacao(INFO_ALUNOS, self.info_alunos)
        return self.info_alunos[_id]

    def cadastra_livro(self):

        titulo_livro = input("Digite o título do livro: ")
        genero = input("Digite o gênero do livro: ")
        autor = input("Digite o Autor: ")
        editora = input("Digite a Editora: ")
        qtd = input("Digite a quantidade: ")

        # verificando se a quantidade é um valor numérico
        while True:
            if qtd.isdigit() is False:
                qtd = input("Digite um valor válido, um número: ")
            else:
                break
        _id = input("Digite a numeração do livro: ")
        # verificando se a numeração do livro é um valor numérico
        while True:
            if _id.isdigit():
                while True:
                    if _id not in self.id_livros and _id.isdigit():
                        break
                    else:
                        print("Livro já cadastrado ou numeração inválida.")
                        _id = input("Digite uma numeração válida: ")
                break
            else:
                print("Digite uma numeração válida.")
        # atualizando dicionário
        self.info_livros[_id] = (
            f"Título: {titulo_livro.capitalize()}, "
            f"Gênero: {genero.capitalize()}, "
            f"Autor: {autor.capitalize()}, "
            f"Editora:  {editora.capitalize()}, "
            f"Quantidade: {qtd}, Numeração: {_id}"
        )
        self.id_livros.append(_id)

        print()
        print("As informações do livro cadasrtado são:")
        print("NUMERAÇÃO: ", _id)
        print(self.info_livros[_id])
        print()
        self.exportacao(IDS_LIVROS, self.id_livros)
        self.exportacao(INFO_LIVROS, self.info_livros)

    def altera_aluno(self):
        while True:
            verificador = input("Digite o ID do Aluno que quer alterar: ")
            if verificador not in self.id_alunos:
                print(
                    "Aluno não cadastrado ou numeração inválida, "
                    "revise e digite uma numeração válida."
                    )
                continue
            else:
                print("O cadastro que vai ser alterado é:")
                print(self.info_alunos[verificador])
                print("Digite as alterações:")
                nome = input("Nome do Aluno: ")
                serie = str(input("Série: "))
                turno = input("Turno: ")
                idade = int(input("Idade: "))
                print("Contato: 00 0 0000 0000")
                contato = input()
                print("Endereço: Rua, Bairro, Número.:")
                endereco = input()
                # atualizando dicionário
                self.info_alunos[verificador] = (
                    f"Nome: {nome.capitalize()}, Série: {serie}, "
                    f"Turno: {turno}, Idade: {idade}, Contato: {contato}, "
                    f"Endereço: {endereco.capitalize()}")
                self.exportacao(INFO_ALUNOS, self.info_alunos)
                break

    def altera_livro(self):
        while True:
            numeracao = input("Digite a numeração do livro que quer alterar: ")
            if numeracao not in self.id_livros:
                print(
                    "Livro não cadastrado ou numeração inválida, "
                    "revise e digite uma numeração válida."
                    )
                continue
            else:
                print("O livro que vai ser alterado é:")
                print(self.info_livros[numeracao])
                print("Digite as alterações:")

                # cadastro de alterações
                titulo_livro = input("Digite o título do livro: ")
                genero = input("Digite o gênero do livro: ")
                autor = input("Digite o Autor: ")
                editora = input("Digite a Editora: ")
                qtd = input("Digite a quantidade: ")
                while True:
                    if qtd.isdigit() is False:
                        qtd = input("Digite um valor válido, um número: ")
                    else:
                        qtd = int(qtd)
                        break

                # atualizando dados no dicionário
                self.info_livros[numeracao] = (
                    f"Título: {titulo_livro.capitalize()}, "
                    f"Gênero: {genero.capitalize()}, "
                    f"Autor: {autor.capitalize()}, "
                    f"Editora:  {editora.capitalize()}, Quantidade: {qtd}")
                self.exportacao(INFO_LIVROS, self.info_livros)
                break

    def fazer_emprestimo(self):
        # r = input("Tem conhecimento do ID do aluno? [S]im [N]ão: ")
        # if r in "nN":
        #     nome = input("Digite o nome do aluno: ")
        #     for chave, valor in self.info_alunos.items():
        #         if nome.lower() in valor \
        #             or nome.capitalize() in valor \
        #                 or nome.title() in valor:
        #             print(" ID:", chave, "\n", valor)
        while True:
            _id = input("Digite o ID do aluno: ")

            if _id not in self.info_alunos:
                print("ID não encontrado, digite um ID válido.")
                continue
            else:
                livro = input("Digite o Livro que será emprestado: ")
                devo = input("Digite a data para devolução(DD/MM): ")
                chave = datetime.now().microsecond

            self.emprestimos[chave] = (self.info_alunos[_id],
                                       livro.title(),
                                       devo
                                       )
            print(" Chave da devolução:", chave, "\n", self.emprestimos[chave])
            self.id_emprestimo[chave] = _id
            self.exportacao(EMPRESTIMOS, self.emprestimos)
            self.exportacao(ID_EMPRESTIMO, self.id_emprestimo)
            break

    def fazer_devolucao(self):
        # r = input("Tem conhecimento do ID do aluno? [S]im [N]ão: ")
        # if r in "nN":
        #     nome = input("Digite o nome do aluno: ")
        #     for chave, valor in self.info_alunos.items():
        #         if nome.lower() in valor \
        #             or nome.capitalize() in valor \
        #                 or nome.title() in valor:
        #             print(" ID:", chave, "\n", valor)

        while True:
            _id = input("Digite o ID do aluno: ")
            if _id not in self.id_emprestimo.values():
                print("O aluno não tem nada para devolver.")
                return False
            else:
                for chave, valor in self.id_emprestimo.items():
                    print("Chave:", chave) if _id \
                        in self.id_emprestimo.values() else print()
                    print("Informações:", self.emprestimos[chave], "\n")

            c = input("Digite a chave para realizar a devolução: ")
            self.emprestimos.pop(c)
            self.id_emprestimo.pop(c)
            print("Devolução realizada.")
            self.exportacao(EMPRESTIMOS, self.emprestimos)
            self.exportacao(ID_EMPRESTIMO, self.id_emprestimo)
            break


class JanelaPrincipal(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.b1 = Biblioteca()
        # Padrão
        # Criando o widget central
        self.widgetCentral = QWidget()

        # Criando janelas para cada botão
        self.janelaCA = JanelaCA(self.b1)
        self.janelaCL = JanelaCL()
        # self.janelaAA = JanelaAA(self.b1)
        self.janelaAL = JanelaAL()
        self.janelaEP = JanelaEP()
        self.janelaDV = JanelaDV()

        # Criando os layouts da janela principal
        self.meuLayout1 = QVBoxLayout()
        self.layout_botoes = QGridLayout()
        self.criabotoes()

        # criando widget do calendário
        self.calendario = QCalendarWidget()
        self.config_estilo_calendario()

        # criando widget da barra de titulo
        self.barraTitulo = BarraTitulo()

        # adicionando barra de titulo na primeira linha do layout principal
        self.meuLayout1.addWidget(
            self.barraTitulo,
            )

        # adicionando calendario na primeira linha do segundo layout
        self.meuLayout1.addWidget(
            self.calendario,
            alignment=Qt.AlignmentFlag.AlignCenter
            )

        # Colocando o widget central no topo da hierarquia de widgets
        self.setCentralWidget(self.widgetCentral)

        self.meuLayout1.addLayout(self.layout_botoes)

        # Setando o meuLayout1 no widget central
        self.widgetCentral.setLayout(self.meuLayout1)

        self.layout_botoes.addWidget(self.CA, 0, 0)
        self.layout_botoes.addWidget(self.CL, 0, 1)
        self.layout_botoes.addWidget(self.AA, 1, 0)
        self.layout_botoes.addWidget(self.AL, 1, 1)
        self.layout_botoes.addWidget(self.EP, 2, 0)
        self.layout_botoes.addWidget(self.DV, 2, 1)

        self.config_style()

        self.CA.clicked.connect(self.janelaCA.show)

        self.CL.clicked.connect(self.janelaCL.show)

        # self.AA.clicked.connect(self.janelaAA.show)

        self.AL.clicked.connect(self.janelaAL.show)

        self.EP.clicked.connect(self.janelaEP.show)

        self.DV.clicked.connect(self.janelaDV.show)

    def config_style(self):
        # Setando tamanho de 1200x800 enquanto trabalho no projeto
        self.setFixedSize(1200, 975)

        # Setando para iniciar com a tela maximizada
        # self.showMaximized()

        # Setando tamanho mínimo da tela
        # self.setMinimumSize(1200, 975)

        # Setando tema
        qdarktheme.setup_theme(
            theme='dark',
            corner_shape='rounded',
            custom_colors={
                "[dark]": {
                    "primary": f"{'#1e81b0'}",
                },
                "[light]": {
                    "primary": f"{'#1e81b0'}",
                },
            }
        )

    def config_estilo_calendario(self):
        qss = """
            QCalendarWidget {
                background-color: #f0f0f0;
                color: #333;
            }
            QCalendarWidget QToolButton {
                background-color: #1e81b0;
                color: #fff;
                border: 1px solid #1e81b0;
                min-width: 20px;
                min-height: 20px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #16658a;
            }
            QCalendarWidget QToolButton:pressed {
                background-color: #115270;
            }
        """

        self.calendario.setStyleSheet(qss)
        self.calendario.setFixedSize(800, 700)

    def criabotoes(self):
        self.CA = Botao("1 - Cadastra Aluno")
        self.CL = Botao("2 - Cadastra Livro")
        self.AA = Botao("3 - Altera Aluno")
        self.AL = Botao("4 - Altera Livro")
        self.EP = Botao("5 - Empréstimo")
        self.DV = Botao("6 - Devoluçao")

    def fazSlot(self, funcao):
        def _slot():
            funcao()
        return _slot


class BarraTitulo(QFrame):
    def __init__(self):
        super().__init__()
        # self.setAutoFillBackground(True)
        self.setFixedHeight(45)
        self.setStyleSheet("background-color: #1e81b0; color: white;")

        layout = QVBoxLayout(self)

        self.titulo_label = QLabel("Biblioteca")
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.titulo_label)


class Botao(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        fonte = self.font()
        fonte.setPixelSize(40)
        fonte.setBold(True)
        self.setFont(fonte)


# classes para as janelas secundárias apenas com estilos
class JanelaCA(QDialog):
    def __init__(self, _biblioteca: Biblioteca, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        biblioteca = _biblioteca
        self.setWindowTitle("Cadastro de Aluno")
        self.setMinimumSize(600, 350)
        layoutca = QFormLayout()
        self.setLayout(layoutca)
        campo_texto = [nome := QLineEdit(), idade := QSpinBox(),
                       serie := QLineEdit(), turno := QLineEdit(),
                       contato := QLineEdit(), endereco := QLineEdit()]
        titulos = ["Nome Aluno", "Idade",
                   "Série", "Turno",
                   "Contato", "Endereço"]
        for titulo, campo in enumerate(campo_texto):
            layoutca.addRow(str(titulos[titulo]), campo)

        botoes_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            )

        layoutca.addWidget(botoes_box)
        botoes_box.accepted.connect(self.faz_slot(
            biblioteca.cadastra_aluno,
            nome,
            idade,
            serie,
            turno,
            contato,
            endereco
        ))

        botoes_box.rejected.connect(self.reject)

    def faz_slot(self, func, *args: Botao):
        def slot():
            n, i, s, t, c, e = args
            msg = func(n.text(),
                       i.text(),
                       s.text(),
                       t.text(),
                       c.text(),
                       e.text())
            for b in args:
                b.clear()
            mensagem = QMessageBox()
            mensagem.setWindowTitle("Cadastro realizado!")
            mensagem.setIcon(mensagem.Icon.Information)
            mensagem.setText(msg)
            mensagem.exec()
        return slot


class JanelaCL(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Cadastro de Livro")
        self.setMinimumSize(600, 800)
        layoutcl = QFormLayout()
        self.setLayout(layoutcl)
        layoutcl.addRow("Titulo Livro:", QLineEdit())
        layoutcl.addRow("Genero:", QLineEdit())
        layoutcl.addRow("Autor:", QLineEdit())
        layoutcl.addRow("Editora:", QLineEdit())
        layoutcl.addRow("Quantidade:", QSpinBox())

        b_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        b_box.setAccessibleName("teste")
        layoutcl.addWidget(b_box)

        b_box.accepted.connect(self.accept)
        b_box.rejected.connect(self.reject)


# class JanelaAA(JanelaCA):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.setWindowTitle("Alteração de Cadastro - Aluno")


class JanelaAL(JanelaCL):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Alteração de Cadastro - livro")


class JanelaEP(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Empréstimo")
        self.setMinimumSize(600, 800)
        layoutep = QFormLayout()
        self.setLayout(layoutep)
        botao_id = QSpinBox()
        botao_id.setRange(0, 9999999)
        layoutep.addRow("ID do ALuno:", botao_id)
        layoutep.addRow("Nome Aluno:", QLineEdit())

        layoutep.addRow("Livro:", QLineEdit())
        botao_data = QDateEdit()
        botao_data.setCalendarPopup(True)
        layoutep.addRow("Devolução:", botao_data)

        b_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        b_box.setAccessibleName("teste")
        layoutep.addWidget(b_box)

        b_box.accepted.connect(self.accept)
        b_box.rejected.connect(self.reject)


class JanelaDV(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Devolução")
        self.setMinimumSize(600, 800)
        layoutdv = QFormLayout()
        self.setLayout(layoutdv)
        botao_id = QSpinBox()
        botao_id.setRange(0, 9999999)
        layoutdv.addRow("ID do ALuno:", botao_id)
        layoutdv.addRow("Nome Aluno:", QLineEdit())

        botao_chave = QSpinBox()
        botao_chave.setRange(0, 9999999)
        layoutdv.addRow("Chave:", botao_chave)

        b_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        b_box.setAccessibleName("teste")
        layoutdv.addWidget(b_box)

        b_box.accepted.connect(self.accept)
        b_box.rejected.connect(self.reject)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    janelaCentral = JanelaPrincipal()

    janelaCentral.show()
    sys.exit(app.exec())
