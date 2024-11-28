from typing import Any

import pytest


def test_something(data: Any = 12):
    assert isinstance(data, int)
