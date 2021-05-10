#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=inherit-non-class,too-few-public-methods
"""anyconfig basic data types.
"""
import pathlib
import typing


IOI_PATH_STR: str = 'path'
IOI_PATH_OBJ: str = 'pathlib.Path'
IOI_STREAM: str = 'stream'

IOI_TYPES: typing.FrozenSet[str] = frozenset(
    (IOI_PATH_STR, IOI_PATH_OBJ, IOI_STREAM)
)


class IOInfo(typing.NamedTuple):
    """Equivalent to collections.namedtuple."""
    src: typing.Union[str, pathlib.Path, typing.IO]
    type: str
    path: str
    extension: str


IOI_KEYS: typing.Tuple[str, ...] = IOInfo._fields

PathT = typing.Union[str, pathlib.Path]
PathOrIOT = typing.Union[PathT, typing.IO]
PathOrIOInfoT = typing.Union[PathT, IOInfo]

InDataT = typing.Mapping[str, typing.Any]

PrimitiveT = typing.Union[int, None, float, bool, InDataT]
InDataExT = typing.Union[PrimitiveT, InDataT]

# vim:sw=4:ts=4:et:
