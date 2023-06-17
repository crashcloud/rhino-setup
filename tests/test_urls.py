from .context import src

import pytest

def test_win_rhino_6():
    assert src.get_download_url('6', 'win') != None
    
def test_win_rhino_7():
    assert src.get_download_url('7', 'win') != None
    
def test_win_rhino_8():
    assert src.get_download_url('8', 'win') != None


def test_mac_rhino_6():
    assert src.get_download_url('6', 'mac') != None
    
def test_mac_rhino_7():
    assert src.get_download_url('7', 'mac') != None
    
def test_mac_rhino_8():
    assert src.get_download_url('8', 'mac') != None


def test_invalid_version():
    with pytest.raises(Exception) as e_info:
        src.get_download_url('9', 'win')
    
def test_invalid_platform():
    with pytest.raises(Exception) as e_info:
        src.get_download_url('7', 'linux')
