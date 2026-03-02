from app.models import Pessoa
from app.repository import PessoaRepository


class PessoaService:
    def __init__(self, repository: PessoaRepository) -> None:
        self.repository = repository

    def cadastrar(self, nome: str, email: str, telefone: str) -> Pessoa:
        self._validar_campos(nome, email, telefone)
        pessoa = Pessoa(id=None, nome=nome.strip(), email=email.strip(), telefone=telefone.strip())
        return self.repository.create(pessoa)

    def consultar(self, pessoa_id: int) -> Pessoa | None:
        return self.repository.get_by_id(pessoa_id)

    def listar(self) -> list[Pessoa]:
        return self.repository.list_all()

    def alterar(self, pessoa_id: int, nome: str, email: str, telefone: str) -> Pessoa | None:
        self._validar_campos(nome, email, telefone)
        pessoa = Pessoa(id=pessoa_id, nome=nome.strip(), email=email.strip(), telefone=telefone.strip())
        return self.repository.update(pessoa)

    def excluir(self, pessoa_id: int) -> bool:
        return self.repository.delete(pessoa_id)

    @staticmethod
    def _validar_campos(nome: str, email: str, telefone: str) -> None:
        if not nome or not nome.strip():
            raise ValueError("Nome é obrigatório.")
        if not email or "@" not in email:
            raise ValueError("E-mail inválido.")
        if not telefone or not telefone.strip():
            raise ValueError("Telefone é obrigatório.")
