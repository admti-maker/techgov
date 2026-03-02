# techgov
Sistema de Gestão Pública

## Sistema multitarefa com rotinas e ações (orientado a objeto)

Implementação inicial do módulo **Cadastro de Pessoas** com as ações:
- inclusão
- consulta
- alteração
- exclusão
- listagem

Arquitetura em camadas orientada a objeto:
- `app/models.py`: entidades de domínio
- `app/repository.py`: persistência PostgreSQL
- `app/services.py`: regras de negócio
- `app/actions.py`: ações/rotinas executáveis
- `app/main.py`: menu interativo multitarefa

## Banco de dados PostgreSQL

Crie a tabela executando:

```bash
psql -U postgres -d techgov -f sql/init.sql
```

Variáveis de ambiente opcionais para conexão:
- `DB_HOST` (default: `localhost`)
- `DB_PORT` (default: `5432`)
- `DB_NAME` (default: `techgov`)
- `DB_USER` (default: `postgres`)
- `DB_PASSWORD` (default: `postgres`)

## Execução

```bash
python -m app.main
```

## Testes

```bash
pytest
```
