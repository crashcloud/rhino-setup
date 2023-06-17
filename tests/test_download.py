import subprocess as proc
from pathlib import Path
from glob import glob
import pytest
import os

from .context import src

cwd = os.path.dirname(os.path.realpath(__file__))
cwd_path = Path(cwd)
parent_path = cwd_path.parent.absolute()
script = f'{parent_path}/src/download-rhino.py'

# import process
# run script
# test outputs
# Ensure ALL versions are available
# TEST RAEL VERSIONS TOOx

versions = ['6', '7', '8']

def run(version:str, platform:str, full_version:str='latest'):
    proc.run( [ 'python', script, 
                '--version' , version,
                '--fullversion', full_version,
                '--platform', platform] )

@pytest.mark.parametrize("version,full_version,platform", [
    ('6', 'latest', 'win'),
    ('6', '6.29.20238.11501', 'win'),

    ('7', 'latest', 'win'),
    ('7', '7.28.23058.03001', 'win'),

    ('8', 'latest', 'win'),

    ('6', 'latest', 'mac'),

    ('7', 'latest', 'mac'),
    ('7', '7.16.22067.13001', 'mac'),

    ('8', 'latest', 'mac'),
    ('8', '8.0.23094.11475', 'mac'),
])
def test_wind_rhino7_latest(version, full_version, platform):
    rhino_exes = glob(f'rhino_{cwd}/*.exe')
    assert len(rhino_exes) == 0

    run(version, platform, full_version)
    rhino_exes = glob(f'rhino_{cwd}/*.exe')
    assert len(rhino_exes) == 1

    for r_exe in rhino_exes:
        os.remove(r_exe)
