"""
This type stub file was generated by pyright.
"""

from . import connresource

class CursorFactory(connresource.ConnectionResource):
    """A cursor interface for the results of a query.

    A cursor interface can be used to initiate efficient traversal of the
    results of a large query.
    """

    __slots__ = ...
    def __init__(
        self, connection, query, state, args, prefetch, timeout, record_class
    ) -> None: ...
    @connresource.guarded
    def __aiter__(self):  # -> CursorIterator:
        ...
    @connresource.guarded
    def __await__(self):  # -> Generator[Any, None, Cursor]:
        ...
    def __del__(self):  # -> None:
        ...

class BaseCursor(connresource.ConnectionResource):
    __slots__ = ...
    def __init__(self, connection, query, state, args, record_class) -> None: ...
    def __repr__(self):  # -> str:
        ...
    def __del__(self):  # -> None:
        ...

class CursorIterator(BaseCursor):
    __slots__ = ...
    def __init__(
        self, connection, query, state, args, record_class, prefetch, timeout
    ) -> None: ...
    @connresource.guarded
    def __aiter__(self):  # -> Self:
        ...
    @connresource.guarded
    async def __anext__(self): ...

class Cursor(BaseCursor):
    """An open *portal* into the results of a query."""

    __slots__ = ...
    @connresource.guarded
    async def fetch(self, n, *, timeout=...):  # -> list[Any]:
        r"""Return the next *n* rows as a list of :class:`Record` objects.

        :param float timeout: Optional timeout value in seconds.

        :return: A list of :class:`Record` instances.
        """
        ...

    @connresource.guarded
    async def fetchrow(self, *, timeout=...):  # -> None:
        r"""Return the next row.

        :param float timeout: Optional timeout value in seconds.

        :return: A :class:`Record` instance.
        """
        ...

    @connresource.guarded
    async def forward(self, n, *, timeout=...) -> int:
        r"""Skip over the next *n* rows.

        :param float timeout: Optional timeout value in seconds.

        :return: A number of rows actually skipped over (<= *n*).
        """
        ...
