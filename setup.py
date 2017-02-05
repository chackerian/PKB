from setuptools import setup, find_packages

setup(
    name='pkb',
    version='0.1',
    packages=find_packages(),
    py_modules=['pkb'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pkb=pkb:cli
    ''',
)