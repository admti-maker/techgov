from app.actions import (
    AlterarPessoaAction,
    CadastrarPessoaAction,
    ConsultarPessoaAction,
    ExcluirPessoaAction,
    ListarPessoasAction,
)
from app.db import DatabaseConnection
from app.repository import PessoaRepository
from app.services import PessoaService


class SistemaMultitarefa:
    def __init__(self) -> None:
        repository = PessoaRepository(DatabaseConnection())
        service = PessoaService(repository)
        self.rotinas = {
            "1": CadastrarPessoaAction(service),
            "2": ConsultarPessoaAction(service),
            "3": AlterarPessoaAction(service),
            "4": ExcluirPessoaAction(service),
            "5": ListarPessoasAction(service),
        }

    def executar(self) -> None:
        while True:
            print("\n=== Sistema de Cadastro de Pessoas ===")
            print("1 - Incluir pessoa")
            print("2 - Consultar pessoa")
            print("3 - Alterar pessoa")
            print("4 - Excluir pessoa")
            print("5 - Listar pessoas")
            print("0 - Sair")
            opcao = input("Escolha uma ação: ").strip()

            if opcao == "0":
                print("Encerrando sistema.")
                break

            action = self.rotinas.get(opcao)
            if not action:
                print("Ação inválida.")
                continue

            try:
                action.execute()
            except ValueError as error:
                print(f"Erro de validação: {error}")
            except Exception as error:
                print(f"Falha ao executar ação: {error}")


if __name__ == "__main__":
    SistemaMultitarefa().executar()
