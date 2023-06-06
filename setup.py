from setuptools import setup, find_packages

setup(
    name='Munchkin',
    version='0.1.0',
    description='This is my discount version of the game Munchkin',
    author='Jacob Thornton',
    author_email='jacobreidth@hotmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        # List your project dependencies here
        'pytest==7.3.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Friends and Family',
        'License :: None?',
        'Programming Language :: Python :: 3.8.2',
    ],
)
