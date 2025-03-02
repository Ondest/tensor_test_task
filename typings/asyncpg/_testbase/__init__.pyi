"""
This type stub file was generated by pyright.
"""

import asyncio
import atexit
import contextlib
import functools
import inspect
import logging
import os
import re
import textwrap
import time
import traceback
import unittest
import asyncpg
from asyncpg import cluster as pg_cluster, connection as pg_connection, pool as pg_pool
from . import fuzzer

@contextlib.contextmanager
def silence_asyncio_long_exec_warning():  # -> Generator[None, Any, None]:
    ...
def with_timeout(timeout):  # -> Callable[..., Any]:
    ...

class TestCaseMeta(type(unittest.TestCase)):
    TEST_TIMEOUT = ...
    def __new__(mcls, name, bases, ns):  # -> Self:
        ...

class TestCase(unittest.TestCase, metaclass=TestCaseMeta):
    @classmethod
    def setUpClass(cls):  # -> None:
        ...
    @classmethod
    def tearDownClass(cls):  # -> None:
        ...
    def setUp(self):  # -> None:
        ...
    def tearDown(self):  # -> None:
        ...
    @contextlib.contextmanager
    def assertRunUnder(self, delta):  # -> Generator[None, Any, None]:
        ...
    @contextlib.contextmanager
    def assertLoopErrorHandlerCalled(
        self, msg_re: str
    ):  # -> Generator[None, Any, None]:
        ...
    def loop_exception_handler(self, loop, context):  # -> None:
        ...

_default_cluster = ...

def create_pool(
    dsn=...,
    *,
    min_size=...,
    max_size=...,
    max_queries=...,
    max_inactive_connection_lifetime=...,
    connect=...,
    setup=...,
    init=...,
    loop=...,
    pool_class=...,
    connection_class=...,
    record_class=...,
    **connect_kwargs,
):  # -> Pool:
    ...

class ClusterTestCase(TestCase):
    @classmethod
    def get_server_settings(cls):  # -> dict[str, str]:
        ...
    @classmethod
    def new_cluster(cls, ClusterCls, *, cluster_kwargs=..., initdb_options=...): ...
    @classmethod
    def start_cluster(cls, cluster, *, server_settings=...):  # -> None:
        ...
    @classmethod
    def setup_cluster(cls):  # -> None:
        ...
    @classmethod
    def setUpClass(cls):  # -> None:
        ...
    @classmethod
    def tearDownClass(cls):  # -> None:
        ...
    @classmethod
    def get_connection_spec(
        cls, kwargs=...
    ):  # -> dict[str, str] | dict[str, Any] | None:
        ...
    @classmethod
    def connect(cls, **kwargs): ...
    def setUp(self):  # -> None:
        ...
    def tearDown(self):  # -> None:
        ...
    def create_pool(self, pool_class=..., connection_class=..., **kwargs): ...

class ProxiedClusterTestCase(ClusterTestCase):
    @classmethod
    def get_server_settings(cls):  # -> dict[str, str]:
        ...
    @classmethod
    def get_proxy_settings(cls):  # -> dict[str, None]:
        ...
    @classmethod
    def setUpClass(cls):  # -> None:
        ...
    @classmethod
    def tearDownClass(cls):  # -> None:
        ...
    @classmethod
    def get_connection_spec(cls, kwargs):  # -> dict[str, str] | dict[str, Any] | None:
        ...
    def tearDown(self):  # -> None:
        ...

def with_connection_options(**options):  # -> Callable[..., Any]:
    ...

class ConnectedTestCase(ClusterTestCase):
    def setUp(self):  # -> None:
        ...
    def tearDown(self):  # -> None:
        ...

class HotStandbyTestCase(ClusterTestCase):
    @classmethod
    def setup_cluster(cls):  # -> None:
        ...
    @classmethod
    def get_cluster_connection_spec(cls, cluster, kwargs=...): ...
    @classmethod
    def get_connection_spec(cls, kwargs=...):  # -> dict[str | Any, list[Any] | Any]:
        ...
    @classmethod
    def connect_primary(cls, **kwargs):  # -> CoroutineType[Any, Any, Any]:
        ...
    @classmethod
    def connect_standby(cls, **kwargs):  # -> CoroutineType[Any, Any, Any]:
        ...
