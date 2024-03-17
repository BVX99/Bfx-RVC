from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='bfx-vc',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
    ],
    author='Blane187',
    author_email='laynzch@email.com',
    description='make ai cover easily',
    url='https://github.com/BVX99/Bfx-RVC',
)
