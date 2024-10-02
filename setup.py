from setuptools import setup
setup(
    name='passive',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'passive=passive:main'
        ]
    }
)
