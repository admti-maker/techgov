from abc import ABC, abstractmethod

from app.services import PessoaService


class Action(ABC):
    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class CadastrarPessoaAction(Action):
    def __init__(self, service: PessoaService) -> None:
        self.service = service

    def execute(self) -> None:
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        pessoa = self.service.cadastrar(nome, email, telefone)
        print(f"Pessoa cadastrada com ID {pessoa.id}.")


class ConsultarPessoaAction(Action):
    def __init__(self, service: PessoaService) -> None:
        self.service = service

    def execute(self) -> None:
        pessoa_id = int(input("ID da pessoa: "))
        pessoa = self.service.consultar(pessoa_id)
        if not pessoa:
            print("Pessoa não encontrada.")
            return
        print(pessoa)


class AlterarPessoaAction(Action):
    def __init__(self, service: PessoaService) -> None:
        self.service = service

    def execute(self) -> None:
        pessoa_id = int(input("ID da pessoa: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        telefone = input("Novo telefone: ")
        pessoa = self.service.alterar(pessoa_id, nome, email, telefone)
        if not pessoa:
            print("Pessoa não encontrada para alteração.")
            return
        print("Pessoa alterada com sucesso.")


class ExcluirPessoaAction(Action):
    def __init__(self, service: PessoaService) -> None:
        self.service = service

    def execute(self) -> None:
        pessoa_id = int(input("ID da pessoa: "))
        sucesso = self.service.excluir(pessoa_id)
        print("Pessoa excluída." if sucesso else "Pessoa não encontrada.")


class ListarPessoasAction(Action):
    def __init__(self, service: PessoaService) -> None:
        self.service = service

    def execute(self) -> None:
        pessoas = self.service.listar()
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return
        for pessoa in pessoas:
            print(pessoa)
