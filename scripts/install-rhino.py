import subprocess as proc
from glob import glob
import argparse
import wget
import sys
import os

FILES_URL = 'https://files.mcneel.com'

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", type=str, required=True, choices=['6', '7', '8'])
parser.add_argument("-fv", "--fullversion", type=str, required=False, default="latest")
parser.add_argument("-c", "--culture", type=str, default="en-us")
parser.add_argument("-p", "--platform", type=str, required=True, choices=['mac', 'win'])
parser.add_argument('-k', '--licensekey', type=str, required=True)

args = parser.parse_args()
version = args.version
culture = args.culture
platform = args.platform
full_version = args.fullversion
license_key = args.licensekey

def get_ext(os: str) -> str:
    if os == 'mac':
        return 'dmg'
    return 'exe'

download_url_stack = {
    'mac' : {
        '6' : {
            'latest' :  'https://www.rhino3d.com/download/rhino-for-mac/6/latest/direct?email=test@email.com',
        },
        '7' : {
            'latest' : 'https://www.rhino3d.com/download/rhino-for-mac/7/latest/direct?email=test@email.com',

            '.30.23130.11001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.30.23130.11001.{get_ext(platform)}',
            '.30.23125.15001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.30.23125.15001.{get_ext(platform)}',
            '.30.23125.03001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.30.23125.03001.{get_ext(platform)}',
            '.29.23107.03001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.29.23107.03001.{get_ext(platform)}',
            '.28.23058.03001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.28.23058.03001.{get_ext(platform)}',
            '.28.23051.01001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.28.23051.01001.{get_ext(platform)}',
            '.27.23032.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.27.23032.13001.{get_ext(platform)}',
            '.26.23009.07001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.26.23009.07001.{get_ext(platform)}',
            '.25.22326.19001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.25.22326.19001.{get_ext(platform)}',
            '.24.22308.15001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.24.22308.15001.{get_ext(platform)}',
            '.23.22282.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.23.22282.13001.{get_ext(platform)}',
            '.22.22255.05001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.22.22255.05001.{get_ext(platform)}',
            '.21.22208.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.21.22208.13001.{get_ext(platform)}',
            '.20.22193.09001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.20.22193.09001.{get_ext(platform)}',
            '.19.22180.09001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.19.22180.09001.{get_ext(platform)}',
            '.19.22165.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.19.22165.13001.{get_ext(platform)}',
            '.18.22124.03001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.18.22124.03001.{get_ext(platform)}',
            '.17.22102.05001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.17.22102.05001.{get_ext(platform)}',
            '.16.22067.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.16.22067.13001.{get_ext(platform)}',
            '.15.22039.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.15.22039.13001.{get_ext(platform)}',
            '.14.22010.17001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.14.22010.17001.{get_ext(platform)}',
            '.13.21348.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.13.21348.13001.{get_ext(platform)}',
            '.12.21313.06341' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.12.21313.06341.{get_ext(platform)}',
            '.11.21293.09001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.11.21293.09001.{get_ext(platform)}',
            '.11.21285.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.11.21285.13001.{get_ext(platform)}',
            '.10.21256.17001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.10.21256.17001.{get_ext(platform)}',
            '.9.21222.15001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.9.21222.15001.{get_ext(platform)}',
            '.8.21196.05001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.8.21196.05001.{get_ext(platform)}',
            '.7.21160.05001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.7.21160.05001.{get_ext(platform)}',
            '.6.21127.19001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.6.21127.19001.{get_ext(platform)}',
            '.5.21100.03001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.5.21100.03001.{get_ext(platform)}',
            '.4.21078.01001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.4.21078.01001.{get_ext(platform)}',
            '.4.21067.13001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.4.21067.13001.{get_ext(platform)}',
            '.3.21053.23031' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.3.21053.23031.{get_ext(platform)}',
            '.3.21039.11201' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.3.21039.11201.{get_ext(platform)}',
            '.2.21021.07001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.2.21021.07001.{get_ext(platform)}',
            '.2.21012.11001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.2.21012.11001.{get_ext(platform)}',
            '.1.20343.09491' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.1.20343.09491.{get_ext(platform)}',
            '.0.20314.03001' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_7.0.20314.03001.{get_ext(platform)}',
        },
        '8' : {
            'latest' : '',
            '8.0.23150.10305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23150.10305.{get_ext(platform)}',
            '8.0.23143.18305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23143.18305.{get_ext(platform)}',
            '8.0.23136.12095' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23136.12095.{get_ext(platform)}',
            '8.0.23129.12305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23129.12305.{get_ext(platform)}',
            '8.0.23125.12175' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23125.12175.{get_ext(platform)}',
            '8.0.23122.12305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23122.12305.{get_ext(platform)}',
            '8.0.23115.04305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23115.04305.{get_ext(platform)}',
            '8.0.23108.14305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23108.14305.{get_ext(platform)}',
            '8.0.23101.16305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23101.16305.{get_ext(platform)}',
            '8.0.23094.11475' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23094.11475.{get_ext(platform)}',
            '8.0.23087.12305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23087.12305.{get_ext(platform)}',
            '8.0.23080.12305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23080.12305.{get_ext(platform)}',
            '8.0.23073.13185' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23073.13185.{get_ext(platform)}',
            '8.0.23066.13185' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23066.13185.{get_ext(platform)}',
            '8.0.23059.12305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23059.12305.{get_ext(platform)}',
            '8.0.23052.12305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23052.12305.{get_ext(platform)}',
            '8.0.23045.12305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23045.12305.{get_ext(platform)}',
            '8.0.23039.08305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23039.08305.{get_ext(platform)}',
            '8.0.23038.12305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23038.12305.{get_ext(platform)}',
            '8.0.23031.14305' : f'{FILES_URL}/rhino/{version}/mac/releases/rhino_wip_8.0.23031.14305.{get_ext(platform)}',
        }
    },
    'win' : {
        '6' : {
            'latest' : 'https://www.rhino3d.com/download/rhino-for-windows/6/latest/direct?email=example@email.com',

            '6.35.21222.17001' : f'{FILES_URL}/dujour/exe/20210810/rhino_{culture}_6.35.21222.17001.{get_ext(platform)}',
            '6.29.20238.11501' : f'{FILES_URL}/dujour/exe/20200825/rhino_{culture}_6.29.20238.11501.{get_ext(platform)}'
        },
        '7' : {
            'latest' : 'https://www.rhino3d.com/download/rhino-for-windows/7/latest/direct?email=example@email.com', # LATEST

            # without num url cannot be known
    #       '7.30.23130.11001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.30.23130.11001.{get_ext(platform)}',
    #       '7.30.23125.15001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.30.23125.15001.{get_ext(platform)}',
    #       '7.30.23125.03001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.30.23125.03001.{get_ext(platform)}',
            '7.29.23107.03001' : f'{FILES_URL}/dujor/exe/20230417/rhino_{culture}_7.29.23107.03001.{get_ext(platform)}',
    #       f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.28.23058.03001.{get_ext(platform)}',
    #       '7.28.23051.01001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.28.23051.01001.{get_ext(platform)}',
    #       '7.27.23032.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.27.23032.13001.{get_ext(platform)}',
    #       '7.26.23009.07001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.26.23009.07001.{get_ext(platform)}',
    #       '7.25.22326.19001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.25.22326.19001.{get_ext(platform)}',
    #       '7.24.22308.15001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.24.22308.15001.{get_ext(platform)}',
    #       '7.23.22282.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.23.22282.13001.{get_ext(platform)}',
    #       '7.22.22255.05001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.22.22255.05001.{get_ext(platform)}',
    #       '7.21.22208.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.21.22208.13001.{get_ext(platform)}',
    #       '7.20.22193.09001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.20.22193.09001.{get_ext(platform)}',
    #       '7.19.22180.09001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.19.22180.09001.{get_ext(platform)}',
    #       '7.19.22165.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.19.22165.13001.{get_ext(platform)}',
    #       '7.18.22124.03001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.18.22124.03001.{get_ext(platform)}',
    #       '7.17.22102.05001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.17.22102.05001.{get_ext(platform)}',
    #       '7.16.22067.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.16.22067.13001.{get_ext(platform)}',
    #       '7.15.22039.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.15.22039.13001.{get_ext(platform)}',
    #       '7.14.22010.17001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.14.22010.17001.{get_ext(platform)}',
    #       '7.13.21348.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.13.21348.13001.{get_ext(platform)}',
    #       '7.12.21313.06341' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.12.21313.06341.{get_ext(platform)}',
    #       '7.11.21293.09001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.11.21293.09001.{get_ext(platform)}',
    #       '7.11.21285.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.11.21285.13001.{get_ext(platform)}',
    #       '7.10.21256.17001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.10.21256.17001.{get_ext(platform)}',
    #       '7.9.21222.15001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.9.21222.15001.{get_ext(platform)}',
    #       '7.8.21196.05001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.8.21196.05001.{get_ext(platform)}',
    #       '7.7.21160.05001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.7.21160.05001.{get_ext(platform)}',
    #       '7.6.21127.19001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.6.21127.19001.{get_ext(platform)}',
    #       '7.5.21100.03001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.5.21100.03001.{get_ext(platform)}',
    #       '7.4.21078.01001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.4.21078.01001.{get_ext(platform)}',
    #       '7.4.21067.13001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.4.21067.13001.{get_ext(platform)}',
    #       '7.3.21053.23031' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.3.21053.23031.{get_ext(platform)}',
    #       '7.3.21039.11201' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.3.21039.11201.{get_ext(platform)}',
    #       '7.2.21021.07001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.2.21021.07001.{get_ext(platform)}',
    #       '7.2.21012.11001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.2.21012.11001.{get_ext(platform)}',
    #       '7.1.20343.09491' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.1.20343.09491.{get_ext(platform)}',
    #       '7.0.20314.03001' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_7.0.20314.03001.{get_ext(platform)}',
        },
        '8' : {
    #       'latest' : 'https://www.rhino3d.com/download/rhino-for-windows/8/latest/direct?email=example@email.com', # LATEST // NOT FIGURED OUT YET
            'latest' : f'{FILES_URL}/dujor/exe/20230530/rhino_{culture}_8.0.23150.10305.{get_ext(platform)}',
            '8.0.23150.10305' : f'{FILES_URL}/dujor/exe/20230530/rhino_{culture}_8.0.23150.10305.{get_ext(platform)}',
    #       '8.0.23143.18305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23143.18305.{get_ext(platform)}',
    #       '8.0.23136.12095' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23136.12095.{get_ext(platform)}',
    #       '8.0.23129.12305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23129.12305.{get_ext(platform)}',
    #       '8.0.23125.12175' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23125.12175.{get_ext(platform)}',
    #       '8.0.23122.12305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23122.12305.{get_ext(platform)}',
    #       '8.0.23115.04305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23115.04305.{get_ext(platform)}',
    #       '8.0.23108.14305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23108.14305.{get_ext(platform)}',
    #       '8.0.23101.16305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23101.16305.{get_ext(platform)}',
    #       '8.0.23094.11475' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23094.11475.{get_ext(platform)}',
    #       '8.0.23087.12305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23087.12305.{get_ext(platform)}',
    #       '8.0.23080.12305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23080.12305.{get_ext(platform)}',
    #       '8.0.23073.13185' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23073.13185.{get_ext(platform)}',
    #       '8.0.23066.13185' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23066.13185.{get_ext(platform)}',
    #       '8.0.23059.12305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23059.12305.{get_ext(platform)}',
    #       '8.0.23052.12305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23052.12305.{get_ext(platform)}',
    #       '8.0.23045.12305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23045.12305.{get_ext(platform)}',
    #       '8.0.23039.08305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23039.08305.{get_ext(platform)}',
    #       '8.0.23038.12305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23038.12305.{get_ext(platform)}',
    #       '8.0.23031.14305' : f'{FILES_URL}/dujor/exe/<num>/rhino_{culture}_8.0.23031.14305.{get_ext(platform)}',
        }
    }
}

download_url = download_url_stack[platform][version][full_version]
exe_name = f'rhino_{version}_{full_version}.exe'
print(f'Downloading Rhino from {download_url} to {exe_name}')

if os.path.isfile(exe_name):
    print('Rhino is already downloaded. Using Cached version')
else:
    wget.download(download_url, exe_name)

cwd = os.getcwd()
rhino_exe_path = f'{cwd}\{exe_name}'

# We use repair incase it is already installed
# https://wiki.mcneel.com/rhino/installingrhino/7
proc.run([ rhino_exe_path,
            '-repair',
            '-quiet',
            '-passive',
            'LICENSE_METHOD=STANDALONE',
            f'LICENSE_KEY={license_key}' ,
            '-norestart',
            'INSTALL_EN=1'])