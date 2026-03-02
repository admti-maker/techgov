from typing import Optional

from app.db import DatabaseConnection
from app.models import Pessoa


class PessoaRepository:
    def __init__(self, db: DatabaseConnection) -> None:
        self.db = db

    def create(self, pessoa: Pessoa) -> Pessoa:
        query = """
        INSERT INTO pessoas (nome, email, telefone)
        VALUES (%s, %s, %s)
        RETURNING id, nome, email, telefone, criado_em, atualizado_em;
        """
        with self.db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (pessoa.nome, pessoa.email, pessoa.telefone))
                row = cur.fetchone()
        return Pessoa(*row)

    def get_by_id(self, pessoa_id: int) -> Optional[Pessoa]:
        query = """
        SELECT id, nome, email, telefone, criado_em, atualizado_em
        FROM pessoas
        WHERE id = %s;
        """
        with self.db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (pessoa_id,))
                row = cur.fetchone()
        return Pessoa(*row) if row else None

    def list_all(self) -> list[Pessoa]:
        query = """
        SELECT id, nome, email, telefone, criado_em, atualizado_em
        FROM pessoas
        ORDER BY id;
        """
        with self.db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
        return [Pessoa(*row) for row in rows]

    def update(self, pessoa: Pessoa) -> Optional[Pessoa]:
        query = """
        UPDATE pessoas
        SET nome = %s,
            email = %s,
            telefone = %s,
            atualizado_em = CURRENT_TIMESTAMP
        WHERE id = %s
        RETURNING id, nome, email, telefone, criado_em, atualizado_em;
        """
        with self.db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (pessoa.nome, pessoa.email, pessoa.telefone, pessoa.id))
                row = cur.fetchone()
        return Pessoa(*row) if row else None

    def delete(self, pessoa_id: int) -> bool:
        query = "DELETE FROM pessoas WHERE id = %s;"
        with self.db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (pessoa_id,))
                return cur.rowcount > 0
