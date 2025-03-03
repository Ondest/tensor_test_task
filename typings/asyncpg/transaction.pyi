"""
This type stub file was generated by pyright.
"""

import enum
from . import connresource

class TransactionState(enum.Enum):
    NEW = ...
    STARTED = ...
    COMMITTED = ...
    ROLLEDBACK = ...
    FAILED = ...

ISOLATION_LEVELS = ...
ISOLATION_LEVELS_BY_VALUE = ...

class Transaction(connresource.ConnectionResource):
    """Represents a transaction or savepoint block.

    Transactions are created by calling the
    :meth:`Connection.transaction() <connection.Connection.transaction>`
    function.
    """

    __slots__ = ...
    def __init__(self, connection, isolation, readonly, deferrable) -> None: ...
    async def __aenter__(self):  # -> None:
        ...
    async def __aexit__(self, extype, ex, tb):  # -> None:
        ...
    @connresource.guarded
    async def start(self):  # -> None:
        """Enter the transaction or savepoint block."""
        ...

    @connresource.guarded
    async def commit(self):  # -> None:
        """Exit the transaction or savepoint block and commit changes."""
        ...

    @connresource.guarded
    async def rollback(self):  # -> None:
        """Exit the transaction or savepoint block and rollback changes."""
        ...

    def __repr__(self):  # -> str:
        ...
