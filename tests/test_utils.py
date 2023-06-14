from utils import get_ext

import pytest

def test_win():
    assert get_ext("win") == "exe"
    
def test_mac():
    assert get_ext("mac") == "dmg"

def test_invalid():
    with pytest.raises(Exception) as e_info:
        get_ext("linux")
