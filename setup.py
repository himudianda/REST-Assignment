from setuptools import setup

setup(
    name='REST Assignment',
    version='0.1',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        run=cli.cli:cli
    ''',
)
