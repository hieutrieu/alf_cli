from setuptools import setup

exec(open('alf/__init__.py').read())

setup(
    name='alf',
    version=__version__,
    description='AFL CLI',
    author='Andrew',
    packages=['alf', 'alf.commands.s3_client'],
    install_requires=[
        'click',
        'pathlib',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        alf=alf.cli:cli
    '''
)
