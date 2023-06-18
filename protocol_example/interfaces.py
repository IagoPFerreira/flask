from typing import Protocol


class Connection(Protocol):
    """Protocolo de conexão com o banco de dados"""

    def execute():
        """Executa uma query no banco e retorna os dados, caso existam """
        ...


class Database(Protocol):
    """Protocolo de um banco de dados"""

    def connect(self, connection_url: str):
        """Realiza uma conexão com o banco de dados"""
        ...
