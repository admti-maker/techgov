import pytest

from app.models import Pessoa
from app.services import PessoaService


class FakePessoaRepository:
    def __init__(self):
        self.data = {}
        self.current = 1

    def create(self, pessoa: Pessoa) -> Pessoa:
        pessoa.id = self.current
        self.data[pessoa.id] = pessoa
        self.current += 1
        return pessoa

    def get_by_id(self, pessoa_id: int):
        return self.data.get(pessoa_id)

    def list_all(self):
        return list(self.data.values())

    def update(self, pessoa: Pessoa):
        if pessoa.id not in self.data:
            return None
        self.data[pessoa.id] = pessoa
        return pessoa

    def delete(self, pessoa_id: int):
        return self.data.pop(pessoa_id, None) is not None


def test_fluxo_crud_pessoa():
    service = PessoaService(FakePessoaRepository())

    pessoa = service.cadastrar("Ana", "ana@email.com", "21999999999")
    assert pessoa.id == 1

    consultada = service.consultar(1)
    assert consultada is not None
    assert consultada.nome == "Ana"

    alterada = service.alterar(1, "Ana Souza", "ana@email.com", "21888888888")
    assert alterada is not None
    assert alterada.nome == "Ana Souza"

    assert service.excluir(1) is True
    assert service.consultar(1) is None


def test_validacao_email():
    service = PessoaService(FakePessoaRepository())

    with pytest.raises(ValueError):
        service.cadastrar("Ana", "email-invalido", "21999999999")
