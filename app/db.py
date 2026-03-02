import os
from contextlib import contextmanager


class DatabaseConfig:
    def __init__(self) -> None:
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", "5432"))
        self.database = os.getenv("DB_NAME", "techgov")
        self.user = os.getenv("DB_USER", "postgres")
        self.password = os.getenv("DB_PASSWORD", "postgres")


class DatabaseConnection:
    def __init__(self, config: DatabaseConfig | None = None) -> None:
        self.config = config or DatabaseConfig()

    @contextmanager
    def get_connection(self):
        import psycopg2

        conn = psycopg2.connect(
            host=self.config.host,
            port=self.config.port,
            dbname=self.config.database,
            user=self.config.user,
            password=self.config.password,
        )
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
