import sys
from setuptools import setup, find_packages

from constants import __version__

setup(
  name = 'audio_convert',
  packages = find_packages(),
  version = 1,
  license='MIT',
  description = 'A simple keygen creator',
  author = 'Behron Georgantas',
  author_email = 'behronsresume@gmail.com',
  url = 'https://github.com/bresume/audio_convert',
  install_requires = [
    'pydub'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)