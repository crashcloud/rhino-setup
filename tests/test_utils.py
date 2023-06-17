from .context import src

import pytest

def test_win():
    assert src.get_ext("win") == "exe"
    
def test_mac():
    assert src.get_ext("mac") == "dmg"

def test_invalid():
    with pytest.raises(Exception) as e_info:
        src.get_ext("linux")
