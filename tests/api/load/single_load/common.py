#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# License: MIT
#
# pylint: disable=missing-docstring
import unittest

import anyconfig.parsers

from tests.base import (
    DATA_00, list_resources
)


class BaseTestCase(unittest.TestCase):

    # see: tests/res/json/basic/
    kind = 'basic'

    @property
    def ies(self):
        path = f'json/{self.kind}/*.json'
        _ies = sorted(
            (inp, DATA_00.get(str(inp), None)) for inp in list_resources(path)
        )
        if not _ies:
            raise RuntimeError(f'No data: {path}')

        return _ies

    @property
    def psr(self):
        return anyconfig.parsers.find(self.ies[0][0], 'json')


class TestCaseWithExpctedData(BaseTestCase):

    # see: tests/res/json/template/ for example.
    @property
    def ies(self):
        return [
            (inp, inp.parent / 'e' / inp.name)
            for inp, _exp in super().ies
        ]

# vim:sw=4:ts=4:et:
