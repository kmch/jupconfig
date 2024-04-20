from setuptools import setup, find_packages

setup(
    name='jupconfig',
    version='0.0.3',
    packages=find_packages(), # organise the internal dependencies, not external 
    install_requires=[
        'autologging', 
    ],    
    description='Set up your Jupyter notebook for autologging etc.',
    author='Kajetan Chrapkiewicz',
    author_email='k.chrapkiewicz17@imperial.ac.uk',
    url='https://github.com/kmch/jupconfig',
)
