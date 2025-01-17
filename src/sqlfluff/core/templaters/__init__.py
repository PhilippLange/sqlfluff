"""Templater Code."""

from sqlfluff.core.templaters.base import TemplatedFile

# Although these shouldn't usually be instantiated from here
# we import them to make sure they get registered.
from sqlfluff.core.templaters.base import RawTemplater, RawFileSlice
from sqlfluff.core.templaters.jinja import JinjaTemplater
from sqlfluff.core.templaters.python import PythonTemplater
from sqlfluff.core.templaters.placeholder import PlaceholderTemplater
from typing import Iterator, Type


def core_templaters() -> Iterator[Type[RawTemplater]]:
    """Returns the templater tuples for the core templaters."""
    yield from [RawTemplater, JinjaTemplater, PythonTemplater, PlaceholderTemplater]


__all__ = (
    "RawFileSlice",
    "TemplatedFile",
    "RawTemplater",
    "JinjaTemplater",
    "PythonTemplater",
    "PlaceholderTemplater",
    "core_templaters",
)
