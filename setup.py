from setuptools import setup, find_packages

setup(
    name='marlenv',
    version='1.0.0',
    url='https://github.com/kc-ml2/marlenv',
    author='Tae Min Ha, Daniel Nam, Won Seok Jung',
    author_email='contact@kc-ml2.com',
    packages=find_packages(),
    install_requires=[
        'gym',
        'mpi4py',
    ],
    python_requires='>=3.6'
)