from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
  name = 'orprov-cli',
  packages = ['orprov','google','google.refine'],
  version = '0.0.5',
  description = 'Open Refine Command Line Interface for Provenance Demo',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url = 'https://github.com/nikolausn/OR-Prov-Reproducibility',
  author = "Lan,Li; Parulian, Nikolaus; Ludaescher Bertram",
  package_data={'orcli': []},
  include_package_data=True,
  install_requires=['urllib2_file','jsondiff'],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7'
  ],
  entry_points={
        'console_scripts': [
            'orprov-cli = orprov.__main__:run'
        ],
    }
)
