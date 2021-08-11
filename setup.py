import os
from setuptools import setup
import subprocess

with open(os.path.join("mazemdp", "version.txt"), "r") as file_handler:
    __version__ = file_handler.read().strip()

# Taken from PyTorch code to have a different version per commit
hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=".").decode('ascii').strip()

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='mazemdp',
    url='https://github.com/osigaud/SimpleMazeMDP',
    author='Olivier Sigaud',
    author_email='Olivier.Sigaud@upmc.fr',
    # Needed to actually package something
    packages=['mazemdp'],
    # Needed for dependencies
    install_requires=['numpy', 'plotly>=5.1.0'],
    # *strongly* suggested for sharing
    version=f'0.1@{hash}',
    # The license can be anything you like
    license='MIT',
    description='An simple maze to test dynamic programming and tabular reinforcement learning algorithms',
    long_description=open('README.md').read(),
)
