import pytest

from src.utils import displays_list

def test_displays_list():
    assert displays_list()[0]['id'] == 441945886
    assert displays_list()[1]['id'] == 41428829


def test_filter_list():