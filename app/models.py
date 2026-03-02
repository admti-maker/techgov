from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Pessoa:
    id: Optional[int]
    nome: str
    email: str
    telefone: str
    criado_em: Optional[datetime] = None
    atualizado_em: Optional[datetime] = None
