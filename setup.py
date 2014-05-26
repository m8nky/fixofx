#! /usr/bin/env python

DISTNAME = 'fixofx'
DESCRIPTION = ''
LONG_DESCRIPTION = ''
MAINTAINER = ''
MAINTAINER_EMAIL = ''
URL = ''
LICENSE = 'Apache 2.0'
DOWNLOAD_URL = ''
VERSION = '0.1'

import os
from setuptools import setup, find_packages
try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

if __name__ == "__main__":
    setup(
        name=DISTNAME,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        url=URL,
        license=LICENSE,
        download_url=DOWNLOAD_URL,
        version=VERSION,
        classifiers=[
            'Development Status :: Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: ',
            'Topic :: '
            ],
        install_requires=[],
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,

        cmdclass={'build_py': build_py},

        entry_points={
            'console_scripts': [
                'fixofx = fixofx',
            ],
        }
    )