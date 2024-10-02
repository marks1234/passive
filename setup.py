from setuptools import setup
setup(
    name='passive',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'passive=passive:main'
        ]
    }
)
