#!/usr/bin/env python3



#installer for ubuntu ClamAV
import subprocess
import os
import glob
import time

enable_llvm = 'no'    # if you want to install LLVM. yes/no
llvm_ver = '3.6.2'       # LLVM supported version
clamav_version = 'clamav-0.100.0'   # ClamAV version to install
add_optional_packages = 'yes'       # Will install additional packages to check unit tests. yes/no
group_name = 'clamav'
user_add = 'clamav'

def update_sys():
    ## Lets update the system with an apt-get update first. ##
    try:
        subprocess.check_call(['apt-get', 'update'])
    except Exception as e:
        print('Updating the system with "apt-get update" failed')
        print(e)

def  pre():
    ## Lets install pre-req ##
    list_packages = ['libssl-dev', 'libxml2-dev', 'zlib1g-dev', 'zlibc', 'libpng-dev', 'libpcre3-dev', 'bzip2',
                     'libjson-c-dev', 'libcurl4-openssl-dev']
    optional_packages = ['check', 'valgrind']
    for package in list_packages:
        try:
            subprocess.check_call(['apt-get', '-y', 'install', package])
        except Exception as err:
            print('A required package has failed to install.')
            print(err)
    if add_optional_packages == 'yes':
        for opt_pack in optional_packages:
            try:
                subprocess.check_call(['apt-get', '-y', 'install', opt_pack])
            except Exception as err:
                print('A optional package has failed to install.')
                print(err)
    else:
        print('Not adding additional packages')


def llvm():
    ##
    if enable_llvm == 'yes':
        os.chdir('/opt')
        os.makedirs('/opt/llvm', 0o755)
        os.chdir('/opt/llvm')
        os.system('wget http://releases.llvm.org/{}/llvm-{}.src.tar.xz'.format(llvm_ver, llvm_ver))
        time.sleep(5)
        os.system('tar -xvf llvm-{}.src.tar.xz'.format(llvm_ver))
        os.chdir('/opt/llvm/llvm-{}.src'.format(llvm_ver))
        try:
            subprocess.check_call(['./configure'])
        except Exception as err:
            print('./configure failed')
            print(err)

        try:
            subprocess.check_call(['make'])
        except Exception as err:
            print('make failed')
            print(err)

        try:
            subprocess.check_call(['make', 'install'])
        except Exception as err:
            print('Make install failed')
            print(err)

def c_install():
    ## Lets install clamav ##
    os.chdir('/opt')
    os.makedirs('/opt/ClamAV', 0o755)
    os.chdir('/opt/ClamAV')
    os.system('wget https://www.clamav.net/downloads/production/%s.tar.gz' % clamav_version)
    time.sleep(10)
    os.system('tar -xvf {}.tar.gz'.format(clamav_version))
    os.chdir('/opt/ClamAV/{}'.format(clamav_version))
    if enable_llvm == 'yes':
        try:
            subprocess.check_call(['./configure', '--with-llvm-linking=static'])
        except Exception as err:
            print(err)
        try:
            subprocess.check_call(['make'])
        except Exception as err:
            print(err)

        try:
            subprocess.check_call(['make', 'install'])
        except Exception as err:
            print(err)

        if add_optional_packages == 'yes':
            os.system('./configure --enable-check')
            os.system('make check VG=1')
        else:
            print('Installation is done')
    else:
        try:
            subprocess.check_call(['./configure'])
        except Exception as err:
            print(err)

        try:
            subprocess.check_call(['make'])
        except Exception as err:
            print(err)

        try:
            subprocess.check_call(['make', 'install'])
        except Exception as err:
            print(err)

    if add_optional_packages == 'yes':
        os.system('./configure --enable-check')
        os.system('make check VG=1')
    else:
        print('Installation is done')


def setup():
    ## We are only going to fix a few minor things ##
    os.system('ldconfig')
    try:
        subprocess.check_call(['groupadd', group_name])
        print('added group successfully')
    except Exception as err:
        print(err)

    try:
        subprocess.check_call(['useradd', '-g', user_add, '-s', '/bin/false', '-c', 'Clam Antivirus', group_name])
        print('added user and added user to group')
    except Exception as err:
        print(err)

    os.system('mkdir /usr/local/share/clamav')
    os.system('chmod 777 /usr/local/share/clamav')


def main():
    update_sys()
    pre()
    llvm()
    c_install()
    setup()


main()
