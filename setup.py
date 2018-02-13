from distutils.core import setup
import subprocess

TRACER_URL = 'git+git@github.com:angr/tracer.git#egg=tracer'
FUZZER_URL = 'git+git@github.com:shellphish/fuzzer.git'

if subprocess.call(['pip', 'install', TRACER_URL]) != 0:
   raise LibError("Unable to install tracer")

if subprocess.call(['pip', 'install', FUZZER_URL]) != 0:
   raise LibError("Unable to install fuzzer")

setup(
        name='driller',
        version='1.0',
        packages=['driller'],
        data_files=[
            ('bin/driller', ('bin/driller/listen.py',),),
        ],
        install_requires=[
            'cle',
            'angr',
            'redis',
            'celery',
            'archinfo',
            'dpkt-fix',
            'termcolor',
        ],
)
