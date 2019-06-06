"""
Twitter Party Recognition

Brian Sutherland <bsuth@umich.edu>
Shameek Ray <shameek@umich.edu>
Nikita Badhwar <nbadhwar@umich.edu>
Rodney Shibu <rodneyss@umich.edu>
Sreeraj Marar <sreerajm@umich.edu>

setup.py format credit: W19 EECS 485 P4-MapReduce
"""

from setuptools import setup

setup(
    name='partycity',
    version='0.1.0',
    packages=['partycity'],
    include_package_data=True,
    install_requires=[
        'pycodestyle==2.5.0',
        'pydocstyle==3.0.0',
        'pylint==2.3.1',
        'pytest==4.3.0',
    ],
    entry_points={
        'console_scripts': [
            'partycity = partycity.__main__:main',
        ]
    },
)
