#!/usr/bin/env python3

import subprocess
import os
import time

oinkcode = 'oinkcode'
daq = 'daq-2.0.6'
snortv = 'snort-2.9.11.1'
directory1 = '/etc/snort'
directory2 = '/var/log/snort'
directory3 = '/usr/local/lib/snort_dynamicrules'
site = 'https://www.snort.org'

def update_sys():
    ## Lets update the system with 'apt-get update'
    try:
        subprocess.check_call(['apt-get', 'update'])
    except Exception as e:
        print('Updating the system with "apt-get update" failed')
        print(e)


def pre_req():
    #Lets install pre-reqs
    list_packages = ['libpcap-dev', 'bison', 'flex', 'libdumbnet-dev', 'libhwloc-dev', 'libluajit-5.1-dev',
                     'libssl-dev', 'libpcre3-dev']
    for package in list_packages:
        try:
            subprocess.check_call(['apt-get', '-y', 'install', package])

        except Exception as err:
            print('A required package has failed to install')
            print(err)


def snort_install_config():
    ## Lets install Snort ##
    os.chdir('/opt')
    os.makedirs(directory1, 0o755)
    os.makedirs(directory2, 0o755)
    os.makedirs(directory3, 0o755)
    subprocess.check_call(['groupadd', 'snort'])
    subprocess.check_call(['useradd', '-g', 'snort', 'snort'])
    subprocess.check_call(['chown', 'snort:snort', '/var/log/snort'])


    try:
        os.system('wget https://www.snort.org/downloads/snort/%s.tar.gz' % daq)
    except Exception as err:
        print(err)
    try:
        os.system('wget https://www.snort.org/downloads/snort/%s.tar.gz' % snortv)
    except Exception as err:
        print(err)
    conf = './configure'
    os.system('tar -xvf {}.tar.gz'.format(daq))
    os.chdir('/opt/%s' % daq)
    subprocess.check_call(['./configure'])
    subprocess.check_call(['make'])
    subprocess.check_call(['make', 'install'])
    os.chdir('/opt')
    os.system('tar -xvf {}.tar.gz'.format(snortv))
    os.chdir('/opt/%s' % snortv)
    subprocess.check_call([conf, '--enable-sourcefire', '--enable-open-appid', '--enable-file-inspect'])
    subprocess.check_call(['make'])
    subprocess.check_call(['make', 'install'])
    os.chdir('/opt')
    snort_p1 = snortv
    snort_p1 = snort_p1[6:]
    snort_p2 = snort_p1.replace('.', '')

    try:
        os.system('wget {}/rules/snortrules-snapshot-{}.tar.gz?oinkcode={} -O snortrules-snapshot-{}.tar.gz'.format(site, snort_p2, oinkcode, snort_p2))
    except Exception as err:
        print(err)
    os.system('tar -xvf snortrules-snapshot-{}.tar.gz -C {}'.format(snort_p2, directory1))
    os.system('cp /etc/snort/etc/* {}'.format(directory1))
    os.system('cp /etc/snort/so_rules/precompiled/Ubuntu-16-4/x86-64/{}/* {}'.format(snort_p1, directory3))
    #subprocess.check_call(['cp', 'etc/gen-msg.map', '/etc/snort'])
    subprocess.check_call(['touch', '{}/rules/white_list.rules'.format(directory1)])
    subprocess.check_call(['touch', '{}/rules/black_list.rules'.format(directory1)])
    subprocess.check_call(['ldconfig'])

    print('*' * 10)
    print('From here, you will need to update the /etc/snort/snort.conf file with the following directories:')
    print(directory1, directory2, directory3)


update_sys()
pre_req()
snort_install_config()
